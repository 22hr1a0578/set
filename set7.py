Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
# Step 1: Get input for the set
input_values = input("Enter values separated by space: ")

# Step 2: Convert the input string into a set of integers
values_set = set(map(int, input_values.split()))

# Step 3: Find the maximum and minimum values
max_value = max(values_set)
min_value = min(values_set)

# Step 4: Print the results
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
