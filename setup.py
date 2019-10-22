#!/usr/bin/env python

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst")) as fd:
    README = fd.read()


def get_requirements(requirements_file="requirements-prod.txt"):
    """Get the contents of a file listing the requirements.

    Args:
        requirements_file (str): The path to the requirements file, relative
                                 to this file.

    Returns:
        list: the list of requirements, or an empty list if
              ``requirements_file`` could not be opened or read.
    """
    with open(requirements_file) as fd:
        lines = fd.readlines()
    dependencies = []
    for line in lines:
        maybe_dep = line.strip()
        if maybe_dep.startswith("#"):
            # Skip pure comment lines
            continue
        if maybe_dep.startswith("git+"):
            # VCS reference for dev purposes, expect a trailing comment
            # with the normal requirement
            __, __, maybe_dep = maybe_dep.rpartition("#")
        else:
            # Ignore any trailing comment
            maybe_dep, __, __ = maybe_dep.partition("#")
        # Remove any whitespace and assume non-empty results are dependencies
        maybe_dep = maybe_dep.strip()
        if maybe_dep:
            dependencies.append(maybe_dep)
    return dependencies


setup(
    name="patchwork",
    version="3.0.0a1",
    description="A patch tracking system for community-based projects.",
    long_description=README,
    url="https://github.com/getpatchwork/patchwork/",
    # Possible options are at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="GPLv2",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements(),
    tests_require=get_requirements(requirements_file="requirements-test.txt"),
    test_suite="patchwork.tests",
)
