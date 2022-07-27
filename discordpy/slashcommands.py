from dotenv import load_dotenv, find_dotenv
import sys
import os
load_dotenv(find_dotenv())
sys.path.insert(1, os.getenv('FILE'))
from discord import app_commands
import discord
#import dining.sabai as sabai
import datetime
from dotenv import load_dotenv, find_dotenv
import math
import re
import rec.rec as rec
import directory.directorysearch as directorysearch
import grades.Course as Course
import grades.gradecalculations as gradecalculations
from discord.app_commands import Choice
from discord.ui import Button

global similarcourses
global similarcoursesstrings
global maincourse
global page
page = 0

class MenuOne(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))

    await interaction.followup.send(file=file, embed=newResult)

class MenuOneTwo(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[2].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[2].number))

    await interaction.followup.send(file=file, embed=newResult)

class MenuOneTwoDrop(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  async def multiplepages(self, interaction: discord.Interaction):
    self.clear_items()
    self.add_item(oneButton())
    self.add_item(twoButton())
    self.add_item(upButton())
    self.add_item(leftButton(disabled=True))
    self.add_item(rightButton())
    await interaction.response.edit_message(view = self)

  async def onepage(self, interaction: discord.Interaction):
    self.clear_items()
    self.add_item(oneButton())
    self.add_item(twoButton())
    self.add_item(upButton())
    await interaction.response.edit_message(view = self)

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))

    await interaction.followup.send(file=file, embed=newResult)


  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[2].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[2].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="<:dropdownarrow:1001307846169870427>", style=discord.ButtonStyle.blurple)
  async def dropdown(self,interaction:discord.Interaction, button:discord.ui.Button):
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
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += "\n{} {}".format(emojidict[i],similarcourse)
    for similarcourse in similarcoursesstrings[2:10]:
      i += 1
      txt += "\n {}) {}".format(i,similarcourse)

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))

    if len(similarcoursesstrings) > 10:
      await self.multiplepages(interaction)
    else:
      await self.onepage(interaction)
    await interaction.edit_original_message(embed=newResult)

