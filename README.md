# extipy

Kernel manager for connecting to IPython kernels started outside of Jupyter

## Installation

```
pip install extipy
```

## Usage

```
jupyter notebook \
  --NotebookApp.kernel_manager_class=extipy.ExternalIPythonKernelManager \
  --Session.key='b""'
```

Note the `--Session.key='b""'` disables message authentication. This is necessary for now as I have not figured out how to fixup the authentication key associated with the current session.
