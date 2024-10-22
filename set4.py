Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
# Step 1: Get input for the set
input_set = input("Enter values for the set separated by space: ")
value_to_delete = int(input("Enter the value to delete: "))

# Convert the input into a set
my_set = set(map(int, input_set.split()))

# Step 2: Attempt to remove the specified value
if value_to_delete in my_set:
    my_set.remove(value_to_delete)
    # Step 3: Print the updated set
    print(" ".join(map(str, sorted(my_set))))
else:
    # If the value is not present
    print("Given value is not present in the set list.")
