from typing import NamedTuple
from dataclasses import dataclass


class UnitByte(NamedTuple):
    KB = 1024
    MB = 1024 * 1024
    GB = 1024 * 1024 * 1024