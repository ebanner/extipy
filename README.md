# extipy

Connect jupyter lab to an external IPython kernel

```python
foo = 5

import IPython
IPython.embed_kernel(local_ns={**locals(), **globals()})
```

<img width="1425" alt="Screenshot 2025-04-26 at 12 29 31 PM" src="https://github.com/user-attachments/assets/631a2a31-2962-47e4-86b6-50c406af7c98" />

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
