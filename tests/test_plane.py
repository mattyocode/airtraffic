from plane import Plane
from airport import Airport
from weather import Weather

import pytest
from unittest.mock import Mock

@pytest.fixture
def plane():
    plane = Plane()
    yield plane
    plane.clear()

stub_airport = Mock(Airport)
stub_weather = Mock(Weather)

def test_plane_land_instruction_1(plane):
    stub_airport.is_full.return_value = False
    assert plane.set_to_land(stub_airport, stub_weather) == 'Landed'

def test_plane_returns_name_string():
    plane1 = Plane("001")
    assert plane1._id_num == "001"

#@pytest.mark.skip('Superceded')
def test_plane_takeoff_instruction_2(plane):
    stub_airport.get_location.return_value = 'London'
    plane._current_location = 'London'
    assert plane.set_to_takeoff(stub_airport, stub_weather) == 'Flying'

def test_not_land_when_airport_full_6(plane):
    with pytest.raises(ValueError, match='Airport is full!') as e:
        stub_airport.is_full.return_value = True
        plane.set_to_land(stub_airport, stub_weather)
    assert e.type is ValueError

def test_not_land_when_weather_is_stormy(plane):
    with pytest.raises(ValueError, match='Weather is stormy') as e:
        stub_airport.is_full.return_value = False
        stub_weather.check_state.return_value = 'Stormy'
        plane.can_land(stub_airport, stub_weather)
    assert e.type is ValueError

def test_land_when_weather_is_sunny(plane):
    stub_airport.is_full.return_value = False
    stub_weather.check_state.return_value = 'Sunny'
    assert plane.set_to_land(stub_airport, stub_weather) == 'Landed'

def test_not_takeoff_when_weather_is_stormy(plane):
    with pytest.raises(ValueError, match='Weather is stormy') as e:
        stub_airport.is_full.return_value = False
        stub_weather.check_state.return_value = 'Stormy'
        plane.set_to_takeoff(stub_airport, stub_weather)
    assert e.type is ValueError


def test_plane_cannot_takeoff_when_flying(plane):
    with pytest.raises(ValueError, match='Plane is in flight!') as e:
        stub_airport.get_location.return_value = 'Madrid'
        stub_weather.check_state.return_value = 'Sunny'
        plane._current_location = 'Madrid'
        plane._status = 'Flying'
        plane.can_takeoff(stub_airport, stub_weather)
    assert e.type is ValueError

def test_plane_assinged_to_airport(plane):
    stub_airport.get_location.return_value = 'London'
    stub_airport.is_full.return_value = False
    stub_weather.check_state.return_value = 'Sunny'
    plane.set_to_land(stub_airport, stub_weather)
    assert plane.current_location() == 'London'

def test_plane_cannot_takeoff_from_airport_not_at(plane):
    with pytest.raises(ValueError, match='Wrong airport') as e:
        stub_airport.get_location.return_value = 'Madrid'
        stub_weather.check_state.return_value = 'Sunny'
        plane.can_takeoff(stub_airport, stub_weather)
    assert e.type is ValueError
    
