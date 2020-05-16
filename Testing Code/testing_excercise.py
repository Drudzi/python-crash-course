# 11-3. Employee:
import unittest

class Employee:
    """Model an employee and rise his salary if you'd like to."""
    
    def __init__(self, first, last, annual_salary):
        """Initialize name and his current annual salary."""
        self.first_name = first.title()
        self.last_name = last.title()
        self.salary = annual_salary
    
    def give_raise(self, amount=5_000):
        """Raise employee's annual salary."""
        self.salary += amount
        print(f"{self.first_name} {self.last_name}'s annual salary has been raised to ${self.salary}.")

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Set up a sample employee to test."""
        self.current_salary = 100_000
        self.employee = Employee('jonathan', 'axelsson', self.current_salary)

    def test_default_raise(self):
        """Test if default raise method works."""
        self.employee.give_raise()
        self.current_salary += 5_000
        self.assertEqual(self.employee.salary, self.current_salary)
    
    def test_custom_raise(self):
        """Test if custom raise amount works."""
        custom_raise_amount = 10_000
        self.current_salary += custom_raise_amount
        self.employee.give_raise(10_000)
        self.assertEqual(self.employee.salary, self.current_salary)

if __name__ == '__main__':
    unittest.main()