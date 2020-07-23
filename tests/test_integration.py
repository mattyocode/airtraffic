from airport import Airport
from plane import Plane
from weather import Weather

import pytest

a1 = Airport("London")
p1 = Plane("001")
p2 = Plane("002")

def test_print_list_of_planes_in_terminal():
    a1.add_plane_to_terminals(p1)
    a1.add_plane_to_terminals(p2)
    assert a1.get_plane_list() == ["001", "002"]