#!/usr/bin/python3
'''Module that contain a class City'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Class that conatain basic info about the city'''
    state_id = ''
    name = ''
