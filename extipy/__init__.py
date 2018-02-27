"""

Kernel manager for connecting to a IPython kernel started outside of Jupyter.

Use this kernel manager if you want to connect a Jupyter notebook to a IPython
kernel started outside of Jupyter.

"""

import glob
import os
import os.path
import re

from tornado import gen

from notebook.services.kernels.kernelmanager import MappingKernelManager


class ExternalIPythonKernelManager(MappingKernelManager):
    """A Kernel manager that connects to a IPython kernel started outside of Jupyter"""

    def _get_latest_kernel_id(self):
        """Return the ID of the most recent kernel that was launched

        This ID is assumed to be the ID of the kernel which was launched via an
        external IPython process.

        Args:
            runtime_dir (str): the directory where kernel files are stored

        Returns:
            kid (int): the ID of the kernel file which was modified most recently

        >>> self = ExternalIPythonKernelManager()

        """
        conn_fnames = glob.glob(f'{self.connection_dir}/kernel-*.json')
        p = '.*kernel-(?P<kid>\d+).json'
        conn_fnames = [conn_fname for conn_fname in conn_fnames for m in [re.match(p, conn_fname)] if m]
        latest_conn_fname = max(conn_fnames, key=os.path.getctime)
        kid = re.match(p, latest_conn_fname).group('kid')
        return kid

    def _attach_to_latest_kernel(self, kernel_id):
        """Attch to the latest externally started IPython kernel

        Args:
            kernel_id (str): ID for this kernel_id

        """
        self.log.info(f'Attaching kernel id = {kernel_id} to an existing kernel...')
        kernel = self._kernels[kernel_id]
        port_names = ['shell_port', 'stdin_port', 'iopub_port', 'hb_port', 'control_port']
        port_names = kernel._random_port_names if hasattr(kernel, '_random_port_names') else port_names
        for port_name in port_names:
            setattr(kernel, port_name, 0)

        # "connect" to latest kernel started by an external python process
        kid = self._get_latest_kernel_id()
        self.log.info(f'Got latest kernel id = {kid} from {self.connection_dir}')
        connection_fname = f'{self.connection_dir}/kernel-{kid}.json'
        kernel.load_connection_file(connection_fname)

    def _should_use_existing(self):
        return os.path.isfile(f'{self.connection_dir}/.pynt')

    @gen.coroutine
    def start_kernel(self, **kwargs):
        """Possibly attach to the most recently started kernel

        This function is a hack. If `self.runtime_dir`/.pynt exists then it
        spins up a new kernel through the call to `super().start_kernel(...)`
        but then turns its attention to the kernel which was started by an
        external python process. Kernel restarts will restart the useless
        kernel and leave the existing kernel alone.

        Args:
            Arguments to pass to `MappingKernelManager.start_kernel()`

        >>> self = ExternalIPythonKernelManager()
        >>> self.connection_dir = '/Users/ebanner/Library/Jupyter/runtime'
        >>> __class__ = ExternalIPythonKernelManager
        >>> kwargs = {}

        """
        self.log.info('Starting kernel!')
        kernel_id = super().start_kernel(**kwargs).result()
        if self._should_use_existing():
            self._attach_to_latest_kernel(kernel_id)
        raise gen.Return(kernel_id)

    # def restart_kernel(self, kernel_id):
    #     """Possibly attach to the most recently started kernel

    #     Args:
    #         Arguments to pass to `MappingKernelManager.start_kernel()`

    #     >>> self = ExternalIPythonKernelManager()
    #     >>> self.connection_dir = '/Users/ebanner/Library/Jupyter/runtime'
    #     >>> kernel_id = self.start_kernel().result()
    #     >>> import time; time.sleep(1)
    #     >>> __class__ = ExternalIPythonKernelManager

    #     """
    #     future = MappingKernelManager.restart_kernel(self, kernel_id)
    #     if self._should_use_existing():
    #         self._attach_to_latest_kernel(kernel_id)
    #     return future
