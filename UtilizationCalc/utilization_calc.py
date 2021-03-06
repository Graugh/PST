import math
import copy


class UtilizationCalc(object):
    def calculate_M(self, no_of_users, no_of_subbands, no_of_radiuses):
        return min(no_of_users, no_of_subbands, no_of_radiuses)

    def calculate_vector_of_radiuses(self, delta, no_of_multicasts):
        radiuses = []
        for m in range(1, int(no_of_multicasts)):
            radiuses.append(round(math.sqrt(delta * delta + m * ((1 - delta * delta)/no_of_multicasts)), 5))
        radiuses.append(1)
        return radiuses

    def calculate_f_list(self, radiuses_list, alpha, rho):
        f = []
        radiuses = copy.copy(radiuses_list)
        radiuses.insert(0, 0)
        for m in range(1, len(radiuses)):
            f.append(round(((radiuses[m] * radiuses[m] - radiuses[m - 1] * radiuses[m - 1])**alpha) * (radiuses[m]**((alpha - 1) * rho)), 5))
        return f

    def calculate_omega_list(self, f_list, alpha):
        omega_list = []
        sum_of_powered_f = 0
        for f in f_list:
            sum_of_powered_f += f**(1/alpha)
        for f in f_list:
            omega_list.append(round((f**(1/alpha))/sum_of_powered_f, 5))
        return omega_list

    def _calculate_u1(self, alpha, delta, u):
        return round(u**(1-alpha) * (1 - delta**2)**(-alpha), 5)

    def calculate_utilization(self, radiuses, omegas, alpha, delta, rho, u):
        sum_over_m = 0
        radiuses.insert(0, 0)
        for m in range(1, len(radiuses)):
            sum_over_m += (radiuses[m]**2 - radiuses[m - 1]**2)**alpha * radiuses[m]**(rho * (alpha - 1)) * omegas[m - 1]**(1 - alpha)
        u1 = self._calculate_u1(alpha, delta, u)
        return round(sum_over_m * (u1/(1 - alpha)), 5)


