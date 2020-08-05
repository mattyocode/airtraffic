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

def test_plane_land_instruction(plane):
    stub_airport.is_full.return_value = False
    assert plane.set_to_land(stub_airport, stub_weather) == 'Landed'

def test_plane_initiates_with_id_num():
    plane1 = Plane("001")
    assert plane1._id_num == "001"

def test_plane_returns_name_str_():
    plane1 = Plane("002")
    assert str(plane1) == "002"

def test_not_land_when_airport_full(plane):
    with pytest.raises(ValueError, match='Airport is full!') as e:
        stub_airport.is_full.return_value = True
        plane.set_to_land(stub_airport, stub_weather)
    assert e.type is ValueError

def test_not_land_when_already_landed(plane):
    with pytest.raises(ValueError, match='Already landed!') as e:
        plane._status = 'Landed'
        plane.set_to_land(stub_airport, stub_weather)
    assert e.type is ValueError

def test_landed_plane_has_airport(plane):
    stub_airport.is_full.return_value = False
    stub_airport.get_location.return_value = 'London'
    stub_weather.check_state.return_value = 'Sunny'
    plane.set_to_land(stub_airport, stub_weather)
    assert plane.current_location() == 'London' 

def test_cannot_land_when_weather_is_stormy(plane):
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

def test_flying_plane_has_no_airport(plane):
    plane._current_location = 'London'
    stub_airport.get_location.return_value = 'London'
    stub_weather.check_state.return_value = 'Sunny'
    plane.set_to_takeoff(stub_airport, stub_weather)
    assert plane._current_location == None

    
    
