class Parser(object):
    """
    An abstract class tha contains a dictionary and has a get method to
    return it and has a parse method that parses a text given.
    """

    def __init__(self):
        """
        The constructor, initializes the dictionary.
        """
        self._ip_dictionary = {}

    def parse(self, raw_ip_info):
        """
        A method that parses a text given as an input and then saves is
        inside the dictionary.
        :param raw_ip_info: the input that needs to be parsed.
        :return: the method returns nothing.
        """
        pass

    def get_ip_dictionary(self):
        """
        Getter
        :return: The method returns the dictionary.
        """
        return self._ip_dictionary
