 Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
# Step 1: Get the number of inputs
n = int(input("Enter the number of values: "))

# Step 2: Initialize an empty list to collect the values
values = []

# Step 3: Get the values from the user
for _ in range(n):
    value = int(input())
    values.append(value)

# Step 4: Create a set from the list to remove duplicates
unique_values = set(values)

# Step 5: Count duplicates
duplicate_count = len(values) - len(unique_values)

# Step 6: Print the re
