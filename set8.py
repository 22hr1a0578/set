 Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
# Step 1: Get input for the first set
input_set1 = input("Enter values for the first set separated by space: ")
set1 = set(map(int, input_set1.split()))

# Step 2: Get input for the second set
input_set2 = input("Enter values for the second set separated by space: ")
set2 = set(map(int, input_set2.split()))

# Step 3: Update the first set with the values from the second set
set1.update(set2)

# Step 4: Print the updated set
print(" ".join(map(str, sorted(set1))))
