1. Describe the Problem
"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
"""

2. Design the Function Signature

def track_tasks(text):
    # Parameters: 
        # a string representing human-readable text
    # Return:
        # bolean, true if valid, false othervise

3. Create Examples as Tests
"""
Given an empty string
It raise an error message 
"""
track_tasks("") => "There is no any text"

"""
Givan a text with no TODO string in it
It returns False
"""
track_tasks("") => False

"""
Given a text with TODO string in it
It returns True
"""
track_tasks("") => True

