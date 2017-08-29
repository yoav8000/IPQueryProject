class BogonIP(Exception):
    """
    An exception that is being raised when a bogon IP address is received.
    """
    pass


class InvalidIPAddress(Exception):
    """
    An exception that is being raised when an invalid IP address is given.
    """
    pass


class TooManyRequests(Exception):
    """
    An exception that is being raised when a 429 http status code is being
    returned from the http get request , meaning too many requests were sent .
    """
    pass
