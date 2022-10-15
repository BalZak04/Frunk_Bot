import discord
from discord.ext import commands

hello_words = ["пидор", "Ниггер", "Nigger", "nigga", "Niger", "нига", "нигер", "нигга", "пидоры", "пидорас"]
info_words = ["Привет", "Как дела", "как ты", "чо как", "чу", "чо", "шо", "каго", "каво", "уёба"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We need banana as {0.user}'. format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    msg_list = msg.split()

    len(list(set(msg_list + hello_words)))
    #if msg in hello_words:
    #if len(list(set(msg_list + hello_words))) < len(msg_list)+len(hello_words):
    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if (find_hello_words):
        await message.channel.send('Осуждаю')

    #print(msg_list)
    #print(hello_words)
    #print(list(set(msg_list+hello_words)))
    #print(len(list(set(msg_list + hello_words))))

    if message.content.startswith('франк'):
        await message.channel.send(f' {message.author.mention}Чу тебе')

    find_info_words = False
    for item in info_words:
        if msg.find(item) >= 0:
            find_info_words = True
    if (find_info_words):
        await message.channel.send('YAYAYY AYY YA')


    if message.content.startswith("Газета"):
        with open('pic/monke.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send('Читаю газету и смотрю кс го КОФИ', file=picture)

    if message.content.startswith("Скамер"):
        with open('pic/scam.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send('Подсчитываю донаты', file=picture)

    if message.content.startswith("Влад"):
        with open('pic/vlad.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send('Ничего необычного, просто фот 0чка влада', file=picture)

    if message.content.startswith("Витя"):
        with open('pic/viktor.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send('Ничего необычного, просто фот 0чка Вити', file=picture)

    if message.content.startswith("Ало"):
        with open('pic/alo.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send('Ало-ало-ало...', file=picture)

    if message.content.startswith("Поддержка"):
        with open('pic/sup.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send('Нам похуй', file=picture)

client.run('MTAzMDgxNzUyMDA4MjQ5MzUxMQ.GW4g69.JZnHOfvQyML4esAawuFFVTw3WfgQ09JHpNWqR8')