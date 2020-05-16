#   The setUp() method:

#In TestAnonymousSurvey, we created a new instance of the actual survey class in each method. 
# The unittest.TestCase class let's you do this more efficient using the setUp() method.
#  The setUp() method allows you to create these instances/objects once and use them in all of your test methods!

#When you include a setUp() in a TestCase class, it runs the setUp() before you run each other method starting with test_.

#Let's use setUp() to create a survey instance and a set of responses that we can use in our test methods!:

import unittest
from testing_class import AnonymousSurvey #Importing the survey class to begin with.

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class Anonymous Survey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What was the first programming language you learned?"
        self.my_survey = AnonymousSurvey(question) #Creating a survey, with a question. Can be used in all methods with self.
        self.responses = ['Python', 'JavaScript', 'C++'] #Setting up some samples of responses that can be accessed in any method.

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0]) #Using the store_response method from our setUp class to store first item in responses list.
        self.assertIn(self.responses[0], self.my_survey.responses) #Testing if the first item in the setup list is stored properly.
    
    def test_store_three_responses(self):
        """Test that three responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response) #Storing every response in self.responses using store_response method.
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses) #Testing if the responses were stored correctly.

print("Testing survey:")
if __name__ == '__main__':
    unittest.main()

# USING SETUP() IS WAY MORE EFFICIENT THAN CREATING NEW INSTANCES IN EACH TEST METHOD.