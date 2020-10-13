"""These lines import the needed libraries, you'll also need to setup your requirements.txt for this (see readme)"""
import discord
from discord.ext import commands

"""Here is where you can change your bot prefix, you can use any character (or characters) but it should be something simple. The default is a period"""
bot = commands.Bot(
	command_prefix=".",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)


"""This is the bot load function, you should see it print a message if it loaded in properly"""
@bot.event 
async def on_ready():  # When the bot is ready
    print(bot.user+' is online')  # Prints the bot's username and identifier

"""This is where you will add the additional cogs, you will need to add them as cogs.filename and they should be placed in the cogs folder.
Each time you add a final cog you should add it here so it will autload on restart. For testing you can use the load cog command."""

extensions = [
	'cogs.example','cogs.loaders'  # Same name as it would be if you were importing it
]

"""You won't need to touch this, this just makes sure this is the proper file""" 
if __name__ == '__bot__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.
		
		
"""This is where you should put your bot token, the instructions for generating that can be found in the readme file"""		
bot.run('Bot Token Goes Here')  # Starts the bot
