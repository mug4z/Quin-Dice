# Author: Mug4z
# Purpose: Have fun with discord API during the confinement, and made a dice system for the role play game Quin.
# Created date: 11.04.2020
# Todo:
#      Fix the problem, why I can't send commands[done]
#      Add the bonus[done] and malus [done] on roll dices
#      add absolute value for eliminate negative number
#      add critcal fail and suceed [done]
#      add roll details [done]
#      add help command [done]
#      add clean features [done]
      
import random
import discord
from discord.ext import commands
#----Variables----#
# This line, enable the same features of discor.client
client = commands.Bot(command_prefix = '$')

#Remove the default help command
client.remove_command('help')
#----Class----#

#----Functions----#
def quinRolleDice():
    d10Dice = random.randint(0, 9)
    d10Dice2 = random.randint(0, 9)

    if d10Dice == 0 and d10Dice2 == 0:
        resultDice = "Echec critique"
    elif d10Dice == d10Dice2:
        resultDice = "Réussite critique"
    else:
        resultDice = abs(d10Dice - d10Dice2)
    return resultDice, d10Dice, d10Dice2

#---Commands---#
@client.command()
async def roll(ctx, *args):
    diceRolled = quinRolleDice()
    firstDice = diceRolled[1]
    secondDice = diceRolled[2]
    resutlDice = diceRolled[0]
    author = ctx.message.author

    if author.nick == None:
        authorName = author.name
    else:
        authorName = author.nick

    if resutlDice == "Echec critique" or resutlDice == "Réussite critique":
        formatedString = "{}: {}[{}],[{}]".format(authorName, resutlDice, firstDice, secondDice)
    if "bonus" in args:
        bonus = int(args[1])
        finalResult = resutlDice + bonus
        formatedString = ("{} roll [{}][{}] your result [{}]").format(authorName, firstDice, secondDice, finalResult)    
    elif "malus" in args:
        malus  = int(args[1])
        finalResult = resutlDice - malus
        formatedString = ("{} roll [{}][{}] your result [{}]").format(authorName, firstDice, secondDice, finalResult)

    await ctx.send(formatedString)

@client.command()
async def cleanRoll(ctx, amount=11):
    channel = ctx.message.channel
    
    await channel.purge(limit=amount)


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help menu",description="There are the description of the commands")
    embed.add_field(name="$help", value="Show this help")
    embed.add_field(name="$roll bonus [number]", value="Roll your dices with a bonus, ex: $roll bonus 4")
    embed.add_field(name="$roll malus [number]", value="Roll your dices with a malus, ex: $roll malus 4")
    embed.add_field(name="$cleanRoll number", value="Remove the last specified number of message the default value is 10, ex: $cleanRoll 11")
    
    await ctx.send(embed=embed)

client.run('BOT TOKEN')
