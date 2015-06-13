#!/usr/env/python

# Test class for galaxy_lib for Galaxy
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import unittest
import galaxy_lib
from planets import Planet

# Variables
planet_list = []

# Classes
# See http://pythontesting.net/framework/unittest/unittest-introduction/
class TestGalaxy_Lib(unittest.TestCase):

  def setUp(self):
    planet_list.append(Planet('A', 'Foo', 1, 1, 10))
    planet_list.append(Planet('B', 'Bar', 5, 2, 7))
    planet_list.append(Planet('C', 'FooBar', -1, -2, 5))

  def test_Distance(self):
    self.assertEqual(galaxy_lib.Distance(0, 2, 2, 1), 2.23606797749979)

  def test_PlanetDistance(self):
    self.assertEqual(galaxy_lib.PlanetDistance(planet_list, 'A', 'B'),
                     4.123105625617661)
    self.assertEqual(galaxy_lib.PlanetDistance(planet_list, 'A', 'B', True), 5)
    self.assertEqual(galaxy_lib.PlanetDistance(planet_list, 'A', 'C'),
                     3.605551275463989)
    # Invalid planet
    self.assertEqual(galaxy_lib.PlanetDistance(planet_list, 'A', 'D'), None)
    self.assertEqual(galaxy_lib.PlanetDistance(planet_list, 'D', 'B', True),
        None)

  def test_GetPlanetByName(self):
    self.assertEqual(galaxy_lib.GetPlanetByName(planet_list, 'A').owner, 'Foo')
    self.assertEqual(galaxy_lib.GetPlanetByName(planet_list, 'B').output, 7)
    self.assertEqual(galaxy_lib.GetPlanetByName(planet_list, 'D'), None)

  def test_CreateFleet(self):
    # Generate some ships on planet A
    Planet.BuildShips(galaxy_lib.GetPlanetByName(planet_list, 'A'))
    # Not enough ships
    self.assertEqual(galaxy_lib.CreateFleet(planet_list, 'A', 20, 'B'), None)
    # Invalid origin
    self.assertEqual(galaxy_lib.CreateFleet(planet_list, 'D', 20, 'B'), None)
    # Invalud destination
    self.assertEqual(galaxy_lib.CreateFleet(planet_list, 'A', 5, 'D'), None)
    # Success Test
    fleet = galaxy_lib.CreateFleet(planet_list, 'A', 5, 'B')
    # Check planet
    self.assertEqual(galaxy_lib.GetPlanetByName(planet_list, 'A').ships, 5)
    # Check fleet
    self.assertEqual(fleet.ships, 5)
    self.assertEqual(fleet.owner, 'Foo')
    self.assertEqual(fleet.destination, 'B')
    self.assertEqual(fleet.travel_time, 5)

if __name__ == "__main__":
    unittest.main()
