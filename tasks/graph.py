from collections import deque
from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = []
        queue = deque([self._root])
        # visited.append(self._root)
        while queue:
            current_node = queue.popleft()
            if current_node in visited:
                continue
            visited.append(current_node)
            bound = current_node.outbound
            for next_node in current_node.outbound[::-1]:
                queue.appendleft(next_node)
        return visited

    def bfs(self) -> list[Node]:
        visited = []
        queue = deque([self._root])
        visited.append(self._root)
        while queue:
            current_node = queue.popleft()
            for next_node in current_node.outbound:
                if next_node not in visited:
                    visited.append(next_node)
                    queue.append(next_node)
        return visited
