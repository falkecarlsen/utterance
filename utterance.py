#!/usr/bin/env python

import argparse
from pathlib import Path

available_path = f'{Path.home()}/.config/utterance/available'
used_path = f'{Path.home()}/.config/utterance/used'


def check_if_available(arg: str) -> bool:
    file = open(available_path, 'r')
    available = file.readlines()
    file.close()
    if f'{arg.lower()}\n' in available:
        return True
    return False


def check_if_used(arg: str) -> bool:
    file = open(used_path, 'r')
    used = file.readlines()
    file.close()
    if f'{arg.lower()}\n' in used:
        return True
    return False


def remove_from_available(arg: str):
    with open(available_path, 'r') as file:
        lines = file.readlines()
    with open(available_path, 'w') as file:
        for line in lines:
            if line.strip('\n') != arg.lower():
                file.write(f'{line}')


def add(arg: str):
    type = 'phrase' if ' ' in arg else 'word'
    if check_if_available(arg):
        print(f'Error: {type} \'{arg}\' is already logged, but has not been used!')
        exit(1)
    if check_if_used(arg):
        print(f'Error: {type} \'{arg}\' is already logged, and has been used!')
        exit(1)

    with open(available_path, 'a') as avail:
        avail.write(f'{arg.lower()}\n')
    print(f'Added {type} \'{arg}\' to available {type}s')


def remove(arg: str):
    type = 'phrase' if ' ' in arg else 'word'
    if check_if_used(arg):
        print(f'Error: {type} \'{arg}\' is already used!')
        exit(1)
    if not check_if_available(arg):
        print(f'Could not find {type} \'{arg}\' in available {type}s, adding...')
        add(arg)

    with open(used_path, 'a') as used:
        used.write(f'{arg.lower()}\n')
    remove_from_available(arg)
    print(f'Removed {type} \'{arg}\' from available {type}s')


def list_contents(file: str):
    with open(file, 'r') as file:
        for x in file.read().split('\n'):
            if x is not '':
                print(x.capitalize())


parser = argparse.ArgumentParser()
parser.add_argument('-a', metavar='STRING', type=str, nargs='?', help='add word or phrase to available list')
parser.add_argument('-r', metavar='STRING', type=str, nargs='?', help='move word or phrase to used list')
parser.add_argument('--avail', action='store_true', help='list all available words or phrases')
parser.add_argument('--used', action='store_true', help='list all used words or phrases')

args = parser.parse_args()

if args.a:
    add(args.a)

if args.r:
    remove(args.r)

if args.avail:
    list_contents(available_path)

if args.used:
    list_contents(used_path)
