from dotenv import load_dotenv, find_dotenv
import sys
import os
load_dotenv(find_dotenv())
sys.path.insert(1, os.getenv('FILE'))
from socket import MsgFlag
import discord, asyncio
from discord import app_commands
from typing import Optional
import discord
from discord.utils import get
import asyncio
#import dining.sabai as sabai
import datetime
from dotenv import load_dotenv, find_dotenv
import math
import time
import re
import rec.rec as rec
import directory
import directory.directorysearch as directorysearch
import directory.Person as Person


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
        await interaction.followup.send(embed=embed)


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
      text="Showing schedule for {}".format(rec.getWeek())
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
async def dance(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} sent a thumbs up!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://media3.giphy.com/media/S6foDbT2nnSoAZlPNS/giphy.gif?cid=790b761118c586046ec8a0611a72b517fe865bf489ed48dc&rid=giphy.gif&ct=g')
    await interaction.followup.send(embed=embed)

@tree.command(name = "surprised", description='Posts a GIF of Truman being surprised')
async def dance(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} was surprised!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://d98lmo17970r8.cloudfront.net/images/2017/12/4/Reax_truman_oh_no.gif')
    await interaction.followup.send(embed=embed)

@tree.command(name = "clap", description='Posts a GIF of Truman clapping')
async def dance(interaction: discord.Interaction):
    await interaction.response.defer()
    embed=discord.Embed(color=0xF59F16)
    embed.set_author(
    name=(f"{interaction.user.name} clapped!"),
    icon_url=(interaction.user.avatar)
    )
    embed.set_image(url='https://c.tenor.com/g12vGZQ5nPUAAAAC/missouri-mizzoufootball.gif')
    await interaction.followup.send(embed=embed)


@tree.command(name = 'hello',description='says hi')
async def slash(interaction: discord.Interaction):
  await interaction.response.send_message(f"hello {interaction.user.name}")

#TOKEN
aclient.run(os.getenv('TOKEN'))