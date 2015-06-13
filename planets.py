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

  def AddShips(self, ships):
    """Add ship(s) to population.

    Args:
      ships: Number of ships.
    """
    self.ships += ships

  def RemoveShips(self, ships):
    """Subtract ship(s) from population.

    Args:
      ships: Number of ships.
    """
    if ships >= self.ships:
      self.ships = 0
    else:
      self.ships -= ships

  def BuildShips(self):
    """End of turn process of ship generation."""
    self.ships += self.output

  def SetOwner(self, newOwner):
    """Set owner of planet. Typically after battle.

    Args:
      newOwner: String of owner to set on planet.
    """
    self.owner = newOwner


if __name__ == "__main__":
  pass
