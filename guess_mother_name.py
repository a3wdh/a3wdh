import random


def guess_mother_name(child_name: str) -> str:
    """Return a guessed mother name for the given child's name.

    The guess is deterministic for a given input but purely heuristic.
    """
    common_mother_names = [
        "Mary",
        "Patricia",
        "Linda",
        "Barbara",
        "Elizabeth",
        "Jennifer",
        "Maria",
        "Susan",
        "Margaret",
        "Dorothy",
    ]
    random.seed(child_name.lower())
    return random.choice(common_mother_names)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python guess_mother_name.py <child_name>")
    else:
        child = sys.argv[1]
        guessed = guess_mother_name(child)
        print(f"Guessed mother name for {child}: {guessed}")
