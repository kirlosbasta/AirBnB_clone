#!/usr/bin/python3
'''Program that contain the entry point of the command interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''the console command interpereter class'''
    prompt = '(hbnb) '

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
