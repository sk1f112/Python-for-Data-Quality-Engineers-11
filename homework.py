import random
# Generate a list of 100 random numbers ranging from 0 to 1000
list1 = [random.randint(0, 1000) for _ in range(100)]

# Get the length of the list
n = len(list1)
# Implementing Bubble Sort algorithm to sort the list in ascending order
for i in range(n):
    for j in range(0, n - i - 1):  # Iterate through the list, ignoring the last sorted elements
        if list1[j] > list1[j + 1]: # Compare elements
            list1[j], list1[j + 1] = list1[j + 1], list1[j] #Swap elements in list

#empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

for num in list1:
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