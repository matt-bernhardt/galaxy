#!/usr/env/python

# Test class for Planets class for Galaxy
# Author: matt.j.bernhardt@gmail.com
# Version: 0.1

# Modules
import unittest
from planets import Planet

# Variables

# Classes
# See http://pythontesting.net/framework/unittest/unittest-introduction/
class TestPlanet(unittest.TestCase):

  def setUp(self):
    self.planet = Planet('A', 'Foo', 0, 0, 10)

  def test_BuildShips(self):
    Planet.BuildShips(self.planet)
    self.assertEqual(self.planet.ships, 10)

  def test_SetOwner(self):
    Planet.SetOwner(self.planet, 'Fubar')
    self.assertEqual(self.planet.owner, 'Fubar')

  def test_FleetArrival(self):
    pass

  def test_FleetDeparture(self):
    pass


if __name__ == "__main__":
    unittest.main()
