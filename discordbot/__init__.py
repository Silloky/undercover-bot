from discordbot.bot import bot
from discordbot.cogs import *
from discordbot.handlers import *
import asyncio

async def register_cogs(bot):
    await bot.add_cog(Help(bot))
    await bot.add_cog(Poll(bot))
    await bot.add_cog(Vote(bot))

def main(bot_token, bot_command_prefix=None):
    if bot_command_prefix is not None:
        bot.command_prefix = bot_command_prefix

    asyncio.run(register_cogs(bot))
    bot.run(bot_token)
