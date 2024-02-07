#!/usr/bin/python3
'''unittest module for the base model class'''
import unittest
from models.base_model import BaseModel


class TestbaseModel(unittest.TestCase):
    '''Test class of base model class'''
    def test_class(self):
        '''test that the class exist'''
        model = BaseModel()
        self.assertEqual('BaseModel', model.__class__.__name__)

    def test_id(self):
        '''test that two inistance doesn't have the same id'''
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_str(self):
        '''test str repersentation of the class inistance'''
        model_1 = BaseModel()
        self.assertIn('[BaseModel]', str(model_1))
        self.assertIn('id', str(model_1))
        self.assertIn('updated_at', str(model_1))
        self.assertIn('created_at', str(model_1))

    def test_save(self):
        '''test that save changes the updated_at attribute to the current time'''
        model_1 = BaseModel()
        before = model_1.updated_at
        model_1.save()
        after = model_1.updated_at
        self.assertNotEqual(before, after)

    def test_save_arg(self):
        '''test the number of arguments'''
        model_1 = BaseModel()
        with self.assertRaises(TypeError):
            model_1.save(self.id)

    def test_to_dict(self):
        '''test to_dict method'''
        model_1 = BaseModel()
        model_dict = model_1.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_arg(self):
        '''test to_dict method arguments number'''
        model_1 = BaseModel()
        with self.assertRaises(TypeError):
            model_1.to_dict(self.id)


if __name__ == '__main__':
    unittest.main()
