# extipy

Connect jupyter lab to an external IPython kernel

<img width="1437" height="792" alt="image" src="https://github.com/user-attachments/assets/bdc30914-3a53-45b8-89dd-6fade6c82521" />

## Install

```
git clone git@github.com:ebanner/extipy.git
cd extipy
pip install -e .
```

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

## Credit

This is largely copied from [pyxll-jupyter](https://github.com/pyxll/pyxll-jupyter).
