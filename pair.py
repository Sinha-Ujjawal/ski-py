from typing import Generic, Tuple, TypeVar
import ski

L = TypeVar("L")
R = TypeVar("R")


class Pair(Generic[L, R]):
    def __init__(self) -> None:
        raise NotImplementedError("Should not be used")

    def __call__(self, func):
        return self(func)


def mk_pair(left: L, right: R) -> Pair[L, R]:
    return ski.V(left)(right)


def fst(p: Pair[L, R]) -> L:
    return p(ski.K)


def snd(p: Pair[L, R]) -> R:
    return p(ski.KI)


def unpack(p: Pair[L, R]) -> Tuple[L, R]:
    return fst(p), snd(p)
