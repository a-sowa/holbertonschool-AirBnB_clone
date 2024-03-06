#!/usr/bin/python3
"""HBNBCommand class for the console."""

import cmd
import shlex
from models import (storage, base_model,
                    user, place, state, city, amenity, review)

class_dict = {
    "BaseModel": base_model.BaseModel,
    "User": user.User,
    "State": state.State,
    "City": city.City,
    "Amenity": amenity.Amenity,
    "Place": place.Place,
    "Review": review.Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel or other class."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in class_dict:
            print("** class doesn't exist **")
            return
        instance = class_dict[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        obj = all_objs.get(key, None)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        if len(args) > 0 and args[0] not in class_dict:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs:
                if len(args) > 0 and args[0] != obj_id.split('.')[0]:
                    continue
                print(all_objs[obj_id])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                obj = all_objs[key]
                setattr(obj, args[2], args[3])
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
