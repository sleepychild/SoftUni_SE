from typing import Generator, Callable, Tuple, Set


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4",
        "Ce O",
        "Mo O Ce",
        "Ee",
        "Mo",
    ),
    (
        "3",
        "Ge Ch O Ne",
        "Nb Mo Tc",
        "O Ne",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    elements: Set[str] = set()
    for _ in range(int(input())):
        for e in input().split():
            elements.add(e)
    tuple(map(print, elements))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
