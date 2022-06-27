import csv

class Course:
    
    def __init__(self, department, title, number, section, term, au, instructor, arange, brange, crange, drange, frange, avggrade):
        self.department = department
        self.title = title
        self.number = number
        self.section = section
        self.term = term
        self.au = au
        self.instructor = instructor
        self.arange = arange
        self.brange = brange
        self.crange = crange
        self.drange = drange
        self.frange = frange
        self.avggrade = avggrade

courseList = []

with open('grades.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        courseList.append(Course(row[0],row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]),int(row[10]),int(row[11]),float(row[12])))

def getCourseList():
    return courseList

def getTerm(course):
    if ("SP" in course.term):
        return "Spring {}".format(course.term[-4:])
    if ("FS" in course.term):
        return "Fall {}".format(course.term[-4:])
    if ("WS" in course.term):
        return "Winter {}".format(course.term[-4:])
    if ("SS" in course.term):
        return "Summer {}".format(course.term[-4:])

def getTotalStudents(course):
    return course.arange + course.brange + course.crange + course.drange + course.frange