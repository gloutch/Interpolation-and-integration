from airflow_test import *
from integration_test import *
from interpolation_test import *
from pressure_map_test import *


file1 = "model/boe103.txt"
file2 = "model/HOR20.txt"
file3 = "model/DU84132V.txt"

## integration_test
test_methode()
test_integrate()
test_derivative()
test_length_curves()
compare_integrate()


## interpolation_test
convergence_interpolation()
test_C2()
display_interpolation(file2)


## airflow_test
create_airflow_map(file3)


## pressure_map_test
create_pressure_map(file2)
