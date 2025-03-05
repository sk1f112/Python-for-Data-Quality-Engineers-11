import random
import string

# Generate random keys for dict
def generate_random_key():
    return random.choice(string.ascii_lowercase)

# Generate random value for dict
def generate_random_value():
    return random.randint(0, 100)

# Generate a dictionary with a random number of key-value pairs (1 to 5)
def generate_single_dict():
    random_dict = {}
    num_keys = random.randint(1, 5)

    for _ in range(num_keys):
        key = generate_random_key()
        value = generate_random_value()
        random_dict[key] = value

    return random_dict

# Generate a random number of dictionaries (between 2 and 10)
def generate_dicts(count=None):
    dicts_list = []
    num_dicts = count or random.randint(2, 10)

    for _ in range(num_dicts):
        random_dict = generate_single_dict()
        dicts_list.append(random_dict)

    return dicts_list

# Merge dicts
def merge_dicts(dicts_list):
    merged_dict = {}
    key_sources = {} # Store which dictionary has the max value for a given key

    for dict_index, current_dict in enumerate(dicts_list, start=1): # Iterate through the list of dictionaries
        for key, value in current_dict.items():
            # If key is not in merged_dict, add it
            if key not in merged_dict:
                merged_dict[key] = value
                key_sources[key] = dict_index # Track which dictionary the key came from
            # If key exists, check for the max value and update accordingly
            elif value > merged_dict[key]:
                merged_dict[key] = value
                key_sources[key] = dict_index # Update source dictionary number

    return rename_keys_if_needed(merged_dict, key_sources, dicts_list)

# Rename keys only if they appear in multiple dictionaries
def rename_keys_if_needed(merged_dict, key_sources, dicts_list):
    final_dict = {}

    for key, value in merged_dict.items():
        if sum(key in curr_d for curr_d in dicts_list) > 1:  # Check if key appears in multiple dicts
            new_key = f"{key}_{key_sources[key]}"
        else:
            new_key = key  # Keep key as is if it's unique
        final_dict[new_key] = value

    return final_dict


def process_dict_homework(dict_count=None):
    dicts = generate_dicts(dict_count)
    print("Generated dicts:")
    for d in dicts:
        print(d)

    merged_result = merge_dicts(dicts)
    print("\nMerged dict:", merged_result)

    return merged_result