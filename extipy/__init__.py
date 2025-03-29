"""

Credit: https://github.com/pyxll/pyxll-jupyter/blob/master/pyxll_jupyter/provisioning/existing.py

"""

from jupyter_client import KernelProvisionerBase
import logging
import json
import os
import subprocess
import glob

_log = logging.getLogger(__name__)


def get_latest_connection_file():
    def get_jupyter_runtime_dir():
        result = subprocess.run(
            ['jupyter', '--runtime-dir'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()

    jupyter_runtime_dir = get_jupyter_runtime_dir()
    connection_filenames = glob.glob(f'{jupyter_runtime_dir}/kernel-*.json')
    latest_connection_filename = max(connection_filenames, key=os.path.getctime)
    return latest_connection_filename


class ExistingProvisioner(KernelProvisionerBase):
    """
    A Kernel Provisioner that re-uses an existing kernel.
    The kernel connection file is fetched as the latest
    modified connection file.
    """
    async def launch_kernel(self, cmd, **kwargs):
        connection_file = get_latest_connection_file()

        with open(connection_file) as f:
            file_info = json.load(f)

        file_info["key"] = file_info["key"].encode()
        return file_info

    async def pre_launch(self, **kwargs):
        kwargs = await super().pre_launch(**kwargs)
        kwargs.setdefault('cmd', None)
        return kwargs

    def has_process(self) -> bool:
        return True

    async def poll(self):
        pass

    async def wait(self):
        pass

    async def send_signal(self, signum: int):
        pass

    async def kill(self, restart=False):
        if restart:
            _log.warning("Cannot restart kernel.")

    async def terminate(self, restart=False):
        if restart:
            _log.warning("Cannot restart kernel.")

    async def cleanup(self, restart):
        pass

