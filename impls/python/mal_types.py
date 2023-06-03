import abc
import typing as t


__all__ = ['Nil', 'Bool', 'Int', 'Real', 'Keyword', 'String', 'List', 'Vector', 'HashMap',
           'AtomType']


class MalType(abc.ABC):
    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError


class Nil(MalType):
    def __repr__(self):
        return 'nil'


class Bool(MalType):
    def __init__(self, val: bool):
        self.val = val

    def __repr__(self):
        return str(self.val)


class Int(MalType):
    def __init__(self, val: int):
        self.val = val

    def __repr__(self):
        return str(self.val)


class Real(MalType):
    def __init__(self, val: float):
        self.val = val

    def __repr__(self):
        return str(self.val)


class Keyword(MalType):
    def __init__(self, val: str):
        self.val = val

    def __repr__(self):
        return f':{self.val}'


class String(MalType):
    def __init__(self, val: str):
        self.val = val

    def __repr__(self):
        return f'"{self.val}"'


class List(MalType):
    def __init__(self, items: t.List[MalType]):
        self.items = items

    def first(self) -> MalType:
        return self.items[0]

    def rest(self) -> 'List':
        return List(self.items[1:])

    def __repr__(self):
        return f'({", ".join(repr(item) for item in self.items)})'


class Vector(MalType):
    def __init__(self, items: t.List[MalType]):
        self.items = items

    def first(self) -> MalType:
        return self.items[0]

    def rest(self) -> List:
        return List(self.items[1:])

    def __repr__(self):
        return f'[{", ".join(repr(item) for item in self.items)}]'


class HashMap(MalType):
    def __init__(self, key_vals: t.Dict[MalType, MalType]):
        self.key_vals = key_vals

    def get(self, key: MalType) -> MalType:
        return self.key_vals[key]

    def __repr__(self):
        return f'{{{", ".join(f"{k}:{v}" for k, v in self.key_vals.items())}}}'
