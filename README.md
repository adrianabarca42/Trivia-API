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
This will install all of the required packages we selected within the ```requirements.txt``` file.

##### Key Dependencies
[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

[SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```psql trivia < trivia.psql```
## Running the server
From within the ```backend``` directory first ensure you are working using your created virtual environment.

To run the server, execute:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Setting the ```FLASK_ENV``` variable to ```development``` will detect file changes and restart the server automatically.

Setting the ```FLASK_APP``` variable to ```flaskr``` directs flask to use the ```flaskr``` directory and the ```__init__.py``` file to find the application.

This application is run on ```http://127.0.0.1:5000/``` by default and is a proxy in the frontend configuration. 
#### Frontend
##### Installing Node and NPM
This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download.](https://nodejs.org/en/download/)

##### Installing project dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the ```frontend``` directory of this repository. After cloning, open your terminal and run:

```npm install```
>_tip_: **npm i** is shorthand for **npm install**

## Required Tasks
## Running Your Frontend in Dev Mode
The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.
```npm start```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Documentation

### Getting Started
Base URL: As of right now, this app can only be run locally. the backend is hosted at the default, http://127.0.0.1:5000/. This is set as a proxy in the frontend configuration. 
Authentication: this application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": False,
  "error": 400,
  "message": "bad request"

}
```

The API will return 4 error types when requests fail:
* 400: Bad Request
* 404: Not Found
* 405: Method Not Allowed
* 422: Unprocessable

### Endpoints
GET /categories
  * General: 
    * Returns dictionary of categories in which keys are the ids and the value is the corresponding string of the category along with the success value.
  * Sample: ```curl http://127.0.0.1:5000/categories```
  ```
  {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
    }, 
  "success": true
  }
  ```
GET /questions
  * General: 
    * Returns list of quesion objects, categories, the current category, total number of questions, and success value.
    * Questions are paginated with up to 10 questions per page.
  * Sample: ```curl http://127.0.0.1:5000/questions```
  ```
  {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": 1, 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "success": true, 
  "total_questions": 18
  }
  ```
GET /categories/<int:category_id>/questions
  * General: 
    * Returns list of question objects corresponding to a specific category, the current category, total number of questions, and success value.
  * Sample: ```curl http://127.0.0.1:5000/categories/2/questions```
  ```
  {
  "current_category": 2, 
  "questions": [
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 2
  }
  ```
POST /questions
  * General: 
    * Creates a new question using the question, answer, category, and difficulty. Returns all the questions, number of total questions, and success value.
    * Questions are paginated with up to 10 questions per page.
  * Sample: ```curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "who is the greatest basketball player of all time", "answer": "Lebron James", "category": 5, "difficulty": 1}'```
  ```
  {
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Lebron James", 
      "category": 5, 
      "difficulty": 1, 
      "id": 21, 
      "question": "Who is the greatest basketball player of all time"
    }
  ], 
  "success": true, 
  "total_questions": 19
  }
  ```
POST /questions/search
  * General: 
    * Returns list of questions based on a search term, total number of questions, and success value.
    * Questions are paginated with up to 10 questions on a page.
  * Sample: ```curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "discovered"}'```
  ```
  {
  "questions": [
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "success": true, 
  "total_questions": 1
  }
  ```
POST /quizzes
  * General: 
    * Returns a random question within the given category, if provided, and that is not one of the previous questions.
  * Sample: ```curl -d '{"previous_questions": [2],"quiz_category": {"type":"Geography","id": "2"}}' -H 'Content-Type: application/json' -X POST                http://127.0.0.1:5000/quizzes```
  ```
  {
  "question": {
    "answer": "Jackson Pollock", 
    "category": 2, 
    "difficulty": 2, 
    "id": 19, 
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  }
  ```
DELETE /questions/<int:question_id>
  * General: 
    * Returns list of questions, total number of questions, question id of the deleted question, and success value.
    * list of questions are paginated with up to 10 questions per page. 
  * Sample: ```curl -H 'Content-Type: application/json' -X DELETE http://127.0.0.1:5000/questions/19
  ```
  {
  "deleted": 19, 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "total_questions": 18
  }
  ```
  ## Deployment N/A
  ## Authors
  Adrian Abarca, the team at Udacity
