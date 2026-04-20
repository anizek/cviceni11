from sorting import bubble_sort

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
        for a in range(len(self.scores)):
            if self.scores[a] == hledana_hodnota:
                vysledek.append(a)
        return vysledek

    def get_sorted(self):
        scores = self.scores[:]
        score = bubble_sort(scores)
        return score

    def average(self):
        return sum(self.scores) / len(self.scores)

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def pass_rate(self):
        passd = 0
        for a in self.scores:
            if a >= 50:
                passd += 1
        return passd / len(self.score)

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentu, prumer {self.average():.1f}"


