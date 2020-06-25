import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active:
while True:
    # Make a random walk:
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # Plot the points in the walk:
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6)) 
    #figsize sets size of output-window in inches. (1 inch per 100 pixels).

    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.Blues,
        edgecolors='none', s=1)
        # range(rw.num_points) creates a list of numbers equal to the number of points in the walk.
        #  This makes early points light and the later points darker.

    # Emphasize the firts and last points:
    ax.scatter(0, 0, c='green', edgecolors='none', s=100) #(0, 0) is the starting point.
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #To get the last point, we access the last values in x- and y-list.

    # Remove the axes:
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #The get_axis method is used to modify the axes and set_visible controls visibility.

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running.lower() == 'n':
        break