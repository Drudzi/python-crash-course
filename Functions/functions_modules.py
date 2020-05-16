#   STORING YOUR FUNCTIONS IN MODULES:
#You can store your functions in separate files called modules.
#You can then import your modules into your main programs.

#The import statement lets Python use functions from modules in your main program.

#Storing your functions in a separate file allows you to hide details of your code and focus on the higher-level logic.


# Importing an entire module:
import module #This line copies functions from module.py to this file.

#To call a function from an imported library...
#type name of module(file) followed by a dot and then functionname():

# module_name.function_name()

module.greet_user_1('drudzi')


# Importing specific functions:

#from module_name import function_name                          If you want to import one function.
#from module_name import function_0, function_ 1, function_2    If you want to import more functions.

from module import build_person_1
me = build_person_1('jonathan', 'axelsson', 'reine', 18)
print(me)
#Notice that you don't need to enter module_name. before function_name when specific functions are imported.


# Using as to give a function an alias:
#If a function name you want to import, conflicts with an existing function...
#...you can use the as-statement to give it a nickname.
from module import get_formatted_name as gtn
#Now, get_formatted_name is called gtn in this program.
print(gtn('jonathan', 'axelsson'))


# Using as to give a module an alias:
#You can also provide an alias for a module, which allows you to faster call imported functions from that module.
import module as m
#Now, module is called m in this program.
m.greet_user_1('drudzi')


# Importing all functions in a module:
#from module_name import *
#The asterisk tells python to copy all the functions into your programs, as if they were original...
                        #...which means you don't have to call all of them with module_name. in front.

#Don't use this method when importing large modules, it might include functions confliction with already existing ones.



#   STYLING FUNCTIONS:

#Always keep in mind when writing your functions, that others may want to use your functions some day.

#Use descriptive names that use lowercase letters and underscores for both functions and modules.
#ALWAYS include a docstring in the beginning of function that describes what it's for.

#If specifying default values, never uses spaces on either side of equal signs:
#def function_name(parameter_0, parameter_1='default')
#This should also be used when calling keyword-arguments: # (keyword='value')

#Don't write more than 79 characters per line, PEP8.

#Separate functions with two blank lines.

#All import statements should be written in the beginning of your program...
#...if you don't write some comments about the program at the very top.