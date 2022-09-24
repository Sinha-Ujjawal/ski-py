from typing import Iterable, List, Optional, Any
import pair
import stack

Deque = pair.Pair[stack.Stack, stack.Stack]

empty: Deque = pair.mk_pair(stack.empty, stack.empty)


def len(deque: Deque) -> int:
    left_stack, right_stack = pair.unpack(deque)
    return stack.len(left_stack) + stack.len(right_stack)


def is_empty(deque: Deque) -> bool:
    left_stack, right_stack = pair.unpack(deque)
    return stack.is_empty(left_stack) and stack.is_empty(right_stack)


def push_left(x: Any, deque: Deque) -> Deque:
    left_stack, right_stack = pair.unpack(deque)
    return _rebalance(pair.mk_pair(stack.push(x, left_stack), right_stack))


def push_right(x: Any, deque: Deque) -> Deque:
    left_stack, right_stack = pair.unpack(deque)
    return _rebalance(pair.mk_pair(left_stack, stack.push(x, right_stack)))


def pop_left(deque: Deque) -> Deque:
    if len(deque) == 1:
        return empty
    left_stack, right_stack = pair.unpack(deque)
    return _rebalance(pair.mk_pair(stack.pop(left_stack), right_stack))


def pop_right(deque: Deque) -> Deque:
    if len(deque) == 1:
        return empty
    left_stack, right_stack = pair.unpack(deque)
    return _rebalance(pair.mk_pair(left_stack, stack.pop(right_stack)))


def peek_left(deque: Deque) -> Optional[Any]:
    left_stack, right_stack = pair.unpack(deque)
    if len(deque) == 1 and stack.is_empty(left_stack):
        return stack.peek(right_stack)
    return stack.peek(left_stack)


def peek_right(deque: Deque) -> Optional[Any]:
    left_stack, right_stack = pair.unpack(deque)
    if len(deque) == 1 and stack.is_empty(right_stack):
        return stack.peek(left_stack)
    return stack.peek(right_stack)


def iter(deque: Deque) -> Iterable[Any]:
    while not is_empty(deque):
        yield peek_left(deque)
        deque = pop_left(deque)


def to_list(deque: Deque) -> List[Any]:
    return list(iter(deque))


def from_iter(items: Iterable[Any]) -> Deque:
    ret = empty
    for item in items:
        ret = push_right(item, ret)
    return ret


def _rebalance(deque: Deque) -> Deque:
    left_stack, right_stack = pair.unpack(deque)
    if stack.is_empty(right_stack):
        l = stack.len(left_stack)
        items = stack.to_list(left_stack)
        new_left_stack = stack.from_iter(items[: l >> 1][::-1])
        new_right_stack = stack.from_iter(items[l >> 1 :])
        return pair.mk_pair(new_left_stack, new_right_stack)
    elif stack.is_empty(left_stack):
        l = stack.len(right_stack)
        items = stack.to_list(right_stack)
        new_left_stack = stack.from_iter(items[l >> 1 :])
        new_right_stack = stack.from_iter(items[: l >> 1][::-1])
        return pair.mk_pair(new_left_stack, new_right_stack)
    else:
        return deque


if __name__ == "__main__":
    assert peek_right(push_left(100, push_left(45, empty))) == 45
    assert peek_left(from_iter([1, 2, 3, 4, 5])) == 1
    assert peek_right(from_iter([1, 2, 3, 4, 5])) == 5
    assert peek_left(pop_left(from_iter([1, 2, 3, 4, 5]))) == 2
    assert peek_left(pop_left(push_left(3, empty))) is None
    assert to_list(from_iter([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
