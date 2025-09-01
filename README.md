# extipy

Debug your python script with a jupyter notebook

<img width="1430" height="786" alt="image" src="https://github.com/user-attachments/assets/deb47a9b-e4df-4861-bb88-3f5254367a2a" />

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
