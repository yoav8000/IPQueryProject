from RestCommunicator import *
from JsonParser import *
from IPInfo import *
from MarkdownFormatter import *
import sys

PREFIX = 'http://ipinfo.io/'
SUFFIX = '/json'  # forces the server to return a json file.


def write_markdown(formatted_info, ip):
    try:
        markdown_file = open('ip_information.md'.format(ip), "w")
        markdown_file.write(formatted_info)
        markdown_file.close()
    except Exception:
        print "Encountered and error in opening the file or writing to it."
        sys.exit(1)


def query_ip():
    if len(sys.argv) != 2:
        print "Usage: QueryIPInfo.py IP-ADDRESS (e.g 8.8.8.8)"
        sys.exit(1)
    else:
        ip_address = sys.argv[1]
        communicator = RestCommunicator()
        raw_info = communicator.send_get_request(PREFIX, ip_address, SUFFIX)
        ip_info = IPInfo(JsonParser(), raw_info)
        md_formatter = MarkdownFormatter(ip_info)
        formatted_info = md_formatter.form()
        write_markdown(formatted_info, ip_address)


if __name__ == '__main__':
    query_ip()
