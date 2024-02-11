#!/usr/bin/python3
'''Module that contain a class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class that conatain basic info about the user like:-
username, password...etc'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
