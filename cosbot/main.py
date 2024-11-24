import sys

if sys.platform == "win32":
    try:
        import asyncio
    except Exception as e:
        print(f"Error setting event loop policy: {e}")

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import discord
from discord.ext import commands
from cosbot.config import settings
from cosbot.models.base import engine, get_session
from alembic import context

# Initialize the bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)


# Event to indicate the bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    # Create database tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_pending()


# Command to test the bot
@bot.command(name="test")
async def test(ctx):
    await ctx.send("Test successful!")


# Run the bot with the token from the environment variables
if __name__ == "__main__":
    bot.run(settings.DISCORD_TOKEN)
