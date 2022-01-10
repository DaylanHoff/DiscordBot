import discord
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
import traceback
import sys
import asyncio
import os
import aiohttp


## Loads of imports

with open("token.txt", 'r') as f:
    token = f.read().strip('\n')


description = '''Roleplay Studios Moderation Bot!'''
bot = commands.Bot(command_prefix='rps?', description=description)
bot.remove_command('help')
bot_bannedwords = ['nigger', 'cunt', 'fuck', 'shit', 'nig', 'nigga', 'furries', 'furrie', 'retard', 'spick', 'chink', 'fag', 'twat', 'your mom', 'fanny', 'your funny']

@bot.event
async def on_ready():
 print('\n\nLogged in as: {} - {}\nVersion: {}\n'.format(bot.user.name, bot.user.id, discord.__version__))
 print('Running up and ready. Let the roleplay begin')
 await bot.change_presence(activity=discord.Game(type=1, name='alongside the players | rps?'))
 bot.load_extension("Music")
 bot.load_extension("Fun")


@bot.event
async def on_reaction_add(reaction, user):
    if user.id == 638052252946530304:
        return
    if reaction.message.channel.id == 597125972843823115:
        if reaction.message.author.id == reaction.message.author.id:
            if reaction.emoji == "❌":
                await reaction.message.clear_reactions()
            if reaction.emoji == "🔢":
                await reaction.message.clear_reactions()
                await reaction.message.add_reaction("1\N{combining enclosing keycap}")
                await reaction.message.add_reaction("2\N{combining enclosing keycap}")
                await reaction.message.add_reaction("3\N{combining enclosing keycap}")
                await reaction.message.add_reaction("4\N{combining enclosing keycap}")
            if reaction.emoji == "👍":
                await reaction.message.clear_reactions()
                await reaction.message.add_reaction("👍")
                await reaction.message.add_reaction("👎")
            if reaction.emoji == "⬆️":
                await reaction.message.clear_reactions()
                await reaction.message.add_reaction("⬆️")
                await reaction.message.add_reaction("⬇️")





@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id) # GET GUILD
    user = await guild.fetch_member(payload.user_id) # MEMBER IN GUILD FETCH
    channel = bot.get_channel(payload.channel_id) # CHANNEL DONE IN
    if payload.message_id == 633672568502485023:
        guild = bot.get_guild(594321081519702026) # GET GUILD
        botcommands = bot.get_channel(641072466760040488) # CHANNEL TO LOG
        veteranrole = discord.utils.get(guild.roles, id=633671142598639617) # ROLE
        await user.add_roles(veteranrole)
        await botcommands.send(f"Added `{user.name}`, `Veteran` Role")
        return
    if payload.user_id == 638052252946530304:
        return



@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 633672568502485023:
        guild = bot.get_guild(594321081519702026) # GET GUILD
        user = await guild.fetch_member(payload.user_id) # MEMBER IN GUILD FETCH
        channel = bot.get_channel(payload.channel_id) # CHANNEL DONE IN
        botcommands = bot.get_channel(641072466760040488) # CHANNEL TO LOG
        veteranrole = discord.utils.get(guild.roles, id=633671142598639617) # ROLE
        await user.remove_roles(veteranrole)
        await botcommands.send(f"Removed `{user.name}`, `Veteran` Role")
        return


@bot.event
async def on_message(message):
    if message.guild.id == 594321081519702026:
        if "<@&595427405305348248>" in message.content: # Developer
            await message.delete()
            await message.channel.send(f'This role is not to be contacted, Any member who posses these role(s) tag is considered Strict Do Not Disturb unless told otherwise., {message.author.mention}')
        if "<@&595412411897348101>" in message.content: # Project Lead
            await message.delete()
            await message.channel.send(f'This role is not to be contacted, Any member who posses these role(s) tag is considered Strict Do Not Disturb unless told otherwise., {message.author.mention}')
        if"<@&595412567288053770>" in message.content: # Project Manager
            await message.delete()
            await message.channel.send(f'This role is not to be contacted, Any member who posses these role(s) tag is considered Strict Do Not Disturb unless told otherwise., {message.author.mention}')
        if message.channel.id == 641072466760040488:
            await message.delete(delay=30)
        if message.channel.id == 597125972843823115:
            await message.add_reaction("🔢")
            await message.add_reaction("👍")
            await message.add_reaction("⬆️")
            await message.add_reaction("❌")
    await bot.process_commands(message)



