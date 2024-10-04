# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # This allows your bot to read message content
intents.guild_scheduled_events = True # This allows the bot to read scheduled events

# Initialize the bot with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am KanaalaBot!")

@bot.command()
async def events(ctx):
    guild = ctx.guild
    scheduled_events = await guild.fetch_scheduled_events()  # Fetch all scheduled events
    if scheduled_events:
        event_list = "Here are the current scheduled events:\n"
        for event in scheduled_events:
            event_list += (
                f"- **{event.name}** on {event.start_time.strftime('%Y-%m-%d %H:%M:%S')} "
                f"at {event.location or 'No Location Specified'}\n"
            )
        await ctx.send(event_list)
    else:
        await ctx.send("There are no scheduled events in this server.")

@bot.command()
async def time(ctx):
    await ctx.send("15 MINUTES!!!!!!!!!!!!!!!!!")

@bot.command()
async def whoami(ctx):
    await ctx.send("AYO SHE????!!!!!!")

bot.run(TOKEN)