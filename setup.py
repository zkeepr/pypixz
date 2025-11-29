#!/usr/bin/env python3

from setuptools import setup

VERSION = "2.0.0"
DESCRIPTION = "A solution for managing your Python dependencies"

setup(
    name="pypixz",
    version=VERSION,
    author="ZKeepr - Organisation on GitHub",
    url="https://github.com/zkeepr/pypixz",
    packages=["pypixz"],
    package_data={"": ["LICENSE"]},
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Stable",

        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",

        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    project_urls={
        "Source": "https://github.com/zkeepr/pypixz",
    },
    keywords=["python", "package", "installer", "pypi", "pip", "manage", "dependencies"]
)
