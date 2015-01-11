import math


class UtilizationCalc(object):
    def calculate_M(self, no_of_users, no_of_subbands, no_of_radiuses):
        return min(no_of_users, no_of_subbands, no_of_radiuses)

    def calculate_vector_of_radiuses(self, delta, no_of_multicasts):
        radiuses = []
        for m in range(1, no_of_multicasts):
            radiuses.append(round(math.sqrt(delta * delta + m * ((1 - delta * delta)/no_of_multicasts)), 5))
        radiuses.append(1)
        return radiuses

    def calculate_f_list(self, radiuses, alpha, rho):
        f = []
        radiuses.insert(0, 0)
        for m in range(1, len(radiuses)):
            f.append(round(((radiuses[m] * radiuses[m] - radiuses[m - 1] * radiuses[m - 1])**alpha) * (radiuses[m]**((alpha - 1) * rho)), 5))
        return f
