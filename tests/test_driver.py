import pytest
import socket

from drivers.Driver import get_driver

def is_port_open(host: str, port: int) -> bool:
    """Check if a given port is open on the specified host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)  # Set timeout for the connection attempt
        return s.connect_ex((host, port)) == 0

def test_appium_server_running():
    """Test if the Appium server is running on port 4723."""
    assert is_port_open('127.0.0.1', 4723), "Appium server is not running on port 4723"


def test_get_driver_valid():
    result = get_driver()
    assert result is not None, "Driver initialization failed!"
