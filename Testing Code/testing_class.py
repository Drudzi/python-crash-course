import unittest
#Let's test some classes. Classes are very common and testing them will make you confident in them working!


#   A variety of Assert methods:

#The unittest.TestCase provides several assert methods.
#The assert methods tests whether a condition you believe is true at a specific point is indeed True.

# Table 11-1:

#Method                     Use
# assertEqual(a, b)         Verify that a == b
# assertNotEqual(a, b)      Verify that a != b
# assertTrue(x)             Verify that x is True
# assertFalse(x)            Verify that x is False
# assertIn(item, list)      Verify that item is in list
# assertNotIn(item, list)   Verify that item is not in list

#Above methods only work in a class that inherits from unittest.TestCase.


#   A Class to test:
#Consider a class that helps administer anonymous surveys:

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

#Let's define a survey and make a question:
question = "What was the first programming language you learned?"
my_survey = AnonymousSurvey(question) #Making an instance of AnonymousSurvey with the question.

my_survey.show_question()
print("Enter 'q' at any time to quit.")

while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    my_survey.store_response(response)

print("Thanks to all of you who participated in the survey!")
my_survey.show_results()


#   Testing the AnonymousSurvey Class:
#Let's write a test verifying that a single response to the survey question is stored properly:

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class Anonymous Survey."""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What was the first programming language you learned?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("Python")
        self.assertIn('Python', my_survey.responses) #Cheking if Python has been stored in list of responses.
    
    def test_store_three_responses(self):
        """Test that three responses are stored properly."""
        question = "What was the first programming language you learned?"
        my_survey = AnonymousSurvey(question)
        responses = ['Python', 'Java', 'C++'] #Making up a list of responses for the test.
        
        for response in responses:
            my_survey.store_response(response) #Storing the responses one by one.
        
        for response in responses:
            self.assertIn(response, my_survey.responses) #Testing the responses one by one!

print("Testing survey:")
if __name__ == '__main__':
    unittest.main()


#   The setUp() method:

#In TestAnonymousSurvey, we created a new instance of the actual survey class in each method. 
# The unittest.TestCase class let's you do this more efficient using the setUp() method.
#  The setUp() method allows you to create these instances/objects once and use them in all of your test methods!

#When you include a setUp() in a TestCase class, it runs the setUp() before you run each other method starting with test_.

#We go over the setUp() method in a separate file called "testing_setUp.py"!