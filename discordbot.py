import asyncio, discord
from discord.ext import commands
import logging
import logging.handlers
from dice import *

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)


intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="$",intents=intents)


@bot.event
async def on_ready():
    print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "Super Bot의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")
        
bot.run("KEY ID", log_handler=None)