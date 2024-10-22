Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
# Step 1: Get input for the first set
input_set1 = input("Enter values for the first set separated by space: ")
set1 = set(map(int, input_set1.split()))

# Step 2: Get input for the second set
input_set2 = input("Enter values for the second set separated by space: ")
set2 = set(map(int, input_set2.split()))

# Step 3: Find the intersection of the two sets
common_values = set1 & set2

# Step 4: Print the common values in sorted order
print(" ".join(map(str, sorted(common_values))))
