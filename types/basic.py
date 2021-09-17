from typing import List


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()

    return full_name


def process_items(items: List[str]):
    for item in items:
        print(item)


process_items(["hi!", "bye"])

