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

  #Methods
  def __init__(self):
    """Initial creation of fleet."""
    pass

  def MoveFleet(self):
    """Movement of fleet at end of turn."""
    pass

if __name__ == "__main__":
  pass
