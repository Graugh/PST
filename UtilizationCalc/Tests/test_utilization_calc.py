import pytest
from UtilizationCalc.utilization_calc import UtilizationCalc


@pytest.fixture
def utilization_calc():
    return UtilizationCalc()

@pytest.mark.parametrize('no_of_users, no_of_subbands, no_of_radiuses, expected_M', [[10, 14, 4, 4],
                                                                                     [3, 7, 13, 3],
                                                                                     [32, 12, 16, 12]])
def test_calculate_M(utilization_calc, no_of_users, no_of_subbands, no_of_radiuses, expected_M):
    assert expected_M == utilization_calc.calculate_M(no_of_users, no_of_subbands, no_of_radiuses)


@pytest.mark.parametrize('min_radius, no_of_multicasts, expected_radiuses', [[0.2, 3, [0.6, 0.82462, 1]],
                                                                             [0.5, 4, [0.66144, 0.79057, 0.90139, 1]]])
def test_calculate_vector_of_radiuses(utilization_calc, min_radius, no_of_multicasts, expected_radiuses):
    assert expected_radiuses == utilization_calc.calculate_vector_of_radiuses(min_radius, no_of_multicasts)

@pytest.mark.parametrize('radiuses, alpha, rho, expected_f_list', [[[0.6, 0.8, 1], 0.5, 0.2, [0.63145, 0.54109, 0.6]],
                                                                   [[0.7, 1], 3, 0.1, [0.10955, 0.13265]]])
def test_calculate_f_list(utilization_calc, radiuses, alpha, rho, expected_f_list):
    assert expected_f_list == utilization_calc.calculate_f_list(radiuses, alpha, rho)

@pytest.mark.parametrize('f_list, alpha, expected_omega_list', [[[0.25, 0.5], 0.5, [0.2, 0.8]],
                                                                [[0.7, 0.3, 0.5], 0.25, [0.77277, 0.02607, 0.20116]]])
def test_calculate_omega_list(utilization_calc, f_list, alpha, expected_omega_list):
    assert expected_omega_list == utilization_calc.calculate_omega_list(f_list, alpha)

@pytest.mark.parametrize('alpha, delta, u, expected_u1', [[0.5, 0.25, 0.1, 0.32660],
                                                          [0.25, 0.2, 0.15, 0.24350]])
def test_calculate_u1(utilization_calc, alpha, delta, u, expected_u1):
    assert expected_u1 == utilization_calc.calculate_u1(alpha, delta, u)