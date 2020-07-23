from airport import Airport
from plane import Plane
import pytest
from unittest.mock import Mock

@pytest.fixture
def airport():
    airport = Airport()
    yield airport
    airport.empty_terminals

stub_plane = Mock(Plane)
stub_plane1 = Mock(Plane)
stub_plane2 = Mock(Plane)
stub_plane3 = Mock(Plane)  

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
    airport.add_plane_to_terminals(stub_plane)
    assert stub_plane in airport._terminals

def test_add_3_plane_object_to_terminals(airport):  
    airport.add_plane_to_terminals(stub_plane1)
    airport.add_plane_to_terminals(stub_plane2)
    airport.add_plane_to_terminals(stub_plane3)
    assert len(airport._terminals) == 3

def test_remove_plane_object_from_terminals(airport):
    airport.add_plane_to_terminals(stub_plane)
    airport.remove_plane_from_terminals(stub_plane)
    assert stub_plane not in airport._terminals

def test_remove_absent_plane_object_from_terminals(airport):
    with pytest.raises(ValueError, match='Plane not at airport') as e:
        airport.remove_plane_from_terminals(stub_plane)
    assert e.type is ValueError


    