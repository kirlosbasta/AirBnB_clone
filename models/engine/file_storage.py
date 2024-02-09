#!/usr/bin/python3
'''Module contain a class called file_storage'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    that serializes instances to a JSON file and deserializes JSON
    file to instances
    '''
    __file_path = 'file.json'
    __objects = {}
    class_dict = {
    "BaseModel": BaseModel
}

    def all(self):
        '''return a dictionary with all the objects of the class'''
        return self.__objects
    
    def new(self, obj):
        '''
        set a new object to the list of objects
        Args:
            obj: Inistance of a class
        '''
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        json_dict = {key: obj.to_dict() for key, obj in self.all().items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json_string = json.dumps(json_dict)
            f.write(json_string)

    def reload(self):
        '''reload json strings from file_path to objects again'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_string = f.read()
                json_obj_dict = json.loads(json_string)
                for key, obj in json_obj_dict.items():
                    FileStorage.__objects[key] = self.class_dict[obj['__class__']](**obj)
        except Exception:
            pass
