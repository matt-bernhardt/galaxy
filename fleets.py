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

  #Methods
  def __init__(self, ships, owner, destination, travel_time):
    self.ships = ships
    self.owner = owner
    self.destination = destination
    self.travel_time = travel_time
    arrived = False

  def MoveFleet(self):
    """Movement of fleet at end of turn."""
    if self.travel_time > 0:
      self.travel_time -= 1
    else:
      self.arrived = True


if __name__ == "__main__":
  pass
