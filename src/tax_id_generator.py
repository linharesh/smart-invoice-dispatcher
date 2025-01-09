import random

class TaxIdGenerator:
    @staticmethod
    def generate_random_tax_id():
        return "{0:03d}.{1:03d}.{2:03d}-{3:02d}".format(
            random.randint(0, 999),
            random.randint(0, 999),
            random.randint(0, 999),
            random.randint(0, 99)
        )