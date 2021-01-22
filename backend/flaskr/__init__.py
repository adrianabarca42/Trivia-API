import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginated_questions(request, list1):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  formatted_questions = [question.format() for question in list1]
  return formatted_questions[start:end]


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={r"/*": {"origins": "*"}})
  '''
  @FINISHED: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
    '''
    @FINISHED: Use the after_request decorator to set Access-Control-Allow
    '''

  @app.route('/categories', methods=['GET'])
  def get_categories():
    try:
      if not request.method == 'GET':
        abort(405)
      categories = Category.query.order_by(Category.type).all()
      if len(categories) == 0:
        abort(404)
      return jsonify({
        'success': True,
        'categories': {category.id: category.type for category in categories}
      })
    except:
      abort(422)
    '''
    @FINISHED: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''

  @app.route('/questions', methods=['GET'])
  def get_questions():
    if not request.method == 'GET':
        abort(405)
    questions = Question.query.order_by(Question.id).all()
    paginate_list = paginated_questions(request, questions)
    if len(paginate_list) == 0:
        abort(404)
    try:
      categories = Category.query.order_by(Category.type).all()
      return jsonify({
        'success': True,
        'questions': paginate_list,
        'total_questions': len(Question.query.all()),
        'current_category': 1,
        'categories': {category.id: category.type for category in categories}
      })
    except:
      abort(422)
    '''
    @FINISHED: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    if not request.method == 'DELETE':
        abort(405)
    question = Question.query.filter(Question.id == question_id).one_or_none()
    if question is None:
      abort(404)
    try:
      question.delete()
      questions = Question.query.order_by(Question.id).all()
      paginate_questions = paginated_questions(request, questions)
      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': paginate_questions,
        'total_questions': len(Question.query.all())
      })
    except:
      abort(422)
  '''
  @FINISHED: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions', methods=['POST'])
  def add_question():
    if not request.method == 'POST':
        abort(405)
    body = request.get_json()
    new_question = body.get('question')
    new_answer = body.get('answer')
    new_difficulty = body.get('difficulty')
    new_category = body.get('category')

    question = Question(
      question = new_question,
      answer = new_answer,
      category = new_category,
      difficulty = new_difficulty
    )
    question.insert()
    questions = Question.query.all()
    paginate_questions = paginated_questions(request, questions)
    if len(paginate_questions) == 0:
      abort(404)
    try:
      return jsonify({
        'success': True,
        'created': question.id,
        'questions': paginate_questions, 
        'total_questions': len(questions),
      })
    except: 
      abort(422)  
  '''
  @FINISHED: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    if not request.method == 'POST':
        abort(405)
    data = request.get_json()
    search_term = data.get('searchTerm')
    questions = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
    paginate_questions = paginated_questions(request, questions)
    if len(paginate_questions) == 0:
      abort(404)
    try:
      return jsonify({
        'success': True,
        'questions': paginate_questions,
        'total_questions': len(paginate_questions)
      })
    except:
      abort(422)


  '''
  @FINISHED: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_questions_by_category(category_id):
    if not request.method == 'GET':
        abort(405)
    questions = Question.query.filter(Question.category == str(category_id)).all()
    paginate_list = paginated_questions(request, questions)
    current_category = Category.query.filter(Category.id == category_id).one_or_none()
    if len(paginate_list) == 0:
      abort(404)
    try:
      return jsonify({
        'success': True,
        'questions': paginate_list,
        'total_questions': len(paginate_list),
        'current_category': current_category.id
      })
    except:
      abort(422)
  '''
  @FINISHED: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    if not request.method == 'POST':
        abort(405)
    body = request.get_json()
    previous_questions = body.get('previous_question', [])
    quiz_category = body.get('quiz_category', None)
    if quiz_category:
      if quiz_category['id'] == 0:
        all_questions = Question.query.all()
      else:
        all_questions = Question.query.filter_by(category = quiz_category['id']).all()
    if len(all_questions) == 0:
      abort(404)
    try:
      final_questions = []
      for question in all_questions:
        if question.id not in previous_questions:
          final_questions.append(question.format())
      if len(final_questions) == 0:
        return jsonify({
          'question': False
        })
      else:
        return jsonify({
          'question': random.choice(final_questions)
        })
    except:
      abort(422)


  '''
  @FINISHED: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random question within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "Not Found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
    }), 400

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "method not allowed"
    }), 405
  
  return app

    
