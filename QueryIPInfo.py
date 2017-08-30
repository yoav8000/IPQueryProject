from RestCommunicator import *
from JsonParser import *
from IPInfo import *
from MarkdownFormatter import *
import sys
import os

PREFIX = 'http://ipinfo.io/'
SUFFIX = '/json'  # forces the server to return a json response.


def write_markdown(formatted_info, ip):
    try:
        markdown_file = open('ip_information.md', "w")
        path = os.path.abspath('ip_information.md')
        markdown_file.write(formatted_info)
        print "File was created successfully in: " + path
        markdown_file.close()
    except IOError:
        print "Encountered and Error in opening the file or writing to it."
    except:
        print "Encountered an unexpected Error."
        sys.exit(1)


def query_ip():
    if len(sys.argv) != 2:
        print "Usage: QueryIPInfo.py IP-ADDRESS (e.g. 8.8.8.8)"
        sys.exit(1)
    else:
        try:
            ip_address = sys.argv[1]
            communicator = RestCommunicator()
            raw_info = communicator.send_get_request(PREFIX, ip_address, SUFFIX)
            ip_info = IPInfo(JsonParser(), raw_info)
            md_formatter = MarkdownFormatter(ip_info)
            formatted_info = md_formatter.form()
            write_markdown(formatted_info, ip_address)
        except:
            pass


if __name__ == '__main__':
    query_ip()
