import requests
import ipaddress
from CustomExceptions import InvalidIPAddress
from CustomExceptions import BogonIP


class RestCommunicator(object):
    """ The class is in charge of sending a get request
        and return the output received from the server depends
        on the IP address,if necessary it raises an exception."""

    def send_get_request(self, prefix, ip_address, suffix):
        """The method validates the ip and if it is a valid ip then it
         sends an http get request to the server (using rest architecture),
          if it doesn't encounter any error - it returns
        the answer it received from the server, otherwise
        it throws the proper exception"""
        try:
            if self.is_a_valid_ip_address(ip_address):  # Check if is a valid IP
                uri = prefix + ip_address + suffix  # Assemble the uri
                response = requests.get(uri)
                if response.content.__contains__('bogon'):  # Is a bogon IP
                    raise BogonIP
                return response.content  # Received a proper answer.
            else:
                raise InvalidIPAddress
        # CHECK RETURN VALUE = 200 AND CHECK IF WE EXCEEDED THE AMOUNT ALLOWED
        except Exception as ex:
            raise ex

    def is_a_valid_ip_address(self, ip_address):
        """The method validates the ip address received and
        returns true if it is an ipv6 or an ipv4 and false otherwise"""
        try:
            unicode_ip_add = unicode(ip_address)
            ipaddress.ip_network(unicode_ip_add)
            return True
        except ValueError as ex:
            return False
