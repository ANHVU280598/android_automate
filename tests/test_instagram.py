import pytest
import socket


from automation_base.Base import Base
from run_file.instagram import Instagram


@pytest.fixture
def base():
    base = Instagram()
    yield base

@pytest.mark.test_by_pass_anouncement
def test_by_pass_anouncement(base):
    # path = '//android.widget.Button[@text="Đã hiểu"]'
    result = base.by_pass_anouncement()
    assert result is False, "Expect return False"

    