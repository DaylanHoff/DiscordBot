tsnumber = 1
fivemnumber = 3
onsetnumber = 1
launchernumber = 3
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



@bot.event
async def on_ready():
 print('\n\nLogged in as: {} - {}\nVersion: {}\n'.format(bot.user.name, bot.user.id, discord.__version__))
 print('Running up and ready. Let the roleplay begin')
 await bot.change_presence(activity=discord.Streaming(name='Roleplay Studios | rps?', url="https://www.twitch.tv/roleplaystudios", details="The Kaboolian Family"))
 bot.load_extension("Music")
 bot.load_extension("Fun")


@bot.event
async def on_reaction_add(reaction, user):
    #list = [595412610174943253, 595412697529450496, 171802480592683008, 595412567288053770]
    if user.id == 638052252946530304:
        return
    if reaction.message.channel.id == 597125972843823115:
        if reaction.message.author.id == user.id:
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



#    for role in user.roles:
#        if role.id in list:
#            for roled in reaction.message.author.roles:
#                if roled.id in list:
#                    return print("Tried to use a reaction on a moderator/admin")
#                if str(reaction.emoji) == "<:kick:644657283728408597>":
#                    channel = bot.get_channel(642537511406796801)
#                    await reaction.message.author.kick()
#                    await reaction.message.channel.send(f"Kicked, {reaction.message.author.mention}")
#                    await reaction.message.delete()
#                    embed = discord.Embed(colour=discord.Colour(0xe27962), description=f"**Staff Kicked Member**\n\nMessage Content:```\n{reaction.message.content}```\n\n **Staff Member:** {user.mention} \n**Kicked:** {reaction.message.author.mention}")
#                    await channel.send(embed=embed)
#                if str(reaction.emoji) == "<:ban:644657283103588363>":
#                    channel = bot.get_channel(642537511406796801)
#                    await reaction.message.author.ban()
#                    await reaction.message.channel.send(f"Banned, {reaction.message.author.mention}")
#                    embed = discord.Embed(colour=discord.Colour(0xe27962), description=f"**Staff Banned Member**\n\nMessage Content:```\n{reaction.message.content}```\n\n **Staff Member:** {user.mention} \n**Banned:** {reaction.message.author.mention}")
#                    await channel.send(embed=embed)




@bot.event
async def on_message_delete(message):
    if message.author.id == 638052252946530304:
        return print("Delete - Was the bot")
    if message.channel.id == 641072466760040488:
        return print("Delete - Was the bot commands channel")
    if message.guild.id == 594321081519702026:
        channel = bot.get_channel(642537511406796801)
        embed = discord.Embed(colour=discord.Colour(0xe27962), description=f"**Message Deleted**\n\n Message:```\n{message.content}```\nMessage Owner: {message.author.mention}")
        return await channel.send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    if before.author.id == 638052252946530304:
        return print("Edit - This was the bot status")
    if before.author.bot == True:
        return print("Edit - I found a bot editing a message")
    if before.guild.id == 594321081519702026:
        channel = bot.get_channel(642537511406796801)
        embed = discord.Embed(colour=discord.Colour(0xe27962), description=f"**Edit Messages**\n\n User: {before.author.mention} Before:```\n{before.content}``` \nAfter:```\n{after.content}```")
        return await channel.send(embed=embed)

@bot.event
async def on_member_ban(guild, user):
    if guild.id == 594321081519702026:
        channel = bot.get_channel(642537511406796801)
        embed = discord.Embed(colour=discord.Colour(0xe27962), description=f"**Server - Ban List Updated**\n\n {user.name} was recently banned")
        return await channel.send(embed=embed)

