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
motto_data = data["famous"] # a 代表prefix_data，b代表postfix_data
prefix_data = data["before"] # 在motto_data前面弄点nonsense_data
postfix_data = data['after']  # 在motto_data后面弄点nonsense_data
nonsense_data = data['bosh'] # 代表文章主要nonsense_data来源

xx = "学生会退会"

repeat_factor = 2

def randomized_yield(iterable):
    global repeat_factor
    pool = list(iterable) * repeat_factor
    while True:
        random.shuffle(pool)
        for ele in pool:
            yield ele

nonsense_generator = randomized_yield(nonsense_data)
motto_generator = randomized_yield(motto_data)

def new_motto():
    global motto_generator
    xx = next(motto_generator)
    xx = xx.replace("a", random.choice(prefix_data) )
    xx = xx.replace("b", random.choice(postfix_data) )
    return xx

def new_paragraph():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            randsrc = random.randint(0,100)
            if randsrc < 5:
                tmp += new_paragraph()
            elif randsrc < 20 :
                tmp += new_motto()
            else:
                tmp += next(nonsense_generator)
        tmp = tmp.replace("x",xx)
        print(tmp)
