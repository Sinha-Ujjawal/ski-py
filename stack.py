from typing import Iterable, List, Optional, Any
import pair
import list as linked_list

Node = pair.Pair[Any, int]
Stack = Optional[pair.Pair[Node, "Stack"]]  # type: ignore

empty: Stack = None


def len(stack: Stack) -> int:
    return linked_list.len(stack)


def is_empty(stack: Stack) -> bool:
    return linked_list.is_empty(stack)


def push(head: Any, stack: Stack) -> Stack:
    return linked_list.cons(head, stack)


def peek(stack: Stack) -> Optional[Any]:
    return linked_list.head(stack)


def pop(stack: Stack) -> Stack:
    return linked_list.tail(stack)


def iter(stack: Stack) -> Iterable[Any]:
    yield from linked_list.iter(stack)


def to_list(stack: Stack) -> List[Any]:
    return list(iter(stack))


def from_iter(items: Iterable[Any]) -> Stack:
    return linked_list.from_iter(items)


if __name__ == "__main__":
    s = push(3, push(2, empty))
    assert peek(s) == 3
    assert peek(pop(s)) == 2
    assert peek(push(100, push(2, push(3, push(45, empty))))) == 100
    assert to_list(s) == [3, 2]
    assert to_list(from_iter([1, 2, 3, 4, 5])) == to_list(
        push(5, push(4, push(3, push(2, push(1, empty)))))
    )
