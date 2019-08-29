import discord

from discord.ext import commands
import datetime
from texttable import Texttable
from cogs.utils import text, database


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, target_member: discord.Member):
        """Kickea a un usuario de un canal de voz"""

        if not target_member.voice:
            await ctx.send(ctx.author.mention + " Sos boludo? No lo puedo kickear porque no esta en ningun canal de voz")
            return

        mensaje: discord.Message = await ctx.send("Se lo damo o no se lo damo?")
        await mensaje.add_reaction(emojis["suegro"])
        await mensaje.add_reaction(emojis["no"])

        await mensaje_cargando(ctx)

        mensaje_actual = await ctx.channel.fetch_message(mensaje.id)

        cantidad_si = next(x for x in mensaje_actual.reactions if x.emoji.name == 'suegro').count
        cantida_no = next(x for x in mensaje_actual.reactions if x.emoji.name == 'no').count

        if cantidad_si > cantida_no:
            # aca recien lo kickea
            await target_member.move_to(None)
            await ctx.send(target_member.mention + " fuiste trolleado")
        elif cantidad_si == cantida_no:
            await ctx.send("Hubo empate")
        else:
            await ctx.send("No se dio :(")

    # @commands.command()
    # async def traer(ctx, target_member: discord.Member):
    #     """Trae a un usuario al canal de voz actual"""
    #     await target_member.move_to(ctx.author.voice.channel)
    #
    # @commands.command()
    # async def mover(ctx, target_member: discord.Member, target_channel: discord.VoiceChannel):
    #     """Mueve a un usuario a un canal de voz"""
    #     await target_member.move_to(target_channel)

    @commands.command()
    async def x(self, ctx):
        messages = await ctx.channel.history(limit=123).flatten()
        for message in messages:
            if message.author.id == self.user.id:
                await message.delete()


def setup(bot):
    bot.add_cog(Admin(bot))
