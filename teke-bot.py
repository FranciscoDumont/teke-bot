# -*- coding: utf-8 -*-

from googletrans import Translator
import schedule
import aiml
from gtts import gTTS

import config
from cogs.utils import database
from cogs.utils import frasesTeke
from cogs.utils.storyTeke import personas
from cogs.utils.text import *

from discord.ext import commands


os.chdir(os.path.abspath(os.path.dirname(__file__)))

description = '''Yo soy el Teke Bot, amo y señor de este servidor.
Me apasiona el dinero, los cigarros y la violencia.

Lista de comandos:'''

traductor = Translator()

# Load AIML kernel
aiml_kernel = aiml.Kernel()
aiml_kernel.learn('std-startup.xml')
aiml_kernel.respond("LOAD AIML B")
with open('bot.properties') as f:
    for line in f:
        parts = line.strip().split('=')
        key = parts[0]
        value = parts[1]
        aiml_kernel.setBotPredicate(key, value)
    print('\n\n\nTeke Seteado')

emojis = {
    "suegro": '<:suegro:569392209422581761>',
    "otrosuegro": '<:suegro:569392209422581761>',
    "lol_gatito": '😹',
    "surf": '🏄',
    "lol": '😂',
    "fuego": '🔥',
    "cien": '💯',
    "no": '<:no:528723240944664586>'
}


INITIAL_EXTENSIONS = [
    'cogs.music',
    'cogs.rpg',
    'cogs.lol'
]


class TekeBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='?', description=description)

        for extension in INITIAL_EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as e:
                print('Failed to load extension {}\n{}: {}'.format(
                    extension, type(e).__name__, e))

    async def on_ready(self):
        print('Logged in as')
        print(self.user)
        print(self.user.name)
        print(self.user.id)
        print('------')

        self.TRISTE = 1
        self.TEKE = 0
        self.MAIN_SERVER = self.get_guild(config.main_server_id)
        self.MAIN_CHANNEL = self.get_channel(config.main_channel_id)

        schedule.every().day.at("00:01").do(self.saludar_cumples)
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_message(self, message):
        await self.process_commands(message)
        # don't respond to ourselves
        #	if message.author != bot.user:
        #		print("Mensaje recibido: "+ str(message.content))
        #        return


        texto_mensaje = message.content.lower().strip().replace('<@485636016175054890>', 'teke')

        if '\'tts ' in texto_mensaje:
            await message.delete()
            return

        if str(message.author) in frasesTeke.respuestas_especificas.keys():
            if random.randint(0, 17) == 0:
                await teke_typing(message.channel)
                await message.channel.send(random.choice(frasesTeke.respuestas_especificas[str(message.author)]))

        if message.author != self.user:
            texto_mensaje_noemoji = remove_emojis(texto_mensaje)
            texto_mensaje_noemoji = re.sub(r'<:[^()]*>', '', texto_mensaje_noemoji).strip()
            try: #reemplazo los ids por los nombres de usuario
                persona_citada = re.search(r'<@(.*)>', texto_mensaje_noemoji).group(1)
                texto_mensaje_noemoji = re.sub(r'<@[^()]*>', database.get_campo(persona_citada.strip(), 'name'), texto_mensaje_noemoji).strip()
            except:
                pass
            if texto_mensaje_noemoji != '' and texto_mensaje_noemoji[-1] == '?':
                if 'teke' in texto_mensaje_noemoji or random.randint(0, 3) == 0 or self.TEKE:
                    respuesta = ""
                    if 'quien' in texto_mensaje_noemoji and 'panchi' not in texto_mensaje_noemoji:
                        respuesta = random.choice(personas)
                        if 'a quien' in texto_mensaje_noemoji:
                            respuesta = "A " + respuesta
                    if not any(palabra in texto_mensaje_noemoji for palabra in ['como ', 'cuando ', 'por que ', 'cual ', 'quien ', 'que ', 'donde ']):
                        await teke_typing(message.channel)
                        respuesta = random.choice(frasesTeke.respuestas_teke)

                    if respuesta:
                        await message.channel.send(respuesta)

            if random.randint(0, 9) == 0:
                emoji_random = random.choice(list(emojis.values()))
                await message.add_reaction(emoji_random)

            if 'teke' in texto_mensaje:
                self.TEKE = 5
                database.teke_cont_add(message.author.id, texto_mensaje.count('teke'))

            if self.TEKE and texto_mensaje_noemoji:
                self.TEKE = self.TEKE - 1
                aiml_message = traductor.translate(texto_mensaje_noemoji, src='es', dest='en').text
                print('\taiml_message = {}'.format(aiml_message))
                aiml_response = aiml_kernel.respond(aiml_message)
                print('\taiml_response = {}'.format(aiml_response))
                aiml_response_es = traductor.translate(aiml_response, src='en', dest='es').text
                print('\taiml_response_es = {}'.format(aiml_response_es))

                await teke_typing(message.channel)
                await message.channel.send(aiml_response_es)

                await self.teke_karma(message)

        if any(palabra in texto_mensaje for palabra in ['culo', 'caca']):
            #if 'culo' in texto_mensaje:
            database.social_add(message.author.id, -10)
            if self.TRISTE >= 1:
                await self.triste_estado(message)
            else:
                print("no puedo estar mas triste")

        if str(message.author) in config.enemigos:
            if random.randint(0, 2) == 0 and not self.TRISTE:
                await self.enojado_estado(message)
                database.social_add(message.author.id, -1)
                return

        if database.check_mujer(message.author.id):
            if random.randint(0, 3) == 0:
                await self.romantico_estado(message)
                database.social_add(message.author.id, 2)

        if random.randint(0, 11) == 0:
            await teke_typing(message.channel)
            await message.channel.send(random.choice(frasesTeke.frases))



        #Dejar este if al final
        if message.author == self.user:
            def check(reaction, user):
                return str(reaction.emoji) == '👍'

            try:
                reaction, user = await self.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                # await message.channel.send('👎')
                return
            else:
                f = discord.File('/home/panchi/Pictures/ben10/suegro.jpeg', filename='SUEGRO.png')
                await message.channel.send(file=f, delete_after=2)


    async def on_member_join(self, member: discord.Member):
        await self.MAIN_CHANNEL.send("Quien es este payaso ???")


    async def teke_karma(self, message):

        amor = [
            'te quiero',
            'lindo',
            'beso',
            'lol',
            'pokemon',
            'jaj',
            'chupar',
            'comida',
            'fachero',
            '😍', '❤', '😻',
            'amo'
        ]

        odio = [
            'puto',
            'gordo',
            'forro',
            'gay',
            'diana',
            'linux',
            'play 4',
            'report',
            'pelotudo',
            'cerra'
        ]

        if any(palabra in message.content.lower() for palabra in amor):
            database.social_add(message.author.id, round(random.uniform(1, 3), 2))
            if database.check_mujer(message.author.id):
                database.social_add(message.author.id, 2)
                #print(respuesta_amor)
            elif database.get_campo(message.author.id, 'social') >= 75.0 :
                database.social_add(message.author.id, 2)
                #print(respuesta_gay)




        if any(palabra in message.content.lower() for palabra in odio):
            database.social_add(message.author.id, -2)



    async def triste_estado(self, message):
        print("Estoy en Triste")
        self.TRISTE -= 1
        await self.change_presence(activity=discord.Game(name='Deprimido'))
        await message.channel.send(random.choice(
            ['Ya me puse sad', 'Eso ultimo que dijiste me hizo acordar a algo', 'Estoy triste',
             'Aww shit, here we go again', 'Hay muchas cosas que pienso pero nunca digo, por ejemplo:']))
        for x in range(1, random.randint(3, 5)):
            print("Triste: " + str(x))
            await message.channel.send(random.choice(frasesTeke.deprimido))
            time.sleep(4)
        await asyncio.sleep(30)
        self.TRISTE = 1
        print("Salgo de Triste")
        await self.change_presence(status=discord.Status.online)

    async def enojado_estado(self, message):
        await self.change_presence(activity=discord.Game(name='Enojado'))
        await message.channel.send(random.choice(frasesTeke.enojado))
        await asyncio.sleep(30)
        await self.change_presence(status=discord.Status.online)

    async def romantico_estado(self, message):
        await self.change_presence(activity=discord.Game(name='Romantico'))
        await message.channel.send(random.choice(frasesTeke.romantico))
        await asyncio.sleep(30)
        await self.change_presence(status=discord.Status.online)

    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    async def repeat(self, ctx, times: int, content='repeating...'):
        """Repeats a message multiple times."""
        for i in range(times):
            await ctx.send(content)

    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

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


    # @self.command()
    # async def traer(ctx, target_member: discord.Member):
    #     """Trae a un usuario al canal de voz actual"""
    #     await target_member.move_to(ctx.author.voice.channel)
    #
    # @self.command()
    # async def mover(ctx, target_member: discord.Member, target_channel: discord.VoiceChannel):
    #     """Mueve a un usuario a un canal de voz"""
    #     await target_member.move_to(target_channel)


    async def agregar(self, ctx, *frase_nueva: str):
        """Agrega una nueva frase """

        frase_nueva = ' '.join(frase_nueva)
        linea = time.ctime() + ' - ' + ctx.message.author.name + ': ' + frase_nueva
        print(linea)
        with open("nuevas-frases.txt", "a+") as text_file:
            print(linea, file=text_file)
            await ctx.send("Agregada con exito")




    async def tts(self, ctx, *text: str):
        if ctx.voice_client is None:
            return
        if ctx.message.author.voice.channel is None:
            return
        text = ' '.join(text)
        tts_es = gTTS(text, lang='es')
        tts_es.save('temp.mp3')
        #os.system("sox temp.mp3 temp.mp3 speed 0.95 rate 24k pitch -850 reverb 60 50 75")
        #os.system("ffmpeg -hide_banner -loglevel panic -i temp.mp3 -y -c copy output.mp3")
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('temp.mp3'))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)


    async def x(self, ctx):
        messages = await ctx.channel.history(limit=123).flatten()
        for message in messages:
            if message.author.id == self.user.id:
                await message.delete()

    async def s(self, ctx):
        await ctx.send("Link del stream:\nhttps://discordapp.com/channels/432329008957358101/470075380141654026")


    def saludar_cumples(self):

        async def mandar_mensajes(id: int):
            user = self.MAIN_SERVER.get_member(id)
            await self.MAIN_CHANNEL.send("@everyone\nHoy es el cumple de {}!!! 💕🎊🎉".format(user.mention))
            await user.send("Hola {}, como estas?\nNo creas que lo he olvidado, Feliz cumpleaños!!! 🎉🎊❤".format(user.mention))

            if self.MAIN_SERVER.voice_client is not None:
                await self.MAIN_SERVER.voice_client.disconnect()

            if user.voice.channel is not None:
                if self.MAIN_SERVER.voice_client is not None:
                    await self.MAIN_SERVER.voice_client.move_to(user.voice.channel)
                await user.voice.channel.connect()

                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('/home/panchi/Music/cancion-feliz-cumple.mp3'))
                self.MAIN_SERVER.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        try:
            cumpleañeros = database.get_today_cumple()
        except Exception as e:
            return

        if cumpleañeros:
            for persona in cumpleañeros:
                id = persona[0]
                self.bg_task = self.loop.create_task(mandar_mensajes(id))

    async def my_background_task(self):
        await self.wait_until_ready()
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)  # task runs every 60 seconds

if __name__ == '__main__':
    client = TekeBot()
    client.run(config.token)
