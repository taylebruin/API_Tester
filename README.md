# INTRODUCTION:
### Tayler Bruin <br>
### 03/30/2022 <br>
### Lab 5 Writeup <br>
# SUMMARY:
The purpose of this project was to test several API endpoints. The project used Python scripting to gather data from the endpoints themselves and in another file to test them. The testing performed was unit testing where we make a request to the API and we have an expected response vs what the actual response was. If the actual match our expected then that part of the API is working and if they don't then that part of the API is not working. We tested four different endpoints to so what it looks like when it works perfectly and when a variety of functions fail.
# DESIGN OVERVIEW:
**api.py:** The purpose of this file was to connect to the API that we are testing. This has a variety of functions to pull data from the API. <br>
**test_api.py:** This file is our testing software. It uses the functions in api.py to gather the data that it needs and tests the results and outputs how well the results are working.
**note:** since there is no visual elements to lab 5a there are no images to share that I can think of.
# Questions:
1. Name and discuss at least two of the benefits of writing unit tests before writing code.
One writing unit tests would force you to have to plan out exactly what you want your code to be doing. You would not be able to simply write and discover what you need as you go which will make your code a lot better. Two it allows for testing your code as you go beyond simply using the built in debugger. This means that just because your code can run does not mean that it is correct.
2. What would be some of the benefits of automating your test scripts (i.e. so they run at each commit)?
This would help you confirm that your commits are not breaking things that you have previously done and that your current things are not broken as well. If you see broken results it is really easy to undo the commit.
3. How long did this lab take for you?
About 8 hours
# LESSONS LEARNED:
### The print function makes it really easy to see what your api is returning
Before you can begin to test your API it is important to make sure that it is returning at least generally what you want. Using the print function in the api.py file allows us to see what is being returned by our various functions and this allows us to see that both our function to pull from the API is working as well as that part of the api is working.
### Python loops are different from other languages
This problem stems from an issue with Python itself compared to other languages. The problem is that Python uses indentation instead of braces to define which code goes together. This means that with loops you need to be very careful about your indentation to make sure that the right things are part of the loop.
### Unit testing is really easy once you have started
When initially designing a unit test it can be difficult to figure out exactly what you are supposed to be doing. Once you put in the time to understand the first test though the rest are relatively easy to figure out because they are all variations on each other. This means if you were maintaining a large code base starting a unit test project could be difficult but expanding it should be really easy. 
# CONCLUSIONS:
- Used python to connect to an API
- Installed python on windows 10
- Used python to perform unit tests
# REFERENCES:
https://pip.pypa.io/en/stable/installation/ <br>
https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab <br>
https://www.w3schools.com/python/python_for_loops.asp <br>


# Test API CRUD Functions Example
This project was built to test several different API's. <br>
Unless you need to add new endpoints you will not need to edit the apy.py file to use this project. <br>
The only file you will need to edit it test_api.py to add new tests if you desire to do so. <br>
In order to use this testing software follow the following steps.
1. open test_api.py
2. go to line 42
3. These commented out links are the API's that we are testing.
4. in order to complete the information for one the links we are going to need to get a cookie for them.
5. To do this open the link you want to test and add the following the end of the link.
/API/vs/auth/google
6. This will allow you to log in with your google account.
7. Use your browser inspector to find the cookie value for it210_session then copy and paste that value replacing the value in quotations on the line.
8. Uncomment out the line that you are testing.
9. run test_api.py to use the current built in tests.
10. if you want to add tests add them in the class method in the test api and remember to start their name with test to make sure it recognizes it.
11. you now know how to use this program to test these API's.
