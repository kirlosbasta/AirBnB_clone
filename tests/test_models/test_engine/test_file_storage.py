#!/usr/bin/python3
"""unittest module for the file storage class"""
import datetime
import unittest
import json
import os
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test class for file storage class"""
    def setUp(self):
        """set up an inistance of FileStorage"""
        self.store = FileStorage()

    def test_class(self):
        '''test that class exis'''
        self.store = FileStorage()
        self.assertIsInstance(self.store, FileStorage)

    def test_all_arg(self):
        '''test all no arg'''
        with self.assertRaises(TypeError):
            self.store.all(self)

    def test_all(self):
        '''test for all should return an dict of obj'''
        self.assertIsInstance(self.store.all(), dict)

    def test_new_arg(self):
        '''test for new should take on arg only'''
        with self.assertRaises(TypeError):
            self.store.new()
        with self.assertRaises(TypeError):
            self.store.new(self, self)
        self.store.new(BaseModel())

    def test_new(self):
        '''test for new should set the key as <obj class name>.id'''
        var = BaseModel()
        self.store.new(var)
        self.assertIn(f'BaseModel.{var.id}', self.store.all())

    def test_save_arg(self):
        '''test save no arg'''
        with self.assertRaises(TypeError):
            self.store.save(self)

    def test_save(self):
        '''test save should convert __objects to json file'''
        var = BaseModel()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])

    def test_reload_arg(self):
        '''reload has no arg'''
        with self.assertRaises(TypeError):
            self.store.reload(self)

    def test_storage_var(self):
        '''test storage variable exist and isinistance from filestorage'''
        if models.storage is not None:
            self.assertIsInstance(models.storage, FileStorage)

    def test_reload(self):
        '''test reload should convert json file to __objects if file exist'''
        self.assertGreaterEqual(len(models.storage.all()), 0)

    def test_reload_file_doesnot_exist(self):
        '''test nothing should happen if the file doesn't exist no exception'''
        if os.path.isfile('file.json'):
            os.remove('file.json')
        models.storage.reload()

    def test_User(self):
        '''test that filestorage support User'''
        var = User()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])

    def test_Amenity(self):
        '''test that filestorage support Amenity'''
        var = Amenity()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])

    def test_City(self):
        '''test that filestorage support City'''
        var = City()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])

    def test_Place(self):
        '''test that filestorage support Place'''
        var = Place()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])

    def test_Review(self):
        '''test that filestorage support Review'''
        var = Review()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])

    def test_State(self):
        '''test that filestorage support State'''
        var = State()
        self.store.new(var)
        self.store.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
            id_name = f'{var.__class__.__name__}.{var.id}'
            self.assertEqual(var.id, json_dict[id_name]['id'])


if __name__ == '__main__':
    unittest.main()
