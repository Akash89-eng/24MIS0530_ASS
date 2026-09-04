from Student import Student
from Faculty import Faculty
from Course import Course
from Fees import Fees
from Alumni import Alumni


def main():
    print("================================")
    print("   COLLEGE MANAGEMENT SYSTEM")
    print("================================")

    student = Student(101, "Akash", "Software Engineering")
    faculty = Faculty(201, "Dr. Kumar", "Computer Science")
    course = Course(301, "Python Programming", "6 Months")
    fees = Fees(101, 50000, "Paid")
    alumni = Alumni(401, "Rahul", 2024)

    print("\n--- Student Details ---")
    student.display()

    print("\n--- Faculty Details ---")
    faculty.display()

    print("\n--- Course Details ---")
    course.display()

    print("\n--- Fees Details ---")
    fees.display()

    print("\n--- Alumni Details ---")
    alumni.display()

    print("\n================================")
    print("Application executed successfully!")
    print("================================")


if __name__ == "__main__":
    main()
