class Student:
    grade = 4

    def __init__(self, name, age):
     self.name = name
     self.age = age
    
    def get_Data(self):
     print({"name": self.name, "age": self.age, "grade": self.grade})

    @classmethod
    def update_grade(cls, grade):
      cls.grade = grade

    @staticmethod
    def check_age(age):
      if age>18:
        print("Above 18")
      else:
        print("Below 18")



s1 = Student('abc',45)
s2 = Student('xyz',32)

Student.update_grade(29)
Student.check_age(23)
Student.check_age(10)

s1.get_Data()
s2.get_Data()

