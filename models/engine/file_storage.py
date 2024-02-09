#!/usr/bin/python3
import uuid
from datetime import datetime
import json
import models
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

class BaseModel:
	"""class BaseModel by using dictionary representation"""
	def __init__(self, *args, **kwargs):
	""""initialize the Id attributes for each instamce"""
		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':
					setattr(self, key, datetime.strptime(value, "%Y-%m-")
				elif key != '__class__':
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = self.updated = datetime.now()
			models.storage.new(self)
	def to_dict(self):
        '''
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        return dic

	class FileStorage:
	"""serializes instances to a JSON file and deserializes JSON file to instances"""
		__file_path = "file.json"
		__objects = {}

		def all(self):
		"""returns the dictionary __objects"""
			return FileStorage.__objects

		def new(self, obj):
		"""sets in __objects the obj with key <obj class name>.id"""
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		FileStorage.__objects[key] = obj

		def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
			serialized_objects = {}
			for key, value in FileStorage.__objects.items():
			serialized_objects[key] = value.to_dict()
		with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)
	
def save(self):
		models.storage.save()

	def reload(self):
	"""deserializes the JSON file to __objects"""
		try:
			with open(Filetorage.__file_path, 'r', encoding = utf '-8')
	loaded_objects = json.load(file)
	for key, value in loaded_object.items():
		class_name, obj_id = key.split('.')
		obj_cls = getattr(models, class_name)
		obj_instance = obj_cls(**value)
		FileStorage.__objects[key] = obj_instance
	except FileNotFoundError:
		pass
