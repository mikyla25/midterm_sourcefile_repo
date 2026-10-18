# Part A: Student Parent Class
class Student:
    def __init__(self, name, course, year_level):
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):
        return (
            f"<h2>{self.name}</h2>\n"
            f"<p>Course: {self.course}</p>\n"
            f"<p>Year Level: {self.year_level}</p>"
        )


# Part B: ITStudent Child Class
class ITStudent(Student):
    skill = "Python"

    def get_skill(self):
        return f"<p>Programming Skill: {self.skill}</p>"


# Part C: StudentApp Class
class StudentApp:
    def __init__(self, title, student):
        self.title = title
        self.student = student

    def route(self, path):
        if path == "/":
            return f"<h1>{self.title}</h1>"

        elif path == "/profile":
            return (
                f"{self.student.get_profile()}\n"
                f"{self.student.get_skill()}"
            )

        else:
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        print(f"Running: {self.title}")

        print("\nGET /")
        print(self.route("/"))

        print("\nGET /profile")
        print(self.route("/profile"))

        print("\nGET /unknown")
        print(self.route("/unknown"))


# Part D: Object Creation and Execution
student = ITStudent("Mikyla A. Lanorio", "BS Information Technology", 4)
app = StudentApp("PSU Student Profile App", student)

app.run()


# Part E: Code Quality and Output