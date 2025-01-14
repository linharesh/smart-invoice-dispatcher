import random

class TaxIdGenerator:

    def generate_random_tax_id(self):
        cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        cpf += self.__calcular_digito(cpf)
        cpf += self.__calcular_digito(cpf)
        return cpf

    def __calcular_digito(self, cpf_parcial):
        soma = sum((len(cpf_parcial) + 1 - i) * int(v) for i, v in enumerate(cpf_parcial))
        digito = 11 - soma % 11
        return str(digito if digito < 10 else 0)