
import discord
from discord.ext import commands
import json
import aiohttp
import ksoftapi
import requests
import random
import asyncio

client = ksoftapi.Client(api_key="ca62a6c4afbf8da590f42c0b38a35e6e272eb7e3")


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot






    @commands.command()
    async def urban(self, ctx, *, msg: str):
        """rps?urban word | Searches urbandictionary"""
        author = ctx.message.author
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        response = requests.get(api, params=[("term", word)]).json()

        if len(response["list"]) == 0: return await ctx.send("Could not find that word!")

        embed = discord.Embed(title = ":mag: Search Word", description = word, color = 0xE7FDFF)
        embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
        embed.add_field(name = "Examples:", value = response['list'][0]["example"])

        await ctx.send(embed=embed)


    @commands.command()
    async def coinflip(self, ctx):
        choice = random.randint(1,2)
        fliping=discord.Embed(title="Flipping the coin..", color=0xE7FDFF)
        fliping.set_author(name="Roleplay Studio's", icon_url='https://roleplaystudios.co/forums/uploads/monthly_2019_10/748346039_RPSForumsLogo.png.ca2169fd3d30240513e882003a2aaf72.png')
        fliping.set_thumbnail(url='https://media.tenor.com/images/938e1fc4fcf2e136855fd0e83b1e8a5f/tenor.gif')
        fliping.set_footer(text="Roleplay Studios")
        fliper = await ctx.send(embed=fliping)
        await asyncio.sleep(5)
        if choice == 1:
            embed=discord.Embed(title="Heads or Tails!", description="I scored Heads!", color=0xE7FDFF)
            embed.set_thumbnail(url='https://cdn10.bigcommerce.com/s-4ulzs/products/9592/images/8617/apimlwhnz__54568.1562144789.1280.1280.jpg?c=2')
            embed.set_footer(text="Roleplay Studios")
            await ctx.send(embed=embed)
            await fliper.delete()
        if choice == 2:
            embed=discord.Embed(title="Heads or Tails!", description="I scored Tails!", color=0xE7FDFF)
            embed.set_thumbnail(url='https://i.ebayimg.com/images/g/XSsAAOSwEMxa6IzM/s-l1600.jpg')
            embed.set_footer(text="Roleplay Studios")
            await ctx.send(embed=embed)
            await fliper.delete()

    @commands.command()
    async def site(self, ctx):
        await ctx.send("**Our Sites & Services** \n*Website:* <https://roleplaystudios.co/> \n*Forums:* <https://roleplaystudios.co/forums/> \n*Discord:* <https://roleplaystudios.co/discord/> \n*Teamspeak:* ts.roleplaystudios.co")

    @commands.command()
    async def rules(self, ctx):
        await ctx.send("Hey! You can check out the rules in <#596905961784999979>, or if you're lazy  https://roleplaystudios.co/forums/index.php?/topic/9-roleplay-studios-official-rules/")
        
       
    @commands.command()
    async def links(self, ctx):
        await ctx.send("**Here's some useful links**\n*Website:* <https://roleplaystudios.co/> \n*Been banned? Appeal:* <https://roleplaystudios.co/forums/index.php?/forum/56-ban-appeals/> \n*Report a player:* <https://roleplaystudios.co/forums/index.php?/forum/20-reports/> \n*Compensation Requests:* <https://roleplaystudios.co/forums/index.php?/forum/19-compensation-requests/> \n*Open Applications:* <https://roleplaystudios.co/forums/index.php?/application/>")

    @commands.command()
    async def factions(self, ctx):
        await ctx.send("**Interested in joining a faction?:** \n<:onset:625443721038659584> | *Civilian Forums:* <https://roleplaystudios.co/forums/index.php?/forum/59-civilians/> \n<:rpspolice:628604896911818772> | *Police Department:* <https://roleplaystudios.co/forums/index.php?/forum/50-police-department/> \n<:rpsfifr:628604830046486528> | *Fire & Rescue:* <https://roleplaystudios.co/forums/index.php?/forum/51-fire-and-rescue/>")

def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun Loaded")
