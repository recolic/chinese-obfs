#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random

def loadJson(fileName):
    import json
    strList = fileName.split(".")
    if strList[len(strList)-1].lower() == "json":
        with open(fileName,mode='r',encoding="utf-8") as file:
            return json.loads(file.read())

data = loadJson("data.json")
famous_data   = list(data['famous']) # a 代表prefix_data，b代表postfix_data
prefix_data   = list(data['before']) # 在famous_data前面弄点nonsense_data
postfix_data  = list(data['after' ]) # 在famous_data后面弄点nonsense_data
nonsense_data = list(data['bosh'  ]) # 代表文章主要nonsense_data来源

repeat_factor = 2

def randomized_yield(iterable):
    global repeat_factor
    pool = list(iterable) * repeat_factor
    while True:
        random.shuffle(pool)
        for ele in pool:
            yield ele

nonsense_generator = randomized_yield(nonsense_data)
famous_generator = randomized_yield(famous_data)

def new_famous():
    global famous_generator
    famous = next(famous_generator)
    famous = famous.replace("a", random.choice(prefix_data) )
    famous = famous.replace("b", random.choice(postfix_data) )
    return famous

def new_paragraph():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    topic = input("请输入文章主题:")
    result = str()
    while ( len(result) < 6000 ) :
        randsrc = random.randint(0,100)
        if randsrc < 5:
            result += new_paragraph()
        elif randsrc < 20 :
            result += new_famous()
        else:
            result += next(nonsense_generator)
    result = result.replace("x",topic)
    print(result)
