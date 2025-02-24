import random
# Generate a list of 100 random numbers ranging from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]

print(random_numbers)

# Get the length of the list
list_length = len(random_numbers)
# Implementing Bubble Sort algorithm to sort the list in ascending order
for pass_num in range(list_length):
    for index in range(0, list_length - pass_num - 1):  # Iterate through the list, ignoring the last sorted elements
        if random_numbers[index] > random_numbers[index + 1]: # Compare elements
            random_numbers[index], random_numbers[index + 1] = random_numbers[index + 1], random_numbers[index] #Swap elements in list

print(random_numbers)

#empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

for num in random_numbers:
    if num % 2 == 0: #Check if the number is even
        even_numbers.append(num)
    elif num % 2 != 0: #Check if the number is odd
        odd_numbers.append(num)

# Calculate the average for even numbers
even_avg = sum(even_numbers) / len(even_numbers)
# Calculate the average for odd numbers
odd_avg = sum(odd_numbers) / len(odd_numbers)

# Print the average results
print("Average of even numbers:", even_avg)
print("Average of odd numbers:", odd_avg)