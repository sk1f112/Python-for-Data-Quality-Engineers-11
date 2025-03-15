import random
import string
from typing import List, Dict


def generate_random_key() -> str:
    """Generate a random lowercase letter as a dictionary key."""
    return random.choice(string.ascii_lowercase)


def generate_random_value(max_value: int) -> int:
    """Generate a random integer value for a dictionary entry."""
    return random.randint(0, max_value)


def generate_single_dict(max_value: int) -> Dict[str, int]:
    """Generate a dictionary with a random number of key-value pairs."""
    random_dict: Dict[str, int] = {}
    num_keys: int = random.randint(1, 5)

    for _ in range(num_keys):
        key: str = generate_random_key()
        value: int = generate_random_value(max_value)
        random_dict[key] = value

    return random_dict


def generate_dicts(count: int, max_value: int) -> List[Dict[str, int]]:
    """Generate a list of dictionaries based on the given count and max value."""
    return [generate_single_dict(max_value) for _ in range(count)]


def merge_dicts(dicts_list: List[Dict[str, int]]) -> Dict[str, int]:
    """Merge dictionaries by keeping the max value for duplicate keys."""
    merged_dict: Dict[str, int] = {}
    key_sources: Dict[str, int] = {}  # Track which dictionary had the max value for each key

    for dict_index, current_dict in enumerate(dicts_list, start=1):
        for key, value in current_dict.items():
            if key not in merged_dict or value > merged_dict[key]:
                merged_dict[key] = value
                key_sources[key] = dict_index

    return rename_keys_if_needed(merged_dict, key_sources, dicts_list)


def rename_keys_if_needed(
        merged_dict: Dict[str, int],
        key_sources: Dict[str, int],
        dicts_list: List[Dict[str, int]]
) -> Dict[str, int]:
    """Rename duplicate keys by appending the source dictionary index."""
    final_dict: Dict[str, int] = {}

    for key, value in merged_dict.items():
        if sum(key in dictionary for dictionary in dicts_list) > 1:
            new_key: str = f"{key}_{key_sources[key]}"
        else:
            new_key = key
        final_dict[new_key] = value

    return final_dict


def process_dict_homework(dict_count: int = 5, max_value: int = 100) -> Dict[str, int]:
    """Generate dictionaries, merge them, and print results."""
    dicts: List[Dict[str, int]] = generate_dicts(dict_count, max_value)

    print("Generated dictionaries:")
    for dictionary in dicts:
        print(dictionary)

    merged_result: Dict[str, int] = merge_dicts(dicts)
    print("\nMerged dictionary:", merged_result)

    return merged_result
