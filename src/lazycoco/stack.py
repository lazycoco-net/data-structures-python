from typing import List, TypeVar, NoReturn, Generic

T = TypeVar('T')


class EmptyStackException(Exception):
    pass


class MyStack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, element: T) -> NoReturn:
        self.items.append(element)

    def pop(self) -> T:
        if self.empty():
            raise EmptyStackException()
        return self.items.pop()

    def peek(self) -> T:
        if self.empty():
            raise EmptyStackException()
        return self.items[-1]

    def empty(self) -> bool:
        return not self.items
