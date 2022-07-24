import discord
from discord.utils import get
import asyncio
#import dining.sabai as sabai
import grades.Course as Course
import grades.gradecalculations as gradecalculations
import datetime
import os
from dotenv import load_dotenv, find_dotenv
import directory.directorysearch as directorysearch
import directory.Person as Person
import rec.rec as rec
import math

load_dotenv(find_dotenv())

client = discord.Client()

@client.event
async def on_message(message):
  global chan
  chan = message.channel
  global msg
  msg = message.content
  auth = message.author.name

  if message.author == client.user:
    return

#DIRECTORY
  if msg.startswith('/directory'):
    info = msg.split()
    if (len(info) == 2):
      p1 = directorysearch.getPerson(info[1], "")
    elif (len(info) > 2):
      p1 = directorysearch.getPerson(info[1], info[2])
    else:
      p1 = (Person.Person("No results", "", "", "", "", "", "", ""))

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
      title="{}".format(p1.name),
      color=0xF59F16,
      )
      embed.set_author(
      url="https://missouri.edu/directory",
      name = 'MU Directory',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )
      embed.set_thumbnail(url="https://www.bangory.org/wp-content/uploads/2016/05/person-icon-233x300.png")
      if p1.title != "":
        embed.add_field(name="Title", value="{}".format(p1.title), inline=True)
      if p1.dept != "":
        embed.add_field(name="Department", value="{}".format(p1.dept), inline=True)
      if p1.email != "":
        embed.add_field(name="Email", value="{}".format(p1.email), inline=True)
      if p1.phone != "":
        embed.add_field(name="Phone", value="{}".format(p1.phone), inline=True)
      if p1.address != "":
        embed.add_field(name="Address", value="{}".format(p1.address), inline=True)
      if p1.city != "" and p1.state == "":
        embed.add_field(name="City", value="{}, {}".format(p1.city), inline=True)
      if p1.city == "" and p1.state != "":
        embed.add_field(name="State", value="{}, {}".format(p1.state), inline=True)
      if p1.city != "" and p1.state != "":
        embed.add_field(name="City/State", value="{}, {}".format(p1.city, p1.state), inline=True)

    await message.channel.send(embed=embed)

#GRADES
  if msg.startswith('/grades'):
    global i
    i = 0
    msg = msg.strip()
    info = msg.split()
    info.pop(0)
    global courses
    courses = gradecalculations.getCourse(info)
    if (courses != []):
      global maincourse
      maincourse = "{} {}".format(courses[0].dept, courses[0].number)
      gradecalculations.generateCourseImage(courses[0])
      embed = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(courses[0].dept, courses[0].number),
      )
      embed.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )
      global similarcourses
      global similarcoursesstrings
      similarcourses = []
      similarcoursesstrings = []
      for i in range(len(courses)):
        if ("{} {} ({})".format(courses[i].dept, courses[i].number, courses[i].title.title())) not in similarcoursesstrings:
          similarcoursesstrings.append("{} {} ({})".format(courses[i].dept, courses[i].number, courses[i].title.title()))
          similarcourses.append(courses[i])
      similarcoursesstrings.remove("{} {} ({})".format(courses[0].dept, courses[0].number, courses[0].title.title()))
      txt = "Similar search results ({}):\t\t\t\t\t*Data last updated on 7/10/2022".format((len(similarcoursesstrings)))
      i = 0
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣"
      }
      for similarcourse in similarcoursesstrings[:3]:
        i += 1
        txt += "\n{} {}".format(emojidict[i],similarcourse)
      embed.set_footer(
        text=txt
      )
      embed.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      embed.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      embed.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)
      file = discord.File("grades/graph.png", filename="{}_{}.png".format(courses[0].dept, courses[0].number))
      embed.set_image(url="attachment://{}_{}.png".format(courses[0].dept, courses[0].number))
      global coursemsg
      coursemsg = await message.channel.send(file=file, embed=embed)
      for x in range(len(similarcoursesstrings[:3])):
        await coursemsg.add_reaction(emojidict[x+1])
      if (len(similarcoursesstrings) > 3):
        await coursemsg.add_reaction("⏬")

    else:
      embed=discord.Embed(
        description = "No courses found! Please try again",
        color=0xF59F16,
      )
      embed.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      await message.channel.send(embed=embed)

