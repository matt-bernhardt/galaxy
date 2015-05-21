#!/usr/env/python

# Battle functions.
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import fleets
import planets

# Variables

# Functions
def IsHit():
  """Check if shot fired from ship hits target.

  Args:
    ???

  Returns:
    Boolean value determining hit.
  """
  pass

def Battle(fleet, planet):
  """Function to play out battle between fleet and planet.

  Args:
    fleet: Attacking fleet of type Fleet.
    planet: Defending planet of type Planet.
  """
  winner = False

  while not(winner):
    for x in fleet.ships:
      if IsHit():
        planet.RemoveShips(1)
      if planet.ships == 0:
        winner = True
        break
    for y in planet.ships:
      if IsHit():
        fleet.RemoveShips(1)
      if fleet.destroyed == True:
        winner = True
        break
  if fleet.ships == 0:
    # Defender wins
  if planet.ships == 0:
    # Attacker wins