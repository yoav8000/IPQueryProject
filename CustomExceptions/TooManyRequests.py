class TooManyRequests(Exception):
    """
    An exception that is being raised when a 429 http status code is being
    returned from the http get request , meaning too many requests were sent .
    """
    pass