#REC
  if (msg.startswith('/rec')):
    rechours = rec.getDaysDictionary(rec.getWeekDictionary())
    embed=discord.Embed(
        title="Rec Center Facility Hours",
        url="https://mizzourec.com/facilities/information/hours/",
        description="""
**Sunday:** {}

**Monday:** {}

**Tuesday:** {}

**Wednesday:** {}

**Thursday:** {}

**Friday:** {}

**Saturday:** {}
""".format(rechours["SUNDAY"], rechours["MONDAY"], rechours["TUESDAY"], rechours["WEDNESDAY"], rechours["THURSDAY"], rechours["FRIDAY"], rechours["SATURDAY"]),
        color=0xF59F16,
    )
    embed.set_author(
      name = "Mizzou Rec",
      url="https://mizzourec.com/",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )
    embed.set_footer(
      text="Showing schedule for {}".format(rec.getWeek())
    )
    await message.channel.send(embed=embed)

#COVID
  if (msg.startswith('/covid')):
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
    )
    embed.set_author(
      name = "MU COVID-19 INFORMATION",
      url="https://missouri.edu/covid",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )
    embed.set_footer(
      text="*Information last updated as of 07/13/2022"
    )
    await message.channel.send(embed=embed)

#GIFCOMMANDS
  if (msg == '/dance'):
    embed=discord.Embed(
    color=0xF59F16
    )
    embed.set_author(
    name=('{} danced!'.format(auth)), 
    icon_url=(message.author.avatar_url)
    )
    embed.set_image(
    url='https://c.tenor.com/BDxIoo-dxPgAAAAC/missouri-tigers-truman-the-tiger.gif'
    )
    await message.channel.send(embed=embed)

  if (msg == '/thumbsup'):
      embed=discord.Embed(
      color=0xF59F16
      )
      embed.set_author(
      name=('{} sent a thumbs up!'.format(auth)), 
      icon_url=(message.author.avatar_url)
      )
      embed.set_image(
      url='https://media3.giphy.com/media/S6foDbT2nnSoAZlPNS/giphy.gif?cid=790b761118c586046ec8a0611a72b517fe865bf489ed48dc&rid=giphy.gif&ct=g'
      )
      await message.channel.send(embed=embed)

  if (msg == '/surprised'):
      embed=discord.Embed(
      color=0xF59F16
      )
      embed.set_author(
      name=('{} was surprised!'.format(auth)), 
      icon_url=(message.author.avatar_url)
      )
      embed.set_image(
      url='https://d98lmo17970r8.cloudfront.net/images/2017/12/4/Reax_truman_oh_no.gif'
      )
      await message.channel.send(embed=embed)
 
  if (msg == '/clap'):
      embed=discord.Embed(
      color=0xF59F16
      )
      embed.set_author(
      name=('{} claps!'.format(auth)), 
      icon_url=(message.author.avatar_url)
      )
      embed.set_image(
      url='https://c.tenor.com/g12vGZQ5nPUAAAAC/missouri-mizzoufootball.gif'
      )
      await message.channel.send(embed=embed)

page = 0

