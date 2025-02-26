import random
import string


def generate_dicts():
    # Generate a random number of dictionaries (between 2 and 10)
    num_dicts = random.randint(2, 10)
    dicts_list = []

    for _ in range(num_dicts):
        # Generate a dictionary with a random number of key-value pairs (1 to 5)
        num_keys = random.randint(1, 5)
        random_dict = {}

        for _ in range(num_keys):
            key = random.choice(string.ascii_lowercase)  # Choose a random lowercase letter
            value = random.randint(0, 100)  # Assign a random integer value between 0 and 100
            random_dict[key] = value

        dicts_list.append(random_dict)

    return dicts_list


def merge_dicts(dicts_list):
    merged_dict = {}
    key_sources = {}  # Store which dictionary has the max value for a given key
    for idx, curr_d in enumerate(dicts_list, start=1):  # Iterate through the list of dictionaries
        for key, value in curr_d.items():
            # If key is not in merged_dict, add it
            if key not in merged_dict:
                merged_dict[key] = value
                key_sources[key] = idx  # Track which dictionary the key came from
            else:
                # If key exists, check for the max value and update accordingly
                if value > merged_dict[key]:
                    merged_dict[key] = value
                    key_sources[key] = idx  # Update source dictionary number

    # Rename keys only if they appear in multiple dictionaries
    final_dict = {}
    for key, value in merged_dict.items():
        if sum(key in curr_d for curr_d in dicts_list) > 1:  # Check if key appears in multiple dicts
            new_key = f"{key}_{key_sources[key]}"
        else:
            new_key = key  # Keep key as is if it's unique
        final_dict[new_key] = value

    return final_dict


random_dicts = generate_dicts()
print("Generated dicts:", random_dicts)

merged_result = merge_dicts(random_dicts)
print("Merged dict:", merged_result)
