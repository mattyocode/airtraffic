from plane import Plane
from airport import Airport
import pytest
from unittest.mock import Mock

@pytest.fixture
def plane():
    plane = Plane()
    yield plane
    plane.clear()

def test_plane_land_instruction_1(plane):
    stub_airport = Mock(Airport)
    stub_airport.is_full.return_value = False
    plane.set_to_land(stub_airport)
    assert plane._status == 'Landed'

def test_plane_takeoff_instruction_2(plane):
    plane.set_to_takeoff()
    assert plane._status == 'Flying'

def test_not_land_when_airport_full_6(plane):
    with pytest.raises(ValueError, match='Airport is full!') as e:
        stub_airport = Mock(Airport)
        stub_airport.is_full.return_value = True
        plane.set_to_land(stub_airport)
    assert e.type is ValueError