@client.event
async def on_reaction_add(reaction, user):
  if user != client.user:
      global page
      global maincourse
      global similarcourses
      global similarcoursesstrings
      if str(reaction.emoji) == "⏬":
          newResult = discord.Embed(
            color=0xF59F16,
            title = "**{} {}**".format(courses[0].dept, courses[0].number),
          )
          newResult.set_author(
          name = 'MU Grades',
          icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
          )

          txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(similarcoursesstrings)), str(math.ceil(len(similarcoursesstrings)/10)))
          i = 0
          emojidict = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣"
          }
          for similarcourse in similarcoursesstrings[:3]:
            i += 1
            txt += "\n{} {}".format(emojidict[i],similarcourse)
          for similarcourse in similarcoursesstrings[3:10]:
            i += 1
            txt += "\n {}) {}".format(i,similarcourse)
          newResult.set_footer(
            text=txt
          )
          newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
          newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
          newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)
          newResult.set_image(url="attachment://{}_{}.png".format(courses[0].dept, courses[0].number))
          await reaction.message.edit(embed=newResult)
          if len(similarcoursesstrings) > 10:
            await coursemsg.add_reaction("⬅️")
            await coursemsg.add_reaction('➡️')
      if str(reaction.emoji) == "➡️":
        await reaction.remove(user)
        if page < len(similarcoursesstrings)/10 - 1:
          page += 1
          newResult = discord.Embed(
            color=0xF59F16,
            title = "**{} {}**".format(courses[0].dept, courses[0].number),
          )
          newResult.set_author(
          name = 'MU Grades',
          icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
          )
          txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(similarcoursesstrings)),page+1,str(math.ceil(len(similarcoursesstrings)/10)))
          emojidict = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣"
          }
          if page == 0:
            i = 0
            for similarcourse in similarcoursesstrings[:3]:
              i += 1
              txt += "\n{} {}".format(emojidict[i],similarcourse)
            for similarcourse in similarcoursesstrings[3:10]:
              i += 1
              txt += "\n {}) {}".format(i,similarcourse)
          else:
            i = page*10
            for similarcourse in similarcoursesstrings[page*10:page*10+10]:
              i += 1
              txt += "\n {}) {}".format(i,similarcourse)
          newResult.set_footer(
            text=txt
          )
          newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
          newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
          newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)
          newResult.set_image(url="attachment://{}_{}.png".format(courses[0].dept, courses[0].number))
          await reaction.message.edit(embed=newResult)
          if len(similarcoursesstrings) > 20:
            await coursemsg.add_reaction("⬅️")
            await coursemsg.add_reaction('➡️')
      if str(reaction.emoji) == "⬅️":
        await reaction.remove(user)
        if page > 0:
          page -= 1
          newResult = discord.Embed(
            color=0xF59F16,
            title = "**{} {}**".format(courses[0].dept, courses[0].number),
          )
          newResult.set_author(
          name = 'MU Grades',
          icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
          )
          txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(similarcoursesstrings)),page+1,str(math.ceil(len(similarcoursesstrings)/10)))
          emojidict = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣"
          }
          if page == 0:
            i = 0
            for similarcourse in similarcoursesstrings[:3]:
              i += 1
              txt += "\n{} {}".format(emojidict[i],similarcourse)
            for similarcourse in similarcoursesstrings[3:10]:
              i += 1
              txt += "\n {}) {}".format(i,similarcourse)
          else:
            i = page*10
            for similarcourse in similarcoursesstrings[page*10:page*10+10]:
              i += 1
              txt += "\n {}) {}".format(i,similarcourse)
          newResult.set_footer(
            text=txt
          )
          newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
          newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
          newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)
          newResult.set_image(url="attachment://{}_{}.png".format(courses[0].dept, courses[0].number))
          await reaction.message.edit(embed=newResult)
          if len(similarcoursesstrings) > 20:
            await coursemsg.add_reaction("⬅️")
            await coursemsg.add_reaction('➡️')
      if str(reaction.emoji) == "1️⃣":
          gradecalculations.generateCourseImage(similarcourses[1])
          newResult = discord.Embed(
            color=0xF59F16,
            title = "**{} {}**".format(similarcourses[1].dept, similarcourses[1].number),
          )
          newResult.set_author(
          name = 'MU Grades',
          icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
          )
          newResult.set_footer(
            text="Queried by: {}\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
          )
          newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
          newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
          newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)
          file = discord.File("grades/graph.png", filename="{}_{}.png".format(similarcourses[1].dept, similarcourses[1].number))
          newResult.set_image(url="attachment://{}_{}.png".format(similarcourses[1].dept, similarcourses[1].number))
          await chan.send(file=file, embed=newResult)
      if str(reaction.emoji) == "2️⃣":
          gradecalculations.generateCourseImage(similarcourses[2])
          newResult = discord.Embed(
            color=0xF59F16,
            title = "**{} {}**".format(similarcourses[2].dept, similarcourses[2].number),
          )
          newResult.set_author(
          name = 'MU Grades',
          icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
          )
          newResult.set_footer(
            text="Queried by: {}\t\t\t\t*Data last updated on 7/10/2022\n".format(maincourse)
          )
          newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
          newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
          newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)
          file = discord.File("grades/graph.png", filename="{}_{}.png".format(similarcourses[2].dept, similarcourses[2].number))
          newResult.set_image(url="attachment://{}_{}.png".format(similarcourses[2].dept, similarcourses[2].number))
          await chan.send(file=file, embed=newResult)
      if str(reaction.emoji) == "3️⃣":
          gradecalculations.generateCourseImage(similarcourses[3])
          newResult = discord.Embed(
            color=0xF59F16,
            title = "**{} {}**".format(similarcourses[3].dept, similarcourses[3].number),
          )
          newResult.set_author(
          name = 'MU Grades',
          icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
          )
          newResult.set_footer(
            text="Queried by: {}\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
          )
          newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[3].instructor.title()), inline=True)
          newResult.add_field(name="**Section**", value="{}".format(similarcourses[3].section), inline=True)
          newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[3]))), inline=True)
          file = discord.File("grades/graph.png", filename="{}_{}.png".format(similarcourses[3].dept, similarcourses[3].number))
          newResult.set_image(url="attachment://{}_{}.png".format(similarcourses[3].dept, similarcourses[3].number))
          await chan.send(file=file, embed=newResult)

#TOKEN
client.run(os.getenv('TOKEN'))  
