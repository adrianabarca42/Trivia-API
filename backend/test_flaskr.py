import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'hello',
            'answer': 'no',
            'category': '1',
            'difficulty': 2
        }
        
        self.new_category1 = {
            'type': 'History'
        }
        self.new_category1 = {
            'type': 'Art'
        }
        self.new_category1 = {
            'type': 'Sports'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertEqual(res.status_code, 200)
    
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))
        self.assertEqual(res.status_code, 200)

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(res.status_code, 200)

    def test_404_page_number(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Not Found')
        self.assertEqual(res.status_code, 404)

    def test_delete_questions(self):
        insert_res = self.client().post('/questions', json=self.new_question)
        insert_data = json.loads(insert_res.data)
        question_id = insert_data['created']

        res = self.client().delete(f'/questions/{question_id}')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_id)
        self.assertEqual(res.status_code, 200)

    def test_404_delete_question(self):
        res = self.client().delete('/questions/500')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Not Found')
        self.assertEqual(res.status_code, 404)

    def test_405_add_question_not_allowed(self):
        res = self.client().post('/questions/500', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'method not allowed')
        self.assertEqual(res.status_code, 405)

    def test_search_question(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'hello'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertEqual(res.status_code, 200)

    def test_405_non_post_method(self):
        res = self.client().delete('/questions/search', json={'searchTerm': 'anything'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'method not allowed')
        self.assertEqual(res.status_code, 405)

    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(res.status_code, 200)
    
    def test_404_no_questions_for_category(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Not Found')
        self.assertEqual(res.status_code, 404)

    def test_quizzes(self):
        res = self.client().post('/quizzes', json = {'previous_questions': [], 'quiz_category': {'id': '1'}})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['question']))
        self.assertEqual(res.status_code, 200)

    def test_404_no_questions_for_quizz(self):
        res = self.client().post('/quizzes', json = {'previous_questions': [], 'quiz_category': {'id': '5'}})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Not Found')
        self.assertEqual(res.status_code, 404)
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
