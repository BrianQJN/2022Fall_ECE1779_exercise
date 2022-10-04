### Week 3 Flask Exercises

Follow the instructions below and complete the following exercises. These exercises will help you to complete questions for your participation mark. 

## Install Flask

https://flask.palletsprojects.com/en/2.2.x/installation/ 

## Run Flask App

https://flask.palletsprojects.com/en/2.2.x/quickstart/

## Part 1: Complete the exercises in the Part1 folder:

In this part, you will update a flask application so that it displays the current date and time whenever the webpage is refreshed.

1. Modify one line of code in currentTime.py to get the current date and time.
2. Run the Flask app locally on your machine to verify if your webpage matches part1_solution.jpg.

Note: your app will be running on http://[your-pirvate-ip]:5000/time

## Part 2: Complete the exercises in the Part2 folder:

In this part, you will update a flask application that calculates collatz steps using the parameter n specified by the user in the webpage URL.

1. Add code in collatzSteps.py to parse the integer from the url and set the variable "n" equal to this value. Use the request object to get the number passed in via the url. 
2. Add code to validate that the input is an integer, and to return an error message to the user if they try to set n as a non-integer type.
3. Run the Flask app locally on your machine to verify if your webpage matches part2_solution.jpg.

Note: your app will be running on http://[your-pirvate-ip]:5000/collatz?n=5

## Part 3: Complete the exercises in the Part3 folder:

In this part, you will complete the html form to allow the user to submit an integer value rather than using the URL paramater as you did in Part 2.

1. Copy your solution from Part1 into collatzSteps.py 
2. Complete the body of the form in collatzStepsForm.py so that the user can input the integer value.
3. Run the Flask app locally on your machine to verify if your webpage matches part3_solution.jpg.

Note: your app will be running on http://[your-pirvate-ip]:5000/collatz_form


## Part 4: Complete the exercises in the Part4 folder:

In this part, you will use templates rather than creating html embedded in the python code.

Here are some resources for working with templates.

- https://flask.palletsprojects.com/en/1.1.x/templating/
- https://www.geeksforgeeks.org/python-using-for-loop-in-flask/

1. Modify collatz.html by adding the contents of the loop so that template will display the collatz steps.
2. Run the Flask app locally on your machine to verify that your output matches part4_solution.jpg. 

Note: your app will be running on http://[your-pirvate-ip]:5000/collatz_form_template 

***

### Once you have finished the exercises, go to [PCRS](https://pcrs.teach.cs.toronto.edu/ECE1779-2022-09/content/quests) to answer the questions for Week 3.
