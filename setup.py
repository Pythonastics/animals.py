import setuptools

from setuptools import setup

with open("README.md") as fh:
	readme = fh.read()
	
setup(
	name="animals.py",
	author="mischievousdev",
	author_email="miscdev.py@gmail.com",
	version="1.0.0",
	long_description=readme,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	license="MIT",
	keywords='animals api random-image'
)