@bot.event
async def on_member_unban(guild, user):
    if guild.id == 594321081519702026:
        channel = bot.get_channel(642537511406796801)
        embed = discord.Embed(colour=discord.Colour(0xe27962), description=f"**Server - Unban Updated**\n\n {user.name} was recenly unbanned")
        return await channel.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id) # RPS
    user = await guild.fetch_member(payload.user_id) # MEMBER IN GUILD FETCH
    if payload.message_id == 667127345869488139:
        guild = bot.get_guild(594321081519702026) # GET GUILD
        botcommands = bot.get_channel(642537511406796801) # CHANNEL TO LOG
        onsetrole = discord.utils.get(guild.roles, id=667117783917789189) # ROLE
        await user.add_roles(onsetrole)
        await botcommands.send(f"Added `{user.name}`, `Onset` Role")    
        return
    if payload.message_id == 667127450861436950:
        guild = bot.get_guild(594321081519702026) # RPS
        botcommands = bot.get_channel(642537511406796801) # CHANNEL TO LOG
        fivemrole = discord.utils.get(guild.roles, id=667117649737678878) # ROLE
        await user.add_roles(fivemrole)
        await botcommands.send(f"Added `{user.name}`, `Five M` Role")    
        return
        ########     Factions Discord #########
    if payload.message_id == 672212222172463134:
        guild = bot.get_guild(668749673863053323) # RPS FACTION
        verification = bot.get_channel(668983182867300359) # Verification Channel
        embed = discord.Embed(colour=discord.Colour(0xFFA500), description=f"**New Verification Request**\n\n User: {user.mention} \nRole Requested:\n**Onset Police Role** \n\n**To approve run rps?role onset-police {user.id}**")
        await verification.send(embed=embed)
        await user.send("We have recieved your role request for `Onset Police` and will get to it soon! I'll notify you when you have been given the role")           
    if payload.message_id == 672212228547543051:
        guild = bot.get_guild(668749673863053323) # RPS FACTION
        verification = bot.get_channel(668983182867300359) # Verification Channel
        embed = discord.Embed(colour=discord.Colour(0xFFA500), description=f"**New Verification Request**\n\n User: {user.mention} \nRole Requested:\n**Onset EMS Role** \n\n**To approve run rps?role onset-ems {user.id}**")
        await verification.send(embed=embed)
        await user.send("We have recieved your role request for `Onset EMS` and will get to it soon! I'll notify you when you have been given the role")            
    if payload.message_id == 672212231643201538:
        guild = bot.get_guild(668749673863053323) # RPS FACTION
        verification = bot.get_channel(668983182867300359) # Verification Channel
        embed = discord.Embed(colour=discord.Colour(0xFFA500), description=f"**New Verification Request**\n\n User: {user.mention} \nRole Requested:\n**FiveM Police Role** \n\n**To approve run rps?role fivem-police {user.id}**")
        await verification.send(embed=embed)
        await user.send("We have recieved your role request for `FiveM Police` and will get to it soon! I'll notify you when you have been given the role")        
    if payload.message_id == 672212249372393522:
        guild = bot.get_guild(668749673863053323) # RPS FACTION
        verification = bot.get_channel(668983182867300359) # Verification Channel
        embed = discord.Embed(colour=discord.Colour(0xFFA500), description=f"**New Verification Request**\n\n User: {user.mention} \nRole Requested:\n**FiveM EMS Role** \n\n**To approve run rps?role fivem-ems {user.id}**")
        await verification.send(embed=embed)
        await user.send("We have recieved your role request for `FiveM EMS` and will get to it soon! I'll notify you when you have been given the role")
    if payload.user_id == 638052252946530304:
        
        return



@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 667127450861436950:
        guild = bot.get_guild(594321081519702026) # GET GUILD
        user = await guild.fetch_member(payload.user_id) # MEMBER IN GUILD FETCH
        botcommands = bot.get_channel(642537511406796801) # CHANNEL TO LOG
        fivemrole = discord.utils.get(guild.roles, id=667117649737678878) # ROLE
        await user.remove_roles(fivemrole)
        await botcommands.send(f"Removed `{user.name}`, `Five M` Role")
        return
    if payload.message_id == 667127345869488139:
        guild = bot.get_guild(594321081519702026) # GET GUILD
        user = await guild.fetch_member(payload.user_id) # MEMBER IN GUILD FETCH
        botcommands = bot.get_channel(642537511406796801) # CHANNEL TO LOG
        onsetrole = discord.utils.get(guild.roles, id=667117783917789189) # ROLE
        await user.remove_roles(onsetrole)
        await botcommands.send(f"Removed `{user.name}`, `Onset` Role")
        return
    if payload.user_id == 638052252946530304:
         return

@bot.event
async def on_message(message):
    if message.channel.id == 641072466760040488:
        await message.delete(delay=30)
    if message.channel.id == 615020786973016083:
        await message.delete()                
    if message.channel.id == 597125972843823115:
        await message.add_reaction("🔢")
        await message.add_reaction("👍")
        await message.add_reaction("⬆️")
        await message.add_reaction("❌")
    if message.channel.id == 668983182867300359:
        await message.delete(delay=86400)
    if message.channel.id == 668983820330205205:
        await message.delete(delay=86400)
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
        draw.text((175, 120), "Check out #rules & #faq", (169, 169, 169), font=font3) #draws the Username of the userrps?test

        img.save('welcome.png')

        channel1 = bot.get_channel(594326525914906626) # Andrews Server
        await channel1.send(file=discord.File('welcome.png')) # Andrews server
    else:
        return


