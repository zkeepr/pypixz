#!/usr/bin/env python3

from typing import Optional
import logging
import sys
import subprocess

from ..exceptions import (
    PackageInstallationError
)


def _build_requirement(package: str, version: Optional[str], version_range: Optional[str]) -> str:
    requirement = package  # Latest version installed by default
    if version:
        return f"{package}=={version}"
    elif version_range:
        return f"{package}{version_range}"  # e.g. "package>=1.2.0" or "package!=2.0.0"

    return requirement


def install_package(package: str, version: Optional[str] = None, version_range: Optional[str] = None, logger: Optional[logging.Logger] = None) -> bool:
    if not logger:
        logger = logging

    # Build the package specifier with version or version range
    try:
        requirement = _build_requirement(package, version, version_range)
    except Exception as error:
        raise PackageInstallationError(logger.error(f"Invalid module specification: {error}")) from error

    logger.debug(f"Preparing to install requirement: {requirement}")

    # Build pip command
    command = [
        sys.executable,
        "-m",
        "pip",
        "install",
        requirement,
        "--disable-pip-version-check",  # avoid noisy warnings
        "--no-input",  # prevent hanging
    ]

    logger.debug(f"Executing pip command: {' '.join(command)}")

    try:
        result = subprocess.run(
            command,
            check=True,  # Raises CalledProcessError if the command fails
            capture_output=True,  # Captures stdout and stderr for debugging/logging
            text=True  # Decodes stdout/stderr as text
        )

        logger.info(f"Package '{package}' installed successfully.")
        if result.stdout:
            logger.debug("Pip output:\n%s", result.stdout)

        return True

    except subprocess.CalledProcessError as error:
        error_msg = error.stderr or "Unknown installation error."
        logger.error("Pip installation failed: %s", error_msg)
        raise PackageInstallationError(f"Failed to install package '{package}': {error_msg}") from error

    except OSError as system_error:
        logger.error("System error during installation: %s", system_error)
        raise PackageInstallationError(f"System failure during installation of '{package}': {system_error}") from system_error
