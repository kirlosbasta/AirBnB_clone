#!/usr/bin/python3
'''unittest module for the State class'''
import datetime
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''Test class for State class'''
    def test_class(self):
        '''test that the class exist'''
        model = State()
        self.assertEqual('State', model.__class__.__name__)

    def test_id(self):
        '''test that two inistance doesn't have the same id'''
        model_1 = State()
        model_2 = State()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_str(self):
        '''test str repersentation of the class inistance'''
        model_1 = State()
        self.assertIn('[State]', str(model_1))
        self.assertIn('id', str(model_1))
        self.assertIn('updated_at', str(model_1))
        self.assertIn('created_at', str(model_1))

    def test_save(self):
        '''test that save changes the updated_at attribute to the
        current time'''
        model_1 = State()
        before = model_1.updated_at
        model_1.save()
        after = model_1.updated_at
        self.assertNotEqual(before, after)

    def test_save_arg(self):
        '''test the number of arguments'''
        model_1 = State()
        with self.assertRaises(TypeError):
            model_1.save(self.id)

    def test_to_dict(self):
        '''test to_dict method'''
        model_1 = State()
        model_dict = model_1.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'State')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_arg(self):
        '''test to_dict method arguments number'''
        model_1 = State()
        with self.assertRaises(TypeError):
            model_1.to_dict(self.id)

    def test_State_recreation(self):
        '''test reacreation of base Model from a dictionary'''
        model_1 = State()
        model_1_dict = model_1.to_dict()
        model_2 = State(**model_1_dict)
        self.assertIsInstance(model_2, State)
        self.assertNotIn('__class__', model_2.__dict__)
        self.assertIsNot(model_1, model_2)
        self.assertEqual(model_1.id, model_2.id)
        self.assertIsInstance(model_2.created_at, datetime.datetime)
        self.assertIsInstance(model_2.updated_at, datetime.datetime)

    def test_name(self):
        '''test that the attribute exist'''
        model = State()
        self.assertEqual(model.name, '')


if __name__ == '__main__':
    unittest.main()