@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour(0xe7fdff), description="**Roleplay Studios Bot** \n *Here are all of my commands:*\n[--> Click here to visit our website <--](https://roleplaystudios.co/)")

    embed.set_thumbnail(url="https://roleplaystudios.co/forums/uploads/monthly_2020_01/982392141_RPSForumsLogo.png.6197f824bec884e42737cc2c5452c1fb.png")
    embed.set_footer(text="Roleplay Studio's Bot")

    embed.add_field(name="<:Fun:641659009279197203> Fun Commands", value="**rps?meme** - *Random Memes*\n**rps?urban** - *Search urban dictionary* \n**rps?coinflip** - *Flips a coin for you* \n <:New:641664980122468373> **rps?avatar** - *Creates a Roleplay Studios Avatar for you*")
    embed.add_field(name="<:Music:641659009236992030> Music Commands", value="**rps?play** - *Play's your requested music* \n**rps?skip** - *Skips the current song* \n**rps?queue** - *Displays the queue of music* \n**rps?volume** - *5% - 100% changes volume* \n**rps?stop** - *Stops playing music* \n**rps?now** - *Displays current playing songng song")
    embed.add_field(name="<:Utility:641659008905773057> Other Commands", value="**rps?site** - *Gives you our site* \n**rps?links** - *Gives you useful links* \n**rps?factions** - *Links to faction applications* \n**rps?ping** - *Displays bot latency*")

    await ctx.send(embed=embed)




@bot.command()
async def role(ctx, faction : str = None, member : int = None):
    logs = bot.get_channel(668953672893333511)
    role = discord.utils.find(lambda r: r.name == 'Role-Giver', ctx.message.guild.roles)
    guild = bot.get_guild(668749673863053323) # RPS FACTION
    if role in ctx.message.author.roles:
        if faction is None:
            await ctx.send("You need to specify a faction (onset-ems/police, fivem-ems/police)")
        if member is None:
            await ctx.send("Please specify an ID (right click them and click copy ID)")
        if faction == "fivem-police":
            user = await ctx.guild.fetch_member(member)
            rpspolice = discord.utils.get(guild.roles, id=672264626586779658) # FiveM Police
            await logs.send(f"Given role to `{user.name}``, Role was `FiveM Police`")
            await user.add_roles(rpspolice)
            await ctx.send(f"Given role to `{user.name}`, Role was `FiveM Police`")   
            await user.send("Hey, Just so you're aware your `Fivem Police role` request was accepted and is given to you")              
        if faction == "fivem-ems":
            user = await ctx.guild.fetch_member(member)
            rpspolice = discord.utils.get(guild.roles, id=672264711034765323) # FiveM EMS
            await logs.send(f"Given role to `{user.name}`, Role was `FiveM EMS`")
            await user.add_roles(rpspolice)
            await ctx.send(f"Given role to `{user.name}`, Role was `FiveM EMS`")     
            await user.send("Hey, Just so you're aware your `Fivem EMS role` request was accepted and is given to you")  
        if faction == "onset-police":
            user = await ctx.guild.fetch_member(member)
            rpspolice = discord.utils.get(guild.roles, id=668953470262575114) # ONSET POLICE
            await logs.send(f"Given role to `{user.name}`, Role was `Onset Police`")
            await user.add_roles(rpspolice)
            await ctx.send(f"Given role to `{user.name}`, Role was `Onset Police`")
            await user.send("Hey, Just so you're aware your Onset `Police role` request was accepted and is given to you")             
        if faction == "onset-ems":
            user = await ctx.guild.fetch_member(member)
            rpspolice = discord.utils.get(guild.roles, id=668953469163536415) # ONSET EMS
            await logs.send(f"Given role to `{user.name}`, Role was `Onset EMS`")
            await user.add_roles(rpspolice)
            await ctx.send(f"Given role to `{user.name}`, Role was `Onset EMS`")
            await user.send("Hey, Just so you're aware your `Onset EMS` role request was accepted and is given to you")
    else:
        await ctx.send("Only command can use this")

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
async def muted(ctx, member : discord.Member):
    if ctx.author.id == 195933799857520640:
        guild = bot.get_guild(594321081519702026) # GET GUILD
        remove = discord.utils.get(guild.roles, id=595462230921707530) # ROLE
        await member.remove_roles(remove)
        await ctx.send("Removed Role")
    else:
        await ctx.send("Nope")



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

