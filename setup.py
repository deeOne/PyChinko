# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

import setuptools

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(name='PyChinko',
    version='0.1.0',
    description='A Pachinko-style arcade game in Pygame',
    long_description=readme,
    author='Ross W. Grimshaw',
    author_email='grimshanky@gmail.com',
    url='https://github.com/deeOne/PyChinko',
    license=license,
    packages=setuptools.find_packages(exclude=('tests','docs')),    
    classifiers=["Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent"],
    python_requires='>=3.10.5')
    
