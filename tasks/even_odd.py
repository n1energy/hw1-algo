__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    odd = sum([0 if el % 2 ==0 else el for el in arr])
    even = sum([0 if el % 2 !=0 else el for el in arr])
    if odd == 0:
        return 0
    return even/odd
