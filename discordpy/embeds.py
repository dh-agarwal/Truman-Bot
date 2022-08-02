from dotenv import load_dotenv, find_dotenv
import sys
import os
load_dotenv(find_dotenv())
sys.path.insert(1, os.getenv('FILE'))
import discord
from dotenv import load_dotenv, find_dotenv
import src.directory.directorysearch as directorysearch
import datetime
from dotenv import load_dotenv, find_dotenv
import src.rec.rec as rec
from src.dining.alldininghalls import getAllDiningHallTimes as getAllDiningHallTimes
from src.dining.alldininghalls import getAllDiningHallTimesDay as getAllDiningHallTimesDay
from src.dining.menus import DiningHall as DiningHall
import src.grades.Course as Course
import src.grades.gradecalculations as gradecalculations
import re
import math


def renderCourse(interaction, coursenum, aclient):
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][coursenum])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][coursenum].dept, aclient.similarcourses[interaction.guild.id][coursenum].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][coursenum].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][coursenum].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][coursenum]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][coursenum].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][coursenum].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][coursenum].number))

    return {"embed": newResult, "file": file}


def minimizeCourse(interaction, aclient):
    gradecalculations.generateCourseImage(aclient.courses[interaction.guild.id][0])
    newResult = discord.Embed(
      color=0xF59F16,
      title = f"**{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({len(aclient.similarcrsstrings[interaction.guild.id])}):\t\t\t\t\t*Data last updated on 7/10/2022"

    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in aclient.similarcrsstrings[interaction.guild.id][:2]:
      i += 1
      txt += f"\n{emojidict[i]} {similarcourse}"

    if len(aclient.similarcrsstrings[interaction.guild.id]) > 2:
      txt += "\n~~more below~~"

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value=f"{aclient.courses[interaction.guild.id][0].instructor.title()}", inline=True)
    newResult.add_field(name="**Section**", value=f"{aclient.courses[interaction.guild.id][0].section}", inline=True)
    newResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    newResult.set_image(url=f"attachment://{coursename}_{aclient.courses[interaction.guild.id][0].number}.png")

    return newResult


def movePage(interaction, aclient):
    newResult = discord.Embed(
      color=0xF59F16,
      title = f"**{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({(len(aclient.similarcrsstrings[interaction.guild.id]))}):\t\t\t\t\t\t\t\t\t\t    Page {aclient.page[interaction.guild.id]+1}/{str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10))}"
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    if aclient.page[interaction.guild.id] == 0:
      i = 0
      for similarcourse in aclient.similarcrsstrings[interaction.guild.id][:2]:
        i += 1
        txt += "\n{} {}".format(emojidict[i],similarcourse)
      for similarcourse in aclient.similarcrsstrings[interaction.guild.id][2:10]:
        i += 1
        txt += "\n {}) {}".format(i,similarcourse)
    else:
      i = aclient.page[interaction.guild.id]*10
      for similarcourse in aclient.similarcrsstrings[interaction.guild.id][aclient.page[interaction.guild.id]*10:aclient.page[interaction.guild.id]*10+10]:
        i += 1
        txt += "\n {}) {}".format(i,similarcourse)

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value="{}".format(aclient.courses[interaction.guild.id][0].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.courses[interaction.guild.id][0].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.courses[interaction.guild.id][0].number))

    return newResult


def expandCourse(interaction, aclient):
    newResult = discord.Embed(
    color=0xF59F16,
    title = f"**{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({(len(aclient.similarcrsstrings[interaction.guild.id]))}):\t\t\t\t\t\t\t\t\t\t    Page 1/{str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10))}"
    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in aclient.similarcrsstrings[interaction.guild.id][:2]:
      i += 1
      txt += f"\n{emojidict[i]} {similarcourse}"
    for similarcourse in aclient.similarcrsstrings[interaction.guild.id][2:10]:
      i += 1
      txt += f"\n {i}) {similarcourse}"

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value=f"{aclient.courses[interaction.guild.id][0].instructor.title()}", inline=True)
    newResult.add_field(name="**Section**", value=f"{aclient.courses[interaction.guild.id][0].section}", inline=True)
    newResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    newResult.set_image(url=f"attachment://{coursename}_{aclient.courses[interaction.guild.id][0].number}.png")

    return newResult


def goToFirstPage(interaction, aclient):
    oldResult = discord.Embed(
      color=0xF59F16,
      title = f"**{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number}**"
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({(len(aclient.similarcrsstrings[interaction.guild.id]))}):\t\t\t\t\t\t\t\t\t\t    Page 1/{str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10))}"
    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in aclient.similarcrsstrings[interaction.guild.id][:2]:
      i += 1
      txt += "\n{} {}".format(emojidict[i],similarcourse)
    for similarcourse in aclient.similarcrsstrings[interaction.guild.id][2:10]:
      i += 1
      txt += "\n {}) {}".format(i,similarcourse)

    oldResult.set_footer(text=txt)
    oldResult.add_field(name="**Instructor**", value=f"{aclient.courses[interaction.guild.id][0].instructor.title()}", inline=True)
    oldResult.add_field(name="**Section**", value=f"{aclient.courses[interaction.guild.id][0].section}", inline=True)
    oldResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    oldResult.set_image(url=f"attachment://{coursename}_{aclient.courses[interaction.guild.id][0].number}.png")

    return oldResult


