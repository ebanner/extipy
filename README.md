# extipy

Kernel provisioner for connecting to IPython kernels started outside of Jupyter

## Credit

This is totally just copied from [pyxll](https://github.com/pyxll).

## Quick start

Embed an IPython kernel in your code and capture all the variables:

```python
import IPython
IPython.embed_kernel(local_ns={**globals(), **locals()})
```

...

```
To connect another client to this kernel, use:
    --existing kernel-31410.json
```

Then attach jupyter lab to it:

```bash
$ export PYXLL_IPYTHON_CONNECTION_FILE=$(jupyter --runtime-dir)/kernel-11100.json
$ jupyter lab --KernelProvisionerFactory.default_provisioner_name=pyxll-provisioner
```
