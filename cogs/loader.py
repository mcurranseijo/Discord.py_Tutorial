import discord
from discord.ext import commands


class LoaderCommands(commands.Cog, name='Developer Commands'):
	'''These are the developer commands'''

	def __init__(self, bot):
		self.bot = bot

	@commands.command(  # Decorator to declare where a command is.
		name='reload',  # Name of the command, defaults to function name.
		aliases=['rl']  # Aliases for the command.
	)  
	async def reload(self, ctx, cog):
		#Reloads the cog useful for quick testing of changes
		extensions = self.bot.extensions  # A list of the bot's cogs/extensions.
		if cog == 'all':  # Lets you reload all cogs at once
			for extension in extensions:
				self.bot.unload_extension(cog)
				self.bot.load_extension(cog)
			await ctx.send('Done')
		if cog in extensions:
			self.bot.unload_extension(cog)  # Unloads the cog
			self.bot.load_extension(cog)  # Loads the cog
			await ctx.send('Done')  # Sends a message where content='Done'
		else:
			await ctx.send('Unknown Cog')  # If the cog isn't found/loaded.
	
	@commands.command(name="unload", aliases=['ul']) 
	async def unload(self, ctx, cog):
		#unload and removes a cog takes in cog same as you would for loading it
		extensions = self.bot.extensions
		if cog not in extensions:
			await ctx.send("Cog is not loaded!")
			return
		self.bot.unload_extension(cog)
		await ctx.send(f"`{cog}` has successfully been unloaded.")
	
	@commands.command(name="load")
	async def load(self, ctx, cog):
	  #Loads in a cog, takes in cog name same as you would import it
		try:

			self.bot.load_extension(cog)
			await ctx.send(f"`{cog}` has successfully been loaded.")

		except commands.errors.ExtensionNotFound:
			await ctx.send(f"`{cog}` does not exist!")

def setup(bot):
	bot.add_cog(LoaderCommands(bot))
