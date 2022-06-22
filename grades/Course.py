import csv
import matplotlib.pyplot as plt
import math
from matplotlib.offsetbox import AnchoredText

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

with open('D:\PythonProjects\MizzouDiscordBot\grades\grades.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        courseList.append(Course(row[0],row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]),int(row[10]),int(row[11]),float(row[12])))

def getTotalStudents(course):
    return course.arange + course.brange + course.crange + course.drange + course.frange

def getCourse(department, number):
    res = 'Class not found! Please try again.'
    for course in courseList:
        if department == course.department and number == course.number:
            res = ''
            res += ("Department: " + course.department + "\n")
            res += ("Title: " + course.title + "\n")
            res += ("Number: " + course.number + "\n")
            res += ("Section: " + course.section + "\n")
            res += ("Term: " + course.term + "\n")
            res += ("AU: " + course.au + "\n")
            res += ("Instructor: " + course.instructor + "\n")
            res += ("A Range: " + str(course.arange) + "\n")
            res += ("B Range: " + str(course.brange) + "\n")
            res += ("C Range: " + str(course.crange) + "\n")
            res += ("D Range: " + str(course.drange) + "\n")
            res += ("F Range: " + str(course.frange) + "\n")
            res += ("Average Grade: " + str(course.avggrade) + "\n")
            return res
    return res

def getCourse(department, number):
    for course in courseList:
        if department == course.department and number == course.number:
            return course

def getCourseHeader(department, number):
    res = 'Class not found! Please try again.'
    for course in courseList:
        if department == course.department and number == course.number:
            res = ''
            res += '**Instructor          Section          Total Students**\n'
            res += (course.instructor.title() + "          " + course.section + "          " + str(getTotalStudents(course)))
            return res
    return res

def generateCourseImage(department, number):
    gradesXAxis = []
    gradesYAxis = []
    for course in courseList:
        if department == course.department and number == course.number:
            gradesXAxis = ("A", "B", "C", "D", "F")
            gradesYAxis = [course.arange, course.brange, course.crange, course.drange, course.frange]
            #plt.figure(figsize=(16,10))
            fig, ax = plt.subplots()
            at = AnchoredText(
               "Avg GPA:" + str(course.avggrade), prop=dict(size=15), frameon=True, loc='upper right')

            ax.add_artist(at)
            plt.bar(gradesXAxis, gradesYAxis, color=['forestgreen', 'yellowgreen', 'gold', 'salmon', 'orangered'], zorder = 3)
            parameter = {'axes.titlesize': 14}
            plt.rcParams.update(parameter)
            plt.title('{} - {}'.format((course.title).title(), course.term))
            plt.grid(zorder = 0)
            # plt.text(0.74, 0.55, "Section: {}".format(course.section), fontsize = 12,transform=plt.gcf().transFigure)
            # plt.text(0.74, 0.5, "Average GPA: {}".format(course.avggrade), fontsize = 12, transform=plt.gcf().transFigure)
            # plt.text(0.74, 0.45, "Total Students: {}".format(str(getTotalStudents(course))), fontsize = 12, transform=plt.gcf().transFigure)
            # plt.subplots_adjust(right=0.72)
            plt.savefig("graph.png")
            plt.close()
            return True
    return False