@bot.command()
async def teamspeak(ctx, numberts:int = None):
    """Changes Status | rps?teamspeak"""
    if ctx.author.id == 171802480592683008:
        global tsnumber
        if numberts is None:
            await ctx.send("Usage: rps?teamspeak 1 (online), 2 (offline), 3 of (Developer)")
        if numberts is 1:
            tsnumber = 1
            await ctx.send("Set to Online")
        if numberts is 2:
            tsnumber = 2
            await ctx.send("Set to Offline")
        if numberts is 3:
            tsnumber = 3
            await ctx.send("Set to In Dev")
    else:
        await ctx.send("Nope you can't use this")


@bot.command()
async def fivem(ctx, numberts:int = None):
    """Changes Status | rps?fivem"""
    if ctx.author.id == 171802480592683008:
        global fivemnumber
        if numberts is None:
            await ctx.send("Usage: rps?fivem 1 (online), 2 (offline), 3 of (Developer)")
        if numberts is 1:
            fivemnumber = 1
        if numberts is 2:
            fivemnumber = 2
        if numberts is 3:
            fivemnumber = 3
    else:
        await ctx.send("Nope you can't use this")

@bot.command()
async def onset(ctx, numberts:int = None):
    """Changes Status | rps?onset"""
    if ctx.author.id == 171802480592683008:
        global onsetnumber
        if numberts is None:
            await ctx.send("Usage: rps?onset 1 (online), 2 (offline), 3 of (Developer)")
        if numberts is 1:
            onsetnumber = 1
        if numberts is 2:
            onsetnumber = 2
        if numberts is 3:
            onsetnumber = 3
    else:
        await ctx.send("Nope you can't use this")

@bot.command()
async def launcher(ctx, numberts:int = None):
    """Changes Status | rps?launcher"""
    if ctx.author.id == 171802480592683008:
        global launchernumber
        if numberts is None:
            await ctx.send("Usage: rps?launcher 1 (online), 2 (offline), 3 of (Developer)")
        if numberts is 1:
            launchernumber = 1
        if numberts is 2:
            launchernumber = 2
        if numberts is 3:
            launchernumber = 3
    else:
        await ctx.send("Nope you can't use this")

    

async def checkstatus():
    await bot.wait_until_ready()
    channel = bot.get_channel(615020786973016083) # CHANNEL TO LOG
    message = await channel.fetch_message(642507454885789697)
    while not bot.is_closed():
        print("changedstatus")
        embed = discord.Embed(description="**Roleplay Studios Service Status** \nThis refreshes every 60s \nAny updates on the status itself may be announced here", color = 0xE7FDFF)
        embed.set_thumbnail(url="https://roleplaystudios.co/forums/uploads/monthly_2019_10/748346039_RPSForumsLogo.png.ca2169fd3d30240513e882003a2aaf72.png")
        # HOMEPAGE
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
                    embed.add_field(name = 'FireRescue Database', value="<:offline:615021855258050576> Offline") # FIRE RESCUE
        async with aiohttp.ClientSession() as session:
            async with session.get('https://roleplaystudios.co/firerescue/login.php') as resp:             
                if tsnumber == 1:
                    embed.add_field(name = 'Teamspeak', value="<:online:615021855585206282> Online")
                if tsnumber == 2:
                    embed.add_field(name = 'Teamspeak', value="<:offline:615021855258050576> Offline") 
                if tsnumber == 3:
                    embed.add_field(name = 'Teamspeak', value="🚧 Dev Only")
                if fivemnumber == 1:
                    embed.add_field(name = 'FiveM Server', value="<:online:615021855585206282> Online")
                if fivemnumber == 2:
                    embed.add_field(name = 'FiveM Server', value="<:offline:615021855258050576> Offline") 
                if fivemnumber == 3:
                    embed.add_field(name = 'FiveM Server', value="🚧 Dev Only")   
                if onsetnumber == 1:
                    embed.add_field(name = 'Onset Server', value="<:online:615021855585206282> Online")
                if onsetnumber == 2:
                    embed.add_field(name = 'Onset Server', value="<:offline:615021855258050576> Offline") 
                if onsetnumber == 3:
                    embed.add_field(name = 'Onset Server', value="🚧 Dev Only")  
                if launchernumber == 1:
                    embed.add_field(name = 'Launcher Server', value="<:online:615021855585206282> Online")
                if launchernumber == 2:
                    embed.add_field(name = 'Launcher Server', value="<:offline:615021855258050576> Offline") 
                if launchernumber == 3:
                    embed.add_field(name = 'Launcher Server', value="🚧 Dev Only")             
        await message.edit(embed=embed)
        await asyncio.sleep(60)

bot.loop.create_task(checkstatus())
bot.run(token)
