# LearnEasy
#### Video Demo:  <https://youtu.be/VmYnvi2qkR8>
#### Description:
It's an online zoom like web application for setting up meetings. I have used HTML, CSS, Bootstrap, JavaScript, Python, SQL and Jinja in this project.
Different functionalities like password cehck, unique username, name with no special characters are applied.
When someone tries to go directly to homepage, it will first prompt you to login.

Starting with the Main.html -
I have used bootstrap, html, CSS and javascript in the file. HTML will layout the basic structure of the page. I have imported the button style from bootstrap and added gradient color in the buttons. Image is set as the background of the page. I have also made the custome scrollbar for the page using CSS. Javascript is used for the autotyping done on the page describing the various functionalities of the application. Once you click on the sign up button it will redirect you to signup.html.

Moving ahead to signup.html -
In this page I have used HTML, CSS, jinja and bootstrap. The hTML will layout the basic structure of the page. The container containing all the feilds is taken from bootsrap. Again the custom scrollbar is made from CSS. When you'll head to app.py you'll notice the functionalities such as -
1. Name should not contain special characters
2. Username should be unique
3. Password should be at least 8 characters long, contain capital and small letters, and numbers should also be included.
I have used HTML form tag to put the feilds together. If the above conditions are not met (it will check through loop) it will throw out the corresponding error, using Jinja.
Once all the conditions are met it will put your given feilds in the database and will redirect you straight to homepage (as it is annoying to login again)!

Moving to Login.html -
For this page I have used HTML, CSS, Bootstrap, SQL and Jinja. The login container is taken from bootstrap and the custom scrollbar is made from CSS. Once you enter credentials, it will check in the database if it exists or not - if it doesn't it will throw an error message using jinja, once the credentials are correct it will redirect you to the homepage.

Homepage.html -
On this page I have used basic HTML and CSS with animation. The hamburger menu is made from CSS, I have also applied the animation functionalities in it, once you'll open and close the menu, ou'll be able to recognize it.The menu contains links to other pages. The profile button is also added.

The boss - App.py
A number of functionalities are applied in this file. First thing first - it always cehcks if your session is active or not, if not it will prompt you to login to the site - you cannot go directly to the homepage through URL as it will prompt you to login again by checking the session.
If you choose to login - app.py will first redirect you to the login page and will verify your credentilas from the DB, if it's not correct it will prompt you to enter the credentials correctly with the help of message shown by jinja.
If you choose to signup - app.py will check if the conditions for each feild are met - if they are not met it will throw an error using jinja, once all the conditions are met it will first save all the details in the database and then it will redirect you to the homepage.