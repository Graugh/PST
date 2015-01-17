import re


class DataReader(object):
    def __init__(self):
        self.data_file = ''

    def open_data_file_from_path(self, path):
        self.data_file = open(path, 'r')

    def _search_for_equation_with_given_variable_in_string(self, variable_name, string):
        return re.search('%s\W*=\W*[\d|\.]*'%variable_name, string)

    def _search_for_value_of_equation(self, equation):
        return float(re.search('[\d|\.]+$', equation).group(0))

    def _get_variable_from_data_file(self, variable_name):
        for line in self.data_file:
            match_equation = self._search_for_equation_with_given_variable_in_string(variable_name, line)
            if match_equation:
                return self._search_for_value_of_equation(match_equation.group(0))

    def create_data_dict(self):
        return {
                    'N' : self._get_variable_from_data_file('N'),
                    'K' : self._get_variable_from_data_file('K'),
                    'Q' : self._get_variable_from_data_file('Q'),
                    'ro' : self._get_variable_from_data_file('ro'),
                    'alfa' : self._get_variable_from_data_file('alfa'),
                    'u' : self._get_variable_from_data_file('u'),
                    'delta' : self._get_variable_from_data_file('delta')
               }
