import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task2/functions.py')))
import pytest
from Task2.functions import validate_email_format  


class TestEmailValidation:

    @pytest.mark.smoke
    def test_valid_email(self):
        assert validate_email_format("kanishkasree804@gmail.com") is True

    @pytest.mark.smoke
    def test_invalid_email(self):
        assert validate_email_format("kanishkasree804.com") is False

    @pytest.mark.regression
    @pytest.mark.parametrize("email,expected", [
        ("mramesh1234@gmail.com", True),
        ("mramesh1234.com", False),
        ("mramesh1234@.com", False),
        ("mramesh1234@", False),
        ("@gmail.com", False),
        ("mramesh1234@gmail", False)
    ])
    def test_multiple_emails(self, email, expected):
        assert validate_email_format(email) == expected
