#!/usr/bin/python3
'''Program that contain the entry point of the command interpreter'''
import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''the console command interpereter class'''
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel, 'User': User, 'City': City, 'State': State,
        'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def do_create(self, args):
        '''create an inistance of the class specified and save it to storage
Usage: create <class_name>'''
        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            model = self.class_dict[arg_list[0]]()
            model.save()
            print(model.id)

    def do_show(self, args):
        '''Prints the string representation of an instance\
based on the class name and id
Usage: show <class_name> <id>'''
        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif '{}.{}'.format(arg_list[0], arg_list[1]) not in \
                models.storage.all():
            print("** no instance found **")
        else:
            inistance = models.storage.all()['{}.{}'.format(arg_list[0],
                                                            arg_list[1])]
            print(str(inistance))

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id
Usage: destroy <class_name> <id>'''
        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif '{}.{}'.format(arg_list[0], arg_list[1]) not in \
                models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()['{}.{}'.format(arg_list[0], arg_list[1])]
            models.storage.save()

    def do_all(self, args):
        '''Prints all string representation of all instances based or\
not on the class name
Usage: (all <class_name>) or (all)'''
        list_inist = []
        arg_list = args.split()
        if len(arg_list) == 0:
            list_inist = [str(val) for val in models.storage.all().values()]
            print(list_inist)
        elif len(arg_list) >= 1 and arg_list[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            for key, obj in models.storage.all().items():
                if f'{arg_list[0]}' in key:
                    list_inist.append(str(obj))
            print(str(list_inist))

    def do_update(self, args):
        '''Updates an instance based on the class name and id by adding or \
updating attribute
Usage: update <class name> <id> <attribute name> "<attribute value>"'''
        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif '{}.{}'.format(arg_list[0], arg_list[1]) not in \
                models.storage.all():
            print("** no instance found **")
        elif len(arg_list) == 2:
            print('** attribute name missing **')
        elif len(arg_list) == 3:
            print('** value missing **')
        else:
            obj_id = '{}.{}'.format(arg_list[0], arg_list[1])
            objects_dict = models.storage.all()
            model = objects_dict[obj_id]
            val = arg_list[3]
            if val.isdigit():
                val = eval(val)
            model.__dict__[arg_list[2]] = val
            model.save()

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, args):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        """Overrite emptyline default to do nothing"""
        pass

    def default(self, line):
        """Override the default onecmd method to handle dynamic commands"""
        p = r"(?P<cls>^[a-zA-Z]+)\.(?P<command>[a-zA-Z]+)\((?P<args>.*?)\)"
        mat = re.search(p, line)
        if mat:
            class_name = mat.group('cls')
            command = mat.group('command')
            args = mat.group('args')
            if command == 'all':
                self.do_all(class_name)
            elif command == 'count':
                self.count(class_name)
            elif command == 'show':
                quote_pattern = r"[\"\'](?P<arg>.*?)[\"\']"
                qu = re.search(quote_pattern, args)
                if qu:
                    self.do_show(" ".join([class_name, qu.group('arg')]))
                else:
                    self.do_show(" ".join([class_name, args]))
            elif command == 'destroy':
                quote_pattern = r"[\"\'](?P<arg>.*?)[\"\']"
                qu = re.search(quote_pattern, args)
                if qu:
                    self.do_destroy(" ".join([class_name, qu.group('arg')]))
                else:
                    self.do_destroy(" ".join([class_name, args]))
            else:
                return super().default(line)
        else:
            return super().default(line)

    def count(self, cls):
        '''print the number of inistace of cls'''
        list_inist = []
        for key, obj in models.storage.all().items():
            if f'{cls}' in key:
                list_inist.append(str(obj))
        print(len(list_inist))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
