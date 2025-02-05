import argparse
from dataclasses import dataclass


@dataclass
class Bar:
    """
    A class used to represent a bar of histogram.

    Attributes:
        key (str): a character to represent
        count (int): a count of the key occurrence
    """

    key: str
    count: int


@dataclass
class MinMax:
    """
    A class used to represent min and max bars in the histogram.

    Attributes:
        min (Bar): a character to represent
        max (Bar): a count of the key occurrence
    """

    min: Bar
    max: Bar


def add_numbers(x: int, y: int) -> int:
    """Add two numbers together.

    Args:a
      x (int): a number
      y (int): a number

    Returns:
      (int). The sum of the two numbers.
    """
    return x + y


def subtract_numbers(x: int, y: int) -> int:
    """Subtract two numbers together.

    Args:a
      x (int): a number
      y (int): a number

    Returns:
      (int). The difference of the two numbers.
    """
    return x - y


def get_filename_from_args(args: list[str]) -> str:
    """Get filename from the passed arguments.

    Args:a
      args (str): arguments

    Returns:
      (str). file name
    """
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    return parser.parse_args(args).fname


def clean_line(s: str) -> str:
    """Clean the line by stripping empty spaces at both ends of the string.

    Args:a
      s (str): string

    Returns:
      (str). stripped string
    """
    return s.lower().strip()


def get_lines_from_file(filename: str) -> list[str]:
    """Get a list of line in the file.

    Args:a
      filename (str): file name

    Returns:
      (list). list of lines in the file
    """
    lines = None
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines


def get_counter_from_list(lines: list) -> dict[str, int]:
    """Get counter dictionary from list of lines.

    Args:
        lines (list): list of lines

    Returns:
        (dict). dictionary mapping from character to its occurrence
    """
    counter = {}
    for line in lines:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
    return counter


def find_min_bar(counter: dict) -> Bar:
    """Find min key and its corresponding values.

    Args:
        counter (dict): dictionary mapping from character to its occurrence

    Returns:
        (Bar). the min key and count.
    """
    min_key = min(counter, key=counter.get)
    return Bar(min_key, counter[min_key])


def find_max_bar(counter: dict) -> Bar:
    """Find max key and its corresponding values.

    Args:
        counter (dict): dictionary mapping from character to its occurrence

    Returns:
        (Bar). the max key and count.
    """
    max_key = max(counter, key=counter.get)
    return Bar(max_key, counter[max_key])


def find_min_max(counter: dict) -> MinMax:
    """Find min and max key and its corresponding values.

    Args:
        counter (dict): dictionary mapping from character to its occurrence

    Returns:
        (MinMax). the min and max keys and counts.
    """
    min_bar = find_min_bar(counter)
    max_bar = find_max_bar(counter)
    return MinMax(min=min_bar, max=max_bar)


def histlib(args: list[str]) -> None:  # pragma: no cover
    """Print min_key, min_counter, max_key, and max_counter of the histogram.

    Args:
        args: arguments
    """
    filename = get_filename_from_args(args)
    lines = get_lines_from_file(filename)
    counter = get_counter_from_list(lines)
    min_max = find_min_max(counter)
    print(f"Min Key = {min_max.min.key} with count = {min_max.min.count}")
    print(f"Max Key = {min_max.max.key} with count = {min_max.max.count}")
