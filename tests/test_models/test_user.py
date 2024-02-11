#!/usr/bin/python3
'''unittest module for the user class'''
import datetime
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Test class for User class'''
    def test_class(self):
        '''test that the class exist'''
        model = User()
        self.assertEqual('User', model.__class__.__name__)

    def test_id(self):
        '''test that two inistance doesn't have the same id'''
        model_1 = User()
        model_2 = User()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_str(self):
        '''test str repersentation of the class inistance'''
        model_1 = User()
        self.assertIn('[User]', str(model_1))
        self.assertIn('id', str(model_1))
        self.assertIn('updated_at', str(model_1))
        self.assertIn('created_at', str(model_1))

    def test_save(self):
        '''test that save changes the updated_at attribute to the
        current time'''
        model_1 = User()
        before = model_1.updated_at
        model_1.save()
        after = model_1.updated_at
        self.assertNotEqual(before, after)

    def test_save_arg(self):
        '''test the number of arguments'''
        model_1 = User()
        with self.assertRaises(TypeError):
            model_1.save(self.id)

    def test_to_dict(self):
        '''test to_dict method'''
        model_1 = User()
        model_dict = model_1.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'User')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_arg(self):
        '''test to_dict method arguments number'''
        model_1 = User()
        with self.assertRaises(TypeError):
            model_1.to_dict(self.id)

    def test_User_recreation(self):
        '''test reacreation of base Model from a dictionary'''
        model_1 = User()
        model_1_dict = model_1.to_dict()
        model_2 = User(**model_1_dict)
        self.assertIsInstance(model_2, User)
        self.assertNotIn('__class__', model_2.__dict__)
        self.assertIsNot(model_1, model_2)
        self.assertEqual(model_1.id, model_2.id)
        self.assertIsInstance(model_2.created_at, datetime.datetime)
        self.assertIsInstance(model_2.updated_at, datetime.datetime)

    def test_email(self):
        '''test that the attribute exist'''
        model = User()
        self.assertEqual(model.email, '')

    def test_first_name(self):
        '''test that the attribute exist'''
        model = User()
        self.assertEqual(model.first_name, '')

    def test_last_name(self):
        '''test that the attribute exist'''
        model = User()
        self.assertEqual(model.last_name, '')

    def test_password(self):
        '''test that the attribute exist'''
        model = User()
        self.assertEqual(model.password, '')


if __name__ == '__main__':
    unittest.main()
