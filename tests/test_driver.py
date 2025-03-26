import pytest
# from drivers.Driver import get_driver
from drivers.Driver import get_driver

def test_get_driver_valid():
    test = 1
    print('work')
    assert test is not None, "Driver initialization failed!"
