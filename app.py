import discord
from discord.ext import commands
import datetime
import time
from urllib import parse, request
import re
import random
import asyncio

bot = commands.Bot(command_prefix = ';;', description = "This is a Helper Bot")

client = discord.Client()

# Startup
@bot.event
async def on_ready():
    print()
    latency_ = bot.latency * 100
    latency = int(latency_)
    print(f'{bot.user} has connected to Discord. | Latency: {latency}ms')
    print()
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name="You 👀"))

# Command: Helpme
@bot.command()
async def helpme(ctx):
    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)
    embedVar = discord.Embed(title="FriendZone Commands", description="**Prefix: ;;**", color=col_embed)
    embedVar.add_field(name="**__Utility__**", value="`ping, info, echo`", inline=True)
    embedVar.add_field(name="**__Fun__**", value="`pair, lifesim, eball, howdeepis, \n howlongis, who, pics, samiku`", inline=False)
    embedVar.add_field(name="**__Math__**", value="`math, rng`")
    await ctx.send(embed = embedVar)

# Command: Ping
@bot.command()
async def ping(ctx):
    rounded = int(bot.latency * 100)
    await ctx.send("Ping: {}ms".format(rounded))

# Command: Disconnect
@bot.command()
@commands.is_owner()
async def disconnect(ctx):
    await ctx.message.add_reaction("✅")
    await ctx.send("**Disconnected**")
    quit()

# Command: Note
@bot.command()
@commands.is_owner()
async def note(ctx, *, args):
    file_object = open('notes.txt', 'a')
    args_ = args[0].capitalize() + args[1:]
    file_object.write("""- {}
    """.format(args_))
    file_object.close()
    await ctx.message.add_reaction("✅")
    await ctx.send("Note Taken.")

# Command: Viewnotes
@bot.command()
@commands.is_owner()
async def viewnotes(ctx):
    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)
    f = open("notes.txt", "r")
    notes = f.read()
    embedVar = discord.Embed(title="Notes", description="**Enclosed Permissions**", color=col_embed)
    embedVar.add_field(name="**Notes List**", value="{}".format(notes), inline=True)
    await ctx.send(embed = embedVar)

# Command: Pics
@bot.command()
async def pics(ctx):
    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)

    pic_lst = ['https://media.discordapp.net/attachments/736470483863732296/790096810776854558/unknown.png', 
    'https://media.discordapp.net/attachments/788301436718940162/788305006646394890/image0.jpg?width=253&height=472',
    'https://media.discordapp.net/attachments/788301436718940162/788304893416570880/image0.jpg?width=883&height=473',
    'https://media.discordapp.net/attachments/788301436718940162/788304826516897792/image0.jpg?width=883&height=473',
    'https://media.discordapp.net/attachments/788301436718940162/788304820674625546/image1.jpg?width=253&height=472',
    'https://media.discordapp.net/attachments/788301436718940162/788304820448395284/image0.jpg?width=253&height=472',
    'https://media.discordapp.net/attachments/788301436718940162/788302649401278514/image0.jpg?width=253&height=472',
    'https://media.discordapp.net/attachments/788301436718940162/788302674746408990/image0.jpg?width=253&height=472',
    'https://media.discordapp.net/attachments/736470483863732296/790099354634420234/unknown.png',
    'https://media.discordapp.net/attachments/788301436718940162/789651836390342696/image1.jpg?width=253&height=472',
    'https://media.discordapp.net/attachments/736470483863732296/790100380196536330/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/790100472861032478/image0.png',
    'https://media.discordapp.net/attachments/736470483863732296/790100553942302780/image0.png',
    'https://media.discordapp.net/attachments/736470483863732296/790100631716888586/image0.png',
    'https://media.discordapp.net/attachments/736470483863732296/790100826156171264/image0.png',
    'https://media.discordapp.net/attachments/736470483863732296/790100914580750366/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/790100972466601984/image0.png',
    'https://media.discordapp.net/attachments/736470483863732296/790101059246489620/image0.png',
    'https://media.discordapp.net/attachments/736470483863732296/790101499984085052/unknown.png?width=421&height=473']

    pic_rng = random.choice(pic_lst)
    text_lst = ["I'm not crying, you are", "It's just dust in my eyes", "Why am I crying?", "So beautiful", "I can take no more", 
    "I-", "Have you ever seen anything so beautiful?", "I think there's chilli powder in my eyes", "Nostalgia go brr", "*sigh*\n*happy noises*", 
    'Wowow it’s the it girls!', "Heather", "Damn they look fine as hell", "🔥🔥🔥", "Holy Jesus"]
    text_rng = random.choice(text_lst)

    embedVar = discord.Embed(title="Memories Of 2020", description="{}".format(text_rng), color=col_embed)
    embedVar.set_image(url = "{}".format(pic_rng))

    await ctx.send(embed = embedVar)


