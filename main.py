#!/usr/env/python

# Base script for Galaxy.
# Stand in until further notice
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import galaxy_lib
import galaxy_map
import planets
import fleets

# Variables
planet_list = []
fleet_list = []

# Functions
def GenerateMap():
  """Wraps galaxy_map.buildmap the builds array of class Planet.

  Returns:
    Array of class Planet
  """
  # TODO: Owner assignment
  # Variables
  planet_array = []
  x = 0

  for item in galaxy_map.buildmap(num_systems, min_dist_origin, max_dist_origin,
      min_dist_system, max_dist_system, x_origin, y_origin):
    planet_array.append(planets.Planet(chr(ord('A') + x), "none", item[0],
        item[1]))
    x += 1
  return planet_array


if __name__ == "__main__":
  # Define default values for testing.
  num_systems = 20
  min_dist_origin = 3
  max_dist_origin = 10
  min_dist_system = 2.5
  max_dist_system = 5
  x_origin = 10
  y_origin = 10

  planet_list = GenerateMap()
  galaxy_map.drawmap(planet_list, x_origin, y_origin)
