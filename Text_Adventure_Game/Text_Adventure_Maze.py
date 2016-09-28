"""
Text Adventure Game
https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/
"""

import maze
import pickle  # Allows us to read a dictionary from a file


if __name__ == "__main__":
    # Using the maze class and object
    m = maze.Maze()

    # Setting coordinates from a dictionary stored in a txt file
    with open('coordinates.txt', 'rb') as handle:
        coordinates = pickle.loads(handle.read())
        m.set_coordinates(coordinates, coordinates.get('Entry'), coordinates.get('Exit'))

    # Displaying the game to the user
    m.default_maze()
