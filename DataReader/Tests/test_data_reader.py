import pytest
from DataReader.data_reader import DataReader

@pytest.fixture
def data_reader():
    return DataReader()

def test_open_data_file(data_reader):
    data_reader.open_data_file_from_path("/var/fpwork/PST/DataReader/Tests/test_example.dat")
    assert hasattr(data_reader.data_file, 'read')

@pytest.mark.parametrize('variable_name, variable_value', [['N', 3],
                                                           ['K', 12],
                                                           ['alfa', 1.4]])
def test_get_variable_from_data_file(data_reader, variable_name, variable_value):
    data_reader.open_data_file_from_path("/var/fpwork/PST/DataReader/Tests/test_example.dat")
    assert data_reader.get_variable_from_data_file(variable_name) == variable_value

def test_create_data_dict(data_reader):
    data_reader.open_data_file_from_path("/var/fpwork/PST/DataReader/Tests/test_example.dat")
    assert data_reader.create_data_dict() == {'N': 3, 'K': 12, 'Q': 10, 'ro': 0.1, 'alfa': 1.4, 'u': 0.6}