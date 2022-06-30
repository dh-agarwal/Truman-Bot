import grades.Course as Course
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import grades.intendedwords as intendedwords
import re

courseList = Course.getCourseList()

def getCourse(searchCriteriaUnsplit):
    searchCriteria = []
    for criteria1 in searchCriteriaUnsplit:
        for criteria2 in (re.split('(\d+)', criteria1)):
            if criteria2 != '':
                searchCriteria.append(criteria2)
    currentMatches = 0
    maxMatches = 0
    for course in courseList:
        for criteria in range(len(searchCriteria)):
            searchCriteria[criteria] = intendedwords.getIntendedWord(searchCriteria[criteria])
            if searchCriteria[criteria] in str(course.department).lower():
                currentMatches += (10-(criteria))
            if len(searchCriteria[criteria]) > 2 and searchCriteria[criteria] in str(course.title).lower():
                currentMatches += (10-(criteria))
            if searchCriteria[criteria] == str(course.number).lower():
                currentMatches += (10-(criteria))
            if searchCriteria[criteria] == str(course.section).lower():
                currentMatches += (10-(criteria))
            if searchCriteria[criteria] == str(course.term[:2]).lower():
                currentMatches += ((10-(criteria))/2)
            if searchCriteria[criteria] == str(course.term[-4:]).lower():
                currentMatches += (10-(criteria))
            if len(searchCriteria[criteria]) > 2 and searchCriteria[criteria] in str(course.instructor).lower():
                currentMatches += (10-(criteria))
        if (currentMatches > maxMatches):
            maxMatches = currentMatches
            maxMatchedCourse = course
        currentMatches = 0
    if (maxMatches == 0):
        return Course.Course("", "Not Found", "", "", "", "", "", 0, 0, 0, 0, 0, 0.0)
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
    font = {'family' : 'Tahoma',
        'size'   : 24}
    plt.rc('font', **font)

    fig, ax = plt.subplots()
    fig.set_size_inches(20, 9)
    at = AnchoredText("Avg GPA: " + str(course.avggrade), prop=dict(size=28), frameon=True, loc='upper right')
    ax.add_artist(at)
    ax1 = plt.subplot()
    ax1.tick_params('y', length=20)

    plt.bar(gradesXAxis, gradesYAxis, color=['forestgreen', 'yellowgreen', 'gold', 'salmon', 'orangered'], zorder = 3)
    if (max(gradesYAxis) < 8):
       plt.yticks(range(1,max(gradesYAxis) + 2))
    elif (max(gradesYAxis) < 24):
       plt.yticks(range(0,max(gradesYAxis) + 6, 5))
    plt.title('{} - {}'.format((course.title).title(), Course.getTerm(course)),fontweight = 'bold', fontsize = 32, pad=30.0)
    plt.grid(zorder = 0)
    plt.subplots_adjust( bottom=.1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.savefig("graph.png", bbox_inches='tight',pad_inches = .5)
    plt.close()