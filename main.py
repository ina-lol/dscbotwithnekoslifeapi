import nextcord
import nekos
from nextcord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def ping(ctx):
    async with ctx.typing():
        await ctx.send(f'Pong! {ctx.message.author.mention}')

@bot.command()
async def img(ctx, message):
    async with ctx.typing():
        await ctx.send(f'Aqui está {nekos.img(message)} ฅ•ω•ฅ')

@bot.command()
async def textcat(ctx):
    async with ctx.typing():
        await ctx.send(nekos.textcat())

@bot.command()
async def fact(ctx):
    async with ctx.typing():
        await ctx.send(nekos.fact())

@bot.command()
async def why(ctx):
    async with ctx.typing():
        await ctx.send(nekos.why())

@bot.command()
async def cat(ctx):
    async with ctx.typing():
        await ctx.send(nekos.cat())
    
bot.run("YOUR TOKEN HERE")