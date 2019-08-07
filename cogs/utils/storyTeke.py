import random

inicio = [
    'Chicos, no saben lo que me pasó ',
    'A ver, para, ',
    'uhh wacho ',
    'Eu man ',
    'Che bros '
]

pasado = [
    'esta tarde ',
    'el otro dia ',
    'ayer ',
    'anoche ',
    'esta mañana ',
    'esta noche '
]

lugares = [
    'en lo de mi viejo ',
    'en lo de Fede Staciuk ',
    'en el techo de mi casa ',
    'abajo de la mesa de la concina ',
    'en Sutton ',
    'en Pueblo Limite ',
    'en Villa Gesell ',
    'en el bondi ',
    'en la cama de mis viejos ',
    'en la casa de mi abuela ',
    'en el auto de Panchi ',
    'en la municpalidad de Sol y Verde ',
    'en el Sarmiento ',
    'en el laburo '
]

estaba = [
    'estaba re traquilo ',
    'estaba cagando re tranquilo ',
    'estaba mirando un re hentai ',
    'me estaba cortando las uñas ',
    'me estaba a punto de cagar ',
    'me estaba clavando un asadito ',
    'estaba viendo anime ',
    'me estaba chamuyando a una piba ',
    'estaba jugando a la play ',
    'estaba jugando a la pelota ',
    'me tire un macaco ',
    'estaba cazando pokemones ',
    'me comi un embutido '
]

interrupcion = [
    'y de la nada ',
    'cuando de pronto ',
    'y derrepente ',
    'y ',
    'y a los 2 minutos ',
    'y cuando me di vuelta ',
    'cuando levante la cabeza ',
    'y cuando mire para abajo '
]

lo_vi = [
    'estaba ',
    'vi a ',
    'me encontre con '
]

personas = [
    'Agustin Arias ',
    'Pablo Paez ',
    'Panchi ',
    'Theo Fiori ',
    'Pocho ',
    'Ale ',
    'Lautaro ',
    'Sofi discord ',
    'Susana Lema ',
    'el papa de Mavi ',
    'Shao Kahn ',
    'Agustin Conte ',
    'Fede Staciuk ',
    'la gorda tryhard ',
    'Dami ',
    'Joaquin ',
    'Joaquin Guarino ',
    'Toni Guarino ',
    'Nacho Zarza ',
    'Leo Vitalevi ',
    'Thiaguito Olmos ',
    'Marcelo Tineli ',
    'Julia ',
    'Maxi Yenfel ',
    'el Teke ',
    'mi Abuela en malla ',
    'Tomas Terra ',
    'Tati ',
    'Crute Gordo ',
    'Cami Staciuk ',
    'Diana ',
    'Lena ',
    'tu vieja ',
    'Carlos Saul Menem ',
    'Ancans ',
    'Vicente Viloni ',
    'Julian Weich '
]

flipaba = [
    'no lo podia creer ',
    'y me re calenté ',
    'ahi se me paro la pija mal ',
    'y directamente me cagué, posta te digo ',
    'me re asuste ',
    'me puse re triste ',
    'automanticamente me agarre el huevo izquierdo ',
    'instantaneamente me agarró retencion de liquidos ',
    'se me bajo la presion ',
    'casi me muero de inanicion ',
    'se me paro la pija como nunca en mi vida'
]

porque = [
    'por que ',
    'por que ',
    'ya que ',
    'debido a que '

]

persona_hace = [
    'tenia la verga al aire ',
    'estaba re en pedo ',
    'me pidio que le de un beso ',
    'me estaba mirando fijo ',
    'me estaba a punto de tocar el huevito ',
    'estaba ahi desde que llegue ',
    'me gusta en secreto ',
    'tenia el culo paspado ',
    'justo recien me habia clavado una mortadela entera de desayuno ',

]


def anecdota():
    return random.choice(inicio) + random.choice(pasado) + random.choice(lugares) + random.choice(estaba) + random.choice(interrupcion) + random.choice(lo_vi) + random.choice(personas) + random.choice(flipaba) + random.choice(porque) + random.choice(persona_hace)
