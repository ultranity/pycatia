from enum import Enum
from typing import TypeVar

from pycatia.enumeration import enumeration_types

T = TypeVar("T", bound=Enum)


class EnumItem(Enum):
    def __int__(self):
        return self.value

    def __str__(self):
        # return super().__str__()
        return self.name


# init index when import
ENUM_INDEX = [x for x in enumeration_types.__dict__.values() if type(x) is tuple]
ENUM_INDEX = {i: x.index(i) for x in ENUM_INDEX for i in x}
