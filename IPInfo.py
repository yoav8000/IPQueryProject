class IPInfo(object):
    """ The class is responsible of holding the information
    on the IP address, it contains a parser object."""

    def __init__(self, parser, raw_ip_info):
        """
         the constructor: the method calls the parser to parse the
         information received and then it initializes three dictionaries:
         one for the location info , second for the coordinates info and
         third for the organizations info and sets the processed information
         inside the three dictionaries.
        :param parser: a parser that is in charge of parsing the information
        according to the format the information is saved.
        :param raw_ip_info: a long string that describes the ip information
        retrieved.
        """
        self._parser = parser
        self._parser.parse(raw_ip_info)
        parser_dict = self._parser.get_ip_dictionary()
        self._location_dict = {}
        self._coordinate_dict = {}
        self._organization_dict = {}
        self.set_parser_info_into_dict(parser_dict)

    def set_parser_info_into_dict(self, parser_dict):
        """
        The method sets the parsed input into the three dictionaries
        that the ip_info object holds.
        :param parser_dict: The dictionary that holds the information about
        the IP address.
        :return: the method doesn't return anything.
        """
        self.set_location_info(parser_dict)
        self.set_coordinate_info(parser_dict)
        self.set_organization_info(parser_dict)

    def set_location_info(self, dict):
        """
        The method is in charge of setting the information saved in the dict
        location that is related to the location into the location dictionary.
        :param dict: the dictionary that holds the processed information.
        :return: the method doesn't return anything.
        """
        self._location_dict['country'] = dict.get('country', '')
        self._location_dict['region'] = dict.get('region', '')
        self._location_dict['city'] = dict.get('city', '')

    def set_coordinate_info(self, dict):
        """
        The method is in charge of setting the information saved in the dict
        location that is related to the coordinates into the location
        dictionary.
        :param dict: the dictionary that holds the processed information.
        :return: the method doesn't return anything.
        """
        location = dict.get('loc')
        if location is not None and location.contains(','):
            loc = location.split(',')
            self._coordinate_dict['latitude'] = loc[0]
            self._coordinate_dict['longitude'] = loc[1]
        else:
            self._coordinate_dict['latitude'] = ''
            self._coordinate_dict['longitude'] = ''

    def set_organization_info(self, dict):
        """
        The method is in charge of setting the information saved in the dict
        location that is related to the organization into the location
        dictionary.
        :param dict: the dictionary that holds the processed information.
        :return: the method doesn't return anything.
        """
        self._organization_dict['organization'] = dict.get('org', '')

    def get_location_info(self):
        """
        The method returns a copy of the location dictionary.
        :return: A copy of the location dictionary
        """
        return dict(self._location_dict)

    def get_coordinate_info(self):
        """
        The method returns a copy of the coordinate dictionary.
        :return: A copy of the coordinate dictionary
        """
        return dict(self._coordinate_dict)

    def get_organization_info(self):
        """
        The method returns a copy of the organizations dictionary.
        :return: A copy of the organizations dictionary
        """
        return dict(self._organization_dict)
