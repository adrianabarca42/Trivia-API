# Trivia API
This project is a typical trivia game where one can test themselves with questions from 6 different subjects. You can create questions, delete questions, and finally play trivia quizzes for either a specific category, or all categories. This project is part of Udacity's Fullstack Web Developer program. By competing this project, I have learned and applied how to create and structure API endpoints, test those endpoints, and handle errors using HTTP status codes. 

## Getting Started
### Pre-requisites and Local Development
Developers looking to use this project should already have Python3, pip, and node insalled on their local machines.

#### Backend

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:
```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

psql trivia < trivia.psql
Running the server
From within the backend directory first ensure you are working using your created virtual environment.

To run the server, execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.
