#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class stats:
    comp: int = 0
    swap: int = 0
    basic: int = 0
    time: float = 0
    mem: float = 0

    def __str__(self):
        return f"{self.comp},{self.swap},{self.basic},{self.time},{self.mem}"


def init():
    global stat
    stat = stats()