def getGifEmbed(dance, interaction):
    actions = {
        "dance": ["danced!", "https://c.tenor.com/BDxIoo-dxPgAAAAC/missouri-tigers-truman-the-tiger.gif"],
        "thumbsup": ["sent a thumbs up!", "https://media3.giphy.com/media/S6foDbT2nnSoAZlPNS/giphy.gif?cid=790b761118c586046ec8a0611a72b517fe865bf489ed48dc&rid=giphy.gif&ct=g"],
        "surprised": ["was surprised!", "https://d98lmo17970r8.cloudfront.net/images/2017/12/4/Reax_truman_oh_no.gif"],
        "clap": ["clapped!", "https://c.tenor.com/g12vGZQ5nPUAAAAC/missouri-mizzoufootball.gif"]
    }
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} {actions[dance][0]}"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url=f"{actions[dance][1]}")

    return embed


def getCovidEmbed(interaction):
    embed=discord.Embed(
    title="Mizzou Covid-19 Information",
    url="https://missouri.edu/covid",
    description="""
**Updates**
    • As the spring 2022 semester comes to a close, we have reached a new stage as vaccination and testing availability, treatments, and changes in guidance from the Centers from Disease Control have all evolved. In recognition of this changed reality, President Mun Choi has suspended UM System policy [HR-702](https://www.umsystem.edu/ums/rules/hrm/hr700/hr702), which set requirements and expectations of staff and faculty regarding COVID-19 safety practices.
    • Additionally, students are no longer required to submit reports of positive COVID tests to the university.
    • The university’s data-tracking dashboard was suspended at the conclusion of the spring semester on May 13, 2022. Archived data can be found on the [case data](https://missouri.edu/covid/cases) page.
    • Faculty and staff members are expected to manage their own personal health regarding COVID as they do for other contagious illnesses. We encourage everyone to follow the latest guidance on the [CDC website](https://www.cdc.gov/coronavirus/2019-ncov/your-health/about-covid-19.html).

**Vaccinations**
    • Students can call the [Student Health Center](https://studenthealth.missouri.edu/) to schedule an appointment for a vaccine or a booster shot (573-882-7481).

**Testing**
    • MU students should contact the [Student Health Center](https://studenthealth.missouri.edu/) at 573-882-7481 for testing.
    • Hours: Mon./Tues./Thurs./Fri. 8 a.m.– 5 p.m, Wed. 9 a.m. – 5 p.m.
    • **Please note:** The Student Health Center is closed on Saturday and Sunday.

**Masking**
    • People may choose to mask at any time. People who have been exposed to someone with COVID-19 should wear a mask. If you have symptoms, you should stay home.
    • If you are [at high risk for severe illness](https://www.cdc.gov/coronavirus/2019-ncov/science/community-levels.html#anchor_47145), talk to your health care provider about whether you need to wear a mask and take other precautions.
""",
    color=0xF59F16,
    timestamp=interaction.created_at
    )

    embed.set_author(
      name = "MU COVID INFO",
      url="https://missouri.edu/covid",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    embed.set_footer(
      text="*Information last updated as of 07/13/2022"
    )

    return embed


def getRecHoursEmbed(interaction):
    rechours = rec.getDaysDictionary(rec.getWeekDictionary())
    dayofweek = datetime.datetime.today().weekday()
    embed=discord.Embed(
        title="Rec Center Facility Hours",
        url="https://mizzourec.com/facilities/information/hours/",
        description=f"""
{"__" if dayofweek == 0 else ""}**Monday:** {rechours["MONDAY"]}{"__" if dayofweek == 0 else ""}

{"__" if dayofweek == 1 else ""}**Tuesday:** {rechours["TUESDAY"]}{"__" if dayofweek == 1 else ""}

{"__" if dayofweek == 2 else ""}**Wednesday:** {rechours["WEDNESDAY"]}{"__" if dayofweek == 2 else ""}

{"__" if dayofweek == 3 else ""}**Thursday:** {rechours["THURSDAY"]}{"__" if dayofweek == 3 else ""}

{"__" if dayofweek == 4 else ""}**Friday:** {rechours["FRIDAY"]}{"__" if dayofweek == 4 else ""}

{"__" if dayofweek == 5 else ""}**Saturday:** {rechours["SATURDAY"]}{"__" if dayofweek == 5 else ""}

{"__" if dayofweek == 6 else ""}**Sunday:** {rechours["SUNDAY"]}{"__" if dayofweek == 6 else ""}""",
        color=0xF59F16,
        timestamp=interaction.created_at
    )

    embed.set_author(
      name = "Mizzou Rec",
      url="https://mizzourec.com/",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    embed.set_footer(
      text=f"Schedule for {rec.getWeek()}"
    )

    embed.set_footer(
      text=f"Schedule for {rec.getWeek()}"
    )

    embed.set_thumbnail(
      url="https://mizzourec.com/wp-content/themes/mizzourec/images/default-mizzourec-smrectcrop.png"
    )

    return embed


def directorySearchEmbed(firstname, lastname):
    if not firstname and not lastname:
        embed=discord.Embed(
        description = 'Please specificy a first or last name!',
        color=0xF59F16,
        )

        embed.set_author(
        url="https://missouri.edu/directory",
        name = 'MU Directory',
        icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
        )

        return embed

    else:
        p1 = directorysearch.getPerson(firstname, lastname)

        if(p1.name == "No results"):
            embed=discord.Embed(
            description = "Student was not found! Please try again.",
            color=0xF59F16,
            )

            embed.set_author(
            url="https://missouri.edu/directory",
            name = 'MU Directory',
            icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
            )
        elif(p1.name == "Too many results"):
            embed=discord.Embed(
            description = "Too many results were returned! Please be more specific.",
            color=0xF59F16,
            )

            embed.set_author(
            url="https://missouri.edu/directory",
            name = 'MU Directory',
            icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
            )
        else:
            embed=discord.Embed(
            title=f"{p1.name}",
            color=0xF59F16,
            )

            embed.set_author(
            url="https://missouri.edu/directory",
            name = 'MU Directory',
            icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
            )

            embed.set_thumbnail(url="https://www.bangory.org/wp-content/uploads/2016/05/person-icon-233x300.png")
            if p1.title != "":
                embed.add_field(name="Title", value=f"{p1.title}", inline=True)
            if p1.dept != "":
                embed.add_field(name="Department", value=f"{p1.dept}", inline=True)
            if p1.email != "":
                embed.add_field(name="Email", value=f"{p1.email}", inline=True)
            if p1.phone != "":
                embed.add_field(name="Phone", value=f"{p1.phone}", inline=True)
            if p1.address != "":
                embed.add_field(name="Address", value=f"{p1.address}", inline=True)
            if p1.city != "" and p1.state == "":
                embed.add_field(name="City", value=f"{p1.city}", inline=True)
            if p1.city == "" and p1.state != "":
                embed.add_field(name="State", value=f"{p1.state}", inline=True)
            if p1.city != "" and p1.state != "":
                embed.add_field(name="City/State", value=f"{p1.city}, {p1.state}", inline=True)
        return embed


def getMenuEmbed(hall, interaction, expanded):
    hallobj = DiningHall(hall)
    embed=discord.Embed(
    title=hall,
    url=hallobj.url,
    color=0xF59F16,
    timestamp=interaction.created_at
    )
    embed.set_author(
      name = "MU Dining",
      url="https://dining.missouri.edu/locations/",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )
    embed.set_thumbnail(
      url=hallobj.logo
    )
    times = hallobj.times
    menu = hallobj.menu
    embed.add_field(name=list(times.keys())[0][:list(times.keys())[0].find(" ")], value=list(times.values())[0], inline = True)
    embed.add_field(name=list(times.keys())[1][:list(times.keys())[1].find(" ")], value=list(times.values())[1], inline = True)
    embed.add_field(name=list(times.keys())[2][:list(times.keys())[2].find(" ")], value=list(times.values())[2], inline = True)
    if expanded:
      embed.set_footer(
      text = "Menu subject to change"
      )
      embed.add_field(name="\u200b", value="**🍽️\tTODAY'S MENU\t🍽️**", inline = False)
      for category in menu:
        itemstxt = ""
        for item in menu[category]:
          itemstxt += f"• {item}\n"
        embed.add_field(name=f"{category}", value=itemstxt, inline = False)
    return embed  


def getDiningEmbed(choice, interaction):

    if (choice == "All"):
      halls = getAllDiningHallTimes()
      txt = ""
      for dininghall in halls:
        txt += f"""{"__**" if halls[dininghall] != "CLOSED" else ""}{dininghall}{"**" if halls[dininghall] != "CLOSED" else ""}: {halls[dininghall]}{"__" if halls[dininghall] != "CLOSED" else ""}\n\n"""
      embed=discord.Embed(
        title="All MU Dining Hall Hours Today",
        url="https://dining.missouri.edu/locations/",
        color=0xF59F16,
        description=txt,
        timestamp=interaction.created_at
      )
      embed.set_author(
      name = "MU Dining",
      url="https://dining.missouri.edu/locations/",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )
      
    elif (choice == "Open"):
      halls = getAllDiningHallTimes()
      txt = ""
      open = 0
      for dininghall in halls:
        if halls[dininghall] != "CLOSED":
          open += 1
          txt += f"**{dininghall}**: {halls[dininghall]}\n\n"
      embed=discord.Embed(
        title=f"MU Dining Halls Open Today ({open})",
        url="https://dining.missouri.edu/locations/",
        color=0xF59F16,
        description=txt,
        timestamp=interaction.created_at
      )
      embed.set_author(
        name = "MU Dining",
        url="https://dining.missouri.edu/locations/",
        icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

    return embed