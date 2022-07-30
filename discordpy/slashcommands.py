from dotenv import load_dotenv, find_dotenv
import sys
import os

load_dotenv(find_dotenv())
sys.path.insert(1, os.getenv('FILE'))
from discord import app_commands
import discord
from dotenv import load_dotenv, find_dotenv
import math
import re
import src.grades.Course as Course
import src.grades.gradecalculations as gradecalculations
from discord.app_commands import Choice
from discord.ui import Button
from embeds import *

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
aclient.maincourse = {}
aclient.page = {}
aclient.similarcourses = {}
aclient.similarcrsstrings = {}
aclient.courses = {}


class MenuOne(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))

    await interaction.followup.send(file=file, embed=newResult)

class MenuOneTwo(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][2])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][2].dept, aclient.similarcourses[interaction.guild.id][2].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][2].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))

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
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))

    await interaction.followup.send(file=file, embed=newResult)


  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][2])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][2].dept, aclient.similarcourses[interaction.guild.id][2].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][2].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="<:dropdownarrow:1001307846169870427>", style=discord.ButtonStyle.blurple)
  async def dropdown(self,interaction:discord.Interaction, button:discord.ui.Button):
    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])), str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
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

    newResult.set_footer(text=txt)
    newResult.add_field(name="**Instructor**", value="{}".format(aclient.courses[interaction.guild.id][0].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.courses[interaction.guild.id][0].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.courses[interaction.guild.id][0].number))

    if len(aclient.similarcrsstrings[interaction.guild.id]) > 10:
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
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])), str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
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
    oldResult.add_field(name="**Instructor**", value="{}".format(aclient.courses[interaction.guild.id][0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(aclient.courses[interaction.guild.id][0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.courses[interaction.guild.id][0].number))
    
    aclient.page[interaction.guild.id]= 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][2])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][2].dept, aclient.similarcourses[interaction.guild.id][2].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][2].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])), str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
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
    oldResult.add_field(name="**Instructor**", value="{}".format(aclient.courses[interaction.guild.id][0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(aclient.courses[interaction.guild.id][0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.courses[interaction.guild.id][0].number))
    
    aclient.page[interaction.guild.id]= 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)


  @discord.ui.button(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)
  async def uparrow(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    aclient.page[interaction.guild.id]= 0
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
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

  @discord.ui.button(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green)
  async def leftbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    if aclient.page[interaction.guild.id]> 0:
      aclient.page[interaction.guild.id]-= 1
      newResult = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
      )

      newResult.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])),aclient.page[interaction.guild.id]+1,str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      if aclient.page[interaction.guild.id]== 0:
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
      if aclient.page[interaction.guild.id]== 0:
        await interaction.edit_original_message(view = MenuOneTwoDropLeftDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(embed=newResult)

  @discord.ui.button(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)
  async def rightbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    if aclient.page[interaction.guild.id] < len(aclient.similarcrsstrings[interaction.guild.id])/10 - 1:
      aclient.page[interaction.guild.id]+= 1
      newResult = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
      )

      newResult.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])),aclient.page[interaction.guild.id]+1,str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      if aclient.page[interaction.guild.id]== 0:
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
      if aclient.page[interaction.guild.id]== math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10 - 1):
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
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
    color=0xF59F16,
    title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])), str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
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
    oldResult.add_field(name="**Instructor**", value="{}".format(aclient.courses[interaction.guild.id][0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(aclient.courses[interaction.guild.id][0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.courses[interaction.guild.id][0].number))
    
    aclient.page[interaction.guild.id]= 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][2])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][2].dept, aclient.similarcourses[interaction.guild.id][2].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][2].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))

    await interaction.followup.send(file=file, embed=newResult)

    oldResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
    )

    oldResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page 1/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])), str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
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
    oldResult.add_field(name="**Instructor**", value="{}".format(aclient.courses[interaction.guild.id][0].instructor.title()), inline=True)
    oldResult.add_field(name="**Section**", value="{}".format(aclient.courses[interaction.guild.id][0].section), inline=True)
    oldResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
    oldResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.courses[interaction.guild.id][0].number))
    
    aclient.page[interaction.guild.id]= 0
    await interaction.edit_original_message(view=MenuOneTwoDropLeftDisabled(), embed=oldResult)

  @discord.ui.button(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)
  async def uparrow(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    aclient.page[interaction.guild.id]= 0
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
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

  @discord.ui.button(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green)
  async def leftbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    if aclient.page[interaction.guild.id]> 0:
      aclient.page[interaction.guild.id]-= 1
      newResult = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
      )

      newResult.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])),aclient.page[interaction.guild.id]+1,str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      if aclient.page[interaction.guild.id]== 0:
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
      if aclient.page[interaction.guild.id]== 0:
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
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][2])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][2].dept, aclient.similarcourses[interaction.guild.id][2].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][2].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))

    await interaction.followup.send(file=file, embed=newResult)

  @discord.ui.button(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)
  async def uparrow(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    aclient.page[interaction.guild.id]= 0
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
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

  @discord.ui.button(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green, disabled = True)
  async def leftbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()

  @discord.ui.button(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)
  async def rightbut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.defer()
    
    if aclient.page[interaction.guild.id] < len(aclient.similarcrsstrings[interaction.guild.id])/10 - 1:
      aclient.page[interaction.guild.id]+= 1
      newResult = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
      )

      newResult.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])),aclient.page[interaction.guild.id]+1,str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      if aclient.page[interaction.guild.id]== 0:
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
      if aclient.page[interaction.guild.id]== math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10 - 1):
        await interaction.edit_original_message(view = MenuOneTwoDropRightDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(view = MenuOneTwoDropAllEnabled(), embed=newResult)


class rightButton(Button):
  def __init__(self):
    super().__init__(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)

  async def callback(self, interaction):
    await interaction.response.defer()
    
    if aclient.page[interaction.guild.id]< len(aclient.similarcrsstrings[interaction.guild.id])/10 - 1:
      aclient.page[interaction.guild.id]+= 1
      newResult = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
      )

      newResult.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])),aclient.page[interaction.guild.id]+1,str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      if aclient.page[interaction.guild.id]== 0:
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
      if aclient.page[interaction.guild.id]== math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10 - 1):
        await interaction.edit_original_message(view = MenuOneTwoDropRightDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(view = MenuOneTwoDropAllEnabled(), embed=newResult)

class leftButton(Button):
  def __init__(self, disabled):
    super().__init__(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green, disabled = disabled)

  async def callback(self, interaction):
    await interaction.response.defer()
    
    if aclient.page[interaction.guild.id]> 0:
      aclient.page[interaction.guild.id]-= 1
      newResult = discord.Embed(
        color=0xF59F16,
        title = "**{} {}**".format(aclient.courses[interaction.guild.id][0].dept, aclient.courses[interaction.guild.id][0].number),
      )

      newResult.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      txt = "Similar search results ({}):\t\t\t\t\t\t\t\t\t\t    Page {}/{}".format((len(aclient.similarcrsstrings[interaction.guild.id])),aclient.page[interaction.guild.id]+1,str(math.ceil(len(aclient.similarcrsstrings[interaction.guild.id])/10)))
      emojidict = {
        1: "1️⃣",
        2: "2️⃣",
      }

      if aclient.page[interaction.guild.id]== 0:
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
      if aclient.page[interaction.guild.id]== 0:
        await interaction.edit_original_message(view = MenuOneTwoDropLeftDisabled(), embed=newResult)
      else:
        await interaction.edit_original_message(embed=newResult)

class upButton(Button):
  def __init__(self):
    super().__init__(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)

  async def callback(self, interaction):
    await interaction.response.defer()
    
    aclient.page[interaction.guild.id]= 0
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
    await interaction.edit_original_message(view = MenuOneTwoDrop(), embed=newResult)

class oneButton(Button):
  def __init__(self):
    super().__init__(emoji="1️⃣", style=discord.ButtonStyle.gray)

  async def callback(self, interaction):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][1])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][1].dept, aclient.similarcourses[interaction.guild.id][1].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][1].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][1]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][1].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][1].number))


    await interaction.followup.send(file=file, embed=newResult)    

