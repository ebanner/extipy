# extipy

Kernel manager for connecting to IPython kernels started outside of Jupyter.

## Installation

```
pip install extipy
```

## Quick start

```
jupyter notebook \
  --NotebookApp.kernel_manager_class=extipy.ExternalIPythonKernelManager \
  --Session.key='b""'
```

Note the `--Session.key='b""'` disables message authentication. This is necessary for now as I have not figured out how to fixup the authentication key associated with the current session.

## Use case

The purpose of this kernel manager is to allow a jupyter notebook to communicate with an IPython kernel started outside of jupyter. The use case in mind is that you have an external python program which calls [`IPython.embed_kernel()`](http://ipython.readthedocs.io/en/stable/api/generated/IPython.html#IPython.embed_kernel) or [`IPython.start_kernel()`](http://ipython.readthedocs.io/en/stable/api/generated/IPython.html#IPython.start_kernel).

Once you have created an IPython kernel in this way, hitting **New Notebook** in the jupyter notebook interface will trigger extipy to guess the kernel and connect to it.

## How it works

This kernel manager lets Jupyter create a brand new kernel like normal. Then it looks in your runtime directory (should be `~/Library/Jupyter/runtime/` on mac) for the most recently modified `kernel-*.json` file and connects to it.
