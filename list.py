from typing import Iterable, List, Optional, Any
import pair

Node = pair.Pair[Any, int]
LinkedList = Optional[pair.Pair[Node, "LinkedList"]]  # type: ignore

empty: LinkedList = None


def len(linked_list: LinkedList) -> int:
    if linked_list is None:
        return 0
    return pair.snd(pair.fst(linked_list))


def is_empty(linked_list: LinkedList) -> bool:
    return linked_list is None


def cons(head: Any, linked_list: LinkedList) -> LinkedList:
    return pair.mk_pair(pair.mk_pair(head, len(linked_list) + 1), linked_list)


def head(linked_list: LinkedList) -> Optional[Any]:
    if linked_list is None:
        return None
    return pair.fst(pair.fst(linked_list))


def tail(linked_list: LinkedList) -> LinkedList:
    if linked_list is None:
        return None
    return pair.snd(linked_list)


def iter(linked_list: LinkedList) -> Iterable[Any]:
    while linked_list is not None:
        yield head(linked_list)
        linked_list = tail(linked_list)


def to_python_list(linked_list: LinkedList) -> List[Any]:
    return list(iter(linked_list))


def from_iter(items: Iterable[Any]) -> LinkedList:
    ret = empty
    for item in items:
        ret = cons(item, ret)
    return ret


if __name__ == "__main__":
    s = cons(3, cons(2, empty))
    assert head(s) == 3
    assert head(tail(s)) == 2
    assert head(cons(100, cons(2, cons(3, cons(45, empty))))) == 100
    assert to_python_list(s) == [3, 2]
    assert to_python_list(from_iter([1, 2, 3, 4, 5])) == to_python_list(
        cons(5, cons(4, cons(3, cons(2, cons(1, empty)))))
    )
