#single inheritence - user, student
#multilevel - user, student, monitor

class User:
    def __init__(self, type):
        self.type = type
        
    def getUserType(self):
        return f"User is: {self.type}"
    
class Student(User):
    def __init__(self, id, name, type):
        super().__init__(type)
        self.id = id
        self.name = name
        
    def getStudentDetail(self):
        return f"Stude ID: {self.id} \nStudent Name: {self.name}"
    
class Monitor(Student):
    def __init__(self, id, name, type, isMonitor):
        super().__init__(id, name, type)
        self.isMonitor = True
    
    def takeAttendance(self):
        return f"Take attendance"
    
class Teacher(User):
    def __init__(self, type):
        super().__init__(type)
    
    def getType(self):
        return self.type
        
monitor = Monitor(1, "Prajwal", "student", True)
print(monitor.getUserType())
print(monitor.getStudentDetail())

teacher = Teacher("teacher")
print(teacher.getType())