import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('ODMzNzkzMTQ3MjIwOTE4MzUz.YH3gYQ.YI-ACLw9Yep9gZvtjdVgrRVI7Ms')
