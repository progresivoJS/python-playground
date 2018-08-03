# set can be used to eliminate duplicates from sequence.

unique_surnames = set(employee_surnames)


# set comprehension
# Observe carefully what is difference with dict comprehension.
users_first_names = {user.first_name for use in users}

# Understand and user the mathematical set operations
# Union A | B
# Intersection A & B
# Difference A - B
# Symmetric Difference A ^ B

def get_both_popular_and_active_users():
    return set(get_list_of_most_active_users()) & set(get_list_of_most_popular_users())