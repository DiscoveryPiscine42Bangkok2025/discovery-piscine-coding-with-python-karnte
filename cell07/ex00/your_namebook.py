#!/usr/bin/env python3

def array_of_names(name: dict):
    name = []
    for first_name, last_name in persons.items():
        name.append(f"{first_name.capitalize()} {last_name.capitalize()}")
    return name



persons = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}

print(array_of_names(persons))