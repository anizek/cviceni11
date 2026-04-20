

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body > 89:
            return "A"
        elif body > 79:
            return "B"
        elif body > 69:
            return "C"
        elif body > 59:
            return "D"
        elif body > 49:
            return "E"
        else:
            return "F"

    def find(self, hledana_hodnota):
        vysledek = []
        for i in range(len(self.scores)):
            if self.scores[i] == hledana_hodnota:
                vysledek.append(i)
        return vysledek