# Command: Rng
@bot.command()
async def rng(ctx, num1: int):
    rng = random.randint(0, num1)
    await ctx.send(rng)

# Command: Echo
@bot.command(pass_context = True)
async def echo(ctx, channel: discord.TextChannel, *, message):
    await ctx.message.add_reaction("✅")
    await channel.send(message)
    asyncio.sleep(2)
    await ctx.message.delete()

# Command: Math
@bot.command()
async def math(ctx, numOne: float, operator, *, numTwo: float):
    if operator == "*":
        final0 = numOne * numTwo
        final = round(final0, 2)
        await ctx.send(final)
    elif operator == "/":
        final1 = numOne / numTwo
        final = round(final1, 2)
        await ctx.send(final)
    elif operator == "+":
        final2 = numOne + numTwo
        final = round(final2, 2)
        await ctx.send(final)
    elif operator == "-":
        final3 = numOne - numTwo
        final = round(final3, 2)
        await ctx.send(final)

@bot.command()
async def members(ctx):
    members_dict = {
        "Ramika": {
            "Name": "Ramika",
            "ID": 559619749932433430   
        },

        "Dhiya": {
            "Name": "Dhiya",
            "ID": 781782138394640405
        },

        "Samar": {
            "Name": "Samar",
            "ID": 715341277906075748
        },

        "Manuka": {
            "Name": "Manuka",
            "ID": 715333794336604171
        },

        "Tony": {
            "Name": "Tony",
            "ID": 547724260613816321
        },

        "Metheshr": {
            "Name": "Metheshr",
            "ID": 590075581228646410
        },

        "Sunny": {
            "Name": "Sunny",
            "ID": 420475521005125643
        },

        "Ishan": {
            "Name": "Ishan",
            "ID": 539758317011206146
        },

        "Casey": {
            "Name": "Casey",
            "ID": 767289588787707934
        },

        "Harry": {
            "Name": "Harry",
            "ID": 384565568264601600
        },

        "Tikki": {
            "Name": "Tikki",
            "ID": 782840010352754728
        },

        "Ananya": {
            "Name": "Ananya",
            "ID": 774155379633684500
        },

        "Chiku": {
            "Name": "Chiku",
            "ID": 751987568056205383
        },

        "Lily": {
            "Name": "Lily",
            "ID": 750642333594157096
        },

        "Neili": {
            "Name": "Neili",
            "ID": 715345106626150473
        },

        "JasmineB": {
            "Name": "Jasmine Moverley Bonne",
            "ID": 786910780028485642
        },

        "JasmineY": {
            "Name": "Jasmine You",
            "ID": 786198983042531360
        },

        "Hayley": {
            "Name": "Hayley",
            "ID": 761141665578614814
        },

        "Emily": {
            "Name": "Emily",
            "ID": 692200517320966164
        },

        "Micah": {
            "Name": "Micah",
            "ID": 758555021452509205
        }
        }

    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)

    embedVar = discord.Embed(title="The FriendZone", description="**Server Members**", color=col_embed)
    embedVar.add_field(name="**The Communist Party:**", value="""
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    """.format(members_dict['Ramika']['ID'], members_dict['Ramika']['Name'], members_dict['Samar']['ID'],
    members_dict['Samar']['Name'], members_dict['Manuka']['ID'], members_dict['Manuka']['Name'], members_dict['Tony']['ID'], 
    members_dict['Tony']['Name'], members_dict['Dhiya']['ID'], members_dict['Dhiya']['Name'], members_dict['Sunny']['ID'], 
    members_dict['Sunny']['Name'], members_dict['Metheshr']['ID'], members_dict['Metheshr']['Name'], members_dict['Ishan']['ID'], 
    members_dict['Ishan']['Name'], members_dict['Casey']['ID'], members_dict['Casey']['Name'], members_dict['Harry']['ID'], 
    members_dict['Harry']['Name']), inline=True)
    embedVar.add_field(name="**Swaggy Girlies:**", value="""
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    <@{}>: {}
    """.format(members_dict['Tikki']['ID'], members_dict['Tikki']['Name'], members_dict['Neili']['ID'],
    members_dict['Neili']['Name'], members_dict['Chiku']['ID'], members_dict['Chiku']['Name'], members_dict['Lily']['ID'], 
    members_dict['Lily']['Name'], members_dict['Ananya']['ID'], members_dict['Ananya']['Name'], members_dict['JasmineB']['ID'], 
    members_dict['JasmineB']['Name'], members_dict['JasmineY']['ID'], members_dict['JasmineY']['Name'], members_dict['Emily']['ID'], 
    members_dict['Emily']['Name'], members_dict['Micah']['ID'], members_dict['Micah']['Name'], members_dict['Hayley']['ID'], 
    members_dict['Hayley']['Name']), inline=True)

    await ctx.send(embed = embedVar)
    


