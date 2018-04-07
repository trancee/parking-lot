#!/usr/bin/env python

import sys

from app import services


def main(input_name):
    if input_name:
        pass

    else:
        while(True):
            command = input("> ")
            print (command)

            if command in ('q', 'quit', 'x', 'exit'):
                break

            args = command.split(' ')
            method = args.pop(0)

            if not hasattr(services, method):
                print ("Method not found")

            if method in dir(services):
                kwargs = {}
                result = getattr(services, method)(*args, **kwargs)
                print (result)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
