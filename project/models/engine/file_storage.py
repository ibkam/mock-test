#!/usr/bin/python3
"""
Contains the file_storage class model
"""


import json


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __obejects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the 'obj'
        with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as file:
            dict_storage = []
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
                json.dump(dict_storage, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        Only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, mode="r") as file:
                obj_file = json.load(file)
            for key in obj_file:
                self.objects[key] = classes[obj_file[key]["__class__"]]
                (obj_file[key])
        except self.__file_path.DoesNotExist:
            pass
