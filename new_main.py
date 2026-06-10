import random
import item_lists
import re
import visual_layout

def choose_one(item):
    return random.choice(list(item))

def set_descriptor():
    if random.random() < 0.05:
        descriptor = choose_one(item_lists.pop_culture_list) + "-style"
    else:
        descriptor = choose_one(item_lists.descriptors)
    return descriptor

def set_setting(descriptor):
    

def set_object():
    return choose_one(item_lists.items)

def set_verb():
    return choose_one(item_lists.verbs)

def set_format():
    if random.random() < 0.95:
        return f"{set_setting} {set_descriptor} {set_object}

