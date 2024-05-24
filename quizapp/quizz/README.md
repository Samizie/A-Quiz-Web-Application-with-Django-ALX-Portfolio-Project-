Creating the Model

The model is going to be a class based model named (QuizModel) containing:
1. question attributes
2. options attributes prefixed with 01-04
3. answer attribute
4. a string method that returns the string representation of the question

Creating the Views

The views contains 
*A Home Function*
-takes in request as post method
-contains variables
    score, wrong, correct, total all equated to 0
-queries the QuizModel
-Iterates through the questions and prints the questions per post request
-contains a logic in the iteration that checks if answer is equal to answer attr in QuizModel and adds 1 to score, or adds 1 to wrong variable if wrong
- stores the new values of the variables in a dictionary context
and returns the context
-if request is not POST method,
    returns the questions and a rendered page

*AddQues function*
This function is for the admin/staff to add new questions to the quizz and save.
Permits only the staff and the admin
-takes in requests
- first checks if current user is staff,
    then creates object form AddQuesForm
    -checks if request method is POST
    -checks if form is valid(i.e if form is well filled) and saves form
    -returns ad serves the question html page
-if user is not a staff returns homepage

*RegisterPage Function*
This function is handling the registration of new users
checks if user is authenticated and redirects user to homepage if true
else:
    -creates a createuserfrom objet for new user
    -checks if form is valid and saves form
    -finally redirects user to login page

*LoginPage Function*
This function handles user logins
-checks if user is authenticated and redirect user to homepage
else:
    -gets username and password through POST method
    -creates a user object with usernme and password as parameters
    checks if user exist by checking if user is not None
    redirects user to homepage if user is not None
    or else reserves the login page to user for login in again

*LogOut Function*
accepts logout request and returns to homepage