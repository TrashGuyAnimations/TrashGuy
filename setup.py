# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='trashguy',
    version=__import__("trashguy").__version__,
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True,
    install_requires=[],
)
