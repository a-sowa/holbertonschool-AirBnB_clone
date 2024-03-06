#!/usr/bin/python3
"""HBNBCommand class for the console"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            obj = all_objs.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
