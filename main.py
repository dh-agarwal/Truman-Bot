import discord
import dining.sabai as sabai
import grades.Course as Course
import grades.gradecalculations as gradecalculations
import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = discord.Client()

@client.event
async def on_message(message):
  msg = message.content
  auth = message.author.name

  if message.author == client.user:
    return

  if msg.startswith('/grades'):
    msg = msg.strip()
    info = msg.split()
    info.pop(0)
    course1 = gradecalculations.getCourse(info)
    if (course1.title != "Not Found"):
      gradecalculations.generateCourseImage(course1)
      embed=discord.Embed(
        color=0xF59F16,
        description = "**{} {}**".format(course1.dept, course1.number),
      )
      embed.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )
      embed.set_footer(
        text="Data last updated on 6/17/2022"
      )
      embed.add_field(name="**Instructor**", value="{}".format(course1.instructor.title()), inline=True)
      embed.add_field(name="**Section**", value="{}".format(course1.section), inline=True)
      embed.add_field(name="**Total Students**", value="{}".format(str(Course.getTotalStudents(course1))), inline=True)
      file = discord.File("graph.png", filename="{}_{}.png".format(course1.dept, course1.number))
      embed.set_image(url="attachment://{}_{}.png".format(course1.dept, course1.number))
      await message.channel.send(file=file, embed=embed)
    else:
      embed=discord.Embed(
        description = "Course was not found! Please try again",
        color=0xF59F16,
      )
      embed.set_author(
      name = 'MU Grades',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )

      await message.channel.send(embed=embed)

  if msg.startswith('/dining'):
    info = msg.split()
    hall = info[1]
    if hall == "sabai":
      sabaibreakfaststring = sabai.getSabaiBreakfast()
      sabailunchstring = sabai.getSabaiLunch()
      name = sabai.getName()

      now = datetime.datetime.now()
      pm = "PM" if now.hour>11 else "AM"
      embed=discord.Embed(
        title="Today's " + name + " Menu",
        url="https://dining.missouri.edu/locations/sabai-summer/",
        description= sabaibreakfaststring + "\n" + sabailunchstring,
        color=0xF59F16,
      )
      embed.set_author(
      name = 'Sabai',
      icon_url='https://i.pinimg.com/originals/b7/dc/4b/b7dc4b733225b5981c48060a9f7e1ccb.jpg'
      )
      embed.set_footer(
        text="This menu is subject to change  •  Today at " + str((now.hour)%12) + ":" + str(now.minute) + " " + pm
      )
      await message.channel.send(embed=embed)
    else:
      embed=discord.Embed(
        description = "Dining hall was not found! Please try again",
        color=0xF59F16,
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


#TOKEN
client.run(os.getenv('TOKEN'))  
