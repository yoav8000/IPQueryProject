from RestCommunicator import *
from JsonParser import *
from IPInfo import *
from MarkdownFormatter import *
import sys


def query_ip():
    if len(sys.argv) != 2:
        print "Usage: QueryIPInfo.py IP-ADDRESS(for exanple: 8.8.8.8) "
        sys.exit(1)
    else:
        ip_address = sys.argv[1]
        h = RestCommunicator()
        prefix = 'https://ipinfo.io/'
        suffix = '/json'  # forces the server to return a json file.
        raw_info = h.send_get_request(prefix, ip_address, suffix)
        ip_info = IPInfo(JsonParser(), raw_info)
        md_formatter = MarkdownFormatter(ip_info)
        formatted_info = md_formatter.form()
        Markdown_file = open("IP Information.md", "w")
        Markdown_file.write(formatted_info)
        Markdown_file.close()


if __name__ == '__main__':
    query_ip()
