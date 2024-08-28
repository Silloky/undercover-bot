from discord.ext.commands import Bot
from discord import Intents

intents = Intents.all()

bot = Bot(command_prefix="!", help_command=None, intents=intents)
