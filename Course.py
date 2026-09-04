class Course:
    def __init__(self, course_id, name, duration):
        self.course_id = course_id
        self.name = name
        self.duration = duration

    def display(self):
        print("Course ID:", self.course_id)
        print("Course Name:", self.name)
        print("Duration:", self.duration)
