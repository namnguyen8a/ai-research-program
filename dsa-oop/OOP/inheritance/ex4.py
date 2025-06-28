class Staff:
    def __init__(self, staff_id):
        self.staff_id = staff_id
    
    def work(self):
        return "Work"

class Teacher(Staff):
    def __init__(self, staff_id, subject):
        super().__init__(staff_id)
        self.subject = subject
    
    def teach(self):
        return f"Teach {self.subject}"

class Principal(Teacher):
    def manage_school(self):
        return "Manage School"

p = Principal("P001", "Math")
print(p.work())
print(p.teach())
print(p.manage_school())