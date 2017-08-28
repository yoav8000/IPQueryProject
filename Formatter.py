class Formatter(object):
    """ The class is an abstract formatter,
     it contains an ip_info received in the constructor tha has all
     of the information on the IP address.
     and has a form method that format the information"""

    def __init__(self, ip_info):
        """ The constructor:
        ip_info is an object that contains the information about the IP
        address"""
        self._ip_info = ip_info

    def form(self):
        """
        The method formats the information held in the ip_info it holds.
        """
        pass
