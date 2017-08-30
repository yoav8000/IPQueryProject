class BogonIP(Exception):
    """
    An exception that is being raised when a bogon IP address is received,
    Meaning, that was in a valid IP address format thought it was a fake IP
    address .
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
