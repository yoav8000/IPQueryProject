from Formatter import *
from enum import Enum


class MarkdownFormatter(Formatter):
    """
    The class is a concrete Formatter which inherits the abstract Formatter
    class, The class is in charge of formatting the information held in the
    ip_info member.
    """

    def __init__(self, ip_info):
        """
        The constructor, calls the super class constructor with the ip_info
        object.
        :param ip_info: The object that holds the information on the ip address.
        """
        Formatter.__init__(self, ip_info)

    def form(self):
        """
        The method is in charge of formatting the ip information in a markdown
        table format, it creates a table for the location, the coordinates
        and the organization of the ip address and concat all of them into a
        long string which is in a markdown format.
        :return: The method returns a string represents the
         information about the ip address divided into tables.
        """
        formated_info = ''
        formated_info += self.create_table_from_dict('Location',
                                                     self._ip_info.get_location_info())
        formated_info += self.create_table_from_dict('Coordinates',
                                                     self._ip_info.get_coordinate_info())
        formated_info += '####  Organizations \n'
        formated_info += self._ip_info.get_organization_info()[
                             'organization'] + '\n'
        return formated_info

    def create_table_from_dict(self, table_header, current_dict):
        end_col = ' |'
        end_line = '\n'
        start_new_col_header = '|:'
        table = ''.join(self.create_table_header(table_header))
        # create a table header

        line_length = self.find_max_length_in_dict(current_dict)
        table = ''.join(
            [table, self.create_table_row(current_dict, line_length,
                                          RowType.header)])
        # create a table
        # rows tha contains all of the header keys

        header_length = len(current_dict)
        for i in range(header_length):
            # creates the seperation between table key and table value.
            hyphen_amount = '-' * line_length
            table = ''.join([table, start_new_col_header, hyphen_amount])
        table = ''.join([table, end_col, end_line])

        table = ''.join(
            [table, self.create_table_row(current_dict, line_length,
                                          RowType.value)])
        return table

    def create_table_header(self, table_header):
        end_line = '\n'
        return ''.join(['#### ', table_header, end_line])

    def create_table_row(self, current_dict, line_length, row_type):
        start_new_col = '| '
        end_col = ' |'
        end_line = '\n'
        row = ''
        for current_key in current_dict:
            if row_type == RowType.header:
                spaces = ' ' * (line_length - len(current_key))
                row = ''.join([row, start_new_col, current_key, spaces])
            elif row_type == RowType.value:
                val = current_dict[current_key]
                spaces = ' ' * (line_length - len(val))
                row = ''.join([row, start_new_col, val, spaces])
                row = ''.join([row, end_col, end_line])
        return row

    def find_max_length_in_dict(self, current_dict):
        max_length = 0
        for key in current_dict:
            key_length = len(key)
            val_length = len(current_dict[key])
            if key_length > max_length:
                max_length = key_length

            if val_length > max_length:
                max_length = val_length

        return max_length


class RowType(Enum):
    header = 1
    value = 2
