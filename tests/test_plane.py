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

def test_plane_takeoff_instruction_2(plane):
    assert plane.set_to_takeoff(stub_weather) == 'Flying'

def test_not_land_when_airport_full_6(plane):
    with pytest.raises(ValueError, match='Airport is full!') as e:
        stub_airport.is_full.return_value = True
        plane.set_to_land(stub_airport, stub_weather)
    assert e.type is ValueError

def test_not_land_when_weather_is_stormy(plane):
    with pytest.raises(ValueError, match='Weather is stormy') as e:
        stub_airport.is_full.return_value = False
        stub_weather.check_state.return_value = 'Stormy'
        plane.set_to_land(stub_airport, stub_weather)
    assert e.type is ValueError

def test_land_when_weather_is_sunny(plane):
    stub_airport.is_full.return_value = False
    stub_weather.check_state.return_value = 'Sunny'
    assert plane.set_to_land(stub_airport, stub_weather) == 'Landed'

def test_not_takeoff_when_weather_is_stormy(plane):
    with pytest.raises(ValueError, match='Weather is stormy') as e:
        stub_airport.is_full.return_value = False
        stub_weather.check_state.return_value = 'Stormy'
        plane.set_to_takeoff(stub_weather)
    assert e.type is ValueError