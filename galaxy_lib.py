#!/usr/env/python

# General use functions.
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import math

# Variables

# Functions
def Distance(x1, y1, x2, y2, roundup=False):
  """Returns a numerical distance between 2 x,y coordinates.

  Args:
    x1: First point X coordinate.
    y1: First point Y coordinate.
    x2: Second point X coordinate.
    y2: Second point Y coordinate.

  Returns:
    Distance between 2 sets of points as a float.
  """
  distance = (math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))
  if roundup:
    return math.ceil(distance)
  else:
    return distance

def PlanetDistance(planet_list, planet_a_name, planet_b_name, roundup=False):
  """Wrapper for distance for lookups by planet."""
  planet_a = None
  planet_b = None
  for planet in planet_list:
    if planet.name == planet_a_name:
      planet_a = planet
    if planet.name == planet_b_name:
      planet_b = planet
  if planet_a and planet_b:
    return Distance(planet_a.x_pos, planet_a.y_pos, planet_b.x_pos,
                    planet_b.y_pos, roundup)
  return None

def GetPlanetByName(planet_list, planet_name):
  """Lookup planet by name.
  Not sure if this should go here or in planets.py"""
  for planet in planet_list:
    if planet.name == planet_name:
      return planet
  return None


if __name__ == "__main__":
  pass
