from setuptools import setup

setup(
    name='extipy',
    version='0.0.3',
    description='Kernel manager for connecting to IPython kernels started outside of Jupyter',
    url='http://github.com/ebanner/extipy',
    author='Edward Banner',
    author_email='edward.banner@gmail.com',
    license='MIT',
    packages=['extipy'],
    zip_safe=False,
    entry_points={
        "jupyter_client.kernel_provisioners": [
            "extipy-provisioner = extipy:ExistingProvisioner"
        ]   
    },  
)
