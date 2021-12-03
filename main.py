import os
from dotenv import load_dotenv
from discord.ext import commands
import kpi_27_day


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='aurora',
             help='Gives predictions for visible auroras in the PNW')
async def aurora_forecast_27days(ctx):
    vis_days = kpi_27_day.aurora_days(2)
    if len(vis_days) > 0:
        vis_days = ', '.join(vis_days)
        response = ('Aurora may be visible in your location on: ' + vis_days)
    else:
        response = 'No visible aurora predicted this month, forecast updates every Monday'
    await ctx.send(response)


bot.run(TOKEN)
