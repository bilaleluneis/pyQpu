from __future__ import annotations
from abc import ABC
from enum import Enum, unique
from typing import TypeVar, List, final, Final, Iterable
from qpu import execute

__author__ = "Bilal El Uneis"
__since__ = "Nov 2019"
__email__ = "bilaleluneis@gmail.com"

VICTOR_LENGTH: Final = 16
QpuDataType = TypeVar('QpuDataType', List[int], List[float])


@final
@unique
class Op(Enum):
    ADD: str = "ADD"


@final
class Vector:
    def __init__(self, vector: QpuDataType):
        Vector.__validate(vector)
        self.__vector: QpuDataType = vector

    @property
    def value(self) -> QpuDataType:
        return self.__vector

    @staticmethod
    def __validate(vector):
        if not type(vector) in [list, List, Iterable]:
            raise VectorTypeError("Vector Type is not Valid!")

        valid_vector_content = all(type(x) is int for x in vector) or all(type(x) is float for x in vector)
        if not valid_vector_content:
            raise VectorTypeError("Vector Type is not Valid!")

        if len(vector) != VICTOR_LENGTH:
            raise VectorSizeError("Vector Size is not Valid!")

    def __add__(self, vector: Vector) -> Vector:
        result: QpuDataType = execute(self.value, vector.value, Op.ADD.value, 1)
        return Vector(result)


class VectorError(ABC, Exception):
    pass


@final
class VectorSizeError(VectorError):
    pass


@final
class VectorTypeError(VectorError):
    pass
