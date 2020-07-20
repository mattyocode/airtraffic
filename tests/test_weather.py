import pytest
from unittest.mock import Mock

from weather import Weather

@pytest.fixture
def weather():
    weather = Weather()
    return weather

def test_check_weather(weather):
    assert weather.check_state() == 'Sunny' or 'Stormy'

def test_check_weather_sunny():
    stub_weather = Mock(Weather)
    stub_weather.check_state.return_value = 'Sunny'
    assert stub_weather.check_state() == 'Sunny'

def test_check_weather_stormy():
    stub_weather = Mock(Weather)
    stub_weather.check_state.return_value = 'Stormy'
    assert stub_weather.check_state() == 'Stormy'

