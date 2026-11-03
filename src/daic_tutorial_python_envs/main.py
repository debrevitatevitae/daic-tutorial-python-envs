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


def multiply(a: int, b: int) -> int:
    """Multiplies two positive numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a * b


def foo1(a):
    """This function is foo."""
    c = a + 1
    if a > 10:
        return 10
    return a + c


def foo2(a):
    """This function is foo."""
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def foo3(a):
    """This function is foo."""
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def foo4():
    """This function is foo."""
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


def foo5():
    """This function is foo."""
    print("The menus of foo4 are: ", foo4())


def foo6():
    """This function is foo."""
    print("This is foo6")


def main() -> None:
    """Main."""
    print(f"Running daic_tutorial_python_envs version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")
    print(f"foo1(5) = {foo1(5)}")
    print(f"foo2(5) = {foo2(5)}")
    print(f"foo3(5) = {foo3(5)}")
    foo4()
    foo5()


if __name__ == "__main__":
    main()
