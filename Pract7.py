#Design and implement Python applications using classes, objects, constructors, methods,and encapsulation.
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.__marks = marks  # Encapsulated attribute

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.__marks)
        print("Grade:", self.calculate_grade())

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"

    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks. Enter a value from 0 to 100.")


# Create objects
student1 = Student("Aarav", 101, 85)
student2 = Student("Priya", 102, 92)

# Call methods
student1.display_details()
print()

student2.display_details()
print()

student1.update_marks(95)
student1.display_details()