@bot.event
async def on_member_join(member):
    if member.guild.id == 594321081519702026:
        user = member
        img = Image.open("template.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("American_Captain.ttf", 35) #Make sure you insert a valid font from your folder.
        font2 = ImageFont.truetype("American_Captain.ttf", 26) #Make sure you insert a valid font from your folder.
        font3 = ImageFont.truetype("American_Captain.ttf", 22) #Make sure you insert a valid font from your folder.
        #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
        draw.text((175, 20), "Welcome, \n {}".format(user.name), (255, 255, 255), font=font) #draws the Username of the user
        draw.text((175, 95), "You are member #{}".format(len(user.guild.members)), (255, 255, 255), font=font2) #draws the Username of the userrps?test
        draw.text((175, 120), "Check out #rules & #faq".format(len(user.guild.members)), (169, 169, 169), font=font3) #draws the Username of the userrps?test

        img.save('welcome.png')
        channel = bot.get_channel(637759427172237312) # My Server
        channel1 = bot.get_channel(594326525914906626) # Andrews Server
        await channel.send(file=discord.File('welcome.png')) # My server
        await channel1.send(file=discord.File('welcome.png')) # Andrews server
    else:
        return


@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour(0xe7fdff), description="**Roleplay Studios Bot** \n *Here are all of my commands:*\n[--> Click here to visit our website <--](https://roleplaystudios.co/)")

    embed.set_thumbnail(url="https://roleplaystudios.co/forums/uploads/monthly_2019_10/748346039_RPSForumsLogo.png.ca2169fd3d30240513e882003a2aaf72.png")
    embed.set_footer(text="Roleplay Studio's Bot")

    embed.add_field(name="<:Fun:641659009279197203> Fun Commands", value="**rps?meme** - *Random Memes*\n**rps?urban** - *Search urban dictionary* \n**rps?coinflip** - *Flips a coin for you* \n <:New:641664980122468373> **rps?avatar** - *Creates a Roleplay Studios Avatar for you*")
    embed.add_field(name="<:Music:641659009236992030> Music Commands", value="**rps?play** - *Play's your requested music* \n**rps?skip** - *Skips the current song* \n**rps?queue** - *Displays the queue of music* \n**rps?volume** - *5% - 100% changes volume* \n**rps?stop** - *Stops playing music* \n**rps?now** - *Displays current playing song*")
    embed.add_field(name="<:Utility:641659008905773057> Other Commands", value="**rps?site** - *Gives you our site* \n**rps?links** - *Gives you useful links* \n**rps?factions** - *Links to faction applications* \n**rps?ping** - *Displays bot latency*")

    await ctx.send(embed=embed)



@bot.command()
async def avatar(ctx):
    """Support RPS by creating your own avatar! | rps?avatar"""


    with requests.get(ctx.message.author.avatar_url) as r:
        img_data = r.content
    with open('image_name.png', 'wb') as handler:
        handler.write(img_data)


    img = Image.open('image_name.png') # image extension *.png,*.jpg
    new_width  = 400
    new_height = 400
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save('image_namee.png') # format may what u want ,*.png,*jpg,*.gif
    background = Image.open("image_namee.png")
    foreground = Image.open("cicle.png")

    background.paste(foreground, (0, 0), foreground)
    background.save("finished.png")
    embed=discord.Embed(color=0xe03445, description="Here's your avatar")
    file = discord.File("finished.png", filename="finished.png")
    embed.set_image(url="attachment://finished.png")
    embed.set_footer(text="Roleplay Studios")
    author = ctx.message.author
    await ctx.send(file=file, embed=embed)

@bot.command(hidden=True, aliases=['purge', 'Purge', 'Clear'])
@commands.has_permissions(manage_emojis=True)
async def clear(ctx, number):
    if number is None:
        number = 100
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    number = number + 1
    channel = ctx.message.channel
    async for x in channel.history(limit=number):
        mgs.append(x)
    await channel.delete_messages(mgs)
    await ctx.send(f"<:rps:617169327736619113> | Deleted {number} of messages")



