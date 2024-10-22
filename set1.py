Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
# Step 1: Take the number of values from the user
n = int(input("Enter the number of values: "))

# Step 2: Initialize an empty set
values_set = set()

# Step 3: Get n values from the user
for _ in range(n):
    value = int(input())
    values_set.add(value)

# Step 4: Convert the set to a sorted list and print the values
sorted_values = sorted(values_set)
print(" ".join(map(str, sorted_values)))
