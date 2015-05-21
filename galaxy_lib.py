#!/usr/env/python

# General use functions.
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import fleets
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
  """Wrapper for distance for lookups by planet.

  Args:
    planet_list: Array of type planet.
    planet_a_name: String name of first planet.
    planet_b_name: String name of second planet.
    roundup: Optional boolean for whether distance is to be rounded up to
        nearest int.

  Returns:
    Distance between 2 selected planets. Rounded up to nearest int if roundup is
        True.
  """
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

  Args:
    planet_list: Array of type planet.
    planet_name: String name of planet.

  Returns:
    Object of type planet.
  """
  for planet in planet_list:
    if planet.name == planet_name:
      return planet
  return None

def CreateFleet(planet_list, planet_name, ships, destination):
  """Create a fleet from a planet. Includes check for capacity of fleet.

  Args:
    planet_list: Array of type planet.
    planet_name: String name of planet of origin.
    ships: Number of ships to add to fleet.
    destination: String name of destination planet.

  Returns:
    Object of type fleet.
  """
  if GetPlanetByName(planet_list, planet_name) and GetPlanetByName(planet_list,
      destination):
    planet = GetPlanetByName(planet_list, planet_name)
    if planet.ships >= ships:
      planet.RemoveShips(ships)
      return fleets.Fleet(ships, planet.owner, destination,
          PlanetDistance(planet_list, planet_name, destination, True))
    else:
      return None
  else:
    return None


if __name__ == "__main__":
  pass