@bot.command()
async def danclear(ctx, number):
    if ctx.author.id == 195933799857520640:
        if number is None:
            number = 100
        mgs = [] #Empty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        number = number + 1
        channel = ctx.message.channel
        async for x in channel.history(limit=number):
            mgs.append(x)
        await channel.delete_messages(mgs)
        deleteafter = await ctx.send(f"<:rps:617169327736619113> | Deleted {number} of messages")
        await deleteafter.delete(delay=10)
    else:
        await ctx.send("Nope")

@bot.command()
async def ping(ctx):
    """Displays bot latency | rps?ping """
    await ctx.send('<:rps:617169327736619113> | 🏓 Pong! {0}'.format(round(bot.latency, 1)))

async def checkstatus():
    await bot.wait_until_ready()
    channel = bot.get_channel(615020786973016083) # CHANNEL TO LOG
    message = await channel.fetch_message(642507454885789697)
    while not bot.is_closed():
        embed = discord.Embed(description="**Roleplay Studios Service Status** \nThis refreshes every 90s \n<:online:615021855585206282> - Online \n<:idle:615021855480479755> - In Progress \n<:offline:615021855258050576> - Offline \n<:restrictedacess:642500737192165407> - Online Developer Only", color = 0xE7FDFF)
        embed.set_thumbnail(url="https://roleplaystudios.co/forums/uploads/monthly_2019_10/748346039_RPSForumsLogo.png.ca2169fd3d30240513e882003a2aaf72.png")
        async with aiohttp.ClientSession() as session:
            async with session.get('https://home.roleplaystudios.co/') as resp:
                if resp.status == 200:
                    embed.add_field(name = 'Homepage:', value="<:online:615021855585206282> Online")
                else:
                    embed.add_field(name = 'Homepage:', value="<:offline:615021855258050576> Offline") # Homepage
        async with aiohttp.ClientSession() as session:
            async with session.get('https://roleplaystudios.co/forums') as resp:
                if resp.status == 200:
                    embed.add_field(name = 'Forums', value="<:online:615021855585206282> Online")
                else:
                    embed.add_field(name = 'Forums', value="<:offline:615021855258050576> Offline") # Forums
        async with aiohttp.ClientSession() as session:
            async with session.get('https://roleplaystudios.co/police/login.php') as resp:
                if resp.status == 200:
                    embed.add_field(name = 'Police Database', value="<:online:615021855585206282> Online")
                else:
                    embed.add_field(name = 'Police Database', value="<:offline:615021855258050576> Offline") # Police
        async with aiohttp.ClientSession() as session:
            async with session.get('https://roleplaystudios.co/firerescue/login.php') as resp:
                if resp.status == 200:
                    embed.add_field(name = 'FireRescue Database', value="<:online:615021855585206282> Online")
                else:
                    embed.add_field(name = 'FireRescue Database', value="<:offline:615021855258050576> Offline")
#        async with aiohttp.ClientSession() as session:
#            async with session.get('http://ts.roleplaystudios.co/') as resp:
#                if resp.status == 200:
#                    embed.add_field(name = 'Teamspeak', value="<:online:615021855585206282> Online")
#                else:
        embed.add_field(name = 'Teamspeak', value="<:restrictedacess:642500737192165407> Dev Only")
        async with aiohttp.ClientSession() as session:
            async with session.get('http://play.roleplaystudios.co/') as resp:
                if resp.status == 200:
                    embed.add_field(name = 'Game Server', value="<:restrictedacess:642500737192165407> Online - Dev Only")
                else:
                    embed.add_field(name = 'Game Server', value="<:offline:615021855258050576> Offline")
        embed.add_field(name = 'RPS Discord', value="<:online:615021855585206282> Online")
        embed.add_field(name = 'RPS Police Discord', value="<:online:615021855585206282> Online")
        embed.add_field(name = 'RPS FireRescue Discord', value="<:online:615021855585206282> Online")
        embed.add_field(name = 'Launcher', value="<:restrictedacess:642500737192165407> Dev Only")
        await message.edit(embed=embed)
        await asyncio.sleep(90)

bot.loop.create_task(checkstatus())
bot.run(token)
