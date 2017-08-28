from RestCommunicator import *
from JsonParser import *
from IPInfo import *
from MarkdownFormatter import *
from CustomExceptions import WrongAmountOfArgs
import sys


def main():
    if len(sys.argv) != 2:
        raise WrongAmountOfArgs
    else:
        try:
            ip_address = sys.argv[1]
            h = RestCommunicator()
            prefix = 'https://ipinfo.io/'
            suffix = '/json'    # forces the server to return a json file.
            raw_info = h.send_get_request(prefix, ip_address, suffix)
            ip_info = IPInfo(JsonParser(), raw_info)
            md_formatter = MarkdownFormatter(ip_info)
            formatted_info = md_formatter.form()
            Markdown_file = open("IP Information.md", "w")
            Markdown_file.write(formatted_info)
            Markdown_file.close()

        except Exception as ex:
            template1 = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message1 = template1.format(type(ex).__name__, ex.args)
            print message1


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
