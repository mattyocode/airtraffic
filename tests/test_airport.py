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
stub_plane1 = Mock(Plane('001'))
stub_plane2 = Mock(Plane('002'))
stub_plane3 = Mock(Plane('003'))

def test_airport_returns_location(airport):
    airport._location = 'Sydney'
    assert airport.get_location() == 'Sydney'

def test_plane_not_at_airport(airport):
    assert airport.plane_in_terminals('001') == False

def test_plane_is_at_airport(airport):
    airport._terminals = ['001']
    assert airport.plane_in_terminals('001') == True

def test_is_airport_full_default_capacity_5(airport):
    airport._terminals = ['001', '002', '003', '004', '005']
    assert airport.is_full() == True

def test_add_plane_object_to_terminals(airport):
    airport.add_plane_to_terminals(stub_plane)
    assert stub_plane in airport._terminals

def test_add_3_plane_objects_to_terminals(airport):
    airport.add_plane_to_terminals(stub_plane1)
    airport.add_plane_to_terminals(stub_plane2)
    airport.add_plane_to_terminals(stub_plane3)
    assert airport.get_plane_list() == ['001', '002', '003']

def test_remove_plane_object_from_terminals(airport):
    airport.add_plane_to_terminals(stub_plane)
    airport.remove_plane_from_terminals(stub_plane)
    assert stub_plane not in airport._terminals

def test_remove_absent_plane_object_from_terminals(airport):
    with pytest.raises(ValueError, match='Plane not at airport') as e:
        airport.remove_plane_from_terminals(stub_plane)
    assert e.type is ValueError


    