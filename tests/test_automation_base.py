import pytest
import socket

from drivers.Driver import get_driver
from automation_base.Base import Base

@pytest.fixture
def base():
    base = Base()
    yield base
    base.driver.quit()

@pytest.mark.test_advance_is_element_present
def test_advance_is_element_present(base):
    path = '//android.widget.TextView[@text="Kiếm Thưởng"]'
    result = base.advance_is_element_present("XPATH", path)
    assert result is not None, "Expect element to be present for XPATH"

@pytest.mark.test_click_on_element
def test_click_on_element(base):
    path = '//android.widget.TextView[@text="Instagram"]'
    result = base.click_on_element("XPATH", path)
    assert result is not False

@pytest.mark.get_element_text
def test_get_element_text(base):
    path = '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[2]/android.view.View[1]//android.widget.TextView'
    result = base.get_element_text("XPATH", path)
    assert result is not False, "Expect element is a text"