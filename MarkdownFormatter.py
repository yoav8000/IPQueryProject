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
        formatted_info = ''
        formatted_info = ''.join([formatted_info,
                                  self.create_table_from_dict('Location',
                                                              self._ip_info.get_location_info())])
        formatted_info = ''.join([formatted_info,
                                  self.create_table_from_dict('Coordinates',
                                                              self._ip_info.get_coordinate_info())])
        formatted_info = ''.join([formatted_info, self.create_table_header(
            'Organizations')])
        formatted_info = ''.join([formatted_info,
                                  self._ip_info.get_organization_info()[
                                      'organization'] + '\n'])
        return formatted_info

    def create_table_from_dict(self, table_header, current_dict):
        """
        The method is in charge of creating a table out of a dictionary.
        First it creates a header and then calls other method that creates
        the table rows depend on their type a header row or a value row.
        :param table_header: The header of the table.
        :param current_dict: The dictionary that holds the information.
        :return: The method returns a string represents a table with the
        information in the dictionary.
        """
        end_col = ' |'
        end_line = '\n'
        start_new_col_header = '|:'
        current_header = self.create_table_header(table_header)
        table = current_header
        # create a table header and join it to the table.

        line_length = self.find_max_length_in_dict(current_dict)
        header_row = self.create_table_row(current_dict, line_length,
                                           RowType.header)
        table = ''.join([table, header_row])
        # create a table row that contains all of the header keys and adds it
        #  to the table.
        header_length = len(current_dict)
        for i in range(header_length):
            # creates the separation between table keys and table values.
            hyphen_amount = '-' * line_length
            table = ''.join([table, start_new_col_header, hyphen_amount])
        table = ''.join([table, end_col, end_line])
        current_row = self.create_table_row(current_dict, line_length,
                                            RowType.value)
        # creates a row for the values
        table = ''.join([table, current_row])
        # add the row to the table.
        return table

    def create_table_header(self, table_header):
        """
        The method creates a table header using the join function.
        :param table_header: The table header.
        :return: the method returns a string that represents the table
        header in a markdown format.
        """
        end_line = '\n'
        return ''.join(['#### ', table_header, end_line])

    def create_table_row(self, current_dict, line_length, row_type):
        """
        The method creates a table row out of the dictionary received using
        the join function, it does so by checking the type of the line (
        header or value) and then it places them in a string that represents
        the row in a markdown format.
        :param current_dict: The dictionary that holds the information.
        :param line_length: the length of the line.
        :param row_type: the type of the row (header or value).
        :return: the method returns a string represents a row in the table.
        """

        start_new_col = '| '
        end_col = ' |'
        end_line = '\n'
        row = ''
        for current_key in current_dict:
            if row_type == RowType.header:
                spaces = ' ' * (line_length - len(current_key))
                # for proper alignment.
                row = ''.join([row, start_new_col, current_key, spaces])
            elif row_type == RowType.value:
                val = current_dict[current_key]
                spaces = ' ' * (line_length - len(val))
                row = ''.join([row, start_new_col, val, spaces])
        row = ''.join([row, end_col, end_line])
        return row

    def find_max_length_in_dict(self, current_dict):
        """
        The method finds the maximum length of a dictionary (from the keys and
        values).
        :param current_dict: the dictionary that holds the information.
        :return: the method return the maximum length.
        """
        max_key_length = max(len(key) for key in current_dict)
        max_val_key = max(current_dict, key=lambda k: len(current_dict[k]))
        max_value_length = len(current_dict[max_val_key])
        if max_key_length > max_value_length:
            return max_key_length
        else:
            return max_value_length


class RowType(Enum):
    """
    An enum class defines the rows type - header or value.
    """
    header = 1
    value = 2
