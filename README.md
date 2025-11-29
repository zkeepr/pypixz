> [!IMPORTANT]
> The PyPixz repository has been moved here. You can still access the [old repository](https://github.com/YourLabXYZ/PyPIxz).

# PyPIxz
A solution for managing your Python dependencies.

```python
import pypixz

# Install a package
pypixz.install_package("pypixz", version_range=">=2.0.0")

# Install dependencies listed in a requirements.txt file
pypixz.install_requirements("requirements.txt")
```

> [!TIP]
> If you want to use PyPixz to install packages that weren't installed at the beginning of your program, we recommend cloning this repository and adding it to your program.


**PyPIxz** allows you to easily and simply manage the dependencies required by your Python program while ensuring a high level of security.
It is designed to be compatible with other internal modules, such as **log management**, and ensures **compatibility** with any **Python environment from version 3.8** onwards.
**PyPIxz requires no dependencies** to be installed; it is self-contained and relies solely on the **Python standard library**.

[![Contributors](https://img.shields.io/github/contributors/zkeepr/pypixz.svg)](https://github.com/zkeepr/pypixz/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/zkeepr/pypixz.svg)](https://github.com/zkeepr/pypixz/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/zkeepr/pypixz.svg)](https://github.com/zkeepr/pypixz/pulls)
[![Forks](https://img.shields.io/github/forks/zkeepr/pypixz.svg)](https://github.com/zkeepr/pypixz/network/members)

---

## Installing PyPIxz and supported versions

PyPIxz is available on PyPI :

```console
python -m pip install pypixz
```

Install with GitHub :

```console
git clone https://github.com/zkeepr/pypixz.git

# Import PyPixz into your project
cp location/of/the/pypixz/path/pypixz/src/pypixz path/where/you/want/to/place/pypixz/
rm -rf location/of/the/pypixz/path/pypixz
```

PyPIxz officially supports **Python 3.8+** :

> [!CAUTION]
> You can use PyPIxz with a version of Python lower than 3.8, but we do not
> guarantee the compatibility of the program or its updates or security.

---

## Supported Features & Best–Practices

PyPIxz is ready to meet the requirements of managing your dependencies in a
robust and reliable way, for today's needs.

- **Fast Installation**: Manage your dependencies from a `requirements.txt` file.
- **Modularity**: Compatible with other tools and libraries, such as `logging`.
- **Broad Compatibility**: Supports modern Python versions (3.8+).

## License

This project is licensed under the
[MIT License](https://github.com/zkeepr/pypixz/blob/master/LICENSE). See
the license file for more details.

---