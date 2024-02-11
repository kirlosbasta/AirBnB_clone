#!/usr/bin/python3
'''Module that contain a class Review'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class that conatain basic info about the Review'''
    place_id = ''
    user_id = ''
    text = ''
