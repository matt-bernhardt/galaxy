#!/usr/env/python

# Planets Class for Galaxy
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
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
  def __init__(self, name, owner, x, y, output):
    """Initial setup of planet including creation during map generation."""
    self.name = name
    self.owner = 'Bar'
    self.x_pos = x
    self.y_pos = y
    self.output = random.randint(0, 10)
    self.ships = 0
    print('Init completed...')
    print(self.owner)

  def FleetArrival(self):
    """Fleet arrival on planet. Check for battle conditions."""
    pass

  def FleetDeparture(self):
    """Create fleet and subtract ship(s) from population."""
    pass

  def BuildShips(self):
    """End of turn process of ship generation."""
    self.ships += self.output

  def SetOwner(self,newOwner):
    """Set owner of planet. Typically after battle."""
    self.owner = newOwner
    print('New owner set to ' + str(newOwner))

if __name__ == "__main__":
  pass
