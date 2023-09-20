import pytest
from lib.track_tasks import *

"""
Given an empty string
It raise an error message 
"""
def test_given_an_empty_string():
    with pytest.raises(Exception) as e:
        track_tasks("")
    error_msg = str(e.value)
    assert error_msg == "There is no any text"

"""
Givan a text with no TODO string in it
It returns False
"""
def test_with_no_todo_in_the_string():
    assert track_tasks("There is no tasks here") == False

"""
Given a text with TODO string in it
It returns True
"""
def test_with_todo_in_string():
    assert track_tasks("There is a TODO in here") == True