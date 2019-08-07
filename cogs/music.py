import discord

from discord.ext import commands
import os
import random


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Joins a voice channel"""
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(ctx.message.author.voice.channel)
        await ctx.message.author.voice.channel.connect()

    #    @bot.command()
    #    async def join(ctx):
    #        await ctx.message.author.voice.channel.connect()

    @commands.command()
    async def play(self, ctx, busqueda: str = None):
        """Plays a file from the local filesystem"""

        if ctx.voice_client is None:
            await Music.join.callback(self, ctx)

        path = '/home/panchi/Dropbox/audios xd/'
        files = os.listdir(path)

        if busqueda:
            aux = []
            for s in files:
                if busqueda.lower() in s.lower():
                    aux.append(s)
            file = random.choice(aux)
        else:
            file = random.choice(files)

        query = path + file
        print(query)
        print(ctx.message.author.voice)

        #        query = '/home/panchi/Dropbox/audios xd/yabba-dabba-doo.mp3'
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(query))

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        try:
            await ctx.voice_client.stop()
        except:
            pass

    @commands.command()
    async def leave(self, ctx):
        """Stops and disconnects the bot from voice"""
        try:
            await ctx.voice_client.disconnect()
        except:
            pass

    @commands.command()
    async def musica(self, ctx, busqueda: str = None):
        path = '/home/panchi/Music/'

        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if any(x in file for x in ['.opus', '.mp3', '.aac', '.ogg', '.mpeg']):
                    files.append(os.path.join(r, file))

        if busqueda:
            aux = []
            for s in files:
                if busqueda.lower() in s.lower():
                    aux.append(s)
            fullpath = random.choice(aux)
        else:
            fullpath = random.choice(files)

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(fullpath))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        ctx.voice_client.source.volume = 20 / 100

        await ctx.send('Now playing: {}'.format(fullpath))


def setup(bot):
    bot.add_cog(Music(bot))
