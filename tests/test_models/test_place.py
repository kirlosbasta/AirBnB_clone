#!/usr/bin/python3
'''unittest module for the user class'''
import datetime
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''Test class for Place class'''
    def test_class(self):
        '''test that the class exist'''
        model = Place()
        self.assertEqual('Place', model.__class__.__name__)

    def test_id(self):
        '''test that two inistance doesn't have the same id'''
        model_1 = Place()
        model_2 = Place()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_str(self):
        '''test str repersentation of the class inistance'''
        model_1 = Place()
        self.assertIn('[Place]', str(model_1))
        self.assertIn('id', str(model_1))
        self.assertIn('updated_at', str(model_1))
        self.assertIn('created_at', str(model_1))

    def test_save(self):
        '''test that save changes the updated_at attribute to the
        current time'''
        model_1 = Place()
        before = model_1.updated_at
        model_1.save()
        after = model_1.updated_at
        self.assertNotEqual(before, after)

    def test_save_arg(self):
        '''test the number of arguments'''
        model_1 = Place()
        with self.assertRaises(TypeError):
            model_1.save(self.id)

    def test_to_dict(self):
        '''test to_dict method'''
        model_1 = Place()
        model_dict = model_1.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'Place')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_arg(self):
        '''test to_dict method arguments number'''
        model_1 = Place()
        with self.assertRaises(TypeError):
            model_1.to_dict(self.id)

    def test_City_recreation(self):
        '''test reacreation of base Model from a dictionary'''
        model_1 = Place()
        model_1_dict = model_1.to_dict()
        model_2 = Place(**model_1_dict)
        self.assertIsInstance(model_2, Place)
        self.assertNotIn('__class__', model_2.__dict__)
        self.assertIsNot(model_1, model_2)
        self.assertEqual(model_1.id, model_2.id)
        self.assertIsInstance(model_2.created_at, datetime.datetime)
        self.assertIsInstance(model_2.updated_at, datetime.datetime)

    def test_name(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.name, '')

    def test_city_id(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.city_id, '')

    def test_user_id(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.user_id, '')

    def test_description(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.description, '')

    def test_number_rooms(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.number_rooms, 0)

    def test_number_bathrooms(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.number_bathrooms, 0)

    def test_max_guest(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.max_guest, 0)

    def test_price_by_night(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.price_by_night, 0)

    def test_latitude(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.latitude, 0.0)

    def test_longitude(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.longitude, 0.0)

    def test_amenity_ids(self):
        '''test that the attribute exist'''
        model = Place()
        self.assertEqual(model.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
