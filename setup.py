from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in plantix/__init__.py
from plantix import __version__ as version

setup(
	name="plantix",
	version=version,
	description="asd",
	author="asdf",
	author_email="asdf",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
