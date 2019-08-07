import discord

import datetime
import re
import os
import random
import asyncio
import time


async def sendRandomPhoto(ctx, path):
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    imagen = (files[index])
    fullpath = path + imagen
    print(fullpath)
    f = discord.File(fullpath, filename='D.png')
    await ctx.send(file=f)


async def teke_typing(ctx):
    await ctx.trigger_typing()
    time.sleep(random.uniform(0.5, 1.2))


async def consola(ctx):
    print("Llego aca 4")
    print("Inicia la consola")
    linea = input("Teke dice: ")
    while linea != "exit" and linea != "":
        await ctx.send(linea)
        linea = input("Teke dice: ")


async def mensaje_cargando(ctx):

    cargando = [
        "`[                    ]`",
        "`[=                   ]`",
        "`[==                  ]`",
        "`[===                 ]`",
        "`[====                ]`",
        "`[=====               ]`",
        "`[======              ]`",
        "`[=======             ]`",
        "`[========            ]`",
        "`[=========           ]`",
        "`[==========          ]`",
        "`[===========         ]`",
        "`[============        ]`",
        "`[=============       ]`",
        "`[==============      ]`",
        "`[===============     ]`",
        "`[================    ]`",
        "`[=================   ]`",
        "`[==================  ]`",
        "`[=================== ]`",
        "`[====================]`"
    ]

    mensaje_cargando: discord.Message = await ctx.send("`[ SE VIENE ]`")
    for x in range(0, len(cargando)):
        await mensaje_cargando.edit(content=cargando[x])
        await asyncio.sleep(0.25)
    await mensaje_cargando.delete()


def zodiaco(cumple: datetime.date):
    if cumple is None:
        return None
    day = cumple.day
    month = cumple.month
    astro_sign = None

    if month == 12:
        astro_sign = 'Sagitario' if (day < 22) else 'Capricornio'
    elif month == 1:
        astro_sign = 'Capricornio' if (day < 20) else 'Aquario'
    elif month == 2:
        astro_sign = 'Aquario' if (day < 19) else 'Piscis'
    elif month == 3:
        astro_sign = 'Piscis' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Tauro'
    elif month == 5:
        astro_sign = 'Tauro' if (day < 21) else 'Geminis'
    elif month == 6:
        astro_sign = 'Geminis' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Escorpio'
    elif month == 11:
        astro_sign = 'Escorpio' if (day < 22) else 'Sagitario'

    return astro_sign


def remove_emojis(text):
    #From https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python

    emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"
                u"\U0001F914"
                "]+", flags=re.UNICODE)
    return(emoji_pattern.sub(r'', text)) # no emoji