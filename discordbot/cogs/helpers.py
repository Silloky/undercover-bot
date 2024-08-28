from discordbot import bot


async def register_cog(cog_cls):
    await bot.add_cog(cog_cls(bot))
