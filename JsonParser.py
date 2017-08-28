from Parser import *
import json


class JsonParser(Parser):
    """
    The class is a concrete parser which inherits the abstract Parser
    and parse an input in a json format.
    """
    def __init__(self):
        """
        the constructor, it calls the super class constructor.
        """
        Parser.__init__(self)

    def parse(self, raw_ip_info):
        """
        The method parse a string in a json format, it holds the information
        in a dictionary.
        :param raw_ip_info: the string that needs to be processed.
        :return: the method doesn't return anything.
        """
        j_object = json.loads(raw_ip_info)
        for key in j_object:
            self._ip_dictionary[key] = j_object[key]
