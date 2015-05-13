#!/usr/env/python

# Test class for Fleets class for Galaxy
# Author: mbernhardt@gmail.com
# Version: 0.1

# Modules
import unittest
from fleets import Fleet

# Variables

# Classes
# See http://pythontesting.net/framework/unittest/unittest-introduction/
class TestFleet(unittest.TestCase):

  def setUp(self):
    self.fleet = Fleet(100, 'Foobar', 'B', 10)

  def test_MoveFleet(self):
    Fleet.MoveFleet(self.fleet)
    self.assertEqual(self.fleet.travel_time, 9)
    self.assertEqual(self.fleet.arrived, False)

  def test_FleetArrival(self):
    self.fleet.travel_time = 0
    Fleet.MoveFleet(self.fleet)
    self.assertEqual(self.fleet.travel_time, 0)
    self.assertEqual(self.fleet.arrived, True)


if __name__ == "__main__":
    unittest.main()
