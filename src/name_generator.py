import random

class NameGenerator:
    @staticmethod
    def generate_random_name():
        first_names = [
            "Miguel", "Sophia", "Arthur", "Alice", "Bernardo", "Julia", "Heitor", "Isabella",
            "Davi", "Manuela", "Lorenzo", "Laura", "Théo", "Luiza", "Pedro", "Valentina",
            "Gabriel", "Giovanna", "Enzo", "Maria", "Matheus", "Helena", "Lucas", "Beatriz",
            "Nicolas", "Mariana", "Guilherme", "Lara", "Rafael", "Eloá", "Joaquim", "Livia", "Samuel", "Lorena"
        ]

        middle_initials = [
            "A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J.", "K.", "L.", "M.", "N.", "O.", "P.", "Q.", "R.", "S.", "T.", "U.", "V.", "W.", "X.", "Y.", "Z."
        ]

        last_names = [
            "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Costa",
            "Gomes", "Martins", "Araújo", "Melo", "Barbosa", "Ribeiro", "Alves", "Cardoso",
            "Pereira", "Lima", "Carvalho", "Teixeira", "Rocha", "Dias", "Moreira", "Nunes",
            "Soares", "Vieira", "Cavalcanti", "Monteiro", "Moura", "Campos", "Freitas", "Barros"
        ]

        first_name = random.choice(first_names)
        middle_initial = random.choice(middle_initials)
        last_name = random.choice(last_names)

        return f"{first_name} {middle_initial} {last_name}"