# Command: Eball
@bot.command()
async def eball(ctx, message):
    lst = ["Yes", "Hell yeah", "Nah", "I Can Sense Something Good!", 
    "Hell Nah Bruh", "Are You Kidding Me?", "That Doesn't Even Have An Answer Lmao", 
    "As I See It, Yes!", "Better Not Tell You Now", "Cannot Predict Now", "Don't Count On It", 
    "Most Likely", "My Reply Is No", "Outlook Good", "Without A Doubt", "100% Yes", "Signs Point To Yes", 
    "Obviously!", "No."]
    rng = random.choice(lst)
    await ctx.send(rng)

# Command: wHO
@bot.command()
async def who(ctx):
    lst = ["Ramika", "Samar", "Manuka", "Ishan", "Sunny", "Harry", "Lily", "Ananya", "Neili", 
    "Chiku", "Tikki", "Jasmine Moverely Bonne", "Metheshr", "Tony", "Micah", "Emily", "Hayley", 
    "Casey"]
    word = ["Defintely Has To Be", "100%", "Bro, It's", "Are You Kidding Me? It is", 
    "It's Truly", "Whithout Hesitation, It's 100%", "Without A Doubt", "It Has To Be", 
    "Smh, Isn't It Obvious That It's", "C'mon, It's 100%"]
    final_w = random.choice(word)
    final = random.choice(lst)
    await ctx.send("{} {}".format(final_w, final))

# Command: Howdeepis
@bot.command()
async def howdeepis(ctx, message):
    lst = ["km", "m", "cm", "mm", "micro metres"]
    rng = random.randint(-100, 1000)
    lst_rng = random.choice(lst)
    await ctx.send("{} {}".format(rng, lst_rng))

# Command: Dm
@commands.is_owner()
@bot.command()
async def dm(ctx, user: discord.User, message):
    await user.send(message)
    await ctx.message.add_reaction("✅")

# Command: Howlongis
@bot.command()
async def howlongis(ctx, message):
    lst = ["km", "m", "cm", "mm", "micro metres"]
    rng = random.randint(-100, 1000)
    lst_rng = random.choice(lst)
    await ctx.send("{} {}".format(rng, lst_rng))

