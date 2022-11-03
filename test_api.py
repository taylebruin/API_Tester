#!/usr/bin/env python3
import random
import string
import unittest

"""TODO: Import the `API` class from the api.py file"""
from api import API

def generate_random_text(l=10):
    """ Helper to generate random text for creating new tasks.
    This is helpful and will ensure that when you run your tests,
    a new text string is created. It is also good for determining
    that two tasks are unique.
    Keyword arguments:
        l (int): How long the generated text should be (default 10)
    Returns:
        A randomly-generated string of length `l`
    """
    chars = string.hexdigits
    return "".join(random.choice(chars) for i in range(l)).lower()

def generate_random_date(year=None, month=None, date=None):
    """ Helper to generate random date for creating new tasks.
    This is helpful as another way of generating random tasks
    Keyword arguments:
        year: Specify a year (default None)
        month: Specify a month (default None)
        date: Specify a date (default None)
    Returns:
        A randomly-generated string representation of a date
    """
    if not year:
        year = str(random.randint(2000, 2025))
    if not month:
        month = str(random.randint(1, 12))
    if not date:
        date = str(random.randint(1, 28))
    return str(year) + "-" + str(month).zfill(2) + "-" + str(date).zfill(2) + "T00:00:00.000Z"

class TestAPI(unittest.TestCase):

    # TODO: update the cookie value and uncomment the desired `base_url, cookie` pair when ready to test
    #base_url, cookie = "https://210s1.itcyber.byu.edu", "s%3AwH7GdEGz-n08fxVv2QuEs54yyXtne01g.R4Gvt2K%2F5KHrHkoPNK4uLuTiRdsH9pY5cX3Vkk1d8Lw" # For s1
    #base_url, cookie = "https://210s2.itcyber.byu.edu", "s%3AkWM0nIzn4GBlqO7n4eNulMzHXWd038m8.03FXBKosCFSn7UI9dGpJ8%2Bv10O5TuqhVbEBzLWv3gaQ" # For s2
    #base_url, cookie = "https://210s3.itcyber.byu.edu", "s%3AxnSoMjS9e1ChKA378oLM0lCst4n49pxv.oBCLuVqgSwmNtuZ0jMEKjYcTGwFtzM4ZV%2FFCin3WJAc" # For s3
    base_url, cookie = "https://210s4.itcyber.byu.edu", "s%3Ay0p_gGwl1qxAwiPEI1jPxLq5nyAOxC_W.gjAkN48uMh52xIzOQnhzQxIhlu5Ad8Ul5PHj1B09iB4" # For s4

    # This will be ran once, when you start your tests.
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.api = API(self.base_url)

    def test_create_task(self):
        """ Tests creating a task is successful.
        This is an example test:
            - Create the task w/dummy data
            - Verify that the task was created
            - Delete the task we created
        You will be required to implement the other tests
        that are defined in BaseTestCase. They will be marked
        with @abc.abstractmethod.
        """
        Text = generate_random_text()
        Date = generate_random_date()

        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(resp.ok, msg=f"The Create Task failed: {resp.reason}.")
        task = resp.json()

        self.assertEqual(task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertFalse(task["Done"], msg="The task's Done returned True, expected False.")
        self.assertIn("UserId", task, msg="All tasks should have a UserId, matching the Id of the user who created it.")

        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])

    def test_read_one_task(self):
        """ Tests Reading a task is successful.
        This is an example test:
            - After creating response should have text I gave
            - Date should be one I gave
            - Done should be false
            - should have userID property
        """
        Text = generate_random_text()
        Date = generate_random_date()
        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(resp.ok, msg=f"The Create Task failed: {resp.reason}.")
        task = resp.json()
        read_test = self.api.read_task(self.cookie, task["_id"])
        current_task = read_test.json()

        self.assertEqual(current_task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(current_task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertFalse(current_task["Done"], msg="The task's Done returned True, expected False.")
        self.assertIn("UserId", task, msg="All tasks should have a UserId, matching the Id of the user who created it.")

        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])

    def test_read_all_tasks(self):
        """ Tests Reading all tasks is successful.
        This is an example test:
            - After creating all tasks should have the same user ID
        """
        Text = generate_random_text()
        Date = generate_random_date()
        resp = self.api.create_task(self.cookie, Text, Date)
        resp1 = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(resp.ok, msg=f"The Create Task failed: {resp.reason}.")
        task = resp.json()
        task1 = resp1.json()
        read_test = self.api.read_all_tasks(self.cookie)
        all_tasks = read_test.json()
        for t in all_tasks:
            self.assertEqual(task["UserId"], t["UserId"], msg="All tasks do not have the same user ID")
        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])
        self.api.delete_task(self.cookie, task1["_id"])
    def test_update_task(self):
        """ Tests Updating a task is successful.
        This is an example test:
            - After updating a task the Done value should be different
        """
        Text = generate_random_text()
        Date = generate_random_date()
        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(resp.ok, msg=f"The Create Task failed: {resp.reason}.")
        task = resp.json()
        read_test = self.api.update_task(self.cookie, task["_id"], True)
        current_task = read_test.json()

        self.assertEqual(current_task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(current_task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertTrue(current_task["Done"], msg="The task's Done returned False, expected True.")
        self.assertIn("UserId", task, msg="All tasks should have a UserId, matching the Id of the user who created it.")

        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])
    def test_delete(self):
        """ Tests Updating a task is successful.
        This is an example test:
            - After updating a task the Done value should be different
        """
        Text = generate_random_text()
        Date = generate_random_date()
        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(resp.ok, msg=f"The Create Task failed: {resp.reason}.")
        task = resp.json()
        read_test = self.api.update_task(self.cookie, task["_id"], True)
        current_task = read_test.json()

        self.assertEqual(current_task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(current_task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertTrue(current_task["Done"], msg="The task's Done returned False, expected True.")
        self.assertIn("UserId", task, msg="All tasks should have a UserId, matching the Id of the user who created it.")

        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])
        delete_test = self.api.read_task(self.cookie, task["_id"])
        should_not_exist = delete_test
        self.assertFalse(should_not_exist, msg="The task should not exist anymore returned as still existing")
    def test_user(self):
        """ Tests returning user information
        This is an example test:
            - After looking for the user we should have
            ID
            username
            and email
        """
        resp = self.api.read_current_user(self.cookie)
        current_user = resp.json()

        self.assertIn("Id", current_user, msg="there is no current user ID.")
        self.assertIn("UserName", current_user, msg="there is no current username.")
        self.assertIn("Email", current_user, msg="there is no current user email.")
    def test_read_task_does_not_exist(self):
        id = generate_random_text(24)
        delete_test = self.api.read_task(self.cookie, id)
        should_not_exist = delete_test
        self.assertFalse(should_not_exist, msg="The task should not exist ever is returned as existing")
    def test_delete_task_does_not_exist(self):
        id = generate_random_text(24)
        delete_test = self.api.delete_task(self.cookie, id)
        should_not_exist = delete_test
        self.assertFalse(should_not_exist, msg="The task should not and should not have been able to return as being deleted")
    def test_update_task_does_not_exist(self):
        id = generate_random_text(24)
        delete_test = self.api.update_task(self.cookie, id, True)
        should_not_exist = delete_test
        self.assertFalse(should_not_exist, msg="The task should not and should not have been able to return as being updated")
    def test_delete_invalid_id(self):
        id = generate_random_text(23)
        delete_test = self.api.delete_task(self.cookie, id)
        should_not_exist = delete_test
        self.assertFalse(should_not_exist, msg="the task returned with a valid Id when it should not have")
    def test_read_all_no_cookie(self):
        test_cookie = " "
        test_no_cookie = self.api.read_all_tasks(test_cookie)
        self.assertFalse(test_no_cookie.ok, msg= "this should come back as false since there is no cookie")
    def test_create_not_enough_info(self):
        """ Tests creating a task is unsuccessful with not enough info
        This is an example test:
            - Create the task w/dummy data
            - Verify that the task was created
            - Delete the task we created
        You will be required to implement the other tests
        that are defined in BaseTestCase. They will be marked
        with @abc.abstractmethod.
        """
        Text = generate_random_text()
        Date = generate_random_date()
        Date = ""

        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertFalse(resp.ok, msg = "A task was created when it should not have been")
    # Make more methods that begin with 'test` to test all endpoints
    # properly work and fail when you expect them to.

# Inside this `if` statement will only run if we call the program as
# the top-level module, i.e. when we run this file, not when we import
# this file
if __name__ == "__main__":
    unittest.main()