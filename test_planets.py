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
        self.planet = Planet('A','Foo',0,0,10)

    def test_BuildShips(self):
        self.assertEqual(Planet.BuildShips(Planet),10)

    def test_SetOwner(self):
        self.assertEqual(Planet.SetOwner(Planet,'Fubar'),'Bar')

if __name__ == "__main__":
    unittest.main()
