import csv
from dataclasses import dataclass

@dataclass
class Course:
    dept: str
    title: str
    number: str
    section: str
    term: str
    au: str
    instructor: str
    arange: int
    brange: int
    crange: int
    drange: int
    frange: int
    average: float

    def __str__(self):
        res = ''
        res += ("Department: " + self.dept + "\n")
        res += ("Title: " + self.title + "\n")
        res += ("Number: " + self.number + "\n")
        res += ("Section: " + self.section + "\n")
        res += ("Term: " + self.term + "\n")
        res += ("AU: " + self.au + "\n")
        res += ("Instructor: " + self.instructor + "\n")
        res += ("A Range: " + str(self.arange) + "\n")
        res += ("B Range: " + str(self.brange) + "\n")
        res += ("C Range: " + str(self.crange) + "\n")
        res += ("D Range: " + str(self.drange) + "\n")
        res += ("F Range: " + str(self.frange) + "\n")
        res += ("Average: " + str(self.average) + "\n")
        return res

    def __hash__(self):
        return hash(str(self))
        
def getTerm(course):
    if ("SP" in course.term):
        return f"Spring {course.term[-4:]}"
    if ("FS" in course.term):
        return f"Fall {course.term[-4:]}"
    if ("WS" in course.term):
        return f"Winter {course.term[-4:]}"
    if ("SS" in course.term):
        return f"Summer {course.term[-4:]}"

def getTotalStudents(course):
    return course.arange + course.brange + course.crange + course.drange + course.frange

courseList = []

for year in range(2022,1997,-1):
    with open('src/grades/gradedata/grades{}.csv'.format(year)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            course1 = Course(row[0],row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]),int(row[10]),int(row[11]),float(row[12]))
            courseList.append(course1)

def getCourseList():
    return courseList