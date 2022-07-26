import discord
from discord.ui import Button

class MenuOne(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.edit_message(view = self, content = "1")

class MenuOneTwo(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.edit_message(view = self, content = "1")

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.edit_message(view = self, content = "2")

class MenuOneTwoDrop(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  async def editafterclicked(self, interaction: discord.Interaction):
    oldview = self
    self.clear_items()
    self.add_item(oneButton())
    self.add_item(twoButton())
    self.add_item(upButton())
    self.add_item(leftButton())
    self.add_item(rightButton())
    await interaction.response.edit_message(view = self, content = "asdf")

  @discord.ui.button(emoji="1️⃣", style=discord.ButtonStyle.gray)
  async def onebut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.edit_message(view = self, content = "1")

  @discord.ui.button(emoji="2️⃣", style=discord.ButtonStyle.gray)
  async def twobut(self,interaction:discord.Interaction, button:discord.ui.Button):
    await interaction.response.edit_message(view = self, content = "2")

  @discord.ui.button(emoji="<:dropdownarrow:1001307846169870427>", style=discord.ButtonStyle.blurple)
  async def dropdown(self,interaction:discord.Interaction, button:discord.ui.Button):
    await self.editafterclicked(interaction)
    await interaction.response.edit_message(view = self, content = "drop")


class rightButton(Button):
  def __init__(self):
    super().__init__(emoji="<:next_check:754948796361736213>", style=discord.ButtonStyle.green)

  async def callback(self, interaction):
    await interaction.response.edit_message(content = "Clicked right")

class leftButton(Button):
  def __init__(self):
    super().__init__(emoji="<:before_check:754948796487565332>", style=discord.ButtonStyle.green)

  async def callback(self, interaction):
    await interaction.response.edit_message(content = "Clicked left")

class downButton(Button):
  def __init__(self):
    super().__init__(emoji="<:dropdownarrow:1001307846169870427>", style=discord.ButtonStyle.blurple)

  async def callback(self, interaction):
    await interaction.response.edit_message(content = "Clicked down")

class upButton(Button):
  def __init__(self):
    super().__init__(emoji="<:upwardarrow:1001308391496503316>", style=discord.ButtonStyle.blurple)

  async def callback(self, interaction):
    await interaction.response.edit_message(content = "Clicked up")

class oneButton(Button):
  def __init__(self):
    super().__init__(emoji="1️⃣", style=discord.ButtonStyle.gray)

  async def callback(self, interaction):
    await interaction.response.edit_message(content = "Clicked one")

class twoButton(Button):
  def __init__(self):
    super().__init__(emoji="2️⃣", style=discord.ButtonStyle.gray)

  async def callback(self, interaction):
    await interaction.response.edit_message(content = "Clicked two")


    