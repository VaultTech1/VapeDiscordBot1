#Imports
import discord
import random
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
#Prefix
client = commands.Bot(command_prefix = '.')

#Status
status = cycle(['VaultTechBot', '! vault#5549'])
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#StartUp
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready and connected to discord.')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question): 
    responses = ['It is certain. ',
                 'It is decidely so.',
                 'I would say no.',
                 'Without a doubt.',
                 'You may rely on it.',
                 'Yes definitely.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Reply hazy try again.',
                 'Better not tell you now.',
                 'Ask again later.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'Outlook not so good.',
                 'My sources say no.',
                 'Very doubtful.',
                 'My reply is no.',
                 'Yes.',
                 'Outlook good.',
                 'Signs point to yes.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(ban_member=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None): 
    await member.kick(reason=reason)

client.run('BOT_TOKEN')
