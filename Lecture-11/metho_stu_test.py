class StudentTest:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def total_score(self):
        return self.score1 + self.score2 + self.score3
    
    def __str__(self):
        return f"Student Name: {self.name}, Total Score: {self.total_score()}"
    
student1 = StudentTest("Alice", 85, 90, 95)
print(student1.name, student1.total_score())
print(student1)