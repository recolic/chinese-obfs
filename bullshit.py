#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
from random import randint
import gzip

def loadJson(fileName):
    import json
    strList = fileName.split(".")
    if strList[len(strList)-1].lower() == "json":
        with open(fileName,mode='r',encoding="utf-8") as file:
            return json.loads(file.read())

data = loadJson("data.json")
famous_data   = list(data['famous'   ]) # a 代表prefix_data，b代表postfix_data
prefix_data   = list(data['prefixes' ]) # 在famous_data前面弄点nonsense_data
postfix_data  = list(data['postfixes']) # 在famous_data后面弄点nonsense_data
nonsense_data = list(data['shits'    ]) # 代表文章主要nonsense_data来源

famous_bits_count = 6
prefix_bits_count = 2
postfix_bits_count = 3
nonsense_bits_count = 5

print("debug: len=", [len(l) for l in [famous_data, prefix_data, postfix_data, nonsense_data]])

repeat_factor = 2

def new_famous():
    global famous_generator
    famous = next(famous_generator)
    famous = famous.replace("$prefix", random.choice(prefix_data) )
    famous = famous.replace("$postfix", random.choice(postfix_data) )
    return famous

def paragraph_tail():
    return "\r\n    "

def paragraph_is_valid(text):
    if len(text) < 16:
        return False
    if text[-1] == '，' or text[-1] == '：':
        return False
    return True

def slice_bits(data, offset, count):

    return 8

topic = 'testing_topic'
input_string = 'hello world'

def data_serialize(data):
    return gzip.compress(data, compresslevel=9)

def decode(text):
    for line in text.split('\r\n'):
        paragraph = line.strip()
        if paragraph == '':
            continue

        # 1. famous-prefix reorder. 

        # 2. element match and decode bits.


def encode(text, topic, data):
    result = '    '
    curr_paragraph = ''
    curr_data_offset = 0
    while curr_data_offset < len(data)*8 :
        if randint(0,100) < 5 and paragraph_is_valid(curr_paragraph):
            result += curr_paragraph + paragraph_tail()
            curr_paragraph = ''
        elif randint(0,100) < 20 :
            # add a famous
            _index0 = slice_bits(data, curr_data_offset, prefix_bits_count)
            curr_data_offset += prefix_bits_count
            _index1 = slice_bits(data, curr_data_offset, famous_bits_count)
            curr_data_offset += famous_bits_count
            _index2 = slice_bits(data, curr_data_offset, postfix_bits_count)
            curr_data_offset += postfix_bits_count

            curr_paragraph += new_famous(famous_data[_index1], prefix_data[_index0], postfix_data[_index2])
        else:
            # TODO
    result = result.replace("$topic",topic)
    print(result)
