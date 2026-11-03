"""Short definition of my module."""

from daic_tutorial_python_envs import __version__


def add(a: int, b: int) -> int:
    """Adds two positive numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts two positive numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a - b


def foo1(a):
    c = a + 1
    if a > 10:
        return 10
    return a + c


def foo2(a):
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def foo3(a):
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def foo4():

    menu_1 = {"1": "Start Game", "2": "Load Game", "3": "Options", "4": "Exit"}

    # fmt: off
    menu_2 = {
      "1": "Start Game",
      "2": "Load Game",
      "3": "Options",
      "4": "Exit"
  }
    # fmt: on

    return menu_1, menu_2


def main() -> None:
    print(f"Running daic_tutorial_python_envs version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
