#!/usr/env/python

# Fleets Class for Galaxy
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules

# Variables

# Classes
class Fleet():
  """Fleet object.

  Attributes:
    ships: Number of ships in fleet.
    owner: Owner of fleet. Format TBD.
    destination: Final destination of fleet.
    travel_time: Number of turns remaining until arrival at destination.
  """
  # Variables
  ships = 0
  owner = 'none'
  destination = 'none'
  travel_time = 0
  arrived = False
  destroyed = False

  #Methods
  def __init__(self, ships, owner, destination, travel_time):
    self.ships = ships
    self.owner = owner
    self.destination = destination
    self.travel_time = travel_time
    arrived = False
    destroyed = False

  def MoveFleet(self):
    """Movement of fleet at end of turn."""
    if self.travel_time > 0:
      self.travel_time -= 1
    if self.travel_time == 0:
      self.arrived = True

  def AddShips(self, ships):
    """Add ship(s) to fleet.

    Args:
      ships: Number of ships.
    """
    self.ships += ships

  def RemoveShips(self, ships):
    """Remove ship(s) from fleet.

    Args:
      ships: Number of ships.
    """
    if ships >= self.ships:
      self.ships = 0
      self.destroyed = True
    else:
      self.ships -= ships


if __name__ == "__main__":
  pass