# Command: Info
@bot.command()
async def info(ctx):
    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)
    member_count = ctx.guild.member_count
    roles = " ".join([str('<@&{}>'.format(r.id)) for r in ctx.guild.roles])

    embedVar = discord.Embed(title="The FriendZone", description="**Server Information**", color=col_embed)
    embedVar.add_field(name="Member Count", value="{} Members".format(member_count), inline=True)
    embedVar.add_field(name="Bot", value="**{}**".format(bot.user), inline=True)
    embedVar.add_field(name="Bot Developer", value="<@{}>".format(559619749932433430), inline=True)
    embedVar.add_field(name="Roles", value="{}".format(roles), inline=False)

    await ctx.send(embed = embedVar)

# Comamand: Samiku
@bot.command()
async def samiku(ctx):
    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)

    pic_lst = ['https://media.discordapp.net/attachments/736470483863732296/783273047549018122/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/789996576026263552/unknown.png', 
    'https://media.discordapp.net/attachments/736470483863732296/789996687547826206/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/789996812260999178/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/789996921154175016/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/789996985246679101/unknown.png',
    'https://media.discordapp.net/attachments/736470483863732296/789997229397639168/unknown.png']

    pic_rng = random.choice(pic_lst)
    text_lst = ["I'm not crying, you are", "It's just dust in my eyes", "Why am I crying?", "So beautiful", "I can take no more"]
    text_rng = random.choice(text_lst)

    embedVar = discord.Embed(title="Samiku Wedding", description="{}".format(text_rng), color=col_embed)
    embedVar.set_image(url = "{}".format(pic_rng))

    await ctx.send(embed = embedVar)


# Command: Lifesim
@bot.command()
async def lifesim(ctx, first_name, connect, second_name):
    if connect == 'and':
        colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
            0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
            0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
            0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
            0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
            0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
            0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
            0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
            0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
            0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
        col_embed = random.choice(colorArray)
        await ctx.send("Finding Lifestyle...")
        house_list = ["Mansion", "Single Storey House", "Double Story House", "Apartment", "Forest House", "Castle"]
        places_list = ["Australia", "India", "Japan", "Africa", "America", "Venice", "Italy", "New Zealand", "Spain", "Portugal", "Singapore", "Dubai"]   

        person1 = first_name[0].capitalize() + first_name[1:]
        person2 = second_name[0].capitalize() + second_name[1:]

        child_rng = random.randint(0, 5)
        rel_yr = random.randint(0, 70)
        match_per = random.randint(30, 100)
        co_rng = random.randint(0, len(places_list) - 1)
        ho_rng = random.randint(0, len(house_list) - 1)
        wed_age = random.randint(19, 35)
        d_age = random.randint(70, 100)
        d_age2 = random.randint(70, 100)

        embedVar = discord.Embed(title="Future Life Style", description="**Found match for {} and {}:**".format(person1, person2), color=col_embed)
        embedVar.add_field(name="=========> Results <=========", value = """

            ...

            **Couple:** {} + {}

            **Match Percentage:** {}%

            **Country:** {}

            **House:** {}

            **Children:** {} Children

            **Wedding Age:** {} Years Old
            
            **Relationship Last:** {} Years

            **{}'s Age Of Death:** {} Years Old

            **{}'s Age Of Death:** {} Years Old
            """.format(person1, person2, match_per, places_list[co_rng], house_list[ho_rng], child_rng, wed_age, rel_yr, person1, d_age, person2, d_age2))
        time.sleep(2)
        await ctx.send(embed = embedVar)


