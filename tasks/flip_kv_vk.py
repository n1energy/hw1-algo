from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)

KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    flipped_dict = {value: key for key, value in d.items()}
    return flipped_dict


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    flipped_dict = {}
    for key, value in d.items():
        flipped_dict[value] = flipped_dict.get(value, [])
        flipped_dict[value].append(key)
    return flipped_dict
