import csv
from matplotlib import font_manager
import matplotlib.pyplot as plt
import math
from matplotlib.offsetbox import AnchoredText
from PIL import Image

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

with open('D:\PythonProjects\TrumanBot\grades\grades.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        courseList.append(Course(row[0],row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]),int(row[10]),int(row[11]),float(row[12])))

def getTotalStudents(course):
    return course.arange + course.brange + course.crange + course.drange + course.frange

def getCourse(searchCriteria):
    currentMatches = 0
    maxMatches = 0
    for course in courseList:
        for criteria in searchCriteria:
            criteria = criteria.lower()
            criteriayear = criteria
            if criteria.lower() == "cs":
                criteria = "cmp_sc"
            if criteria == str(course.department).lower():
                currentMatches += 1
            if criteria == str(course.title).lower():
                currentMatches += 1
            if criteria == str(course.number).lower():
                currentMatches += 1
            if criteria == str(course.section).lower():
                currentMatches += 1
            if (len(criteria) == 2 and criteria == str(course.term)[:2].lower()):
                currentMatches += 1
            if ((len(criteria) == 4) and (criteria == str(course.term)[2:6])):
                currentMatches += 1
            if criteriayear.lower() == str(course.term).lower():
                currentMatches += 1
            if criteria == str(course.instructor).lower():
                currentMatches += 1
        if (currentMatches > maxMatches):
            maxMatches = currentMatches
            maxMatchedCourse = course
        currentMatches = 0
    if (maxMatches == 0):
        return Course("", "Not Found", "", "", "", "", "", 0, 0, 0, 0, 0, 0.0)
    return maxMatchedCourse

def getCourseString(course):
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

def generateCourseImage(course):
    gradesXAxis = ("A", "B", "C", "D", "F")
    gradesYAxis = [course.arange, course.brange, course.crange, course.drange, course.frange]
    fig, ax = plt.subplots()
    at = AnchoredText("Avg GPA: " + str(course.avggrade), prop=dict(size=12), frameon=True, loc='upper right')
    ax.add_artist(at)
    plt.bar(gradesXAxis, gradesYAxis, color=['forestgreen', 'yellowgreen', 'gold', 'salmon', 'orangered'], zorder = 3)
    if (max(gradesYAxis) < 8):
       plt.yticks(range(1,max(gradesYAxis) + 2))
    elif (max(gradesYAxis) < 24):
       plt.yticks(range(0,max(gradesYAxis) + 6, 5))
    plt.title('{} - {}'.format((course.title).title(), course.term), fontweight = 'bold')
    plt.grid(zorder = 0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.savefig("graph.png")
    plt.close()
    image = Image.open('graph.png')
    new_image = image.resize((1280, 960))
    new_image.save('graph.png')