class MenuOneTwoDropAllEnabled(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(courses[0].dept, courses[0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(similarcoursesstrings)), str(math.ceil(len(similarcoursesstrings)/10)))
    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += "\n{} {}".format(emojidict[i],similarcourse)
    for similarcourse in similarcoursesstrings[2:10]:
      i += 1
      txt += "\n {}) {}".format(i,similarcourse)

    oldResult.set_footer(text=txt)
    oldResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
    global page
    page = 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[2].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[2].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(courses[0].dept, courses[0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(similarcoursesstrings)), str(math.ceil(len(similarcoursesstrings)/10)))
    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += "\n{} {}".format(emojidict[i],similarcourse)
    for similarcourse in similarcoursesstrings[2:10]:
      i += 1
      txt += "\n {}) {}".format(i,similarcourse)

    oldResult.set_footer(text=txt)
    oldResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
    global page
    page = 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)


  @discord.ui.button(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)
  async def uparrow(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
    page = 0
    gradecalculations.generateCourseImage(courses[0])
    newResult = discord.Embed(
      color=0xF59F16,
      title = f"**{courses[0].dept} {courses[0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({len(similarcoursesstrings)}):\t\t\t\t\t*Data last updated on 7/10/2022"

    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += f"\n{emojidict[i]} {similarcourse}"

    if len(similarcoursesstrings) > 2:
      txt += "\n~~continued below~~"

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value=f"{courses[0].instructor.title()}", inline=True)
    newResult.add_field(name="**Section**", value=f"{courses[0].section}", inline=True)
    newResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(courses[0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    newResult.set_image(url=f"attachment://{coursename}_{courses[0].number}.png")
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

  @discord.ui.button(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green)
  async def leftbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
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
      }

      if page == 0:
        i = 0
        for similarcourse in similarcoursesstrings[:2]:
          i += 1
          txt += "\n{} {}".format(emojidict[i],similarcourse)
        for similarcourse in similarcoursesstrings[2:10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)
      else:
        i = page*10
        for similarcourse in similarcoursesstrings[page*10:page*10+10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)

      newResult.set_footer(text=txt)
      newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
      if page == 0:
        await interaction.edit_original_message(view = MenuOneTwoDropLeftDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(embed=newResult)

  @discord.ui.button(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)
  async def rightbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
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
      }

      if page == 0:
        i = 0
        for similarcourse in similarcoursesstrings[:2]:
          i += 1
          txt += "\n{} {}".format(emojidict[i],similarcourse)
        for similarcourse in similarcoursesstrings[2:10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)
      else:
        i = page*10
        for similarcourse in similarcoursesstrings[page*10:page*10+10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)

      newResult.set_footer(text=txt)
      newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
      if page == math.ceil(len(similarcoursesstrings)/10 - 1):
        await interaction.edit_original_message(view = MenuOneTwoDropRightDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(view = MenuOneTwoDropAllEnabled(), embed=newResult)

class MenuOneTwoDropRightDisabled(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  async def multiplepages(self, interaction: discord.Interaction):
    self.clear_items()
    self.add_item(oneButton())
    self.add_item(twoButton())
    self.add_item(upButton())
    self.add_item(leftButton(disabled = False))
    self.add_item(rightButton())
    await interaction.response.edit_message(view = self)

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
    color=0xF59F16,
    title = "**{} {}**".format(courses[0].dept, courses[0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(similarcoursesstrings)), str(math.ceil(len(similarcoursesstrings)/10)))
    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += "\n{} {}".format(emojidict[i],similarcourse)
    for similarcourse in similarcoursesstrings[2:10]:
      i += 1
      txt += "\n {}) {}".format(i,similarcourse)

    oldResult.set_footer(text=txt)
    oldResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
    global page
    page = 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[2].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[2].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(courses[0].dept, courses[0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(similarcoursesstrings)), str(math.ceil(len(similarcoursesstrings)/10)))
    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += "\n{} {}".format(emojidict[i],similarcourse)
    for similarcourse in similarcoursesstrings[2:10]:
      i += 1
      txt += "\n {}) {}".format(i,similarcourse)

    oldResult.set_footer(text=txt)
    oldResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
    global page
    page = 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)

  @discord.ui.button(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)
  async def uparrow(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
    page = 0
    gradecalculations.generateCourseImage(courses[0])
    newResult = discord.Embed(
      color=0xF59F16,
      title = f"**{courses[0].dept} {courses[0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({len(similarcoursesstrings)}):\t\t\t\t\t*Data last updated on 7/10/2022"

    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += f"\n{emojidict[i]} {similarcourse}"

    if len(similarcoursesstrings) > 2:
      txt += "\n~~continued below~~"

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value=f"{courses[0].instructor.title()}", inline=True)
    newResult.add_field(name="**Section**", value=f"{courses[0].section}", inline=True)
    newResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(courses[0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    newResult.set_image(url=f"attachment://{coursename}_{courses[0].number}.png")
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

  @discord.ui.button(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green)
  async def leftbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
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
      }

      if page == 0:
        i = 0
        for similarcourse in similarcoursesstrings[:2]:
          i += 1
          txt += "\n{} {}".format(emojidict[i],similarcourse)
        for similarcourse in similarcoursesstrings[2:10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)
      else:
        i = page*10
        for similarcourse in similarcoursesstrings[page*10:page*10+10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)

      newResult.set_footer(text=txt)
      newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
      if page == 0:
        await interaction.edit_original_message(view = MenuOneTwoDropLeftDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(view = MenuOneTwoDropAllEnabled(), embed=newResult)

  @discord.ui.button(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green, disabled = True)
  async def rightbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()

class MenuOneTwoDropLeftDisabled(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[2].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[2].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)
  async def uparrow(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
    page = 0
    gradecalculations.generateCourseImage(courses[0])
    newResult = discord.Embed(
      color=0xF59F16,
      title = f"**{courses[0].dept} {courses[0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({len(similarcoursesstrings)}):\t\t\t\t\t*Data last updated on 7/10/2022"

    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += f"\n{emojidict[i]} {similarcourse}"

    if len(similarcoursesstrings) > 2:
      txt += "\n~~continued below~~"

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value=f"{courses[0].instructor.title()}", inline=True)
    newResult.add_field(name="**Section**", value=f"{courses[0].section}", inline=True)
    newResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(courses[0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    newResult.set_image(url=f"attachment://{coursename}_{courses[0].number}.png")
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

  @discord.ui.button(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green, disabled = True)
  async def leftbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()

  @discord.ui.button(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)
  async def rightbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    global page
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
      }

      if page == 0:
        i = 0
        for similarcourse in similarcoursesstrings[:2]:
          i += 1
          txt += "\n{} {}".format(emojidict[i],similarcourse)
        for similarcourse in similarcoursesstrings[2:10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)
      else:
        i = page*10
        for similarcourse in similarcoursesstrings[page*10:page*10+10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)

      newResult.set_footer(text=txt)
      newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
      if page == math.ceil(len(similarcoursesstrings)/10 - 1):
        await interaction.edit_original_message(view = MenuOneTwoDropRightDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(view = MenuOneTwoDropAllEnabled(), embed=newResult)


class rightButton(Button):
  def __init__(self):
    super().__init__(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)

  async def callback(self, interaction):
    await interaction.response.defer()
    global page
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
      }

      if page == 0:
        i = 0
        for similarcourse in similarcoursesstrings[:2]:
          i += 1
          txt += "\n{} {}".format(emojidict[i],similarcourse)
        for similarcourse in similarcoursesstrings[2:10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)
      else:
        i = page*10
        for similarcourse in similarcoursesstrings[page*10:page*10+10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)

      newResult.set_footer(text=txt)
      newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
      if page == math.ceil(len(similarcoursesstrings)/10 - 1):
        await interaction.edit_original_message(view = MenuOneTwoDropRightDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(view = MenuOneTwoDropAllEnabled(), embed=newResult)

class leftButton(Button):
  def __init__(self, disabled):
    super().__init__(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green, disabled = disabled)

  async def callback(self, interaction):
    await interaction.response.defer()
    global page
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
      }

      if page == 0:
        i = 0
        for similarcourse in similarcoursesstrings[:2]:
          i += 1
          txt += "\n{} {}".format(emojidict[i],similarcourse)
        for similarcourse in similarcoursesstrings[2:10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)
      else:
        i = page*10
        for similarcourse in similarcoursesstrings[page*10:page*10+10]:
          i += 1
          txt += "\n {}) {}".format(i,similarcourse)

      newResult.set_footer(text=txt)
      newResult.add_field(name="**Instructor**", value="{}".format(courses[0].instructor.title()), inline=True)
      newResult.add_field(name="**Section**", value="{}".format(courses[0].section), inline=True)
      newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(courses[0]))), inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      newResult.set_image(url="attachment://{}_{}.png".format(coursename, courses[0].number))
      if page == 0:
        await interaction.edit_original_message(view = MenuOneTwoDropLeftDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(embed=newResult)

class upButton(Button):
  def __init__(self):
    super().__init__(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)

  async def callback(self, interaction):
    await interaction.response.defer()
    global page
    page = 0
    gradecalculations.generateCourseImage(courses[0])
    newResult = discord.Embed(
      color=0xF59F16,
      title = f"**{courses[0].dept} {courses[0].number}**"
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = f"Similar search results ({len(similarcoursesstrings)}):\t\t\t\t\t*Data last updated on 7/10/2022"

    i = 0
    emojidict = {
      1: "1️⃣",
      2: "2️⃣",
    }

    for similarcourse in similarcoursesstrings[:2]:
      i += 1
      txt += f"\n{emojidict[i]} {similarcourse}"

    if len(similarcoursesstrings) > 2:
      txt += "\n~~continued below~~"

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value=f"{courses[0].instructor.title()}", inline=True)
    newResult.add_field(name="**Section**", value=f"{courses[0].section}", inline=True)
    newResult.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(courses[0]))}", inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
    newResult.set_image(url=f"attachment://{coursename}_{courses[0].number}.png")
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

class oneButton(Button):
  def __init__(self):
    super().__init__(emoji="1️⃣", style=discord.ButtonStyle.gray)

  async def callback(self, interaction):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[1].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[1].number))


    await interaction.followup.send(file=file, embed=newResult)    

class twoButton(Button):
  def __init__(self):
    super().__init__(emoji="2️⃣", style=discord.ButtonStyle.gray)

  async def callback(self, interaction):
    await interaction.response.defer()
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
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(maincourse)
    )

    newResult.add_field(name="**Instructor**", value="{}".format(similarcourses[2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(similarcourses[2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(similarcourses[2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', similarcourses[2].dept)
    file = discord.File("grades/graph.png", filename="{}_{}.png".format(coursename, similarcourses[2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, similarcourses[2].number))

    await interaction.followup.send(file=file, embed=newResult)


class client(discord.Client):
  def __init__(self):
    super().__init__(intents = discord.Intents.default())
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync()
      self.synced = True
    print(f"Logged in as {self.user}")

aclient = client()
tree = app_commands.CommandTree(aclient)


#GRADES
@tree.command(name = "courses", description='Searches and displays data for a specified course')
@app_commands.rename(info='search-query')
@app_commands.describe(info='ex. CS 3050 2018 Spring Xu')
async def courses(interaction: discord.Interaction, info: str = ""):
    await interaction.response.defer()
    global i
    i = 0

    info = info.strip().split()

    global courses
    courses = gradecalculations.getCourse(info)

    if (courses != []):
      global page
      page = 0
      global maincourse
      maincourse = f"{courses[0].dept} {courses[0].number}"

      gradecalculations.generateCourseImage(courses[0])
      embed = discord.Embed(
        color=0xF59F16,
        title = f"**{courses[0].dept} {courses[0].number}**"
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
        if (f"{courses[i].dept} {courses[i].number} - {courses[i].title.title()}") not in similarcoursesstrings:
          similarcoursesstrings.append(f"{courses[i].dept} {courses[i].number} - {courses[i].title.title()}")
          similarcourses.append(courses[i])
      similarcoursesstrings.remove(f"{courses[0].dept} {courses[0].number} - {courses[0].title.title()}")
      txt = f"Similar search results ({len(similarcoursesstrings)}):\t\t\t\t\t*Data last updated on 7/10/2022"

      i = 0
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      for similarcourse in similarcoursesstrings[:2]:
        i += 1
        txt += f"\n{emojidict[i]} {similarcourse}"

      if len(similarcoursesstrings) > 2:
        txt += "\n~~continued below~~"

      embed.set_footer(text=txt)
      embed.add_field(name="**Instructor**", value=f"{courses[0].instructor.title()}", inline=True)
      embed.add_field(name="**Section**", value=f"{courses[0].section}", inline=True)
      embed.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(courses[0]))}", inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', courses[0].dept)
      file = discord.File("grades/graph.png", filename=f"{coursename}_{courses[0].number}.png")
      embed.set_image(url=f"attachment://{coursename}_{courses[0].number}.png")

      if len(similarcoursesstrings) == 0:
        await interaction.followup.send(file=file, embed=embed)
      elif len(similarcoursesstrings) == 1:
        await interaction.followup.send(view=MenuOne(), file=file, embed=embed)
      elif len(similarcoursesstrings) == 2:
        await interaction.followup.send(view=MenuOneTwo(), file=file, embed=embed)
      else:
        await interaction.followup.send(view=MenuOneTwoDrop(), file=file, embed=embed)
      

    else:
      embed=discord.Embed(
        description = "No courses found! Please try again",
        color=0xF59F16,
      )

      embed.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      await interaction.followup.send(embed=embed)


#DIRECTORY
@tree.command(name = "directory", description='Searches the directory for the specified student')
@app_commands.rename(firstname='first-name', lastname='last-name')
@app_commands.describe(
    firstname='First name of student',
    lastname='Last name of student'
)
async def personsearch(interaction: discord.Interaction, firstname: str = "", lastname: str = ""):
    await interaction.response.defer()
    if not firstname and not lastname:
        await interaction.followup.send('Please specificy a first or last name!', ephemeral=True)

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
        await interaction.followup.send(embed=embed)


#DINING
@tree.command(name = "dining", description='Displays the menu and hours for the specified dining hall')
@app_commands.describe(hall='Dining Hall')
@app_commands.choices(hall = [
    Choice(name = "Sabai", value = "Sabai"),
    Choice(name = "Plaza 900 Dining", value = "Plaza 900 Dining"),
    Choice(name = "Baja Grill", value = "Baja Grill"),
    Choice(name = "Sunshine Sushi", value = "Sunshine Sushi"),
    Choice(name = "Wheatstone Bistro", value = "Wheatstone Bistro")
])
async def dining(interaction: discord.Interaction, hall : str):
    await interaction.response.defer()
    await interaction.followup.send(f"{hall}")

#REC
@tree.command(name = "rec", description='Displays hours for the Rec Facility this week')
async def rechours(interaction: discord.Interaction):
    await interaction.response.defer()
    rechours = rec.getDaysDictionary(rec.getWeekDictionary())
    dayofweek = datetime.datetime.today().weekday()
    embed=discord.Embed(
        title="Rec Center Facility Hours",
        url="https://mizzourec.com/facilities/information/hours/",
        description=f"""
{"__" if dayofweek == 6 else ""}**Sunday:** {rechours["SUNDAY"]}{"__" if dayofweek == 6 else ""}

{"__" if dayofweek == 0 else ""}**Monday:** {rechours["MONDAY"]}{"__" if dayofweek == 0 else ""}

{"__" if dayofweek == 1 else ""}**Tuesday:** {rechours["TUESDAY"]}{"__" if dayofweek == 1 else ""}

{"__" if dayofweek == 2 else ""}**Wednesday:** {rechours["WEDNESDAY"]}{"__" if dayofweek == 2 else ""}

{"__" if dayofweek == 3 else ""}**Thursday:** {rechours["THURSDAY"]}{"__" if dayofweek == 3 else ""}

{"__" if dayofweek == 4 else ""}**Friday:** {rechours["FRIDAY"]}{"__" if dayofweek == 4 else ""}

{"__" if dayofweek == 5 else ""}**Saturday:** {rechours["SATURDAY"]}{"__" if dayofweek == 5 else ""}""",
        color=0xF59F16,
    )

    embed.set_author(
      name = "Mizzou Rec",
      url="https://mizzourec.com/",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    embed.set_footer(
      text=f"Showing schedule for {rec.getWeek()}"
    )

    await interaction.followup.send(embed=embed)


#COVID
@tree.command(name = "covid", description='Displays information regarding Covid-19 in Mizzou')
async def covidinfo(interaction: discord.Interaction):
    await interaction.response.defer()
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
      name = "MU COVID INFO",
      url="https://missouri.edu/covid",
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    embed.set_footer(
      text="*Information last updated as of 07/13/2022"
    )

    await interaction.followup.send(embed=embed)


#GIF COMMANDS
@tree.command(name = "dance", description='Posts a GIF of Truman dancing')
async def dance(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} danced!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://c.tenor.com/BDxIoo-dxPgAAAAC/missouri-tigers-truman-the-tiger.gif')
    await interaction.followup.send(embed=embed)

@tree.command(name = "thumbsup", description='Posts a GIF of Truman giving a thumbs up')
async def thumbsup(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} sent a thumbs up!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://media3.giphy.com/media/S6foDbT2nnSoAZlPNS/giphy.gif?cid=790b761118c586046ec8a0611a72b517fe865bf489ed48dc&rid=giphy.gif&ct=g')
    await interaction.followup.send(embed=embed)

@tree.command(name = "surprised", description='Posts a GIF of Truman being surprised')
async def surprised(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} was surprised!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://d98lmo17970r8.cloudfront.net/images/2017/12/4/Reax_truman_oh_no.gif')
    await interaction.followup.send(embed=embed)

@tree.command(name = "clap", description='Posts a GIF of Truman clapping')
async def clap(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} clapped!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://c.tenor.com/g12vGZQ5nPUAAAAC/missouri-mizzoufootball.gif')
    await interaction.followup.send(embed=embed)


#TOKEN
aclient.run(os.getenv('TOKEN'))