class Student:

    def __init__(self,
                 student_id: int = 0,
                 first_name: str = "",
                 last_name: str = "",
                 grades: list = None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
        for grade in grades or []:
            self.add_grade(grade)

    def add_grade(self, grade: int):
        if not 1 <= grade <= 5:
            raise ValueError("Grade must be between 1 and 5")
        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return (f"[{self.student_id}] {self.last_name} {self.first_name} "
                f"- середній бал: {self.get_average():.2f}")


class Group:

    def __init__(self,
                 name: str = "Unnamed group"):
        self.name = name
        self.students = []

    def add_student(self, student: Student) -> None:
        for item in self.students:
            if item.student_id == student.student_id:
                raise ValueError(
                    f"Student with ID {student.student_id} already exists"
                )
        self.students.append(student)

    def remove_student(self, student_id: int):
        for item in self.students:
            if item.student_id == student_id:
                self.students.remove(item)
                print(f"Студента {item.last_name} {item.first_name} видалено.")
                return
        raise ValueError(f"Student with ID {student_id} not found")

    def print_rating(self) -> None:
        print(f"\nРейтинг групи {self.name}:")
        if not self.students:
            print("\tГрупа порожня.")
            return

        sorted_students = sorted(self.students,
                                 key=lambda s: s.get_average(),
                                 reverse=True)

        for place, item in enumerate(sorted_students, start=1):
            print(f"\t{place}. {item}")


def main():
    group = Group("ІР-11")

    student1 = Student(1, "Іван", "Петренко", [5, 4, 5, 5])
    student2 = Student(2, "Олена", "Коваль", [4, 4, 3, 5])
    student3 = Student(3, "Андрій", "Шевченко", [5, 5, 5, 5])
    student4 = Student(4, "Марія", "Бондар", [3, 4, 3, 4])

    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)
    group.add_student(student4)

    student2.add_grade(5)

    group.print_rating()

    print("\nВидаляємо студента з id 4:")
    try:
        group.remove_student(4)
        group.remove_student(10)
    except ValueError as error:
        print(error)

    group.print_rating()


if __name__ == "__main__":
    main()
