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