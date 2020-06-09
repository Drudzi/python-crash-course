#   Rolling Dice with Plotly.
#We'll use plotly to produce interactive visualizations.
# Plotly is particularly useful when you want to display visuals in in a browser...
#  because they will automatically fit the users screen.

# In this project, we'll analyze the results of rolling dice.
#  We will try to determine which numbers are most likely to occur.

from random import randint

class Die:
    """A class representing a single Die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)