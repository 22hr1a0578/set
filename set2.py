Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
# Step 1: Get input in a single line separated by space
input_values = input("Enter values separated by space: ")

# Step 2: Split the input string into a list of integers and convert to a set
values_set = set(map(int, input_values.split()))

# Step 3: Convert the set to a sorted list and print the values
sorted_values = sorted(values_set)
print(" ".join(map(str, sorted_values)))
