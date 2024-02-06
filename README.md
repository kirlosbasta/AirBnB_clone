0x00.AirBnB clone - The console
Welcome to the AirBnB clone project!
This project involves the creation of python packages and command interpreters using cmd module, serializing and deserializing a class, and unit testing.

Command interpreters are written in a simple framework provided by the cmd class.
It is started by typing import cmd.
It uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler.
example of a command interpreter is as follows:
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print "hello"
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
