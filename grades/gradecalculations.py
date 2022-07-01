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
            if searchCriteria[criteria] in str(course.dept).lower():
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

def generateCourseImage(course):
    gradesXAxis = ("A", "B", "C", "D", "F")
    gradesYAxis = [course.arange, course.brange, course.crange, course.drange, course.frange]
    font = {'family' : 'Tahoma',
        'size'   : 26}
    plt.rc('font', **font)

    fig, ax = plt.subplots()
    fig.set_size_inches(20, 9)
    at = AnchoredText("Average: {:.2f}/4.00\nMedian:  {:.2f}/4.00".format(course.average, course.median), prop=dict(size=30), frameon=True, loc='upper right')
    ax.add_artist(at)

    ax1 = plt.subplot()
    ax1.tick_params('y', length=20, pad=10.0)
    ay1 = plt.subplot()
    ay1.tick_params('x', length=0, pad=20.0)

    plt.bar(gradesXAxis, gradesYAxis, color=['forestgreen', 'yellowgreen', 'gold', 'salmon', 'orangered'], zorder = 3)
    if (max(gradesYAxis) < 8):
       plt.yticks(range(1,max(gradesYAxis) + 2))
    elif (max(gradesYAxis) < 24):
       plt.yticks(range(0,max(gradesYAxis) + 6, 5))
    plt.title('{} - {}'.format((course.title).title(), Course.getTerm(course)),fontweight = 'bold', fontsize = 34, pad=30.0)
    plt.grid(zorder = 0)
    plt.subplots_adjust( bottom=.1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.savefig("graph.png", bbox_inches='tight',pad_inches = .5)
    plt.close()