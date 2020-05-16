def greet_user_1(username): #When defining function, enter a variable name inside parentheses.
    #When calling function, write some value in parentheses and it is assoctiated with variable(username) in function.
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title() #THIS IS THE RETURN COMMAND. Given value is the return value.

def build_person_1(first_name, last_name, middle_name='', age=None): #None is like ''(empty string), but for numbers. 
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name} #Building a dictionary of name.
    if middle_name:
        person['middle'] = middle_name
    if age: #If age != None, do the following.
        person['age'] = age
    return person