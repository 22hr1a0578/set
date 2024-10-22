Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
# Step 1: Get input in a single line separated by space
input_values = input("Enter values separated by space: ")

# Step 2: Split the input string and convert to a set
values_set = set(map(int, input_values.split()))

# Step 3: Print the number of unique elements in the set
print(len(values_set))
