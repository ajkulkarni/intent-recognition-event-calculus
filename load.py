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

def mapObjectToVerb():
    pre = "v0"
    for i in range(16, 24):
        source = open('Charades_v1_mapping.txt')
        object_list = []
        verb = pre + str(i)
        for line in source:
            mapping = line.split()
            if(mapping[2] == verb):
                object_list.append(mapping[1])
        source.close()
        print verb
        print object_list

def mapVerbToObject():
    pre = "o0"
    for i in range(19, 28):
        source = open('Charades_v1_mapping.txt')
        verb_list = []
        obj = pre + str(i)
        for line in source:
            mapping = line.split()
            if(mapping[1] == obj):
                verb_list.append(mapping[2])
        source.close()
        print obj
        print verb_list

if __name__ == '__main__':
    #loadConstants();
    #loadObjects();
    #mapObjectToVerb();
    mapVerbToObject();
