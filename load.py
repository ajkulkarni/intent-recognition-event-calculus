import os
import sys
import pandas as pd

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

def getClass():
    column_list = ['id','subject','scene','quality','relevance','verified','script','objects','descriptions','actions','length']
    df = pd.read_csv('Charades_v1_train.csv', header=None, names=column_list)
    target = open('class', 'w+')
    object_list = df['actions'].values.T.tolist()
    for obj in object_list:
        obj = str(obj)
        classes = obj.split(";")
        if(len(classes) > 0):
            target.write("[")
            for classid in classes:
                target.write(classid.split(" ")[0] + ",")
            target.write("]")
            target.write("\n")

def getObject():
    source = open('Charades_v1_objectclasses.txt')
    mapping = {}
    for line in source:
        object_list = line.split()
        object_sub_list = object_list[1].split("/")
        if(len(object_sub_list) > 1):
            for obj in object_sub_list:
                mapping[obj] = object_list[0]
        else:
            mapping[object_list[1]] = object_list[0]
    column_list = ['id','subject','scene','quality','relevance','verified','script','objects','descriptions','actions','length']
    df = pd.read_csv('Charades_v1_train.csv', header=None, names=column_list)
    target = open('objectid', 'w+')
    object_list = df['objects'].values.T.tolist()
    for obj in object_list:
        obj = str(obj)
        classes = obj.split(";")
        if(len(classes) > 0):
            target.write("[")
            for classid in classes:
                target.write(str(mapping.get(classid.split(" ")[0])) + ",")
            target.write("]")
            target.write("\n")

def getMapping():
    source1 = open('Charades_v1_objectclasses.txt')
    objectid_mapping = {}
    for line in source1:
        object_list = line.split()
        object_sub_list = object_list[1].split("/")
        if(len(object_sub_list) > 1):
            for obj in object_sub_list:
                objectid_mapping[obj] = object_list[0]
        else:
            objectid_mapping[object_list[1]] = object_list[0]

    source2 = open('Charades_v1_mapping.txt')
    mapping = []
    for line in source2:
        mapping.append(line.split())

    column_list = ['id','subject','scene','quality','relevance','verified','script','objects','descriptions','actions','length']
    df = pd.read_csv('Charades_v1_train.csv', header=None, names=column_list)
    target = open('mapping.db', 'w+')
    object_list = df['objects'].values.T.tolist()
    class_list = df['actions'].values.T.tolist()

    for index in range(7986):
        obj = str(object_list[index])
        objects = obj.split(";")
        objects_id = []
        if(len(objects) > 0):
            for ob in objects:
                objects_id.append(str(objectid_mapping.get(ob)))

        cl = str(class_list[index])
        classes = cl.split(";")
        class_id = []
        if(len(classes) > 0):
            for clas in classes:
                class_id.append(str(clas.split()[0]))

        for cid in class_id:
            for oid in objects_id:
                for relation in mapping:
                    if(relation[0] == cid and relation[1] == oid):
                        target.write("Mapping(" + relation[1] + "," + relation[2] + "," + relation[0] + ")" + "\n")



if __name__ == '__main__':
    #loadConstants();
    #loadObjects();
    #mapObjectToVerb();
    #mapVerbToObject();
    #getClass();
    #getObject();
    getMapping();
