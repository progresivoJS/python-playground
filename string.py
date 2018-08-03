# use format function like **kwargs

def get_formmated_user_info(user):
    output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)

def get_format():
    print("{1}, {0}".format("World!", "Hello"))

get_format()
    
# join
# use ''.join() instead of string append
# It's faster and use less memory.

result_list = ['I', 'am', 'Groot']
result_string = '-'.join(result_list)
print(result_string)

# chain string functions.
# But no more than three chained functions.
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip().upper().replace(':', ' by')
print(formatted_book_info)