class twoButton(Button):
  def __init__(self):
    super().__init__(emoji="2️⃣", style=discord.ButtonStyle.gray)

  async def callback(self, interaction):
    await interaction.response.defer()
    gradecalculations.generateCourseImage(aclient.similarcourses[interaction.guild.id][2])

    newResult = discord.Embed(
      color=0xF59F16,
      title = "**{} {}**".format(aclient.similarcourses[interaction.guild.id][2].dept, aclient.similarcourses[interaction.guild.id][2].number),
    )

    newResult.set_author(
    name = 'MU Grades',
    icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
    )

    newResult.set_footer(
      text="Queried by: {}\t\t\t\t\t*Data last updated on 7/10/2022".format(aclient.maincourse[interaction.guild.id])
    )

    newResult.add_field(name="**Instructor**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].instructor.title()), inline=True)
    newResult.add_field(name="**Section**", value="{}".format(aclient.similarcourses[interaction.guild.id][2].section), inline=True)
    newResult.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(aclient.similarcourses[interaction.guild.id][2]))), inline=True)

    coursename = re.sub(r'[^a-zA-Z]', '', aclient.similarcourses[interaction.guild.id][2].dept)
    file = discord.File("src/grades/graph.png", filename="{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))
    newResult.set_image(url="attachment://{}_{}.png".format(coursename, aclient.similarcourses[interaction.guild.id][2].number))

    await interaction.followup.send(file=file, embed=newResult)


#REC
@tree.command(name = "rec", description='Displays hours for the Rec Facility this week')
async def rechours(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(embed=getRecHoursEmbed(interaction))


#COVID
@tree.command(name = "covid", description='Displays information regarding Covid-19 in Mizzou')
async def covidinfo(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(embed=getCovidEmbed(interaction))


#GIF COMMANDS
@tree.command(name = "dance", description='Posts a GIF of Truman dancing')
async def dance(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(embed=getGifEmbed("dance", interaction))

@tree.command(name = "thumbsup", description='Posts a GIF of Truman giving a thumbs up')
async def thumbsup(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(embed=getGifEmbed("thumbsup", interaction))

@tree.command(name = "surprised", description='Posts a GIF of Truman being surprised')
async def surprised(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(embed=getGifEmbed("surprised", interaction))

@tree.command(name = "clap", description='Posts a GIF of Truman clapping')
async def clap(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(embed=getGifEmbed("clap", interaction))


#DIRECTORY
@tree.command(name = "directory", description='Searches the directory for the specified student')
@app_commands.rename(firstname='first-name', lastname='last-name')
@app_commands.describe(
    firstname='First name of student',
    lastname='Last name of student'
)
async def personsearch(interaction: discord.Interaction, firstname: str = "", lastname: str = ""):
    await interaction.response.defer()
    await interaction.followup.send(embed=directorySearchEmbed(firstname, lastname))


#DINING
@tree.command(name = "dining", description='Displays the menu and hours for the specified dining hall')
@app_commands.describe(hall='Dining Hall')
@app_commands.choices(hall = [
    Choice(name = "All", value = "All"),
    Choice(name = "Open", value = "Open"),
    Choice(name = "Sabai", value = "Sabai"),
    Choice(name = "Plaza 900 Dining", value = "Plaza 900 Dining"),
    Choice(name = "Baja Grill", value = "Baja Grill"),
    Choice(name = "Sunshine Sushi", value = "Sunshine Sushi"),
    Choice(name = "Wheatstone Bistro", value = "Wheatstone Bistro"),
    Choice(name = "Infusion", value = "Infusion")
])
async def dining(interaction: discord.Interaction, hall : str):
    await interaction.response.defer()
    await interaction.followup.send(embed=getDiningEmbed(hall, interaction))


#GRADES
@tree.command(name = "courses", description='Searches and displays data for a specified course')
@app_commands.rename(info='search')
@app_commands.describe(info='ex. CS 3050 2018 Spring Xu')
async def courses(interaction: discord.Interaction, info: str):
    await interaction.response.defer()

    info = info.strip().split()

    aclient.courses[interaction.guild.id] = gradecalculations.getCourse(info)
    aclient.similarcourses[interaction.guild.id] = []
    aclient.similarcrsstrings[interaction.guild.id] = []

    if (aclient.courses[interaction.guild.id] != []):
      
      aclient.page[interaction.guild.id] = 0
      aclient.maincourse[interaction.guild.id] = f"{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number}"

      gradecalculations.generateCourseImage(aclient.courses[interaction.guild.id][0])
      embed = discord.Embed(
        color=0xF59F16,
        title = f"**{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number}**"
      )

      embed.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      for i in range(len(aclient.courses[interaction.guild.id])):
        if (f"{aclient.courses[interaction.guild.id][i].dept} {aclient.courses[interaction.guild.id][i].number} - {aclient.courses[interaction.guild.id][i].title.title()}") not in aclient.similarcrsstrings[interaction.guild.id]:
          aclient.similarcrsstrings[interaction.guild.id].append(f"{aclient.courses[interaction.guild.id][i].dept} {aclient.courses[interaction.guild.id][i].number} - {aclient.courses[interaction.guild.id][i].title.title()}")
          aclient.similarcourses[interaction.guild.id].append(aclient.courses[interaction.guild.id][i])
      aclient.similarcrsstrings[interaction.guild.id].remove(f"{aclient.courses[interaction.guild.id][0].dept} {aclient.courses[interaction.guild.id][0].number} - {aclient.courses[interaction.guild.id][0].title.title()}")
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

      embed.set_footer(text=txt)
      embed.add_field(name="**Instructor**", value=f"{aclient.courses[interaction.guild.id][0].instructor.title()}", inline=True)
      embed.add_field(name="**Section**", value=f"{aclient.courses[interaction.guild.id][0].section}", inline=True)
      embed.add_field(name="**Total Students**", value=f"{str(Course.getTotalStudents(aclient.courses[interaction.guild.id][0]))}", inline=True)

      coursename = re.sub(r'[^a-zA-Z]', '', aclient.courses[interaction.guild.id][0].dept)
      file = discord.File("src/grades/graph.png", filename=f"{coursename}_{aclient.courses[interaction.guild.id][0].number}.png")
      embed.set_image(url=f"attachment://{coursename}_{aclient.courses[interaction.guild.id][0].number}.png")

      if len(aclient.similarcrsstrings[interaction.guild.id]) == 0:
        await interaction.followup.send(file=file, embed=embed)
      elif len(aclient.similarcrsstrings[interaction.guild.id]) == 1:
        await interaction.followup.send(view=MenuOne(), file=file, embed=embed)
      elif len(aclient.similarcrsstrings[interaction.guild.id]) == 2:
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

#TOKEN
aclient.run(os.getenv('TOKEN'))