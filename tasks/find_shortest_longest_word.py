from typing import Optional
import re

__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    l = re.findall(r"\w+", text)
    try:
        longest = max(l, key=len)
        shortest = min(l, key=len)
        s = (shortest, longest)

    except ValueError:
        s = (None, None)
    return s
