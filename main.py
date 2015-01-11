from DataReader.data_reader import DataReader
from UtilizationCalc.utilization_calc import UtilizationCalc
import sys

data_reader = DataReader()
data_reader.open_data_file_from_path(sys.argv[1])
data = data_reader.create_data_dict()
utilization_calc = UtilizationCalc()
M = utilization_calc.calculate_M(data['N'], data['K'], data['Q'])
R = utilization_calc.calculate_vector_of_radiuses(data['delta'], M)
f_list = utilization_calc.calculate_f_list(R, data['alfa'], data['ro'])
omegas = utilization_calc.calculate_omega_list(f_list, data['alfa'])
utilization = utilization_calc.calculate_utilization(R, omegas, data['alfa'], data['delta'], data['ro'], data['u'])
print "Omega = "
print omegas
print "Radiuses = "
print R
print "Utilization = "
print utilization