# Command: Pair
@bot.command()
async def pair(ctx, member1_, plus, member2_):
    if plus == 'and':
        colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
            0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
            0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
            0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
            0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
            0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
            0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
            0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
            0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
            0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
        col_embed = random.choice(colorArray)

        member1 = member1_[0].capitalize() + member1_[1:]
        member2 = member2_[0].capitalize() + member2_[1:]

        low = 45
        love_per = random.randint(low, 100)
        love_ro = int(round(love_per / 2))
        l_bar = ["|"] * love_ro
        trust_per = random.randint(low, 100)
        t_ro = int(round(trust_per / 2))
        t_bar = ["|"] * t_ro
        communications_per = random.randint(low, 100)
        c_ro = int(round(communications_per / 2))
        c_bar = ["|"] * c_ro
        values_per = random.randint(low, 100)
        v_ro = int(round(values_per / 2))
        v_bar = ["|"] * v_ro
        emotions_per = random.randint(low, 100)
        e_ro = int(round(emotions_per / 2))
        e_bar = ["|"] * e_ro
        sharedactivities_per = random.randint(low, 100)
        s_ro = int(round(sharedactivities_per / 2))
        s_bar = ["|"] * s_ro

        summary_per_a = (love_per + trust_per + communications_per + values_per + emotions_per + sharedactivities_per) / 6

        per_bar = "|________________________________________________|"
        summary_per = round(summary_per_a, 2)

        embedVar = discord.Embed(title="Found Match", description="**Found match for {} and {}:**".format(member1, member2), color=col_embed)
        embedVar.add_field(name="Match", value="""Couple: {} + {}

        Love: {}% 

         `{}`
        `{}`
        
        Trust: {}%

         `{}`
        `{}`

        Communications: {}%

         `{}`
        `{}`

        Values: {}%

         `{}`
        `{}`

        Emotions: {}%

         `{}`
        `{}`
        
        Shared Activities: {}%

         `{}`
        `{}`
        

           -------------------> [Summary: {}%] <-------------------
        """.format(member1, member2, love_per, "".join(l_bar), per_bar, trust_per, "".join(t_bar), per_bar, 
        communications_per, "".join(c_bar), per_bar, values_per, "".join(v_bar), per_bar, emotions_per, "".join(e_bar), 
        per_bar, sharedactivities_per, "".join(s_bar), per_bar, summary_per)
, inline=False)

        await ctx.send("Finding Match...")
        time.sleep(3)
        await ctx.send(embed = embedVar)


