import discord

from discord.ext import commands
import datetime
from texttable import Texttable
from cogs.utils import text, database


class RPG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cargar_usuarios(self, ctx):
        """Carga a los nuevos usuarios a la dase de datos"""
        guild: discord.Guild = ctx.guild

        for member in guild.members:
            database.crear_usuario(member.id, member.name, member.mention)

    @commands.command()
    async def rpg(self, ctx, target_member: discord.Member = None):
        """Muestra las estadisticas de un usuario"""

        if not target_member:
            target_member = ctx.author

        mensaje = """Estadisticas de: {} \n```yaml\nGold: {}\nSexo: {}\nCumple: '{}'\nSigno: {}\nLvl: {}\nExp: {}\nSocial: {}\nCantidad_de_Tekes: {}\n```
        """.format(target_member.mention,
                   database.get_campo(target_member.id, 'gold'),
                   "Mujer" if database.get_campo(target_member.id, 'sex') else "Hombre",
                   database.get_campo(target_member.id, 'cumple'),
                   text.zodiaco(database.get_cumple(target_member.id)),
                   database.get_campo(target_member.id, 'lvl'),
                   database.get_campo(target_member.id, 'exp'),
                   database.get_campo(target_member.id, 'social'),
                   database.get_campo(target_member.id, 'teke_cont')
                   )
        await ctx.send(mensaje)

    @commands.command()
    async def set_cumple(self, ctx, dia: int, mes: int, anio: int):
        try:
            cumple = datetime.date(anio, mes, dia)
            database.cumple_set(ctx.author.id, cumple)
        except:
            await ctx.send('Error: no se pudo setear cumple')
        else:
            await ctx.send('Cumple seteado con exito. {}'.format(cumple))

    @commands.command()
    async def top(self, ctx, atributo):
        """Muestra las estadisticas de un usuario"""

        if atributo == 'teke':
            atributo = 'teke_cont'

        mensaje = "TOP 5 {}\n".format(atributo.upper())
        tabla = Texttable()
        tabla.add_row(['Puesto', 'Nombre', atributo])

        try:
            top = database.top(atributo)
        except Exception as e:
            print(e)
            await ctx.send('Exception: {}'.format(e))
            return

        for (i, linea) in enumerate(top, start=1):
            tabla.add_row([i, linea[1], linea[2]])

        await ctx.send("```diff\n" + mensaje + tabla.draw() + "\n```")


def setup(bot):
    bot.add_cog(RPG(bot))
