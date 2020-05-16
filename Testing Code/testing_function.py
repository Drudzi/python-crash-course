#To catch problems in your code, you can test it using the unittest module in Python Standard library.
#Writing tests will make you confident that your code works.


#   Testing a Function:
#Sample function to test:

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("Please give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}")

#If you want to modify the get_formatted_name() function so it also can handle middle names, you want to make sure you don't break...
#...the way it handles only a first and a last name.
#For that, we can automate the testing with unittest module.


#   Unit tests and test cases:
#unittest provides tools for testing your code.

# A so called unit test verifies that one specific aspect of a function's behaviour is correct.
# A so called test case is a collection of unit tests that together prove that a function behaves the way it's supposed to.

#A good test case considers all the possible kinds of input a function can recieve. That's called full coverage.

#It's often good enough to write tests for your code's critical behaviors, and then go for full coverage if it sees widespread use.


#   A passing test:
#Let's verify get_formatted_name() works when it's given a first and a last name:
import unittest
print("Testing get_formatted_name().")
class NamesTestCase(unittest.TestCase): #Test-class must inherit from unittest.TestCase so Python knows how to run the test methods.
    #When defining a test-case-class, always include Test in class name, make sure to make it descriptive and relative to the function you're testing.
    """Tests for get_formatted_name()."""

    def test_first_last_name(self): #With this method, we verify that names with only a first and a last name are formatted correctly.
        #Name test methods beginning with 'test_', then Python runs these tests automatically.
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #Assert methods are very useful...
        #...they verify that a result you recieved matches the result you expected to recieve.
        #assert.Equal checks if first argument equals second argument and returns positive if it did.

if __name__ == '__main__': #This __name__ variable is set when program is executed.
    #If the file is being run as your main program, __name__ is set to __main__.
    unittest.main() #If that's the case, we run unittest.main() which actually runs the test case.

#Output looks like this when this test passes:

#   .
#   .............................................
#   Ran 1 test in 0.000s
#   OK


#   A failing test:
#Let's modify get_formatted_name so it can also take middle name, but fail when onlt first and last name are given:

def get_formatted_name_1(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

# class NamesTestCase_1(unittest.TestCase): #New class testing modified function.
#     """Tests for get_formatted_name()."""

#     def test_first_last_name(self):
#         """Do names like 'Janis Joplin' work?"""
#         formatted_name = get_formatted_name_1('janis', 'joplin') THIS WOULD GIVE ERROR BCUZ IT NEEDS THREE ARGUMENTS
#         self.assertEqual(formatted_name, 'Janis Joplin')

# if __name__ == '__main__':
#     unittest.main()


#   Responding to a Failed test:
#When a test fails, change the tested code. Not the test itself.

#Let's solve the positional-arguments-error that occured above making middle name optional:

def get_formatted_name_2(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# print("Testing get_formatted_name_2().")

# class NamesTestCase_2(unittest.TestCase): #New class testing modified function.
#     """Tests for get_formatted_name()."""

#     def test_first_last_name(self):
#         """Do names like 'Janis Joplin' work?"""
#         formatted_name = get_formatted_name_2('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

# if __name__ == '__main__':
#     unittest.main()


#   Adding new tests:

class NamesTestCase_3(unittest.TestCase): #New class testing modified function.
    """Tests for get_formatted_name()."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name_2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name_2('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

#This will give:
#   ..
#   ......................................
#   Ran 2 tests in 0.000s
#   OK