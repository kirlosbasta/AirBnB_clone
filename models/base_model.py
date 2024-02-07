#!/usr/bin/python3
"""Module that conatain class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    '''
    class BaseModel that defines all common attributes/methods
    for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize the id and created_at and updated_at
        attributes for each inistance or recreate the inistance from kwargs'''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                else:
                    self.__dict__[key] = value
            self.created_at = datetime.fromisoformat(
                self.__dict__['created_at'])
            self.updated_at = datetime.fromisoformat(
                self.__dict__['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''string representaion of of the class inistance'''
        string = f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
        return string

    def save(self):
        '''
        updates the public instance attribute updated_at with the
        current datetime
        '''
        self.updated_at = datetime.now()

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
