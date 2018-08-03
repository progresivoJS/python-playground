# set can be used to eliminate duplicates from sequence.

unique_surnames = set(employee_surnames)


# set comprehension
# Observe carefully what is difference with dict comprehension.
users_first_names = {user.first_name for use in users}