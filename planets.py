#!/usr/env/python

# Planets Class for Galaxy
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import galaxy_lib
import fleets
import random

# Variables

# Classes
class Planet():
  """Planet object.

  Attributes:
    name: Name of planet. Typically single alpha character.
    owner: Owner of planet. Format TDB.
    x_pos: X coordinate.
    y_pos: Y coordindate.
    output: Number of ships generated each turn.
    ships: Number of ships currently hosted at planet.
  """
  # Variables
  name = 'none'
  owner = 'none'
  x_pos = 0
  y_pos = 0
  output = 0
  ships = 0

  # Methods
  def __init__(self, name, owner, x, y, output=None):
    """Initial setup of planet including creation during map generation."""
    self.name = name
    self.owner = owner
    self.x_pos = x
    self.y_pos = y
    if output == None:
      self.output = random.randint(0, 10)
    else:
      self.output = output
    self.ships = 0

  def FleetArrival(self, fleet):
    """Fleet arrival on planet. Check for battle conditions."""
    pass

  def FleetDeparture(self, planet_list, destination, ships):
    """Create fleet and subtract ship(s) from population.

    Args:
      planet_list: Array of type Planet
      destination: Name of destination planet as string.
      ships: Number of ships to add to fleet as integer.

    Returns:
      Fleet
    """
    travel_time = galaxy_lib.PlanetDistance(planet_list, self.name,
        destination, True)
    newFleet = fleets.Fleet(ships, self.owner, destination, travel_time)
    self.ships -= ships
    return newFleet

  def BuildShips(self):
    """End of turn process of ship generation."""
    self.ships += self.output

  def SetOwner(self, newOwner):
    """Set owner of planet. Typically after battle."""
    self.owner = newOwner


if __name__ == "__main__":
  pass
