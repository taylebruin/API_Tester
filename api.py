"""TO DO: Add a Shebang"""
#!/usr/bin/env python3

"""TO DO: Import urljoin from urllib.parse"""
from urllib.parse import urljoin

"""TO DO: Import the requests"""
import requests

class API(object):

    def __init__(self, base_url):
        """ Creates the API client.
        Parameters:
            base_url (str): The base URL for the API.
        Returns:
            New API class for testing an API.
        """
        self.base_url = base_url

    def create_task(self, cookie, Text, Date):
        """ Create a new task
        Parameters:
            cookie (str): Pre-authorized cookie
            Text (str): Text/description of the task.
            Date (str): Due date of the task
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks")
        data = '{ "Text": "%s", "Date": "%s" }' % (Text, Date)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("POST", url, headers=headers, data=data)
        return response

    def read_all_tasks(self, cookie):
        """ Reads all of the tasks
        Parameters:
            cookie (str): Pre-authorized cookie
        Returns:
            Response from the server
        """
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        url = urljoin(self.base_url, "api/v1/tasks")
        response = requests.request("GET", url, headers=headers)
        return response

    def read_task(self, cookie, task_id):
        """ Reads a single task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id (str): id for the task you want to be returned
        Returns:
            Response from the server
        """
        id= task_id
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        url = urljoin(self.base_url, "api/v1/tasks/"  + id )
        response = requests.request("GET", url, headers=headers)
        return response

    def update_task(self, cookie, task_id, Done):
        """ Updates the done value of a single task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id (str): id for the task you want to be updated
            Done (bool): boolean for the value you will be changing it to
        Returns:
            Response from the server
        """
        id= task_id
        done = str(Done)
        done = done.lower()
        url = urljoin(self.base_url, "api/v1/tasks/" + id)
        data = '{"Done": "%s" }' % (done)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("PUT", url, headers=headers, data=data)
        return response
        # Note: Cast your `Done` parameter to a
        # string, and use the `.lower()` method
        # on it, before you stick it in the
        # `data` object.

    def delete_task(self, cookie, task_id):
        """ deletes a single task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id (str): id for the task you want to be deleted
        Returns:
            Response from the server
        """
        id= task_id
        url = urljoin(self.base_url, "api/v1/tasks/" + id)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("DELETE", url, headers=headers)
        return response

    def read_current_user(self, cookie):
        """ Returns information about the current user
        Parameters:
            cookie (str): Pre-authorized cookie
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/user")
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("GET", url, headers=headers)
        return response

if __name__ == "__main__":
    # Remember, this section of code is for you. Do with
    # it what you will, to see what the code looks like
    # for different requests. You may add more api calls
    # or remove them. I have found that if I add too
    # many `print()`s, the output becomes overloaded and
    # unhelpful, but again, this is personal preference.
    base_url = "https://210s1.itcyber.byu.edu"
    cookie = "s%3AwH7GdEGz-n08fxVv2QuEs54yyXtne01g.R4Gvt2K%2F5KHrHkoPNK4uLuTiRdsH9pY5cX3Vkk1d8Lw"
    api = API(base_url)
    #response = api.create_task(cookie, "Test the API", "2020-02-20")
    #response = api.create_task(cookie, "Test two things in the API", "2020-02-20")
    test_id = "6239ed9aca21585750ee256b"
    done_test = None
    done_test = True
    current_user = api.read_current_user(cookie)
    #test_delete = api.delete_task(cookie, test_id)
    #print(test_delete)
    #print(test.json())
    #print(response.ok)
    #print(response.status_code)
    #print(response.text)
    #print(response.json())


