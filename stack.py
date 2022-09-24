from typing import Iterable, List, Optional, Any
import pair

Node = pair.Pair[Any, int]
Stack = Optional[pair.Pair[Node, "Stack"]]  # type: ignore

empty: Stack = None


def len(stack: Stack) -> int:
    if stack is None:
        return 0
    return pair.snd(pair.fst(stack))


def is_empty(stack: Stack) -> bool:
    return stack is None


def push(head: Any, stack: Stack) -> Stack:
    return pair.mk_pair(pair.mk_pair(head, len(stack) + 1), stack)


def peek(stack: Stack) -> Optional[Any]:
    if stack is None:
        return None
    return pair.fst(pair.fst(stack))


def pop(stack: Stack) -> Stack:
    if stack is None:
        return None
    return pair.snd(stack)


def iter(stack: Stack) -> Iterable[Any]:
    while stack is not None:
        yield peek(stack)
        stack = pop(stack)


def to_list(stack: Stack) -> List[Any]:
    return list(iter(stack))


def from_iter(items: Iterable[Any]) -> Stack:
    ret = empty
    for item in items:
        ret = push(item, ret)
    return ret


if __name__ == "__main__":
    s = push(3, push(2, empty))
    assert peek(s) == 3
    assert peek(pop(s)) == 2
    assert peek(push(100, push(2, push(3, push(45, empty))))) == 100
    assert to_list(s) == [3, 2]
    assert to_list(from_iter([1, 2, 3, 4, 5])) == to_list(
        push(5, push(4, push(3, push(2, push(1, empty)))))
    )
