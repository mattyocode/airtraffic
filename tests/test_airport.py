from airport import Airport
from plane import Plane
import pytest
from unittest.mock import Mock

p = Mock()

def test_plane_not_at_airport_3():
    a01 = Airport(1)
    assert a01.plane_in_terminals(p) == False

def is_airport_full_4():
    pass