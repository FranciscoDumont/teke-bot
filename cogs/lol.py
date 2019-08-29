import discord

from discord.ext import commands
import os
import random
import requests
import io
import json
import aiohttp
import asyncio
import re
import wikiquote
import rule34


from cogs.utils import text, storyTeke


class LOL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        ctx = await self.bot.get_context(message)

        if random.randint(0, 16) == 0:
            await text.teke_typing(message.channel)
            await self.quote.callback(self, ctx)

        if random.randint(0, 199) == 0:
            print("Entro en random Hentai")
            await message.channel.send(random.choice(
                ['Como me gustaria encontrar esto en mi cuarto', 'Mira el bombonazo que me voy a comer ahora']))
            await self.hentai.callback(self, ctx)

        if random.randint(0, 199) == 0:
            print("Entro en random Rule34")
            await message.channel.send('Como me gustaria encontrar esto en mi cuarto')
            await self.rule.callback(self, ctx)

        if random.randint(0, 199) == 0:
            print("Entro en random reddit")
            await message.channel.send('Vieron este meme ? :joy:')
            await self.reddit.callback(self, ctx)


    @commands.command()
    async def hola(self, ctx):
        """Manda una anecdota"""
        await ctx.send(storyTeke.anecdota())

    @commands.command()
    async def sexo(self, ctx):
        """Me deja controlar a Teke bot desde la consola"""
        await text.consola(ctx)

    @commands.command()
    async def lobo(self, ctx):
        """Manda una foto del Lobo Rosarino"""
        await text.sendRandomPhoto(ctx, '/home/panchi/Pictures/Lobo/')

    @commands.command()
    async def dota(self, ctx):
        """Manda una imagen de una heroe de dota"""
        await text.sendRandomPhoto(ctx, '/home/panchi/Pictures/dota-portraits/')

    @commands.command()
    async def ben10(self, ctx):
        """Manda una imagen de Ben 10"""
        await text.sendRandomPhoto(ctx, '/home/panchi/Pictures/ben10/')

    @commands.command()
    async def wall(self):
        """Me cambia el fondo de escritorio (sfw)"""
        os.system("feh --randomize --bg-fill /home/panchi/Pictures/Wallpapers/")

    # os.system("feh --randomize --bg-fill /home/panchi/Pictures/Wallpapers/anime/")

    @commands.command()
    async def combo(self, ctx, number: int):
        """Manda N imagenes de heroes de Dota"""
        i = 1
        while i <= number < 20:
            await text.sendRandomPhoto(ctx, '/home/panchi/Pictures/dota-portraits/')
            i = i + 1

    @commands.command()
    async def ben(self, ctx, number: int):
        """Manda N imagenes de Ben 10"""
        i = 1
        while i <= number and i < 20:
            await text.sendRandomPhoto(ctx, '/home/panchi/Pictures/ben10/')
            i = i + 1

    @commands.command()
    async def hentai(self, ctx, choices: str = ''):
        """Manda hentai de https://konachan.com"""
        # https://konachan.com/post.json?tags=rating%3Aexplicit+order%3Arandom&limit=1
        choices = choices.strip()
        url = 'https://konachan.com/post.json?tags=rating%3Aexplicit+' + choices + '&limit=50'
        response = requests.get(url)
        json_data = json.loads(response.text)
        if json_data:
            hentai_url = random.choice(json_data)["jpeg_url"]
        else:
            await ctx.send("No encontré eso")
            return
        print(hentai_url)
        # await ctx.send(hentai_url)

        async with aiohttp.ClientSession() as session:
            async with session.get(hentai_url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cool_image.png'))

    # @commands.command()
    # async def rule34(ctx, choices: str = ''):
    #     """Manda rule34 de https://rule34.xxx"""
    #     # https://github.com/KuroZen/r34-json-api
    #     choices = choices.strip()
    #     url = 'https://r34-json-api.herokuapp.com/posts?tags=' + choices + '&limit=100'
    #     response = requests.get(url)
    #     json_data = json.loads(response.text)
    #     if json_data:
    #         rule34_url = random.choice(json_data)["file_url"]
    #     else:
    #         await ctx.send("No encontré eso")
    #         return
    #     print(rule34_url)
    #     #	await ctx.send(hentai_url)
    #
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(rule34_url) as resp:
    #             if resp.status != 200:
    #                 return await ctx.send('Could not download file...')
    #             data = io.BytesIO(await resp.read())
    #             await ctx.send(file=discord.File(data, 'cool_image.png'))

    @commands.command(name='rule34')
    async def rule(self, ctx, choices: str = ''):
        """Manda rule34 de https://rule34.xxx"""
        choices = choices.strip()

        loop = asyncio.get_event_loop()
        boke = rule34.Rule34(loop)

        try:
            urls = await boke.getImageURLS(choices, singlePage=True, randomPID=True)
            rule34_url = random.choice(urls)
        except Exception:
            await ctx.send("No encontré eso")
            return

        print(rule34_url)

        async with aiohttp.ClientSession() as session:
            async with session.get(rule34_url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cool_image.png'))

    @commands.command()
    async def reddit(self, ctx, subreddit: str = ''):
        """Manda una imagen de un subrredit; default=r/SquarePosting"""

        if subreddit == '':
            subreddit = random.choice(["SquarePosting", "dankgentina"])

        subreddit = subreddit.strip()
        url = 'https://www.reddit.com/r/{}/top/.json?sort=top&t=week&limit=50'.format(subreddit)
        response = requests.get(url, headers={'User-agent': 'Teke-Bot'})
        json_data = json.loads(response.text)
        if json_data:
            post_json = random.choice(json_data["data"]["children"])["data"]
            title = post_json["title"]
            is_video = post_json["is_video"]
            image_url = post_json["url"]
        else:
            await ctx.send("No encontré eso")
            return

        if is_video:
            print("Era un video")
            await  self.reddit.callback(ctx)
            return

        if not any(x in image_url for x in ['.png', '.jpg', '.jpeg']):
            print("No era una imagen")
            await self.reddit.callback(ctx)
            return

        print(image_url)

        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, title + '.jpeg'))

    @commands.command()
    async def duki(self, ctx):
        """Manda un pedazo de cancion de Duki"""
        path = '/home/panchi/Downloads/Duki/'
        files = os.listdir(path)
        index = random.randrange(0, len(files))
        cancion_filename = (files[index])
        fullpath = path + cancion_filename
        print(fullpath)
        with open(fullpath, 'r') as f:
            cancion_json = json.load(f)
        titulo = cancion_json["songs"][0]["title"]
        letra = cancion_json["songs"][0]["lyrics"]

        letra_procesada = re.sub(r'\[[^()]*\]', '', letra)
        lista_de_parrafos = letra_procesada.split("\n\n")
        await ctx.send(random.choice(lista_de_parrafos))

        # print(letra)
        # print("\n-----------------------\n")
        # print(letra_procesada)
        # print(lista_de_parrafos)

    @commands.command()
    async def quote(self, ctx, autor: str = ''):
        """Manda una frase de un filosofo"""
        autores = ['Séneca', 'El_arte_de_la_guerra', 'Charly_García', 'Carlos_Menem', 'Epicteto', 'Sócrates',
                   'Stephen_King',
                   'Bruce_Lee', 'Diego_Armando_Maradona', 'Ricardo_Iorio', 'Naruto:_Shippūden', 'Nach',
                   'Jorge_Luis_Borges',
                   'Oscar_Wilde',
                   'Jostein_Gaarder', 'Jesús_de_Nazaret', 'Ateísmo', 'Charles_Darwin', 'Stephen_Hawking',
                   'Gabriel_García_Márquez',
                   'Sigmund_Freud', 'El_guardián_entre_el_centeno', 'Charles_Bukowski', 'Confucio', 'Dale_Carnegie']

        if autor == '':
            autor = random.choice(autores)

        frases = wikiquote.quotes(autor, lang='es', max_quotes=0)

        print("Autor: {} Cant: {}".format(str(autor), len(frases)))
        await ctx.send(random.choice(frases))

    @commands.command()
    async def agregar(self, ctx, *frase_nueva: str):
        """Agrega una nueva frase """

        frase_nueva = ' '.join(frase_nueva)
        linea = time.ctime() + ' - ' + ctx.message.author.name + ': ' + frase_nueva
        print(linea)
        with open("nuevas-frases.txt", "a+") as text_file:
            print(linea, file=text_file)
            await ctx.send("Agregada con exito")

    @commands.command()
    async def s(self, ctx):
        await ctx.send("Link del stream:\nhttps://discordapp.com/channels/432329008957358101/470075380141654026")


def setup(bot):
    bot.add_cog(LOL(bot))
