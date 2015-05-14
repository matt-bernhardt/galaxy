#!/usr/env/python

# Basic module to generate a galaxy based on passed parameters.
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import galaxy_lib
import random
import planets

# Variables


# Functions
def buildmap(num_systems, min_dist_origin, max_dist_origin, min_dist_system,
             max_dist_system, x_origin, y_origin):
  """Builds Galaxy Map based on passed criteria.

  Current iteration only returns a set of coordinates for planets. No names or
  values around planets are determined.

  Args:
    num_systems: Number of systems to place on map.
    min_dist_origin: Minimum allowable distance from origin.
    max_dist_origin: Maximum allowable distance from origin.
    min_dist_system: Minimum allowable distance from other systems.
    max_dist_system: Maximum allowable distance from other systems.
    x_origin: X coordinate of map origin.
    y_origin: Y coordinate of map origin.

  Returns:
    2 dimensional array of planet coordinates.
  """
  # TODO: Build class array directly in buildmap.
  # Initialize array
  planets = [[0 for z in range(num_systems)] for z in range(num_systems)]
  max_attempts = 1000
  for x in range(0, num_systems - 1):
    # Initial validator
    valid_system = False
    attempt = 0
    while not(valid_system):
      attempt += 1
      if (attempt > max_attempts):
        print "Unable to generate map."
        print "Failed on %s" % x
        quit()
      # Generate random coordinates
      test_x = (random.randint(0, x_origin * 2))
      test_y = (random.randint(0, y_origin * 2))

      dist_to_origin = galaxy_lib.Distance(test_x, test_y, x_origin, y_origin)

      if (min_dist_origin < dist_to_origin < max_dist_origin):
        if (x == 0):
          planets[x][0] = test_x
          planets[x][1] = test_y
          break

        for y in range(0, x):
          dist_to_system = galaxy_lib.Distance(test_x, test_y, planets[y][0],
              planets[y][1])
          if (min_dist_system < dist_to_system < max_dist_system):
            planets[x][0] = test_x
            planets[x][1] = test_y
            valid_system = True
  return planets

def drawmap(planets, x_origin, y_origin):
  """Draws a map of based on a set of coordinates.

  Args:
    planets: Array of class Planet.
    x_origin: X coordinate of origin.
    y_origin: Y coordinate of origin.
  """
  for y in range(0, y_origin * 2):
    for x in range(0, x_origin * 2):
      empty = True
      for z in range(0, len(planets) - 1):
        if ((planets[z].x_pos == x) and (planets[z].y_pos == y)):
          print(" %s" % planets[z].name),
          empty = False
      if ((x == x_origin) and (y == y_origin)):
        print('**'),
      elif (empty):
        print('..'),
    print('\n')


if __name__ == "__main__":
  pass
