#   RANDOM WALKS:
# A random walk is a path that is determined by a series of completely random decisions.
#  Random walks have practical applications in nature, physics, biology, chemistry and economics.
#
#   ex) A pollen grain floating on a drop of water moves across the surface of the water because...
#        it's constantly pushed around by water molecules. Molecular motion in a water drop is random...
#         so the path a pollen grain traces on the surface is a random walk.
#
# Random walks can model many real-world situations.

from random import choice
# choice chooses a random item in a list of items.

# Let's create a class that will make random decisions about which direction the walk should take:
class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points #Number of points in the walk.

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue #continue goes back to the beginning of the loop.
            
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            #To get the right position, we need to base it on where it already is.
            # That's why we take the x- and y-values of the latest added position ([-1]).
            #  From there on, we add the next x- and y-steps to get the new position.

            self.x_values.append(x)
            self.y_values.append(y)
            #We append the new position to the lists.
        
    def get_step(self):
        """Get the a new position."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3 ,4])
        #choice chooses a random item from a given list of items.

        step = direction * distance
        return step