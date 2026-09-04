class Faculty:
    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department

    def display(self):
        print("Faculty ID:", self.faculty_id)
        print("Name:", self.name)
        print("Department:", self.department)
