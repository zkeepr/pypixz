#!/usr/bin/env python3

import logging

from src.pypixz import install_package


logging.basicConfig(
    level=logging.DEBUG,  # Niveau minimal affiché
    format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("main")
install_package("pypixz", version_range="<=1.1.3", logger=logger)
