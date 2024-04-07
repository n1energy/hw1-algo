from typing import Any
from collections import deque

__all__ = ("Node", "Graph")


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: "Node"):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f"Node({repr(self.value)})"

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
