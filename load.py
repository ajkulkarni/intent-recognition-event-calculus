import os
import sys

def loadObjects():
    source = open('Charades_v1_objectclasses.txt')
    target = open('output', 'a')
    for line in source:
        object_list = line.split()
        object_sub_list = object_list[1].split("/")
        if(len(object_sub_list) > 1):
            for obj in object_sub_list:
                target.write(obj +" causes " + object_list[0] +".\n")
        else:
            target.write(object_list[1] +" causes " + object_list[0] +".\n")

def loadConstants():
    source = open('Charades_v1_objectclasses.txt')
    target = open('output', 'w+')
    for line in source:
        object_list = line.split()
        object_sub_list = object_list[1].split("/")
        if(len(object_sub_list) > 1):
            for obj in object_sub_list:
                target.write(obj +" :: inertialFluent;\n")
        else:
            target.write(object_list[1] +" :: inertialFluent;\n")

if __name__ == '__main__':
    loadConstants();
    loadObjects();
