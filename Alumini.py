class Alumni:
    def __init__(self, alumni_id, name, graduation_year):
        self.alumni_id = alumni_id
        self.name = name
        self.graduation_year = graduation_year

    def display(self):
        print("Alumni ID:", self.alumni_id)
        print("Name:", self.name)
        print("Graduation Year:", self.graduation_year)
