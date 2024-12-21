def set_operations(set1, set2):
 # Union of sets
 union_result = set1.union(set2)

 # Intersection of sets
 intersection_result = set1.intersection(set2)

 # Difference of sets (set1 - set2 and set2 - set1)
 difference_result1 = set1.difference(set2)
 difference_result2 = set2.difference(set1)

 # Symmetric difference of sets
 symmetric_difference_result = set1.symmetric_difference(set2)

 # Display results
 print("Set 1:", set1)
 print("Set 2:", set2)
 print("Union:", union_result)
 print("Intersection:", intersection_result)
 print("Difference (Set1 - Set2):", difference_result1)
 print("Difference (Set2 - Set1):", difference_result2)
 print("Symmetric Difference:", symmetric_difference_result)
# Function to get set input from the user
def get_set_input(set_number):
 elements = input(f"Enter elements of Set {set_number} separated by spaces: ")
# Convert the input into a set of integers
 return set(map(int, elements.split())) 
# Main program
set1 = get_set_input(1)
set2 = get_set_input(2)
set_operations(set1, set2)