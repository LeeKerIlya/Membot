import discord
from discord.ext import commands
 
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix='$', intents=intents)
 
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    with open('images/mem2.jpg', 'rb') as f:
     picture = discord.File(f)
    await ctx.send(file=picture)
    
    def get_fox_image_url():    
     url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']
