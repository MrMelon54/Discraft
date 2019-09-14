import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix='/', description='A bot that responds to Minecraft commands.')
client = discord.Client()

TOKEN = 'Insert token here'

def ismember(name: str):
	memb = (set(map(str, bot.get_all_members())))
	namef= name, "#"
	namefi = ''.join(namef)
	#print(namefi)
	#print(memb)
	membi=''.join(memb)
	#print(membi)
	if namefi in membi:
		return 1
	else:
		return 0

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

	
@bot.command(pass_context = True)
@commands.has_any_role("Despotizmus")
async def kick(ctx, userName: discord.Member):
	#if ctx.message.author.server_permissions.administrator:
	await ctx.send(f'{userName.name} has been kicked!')
	await ctx.guild.kick(userName)
	#else:
	#await ctx.send(f'No permission!')
	
	
'''@bot.command(pass_context = True)
@commands.has_any_role("Member")
async def kick(ctx, userName: discord.Member):
	#if ctx.message.author.server_permissions.administrator:
	#await ctx.send(f' {userName.name} has been kicked!')
	#await ctx.guild.kick(userName)
	#else:
	await ctx.send(f'No permission!')

@bot.command(pass_context=True)
@commands.has_any_role("Despotizmus")
async def user_info(ctx, user: discord.Member):
    await ctx.send(f'The username of the user is {user.name}')
    await ctx.send(f'The ID of the user is {user.id}')
    await ctx.send(f'The status of the user is {user.status}')
    await ctx.send(f'The role of the user is {user.top_role}')
    await ctx.send(f'The user joined at {user.joined_at}')'''

	
	
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "cuz why not?"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    # await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} has been banned!")
    
@kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await bot.send_message(ctx.message.channel, text)

@bot.command()
async def ismembere(ctx, name: str):
	print(ismember(name))
	
@bot.command()
async def kill(ctx, name: str):
	memb = (set(map(str, bot.get_all_members())))
	namef= name, "#"
	namefi = ''.join(namef)
	#print(namefi)
	#print(memb)
	membi=''.join(memb)
	#print(membi)
	if namefi in membi:
		final=name, " has been killed by ", str(ctx.message.author)
		await ctx.send(''.join(final))
	else:
		await ctx.send('Player not found')

bot.run(TOKEN)

