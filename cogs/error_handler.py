import traceback
import sys
from discord.ext import commands
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(
                f'{ctx.command} has been disabled. If you believe this is a mistake, please contact @Willy#7692')

        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')

        elif isinstance(error, commands.CommandNotFound):
            return await ctx.send(f'{ctx.command} is not found.')

        elif isinstance(error, commands.BadArgument):
            return await ctx.send(f'One or more of arguments are incorrect. Please see {ctx.prefix}help for more info')

        elif isinstance(error, commands.NotOwner):
            return await ctx.send(
                'Sorry, this command can only be used by my owner. If you believe this is a mistake, please contact @Willy#7692')
        print('Ignoring exception in command {}:'.format(ctx.command))
        traceback.print_exception(type(error), error, error.__traceback__)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))