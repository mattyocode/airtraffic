from plane import Plane
import pytest

p = Plane()

def test_plane_land_instruction_1():
    p.set_to_land()
    assert p._status == 'Landed'

def test_plane_takeoff_instruction_2():
    p.set_to_takeoff()
    assert p._status == 'Flying'
