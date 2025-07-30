import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task2')))
from Task2.user import User
from Task2.data_manager import DataManager
import pytest


class TestDataManagerIntegration:

    @pytest.mark.regression
    def test_loading_users(self):
        manager = DataManager("Task2\\sample.json")
        users = manager.load_test_users()
        assert len(users) > 0
        for user in users:
            assert isinstance(user, User)

    @pytest.mark.smoke
    def test_user_validation_positive(self, sample_user):
        user = User(sample_user["name"], sample_user["email"], sample_user["password"])
        assert user.is_valid() is True

    @pytest.mark.regression
    def test_user_validation_negative(self):
        user = User("", "kanishkasree.com", "")
        assert user.is_valid() is False
