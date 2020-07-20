from airport import Airport
from plane import Plane
import pytest
from unittest.mock import Mock

@pytest.fixture
def airport():
    airport = Airport()
    yield airport
    airport.empty_terminals

def test_plane_not_at_airport_3(airport):
    assert airport.plane_in_terminals(1) == False

def test_plane_is_at_airport_4(airport):
    print(airport._terminals)
    airport._terminals = [1]
    assert airport.plane_in_terminals(1) == True

def test_is_airport_full_default_capacity_5(airport):
    print(airport._terminals)
    airport._terminals = [1, 2, 3, 4, 5]
    assert airport.is_full() == True

def test_add_plane_object_to_terminals(airport):
    stub_plane = Mock(Plane)
    airport.add_plane_to_terminal(stub_plane)
    assert stub_plane in airport._terminals
