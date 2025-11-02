"""Implementação simples de Pilha (Stack).

Classe Stack com métodos: push, pop, peek, is_empty e __len__.
"""

from typing import List, Generic, TypeVar, Optional

T = TypeVar("T")


class Stack(Generic[T]):
    """Pilha LIFO simples.

    Exemplo:
        s = Stack[int]()
        s.push(1)
        s.pop()  # -> 1
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"
