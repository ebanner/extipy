# extipy

Connect jupyter lab to an external IPython kernel

## Credit

This is largely copied from [pyxll-jupyter](https://github.com/pyxll/pyxll-jupyter).

## Quick start

Embed an IPython kernel in your code and capture all the variables in scope:

```python
import IPython
IPython.embed_kernel(local_ns={**locals(), **globals()})
```

Then attach jupyter lab to it:

```bash
$ jupyter lab --KernelProvisionerFactory.default_provisioner_name=extipy-provisioner
```
