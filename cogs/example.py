"""Here are your needed imports you may need to add to theese depending on what your doing"""
import discord
from discord.ext import commands


"""
This creates the class your cog runs in, 'ExampleCog' should be replaced with whatever you want your cog name to be.
"""
class ExampleCog(commands.Cog):
  """This creates and defines the needed info for you"""
  def __init__(self,bot):
    self.bot = bot
		
  @commands.command(
    name="example", #This is the name of the command
    brief="This command returns an example message", #This is a short description of the command
    aliases=['exam','ex'] #These are alternate ways to summon the command
    )
  #This is the minimum for setting up a command, it takes in no arguments and
  #returns whatever you choose with no additional user input
  async def example(self,ctx):
		  await ctx.send('Hello There, this is an example command')
		  
  @commands.command(
    name="embed", #This is the name of the command
    brief="This command returns an example embed with all field filled", #This is a short description of the command
    aliases=['em','emb'] #These are alternate ways to summon the command
    )
  async def embed(self,ctx):

    #This line creates an embed, a title is needed but the description, 
    #and url are optional
	  embed=discord.Embed(title="This is a title for an embed", url="https://hostsapling.net/",description="This is the description, it is optional")
    
    #This is an author, it's an optional field that requires a name
    #You can also add the url and icon_url
	  embed.set_author(
      name="This is the author name, it's also optional",
      url="https://github.com/mcurranseijo/Discord.py_Tutorial",
      icon_url="https://avatars1.githubusercontent.com/u/68172072?s=96&v=4")


    #These are fields, they reuire a name and value and can be set to inline or 
    #or not inline
	  embed.add_field(name="This is a field,", value="it needs a name and value", inline=False)
	  embed.add_field(name="This is an inline field", value="alone it looks the same", inline=True)
	  embed.add_field(name="But this is also an inline field", value="together they display lined up across", inline=True)

    #This is a footer it can be used to add text at the bottom of an embed
	  embed.set_footer(text="This is the footer text you don't need it add it but it is useful")
	  await ctx.send(embed=embed)


  #The below method takes the full args and returns it all together there are other
  #ways to format it that you can learn as you gain more skills
  @commands.command(
    name="args", #This is the name of the command
    brief="This command returns what the user says", #This is a short description of the command
    aliases=['ar','arg'] #These are alternate ways to summon the command
  )
  async def args(self,ctx,*,args):
      await ctx.send(args)

		
def setup(bot):
    """Imports the cog, this should also be set to the name of the class"""
    bot.add_cog(ExampleCog(bot))