# Command: Code
@bot.command()
async def code(ctx, code):
    colorArray = [0xFF6633, 0xFFB399, 0xFF33FF, 0xFFFF99, 0x00B3E6, 
        0xE6B333, 0x3366E6, 0x999966, 0x99FF99, 0xB34D4D,
        0x80B300, 0x809900, 0xE6B3B3, 0x6680B3, 0x66991A, 
        0xFF99E6, 0xCCFF1A, 0xFF1A66, 0xE6331A, 0x33FFCC,
        0x66994D, 0xB366CC, 0x4D8000, 0xB33300, 0xCC80CC, 
        0x66664D, 0x991AFF, 0xE666FF, 0x4DB3FF, 0x1AB399,
        0xE666B3, 0x33991A, 0xCC9999, 0xB3B31A, 0x00E680, 
        0x4D8066, 0x809980, 0xE6FF80, 0x1AFF33, 0x999933,
        0xFF3380, 0xCCCC00, 0x66E64D, 0x4D80CC, 0x9900B3, 
        0xE64D66, 0x4DB380, 0xFF4D4D, 0x99E6E6, 0x6666FF];
    col_embed = random.choice(colorArray)
    if code == "-":
        embedVar = discord.Embed(title="Lifesim", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
        {}
        ```
        """.format(code))
        await ctx.send(embed = embedVar)
    elif code == "eball":
        embedVar = discord.Embed(title="8Ball", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
@bot.command()
async def eball(ctx, message):
    lst = ["Yes", "Hell yeah", "Nah", "I Can Sense Something Good!", 
    "Hell Nah Bruh", "Are You Kidding Me?", "That Doesn't Even Have An Answer Lmao", 
    "As I See It, Yes!", "Better Not Tell You Now", "Cannot Predict Now", "Don't Count On It", 
    "Most Likely", "My Reply Is No", "Outlook Good", "Without A Doubt", "100% Yes", "Signs Point To Yes", 
    "Obviously!", "No."]
    rng = random.choice(lst)
    await ctx.send(rng)
        ```
        """)
        await ctx.send(embed = embedVar)
    elif code == "howdeepis":
        embedVar = discord.Embed(title="Howdeepis", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
@bot.command()
async def howdeepis(ctx, message):
    lst = ["km", "m", "cm", "mm", "micro metres"]
    rng = random.randint(-100, 1000)
    lst_rng = random.choice(lst)
    await ctx.send("{} {}".format(rng, lst_rng))

@bot.command()
async def howlongis(ctx, message):
    lst = ["km", "m", "cm", "mm", "micro metres"]
    rng = random.randint(-100, 1000)
    lst_rng = random.choice(lst)
    await ctx.send("{} {}".format(rng, lst_rng))
        ```
        """)
        await ctx.send(embed = embedVar)
    elif code == "howlongis":
        embedVar = discord.Embed(title="Howlongis", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
@bot.command()
async def howdeepis(ctx, message):
    lst = ["km", "m", "cm", "mm", "micro metres"]
    rng = random.randint(-100, 1000)
    lst_rng = random.choice(lst)
    await ctx.send("{} {}".format(rng, lst_rng))

@bot.command()
async def howlongis(ctx, message):
    lst = ["km", "m", "cm", "mm", "micro metres"]
    rng = random.randint(-100, 1000)
    lst_rng = random.choice(lst)
    await ctx.send("{} {}".format(rng, lst_rng))
```
        """)
        await ctx.send(embed = embedVar)
    elif code == "math":
        embedVar = discord.Embed(title="Math", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
@bot.command()
async def math(ctx, numOne: float, operator, *, numTwo: float):
    if operator == "*":
        final0 = numOne * numTwo
        final = round(final0, 2)
        await ctx.send(final)
    elif operator == "/":
        final1 = numOne / numTwo
        final = round(final1, 2)
        await ctx.send(final)
    elif operator == "+":
        final2 = numOne + numTwo
        final = round(final2, 2)
        await ctx.send(final)
    elif operator == "-":
        final3 = numOne - numTwo
        final = round(final3, 2)
        await ctx.send(final)
```
        """)
        await ctx.send(embed = embedVar)
    elif code == "echo":
        embedVar = discord.Embed(title="Echo", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
@bot.command(pass_context = True)
async def echo(ctx, channel: discord.TextChannel, *, message):
    await ctx.message.add_reaction("✅")
    await channel.send(message)
    asyncio.sleep(2)
    await ctx.message.delete()
```
        """)
        await ctx.send(embed = embedVar)
    elif code == "helpme":
        embedVar = discord.Embed(title="Help", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
        ```py
@bot.command()
async def helpme(ctx):
    embedVar = discord.Embed(title="FriendZone Commands", description="**Prefix: ;;**", color=0x8F1500)
    embedVar.add_field(name="**__Utility__**", value="`ping, info, echo`", inline=True)
    embedVar.add_field(name="**__Fun__**", value="`pair, lifesim, eball, howdeepis, /n howlongis, who`", inline=False)
    embedVar.add_field(name="**__Math__**", value="`math, rng`")
    await ctx.send(embed = embedVar)

```
        """)
        await ctx.send(embed = embedVar)
    elif code == "who":
        embedVar = discord.Embed(title="Who", description="**Behind The Code**", color=col_embed)
        embedVar.add_field(name="Python 3 Code:", value="""
            ```py
@bot.command()
async def who(ctx):
    lst = ["Ramika", "Samar", "Manuka", "Ishan", "Sunny", "Harry", "Lily", "Ananya", "Neili", 
    "Chiku", "Tikki", "Jasmine Moverely Bonne", "Metheshr", "Tony", "Micah", "Emily", "Hayley", 
    "Casey"]
    word = ["Defintely Has To Be", "100%", "Bro, It's", "Are You Kidding Me? It is", 
    "It's Truly", "Whithout Hesitation, It's 100%", "Without A Doubt", "It Has To Be", 
    "Smh, Isn't It Obvious That It's", "C'mon, It's 100%"]
    final_w = random.choice(word)
    final = random.choice(lst)
    await ctx.send("{} {}".format(final_w, final))

```
        """)
        await ctx.send(embed = embedVar)
        

bot.run('NzU3MTQzMzEzMTg1ODk4NTE1.X2cGqA.dzJpfNFgWUHq-vkwr22m3LHptUY')
