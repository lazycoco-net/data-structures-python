from setuptools import setup, find_packages

setup(
    name='data-structures-python',
    version='1.0',
    packages=find_packages(where="src", exclude=("test",)),
    package_dir={"": "src"}
)
