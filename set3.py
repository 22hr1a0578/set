Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
# Step 1: Get input for the first set
input_set1 = input("Enter values for the first set separated by space: ")
set1 = set(map(int, input_set1.split()))

# Step 2: Get input for the second set
input_set2 = input("Enter values for the second set separated by space: ")
set2 = set(map(int, input_set2.split()))

# Step 3: Find the difference between the two sets
difference = set1 - set2

# Step 4: Print the unique values in sorted order
print(" ".join(map(str, sorted(difference))))
