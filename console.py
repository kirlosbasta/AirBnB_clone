#!/usr/bin/python3
'''Program that contain the entry point of the command interpreter'''
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''the console command interpereter class'''
    prompt = '(hbnb) '
    class_dict = {'BaseModel': BaseModel}

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
        elif '{}.{}'.format(arg_list[0], arg_list[1]) not in models.storage.all():
            print("** no instance found **")
        else:
            inistance = models.storage.all()['{}.{}'.format(arg_list[0], arg_list[1])]
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
        elif '{}.{}'.format(arg_list[0], arg_list[1]) not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()['{}.{}'.format(arg_list[0], arg_list[1])]
            models.storage.save()

    def do_all(self, args):
        '''Prints all string representation of all instances based or not on the class name
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
        '''Updates an instance based on the class name and id by adding or updating attribute
Usage: update <class name> <id> <attribute name> "<attribute value>"'''
        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif '{}.{}'.format(arg_list[0], arg_list[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(arg_list) == 2:
            print('** attribute name missing **')
        elif len(arg_list) == 3:
            print('** value missing **')
        else:
            obj_id = '{}.{}'.format(arg_list[0], arg_list[1])
            objects_dict = models.storage.all()
            model = objects_dict[obj_id]
            model.__dict__[arg_list[2]] = eval(arg_list[3])
            model.save()

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
