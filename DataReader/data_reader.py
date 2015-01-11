import re


class DataReader(object):
    def __init__(self):
        self.data_file = ''

    def open_data_file_from_path(self, path):
        self.data_file = open(path, 'r')

    def _get_variable_from_data_file(self, variable_name):
        for line in self.data_file:
            match_variable = re.search('%s=[\d|\.]*'%variable_name, line)
            if match_variable:
                match_value = re.search('[\d|\.]+$', match_variable.group(0))
                return float(match_value.group(0))

    def create_data_dict(self):
        return {
                    'N' : self._get_variable_from_data_file('N'),
                    'K' : self._get_variable_from_data_file('K'),
                    'Q' : self._get_variable_from_data_file('Q'),
                    'ro' : self._get_variable_from_data_file('ro'),
                    'alfa' : self._get_variable_from_data_file('alfa'),
                    'u' : self._get_variable_from_data_file('u')
               }
