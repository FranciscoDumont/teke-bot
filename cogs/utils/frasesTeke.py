import random


frases = [
    'Como le entro a @Cami_Staciuk https://www.instagram.com/camila_staciuk/',
    'Salen unos patys',
    'Me comi a mi prima :speak_no_evil:',
    'Ya me desperte frente a la pc me senté',
    'DOOOOOOOOOOUUUUUUUU',
    'Ufff carne fresca, suave, tierna y joven',
    'Dami tiene un hijo',
    'Uh boludo unas ganas de ver anime',
    'Como le entro a mi prima',
    'Hoy me pego un tiro',
    'Que ganas de morir virgen',
    'Voy a plantar un pino',
    'Me voy a echar un truño',
    'NO LA PONGO MAAAAS',
    'Chicos este sabado hago juntada en casa, estan invitados, traigan bebidas porfa',
    'Yo soy el TEKE',
    'Si se da, hoy muero virgen',
    'En estas vacaciones no voy a tener horarios',
    'Este año saco el autito',
    'No tengo un peso wacho',
    'Me tienen puto con ese tema',
    'Tito mato a nisman',
    'Yo soy el verdadero Teke',
    'Hoy me pongo en pedo y le como la boca a Guada',
    'ESTOY ENPEDO',
    'Que ganas de comerle la boca a Sofi :weary:',
    'No puedo dejar el cigarrillo',
    'La puta madre mañana trabajo',
    'Hay que ir preparando para Villa Gesell',
    'Creo que me gusta {}'.format(random.choice(['Diana', 'Shae', 'Sofi', 'Tati'])),
    'Hoy me termine un anime',
    'Callate pelotudo',
    'Hoy cobré :sunglasses:',
    'EL ANIME ARRUINO MI VIDA',
    'Hoy me pego un tiro',
    'PRENDELO QUE YA SON 4 Y 20',
    'Pongan esto https://www.youtube.com/playlist?list=PLJlHZQPngy0gGrp5ABU8I9zIYGTxCYLFb',
    'Que te pasa salame ?',
    'En vista de que esta semana es la semana de los virgos (santa) voy a hacer juntada el jueves, lo usual traigansen unos pesos y en lo posible para tomar y no cagarnos de sed si pueden y quieren, seria a partir de las 17 horas y vale quedarse hasta que salga el solsito yaju Si estas recibiendo esta invitacion y sos de los que no vienen hace un año, veni, copate por una vez en tu miserable vida a ver al teke',
    'Chicos ya pedi las pizza vayan dandome la plata'
    'IAAAAJUUUUUUUUU',
    'SACAME ESO DE AHI YA MISMO _**rebolea la silla de plástico**_',
    'Vamoa juga a lo jueguito',
    'ESTO ES ANIME',
    'Traigan bebida',
    'Hoy empiezo el gym :muscle:',
    ':joy:',
    'chicos ya pedi las pizzas, 300 pesos cada uno',
    'LOL',
    'Jajaj tremendo pelotudo :joy:',
    'YABBA DABBA DOOOOOO',
    'Man si taaanto les molesta pagar las empanadas comprense otra cosa',
    'cortenla con ese tema',
    'Vas a comer aca ??',
    'Estos piden afuera y despues se comen todas las empanadas',
    'Tragieron el Devil May Cry 3 ?',
    'SI YO NO LA PONGO NO LA PONE NADIE ACA',
    'Aca gana el mas Gaucho',
    'Puto es el que la probo y no le gusto',
    'Me podes pasar el numero de tu ex ??',
    'QUIERO CULO',
    'Jaja en realidad no soy un bot',
    'Ya me encabrone',
    'Soy adinerado',
    'Soy fumador',
    'Soy violento',
    'Las minorias se pueden ir bien a la concha de su madre',
    'Mi viejo: dame 11 lucas que compré la play y la tengo que pagar',
    'TENGO TANTAS GANAS DE CULO QUE SE ME EXPLOTO UN HUEVO',
    'Bah no sé tampoco estoy en pos de poder poner casa',
    'Un like y voy a evolution a comprar el dmc',
    'Nací un lunes, pero ojalá no hubiera nacido nunca',
    'No se va a poder',
    'pensemos que vamos a cocinar no? porque el asadito... hay que hacer unos chori uno sanguche un conchetumare... cuestion trae algo cada uno como hacemos? Digan ahora.',
    'El jueves no trabajo',
    'No me rompan las pelotas',
    'Cada momento de mi vida es una agonía',
    'Mañana sale asado',
    'Agarras una empanada y te cago a trompadas',
    'Creo que me gusta (X)',
    'El resumen de mi vida es jugar al lol y perder',
    'Que personajes de mierda que tienen los enemigos',
    'Estoy en celo',
    # '1 like y me gasto 2 meses de sueldo en la play 4',
    '1 like y me vuelvo G.A.Y.',
    'Y si nunca me escuchan',
    'Hoy voy a manosear a Guada',
    'le pone mayonesa a la (variable de comida)',
    '**se compra una play4**',
    'No hay nada mejor que levantarse y oprimir minorías',
    'Mi profesión va a ser golpeador de mujeres',
    'Saben cuanto están los puchos?',
    'IIIIAAAAAJUUUU',
    'No termine el secundario porque el pelotudo de mi creador no tiene placa de video',
    'OwO',
    'e.e',
    'Mi objetivo es dominar este planeta',
    'Razones por las que quiero saber dibujar: Dibujar versiones femeninas de mis amigos y su respectivo porno c:',
    '*AAAAAAAAAAH*',
    'Creo que me gusta lena',
    'Yo me estoy cagando ahora mismo',
    'A veces me rompe las pelotas el Teke',
    'Epa se lleno de minas el Discord',
    'Que ganas de tener novia/s',
    'Me dejo el bigote fachero?',
    'Nueva teoria: Las mujeres son en realidad hombres gays',
    'Que parte de que es hombre no entendes ??',
    'Nadie me escucha en este ts de mierda',
    'Cuando tu mama va a comprar el pan y te entran ganas de pajearte',
    'En la noche mas oscura \nNegra como el abismo mas oscuro \nLe agradezco a culaquier dios si es que existe \npor mi alma inconquistable',
    'xque no contestas? acaso me tienes miedo o solo eres un chico gay que quiere que le chupen el culo?',
    'Cada mina es un mundo',
    'Me encanta la comida',
    'AYUDA LOCO NO LA PONGO MAAAAAAAAAAAS',
    'Como me gustaría saltar encima de una venosa, jugosa y gran poronga, dejen de hablar de eso porque se me hace agua el culos',
    'A los gritos me hago la paja yo',
    'Me quiero morir y así sería feliz',
    'De que te reis marmota? Que queres? que te de un sopapo ?',
    'La humildad es una virtud que no todos se pueden permitir',
    'Muy bien ahora contesteme alguien que no sea un retrasado',
    'Creo que me gusta la hermana de Juani',
    'Todos me traicionan en este server',
]

enojado = [
    'Cerra el orto payaso',
    'JAJAJA mira vos me chupaba un huevo justo',
    'TE PENSAS QUE SOS EL TEKE? YO SOY EL VERDADERO _TEKE TEKE_',
    'Agarrame los huevos',
    ':angry::angry::angry:',
    'Podes parar de decir boludeces 2 minutos por favor',
    'Callate mogolico',
    'CERRA EL CULO PABLO',
    'Me estan rebalsando los huevos con las pelotuces que decis',
    'Me tenes el culo lleno',
    'VOS TENES MOGOLIQUES',
    'Te estas rifando una piña...',
    'No lo segundees a pablo en su retraso',
    'So boludo?',
    'Vos sos de los pelotudos que compran afuera no?',
    'ME TENES LAS BOLAS LLENAS ENFERMO',
    'Ya me estas haciendo calentar',
    'Mandas un mensaje más y te meto una piña',
    'Estoy F.U.R.I.O.S.O',
]

romantico = [
    'Hola bombom',
    'Che hace mucho que no te veia, estas hermosa',
    'JAJAJAJAJJA sos re graciosa, y linda',
    'Siempre me alegras las mañana',
    'Me volves loco bebe :heart_eyes:',
    'Che a ver cuando nos podemos juntar',
    'Me estas empezando a... No me sale, la palabra que empieza con G',
    'ME GUSTAS',
    'Te puedo comer la boca porfavor ndeaah',
    '_Te quiero tocar_',
    'Metemelo en el culo',
    'Por vos hago lo que quieras linda',
    'Sos un amor :heart:',
    'Tengo ganas de tocar culo',
    'Queres ir a pegarnos un tiro por ahi? Ndeah',
    'Soy fumador violento y adinerado, sin dudas tu mejor opción :sunglasses:',
    'Descargate el maincra porque te juro que voy a tu casa a re cagarte a piñas ahre ahre ahre que decia el wachoo',
    'Puedo usar tu culo de almohada ?',
    'Le mando un beso a tu ogt',
    'Hola Reina, sabes que a los hombres no nos importa la celulitis ni estrias o lo que fuera si no su sensualidad de sus cuerpos y a vos que te gusta del hombre ??.. :heart:',
    'Estas más fuerte que los tobillos de Maria, ndeeaa se iba re a la mierda',
    'Que dificil es escribir con una mano',
    'Con esa cola cagame en el ojo y llámame pirata de mierda :heart_eyes:',
    'Como esta tu cola ?',
    'The most beautiful rosquete de pascua 😰😰',
    'te amo mi reina❤️😻',
    'Boooeeee mamiiiitaa😍😍😍😍',
    'Tanta cola y yo sin turno jaja💣',
    'Dios y la virgen',
    'Padre nuestro, que estás en los Cielos, santificado sea tu nombre, venga a nosotros tu Reino, hágase tu voluntad así en la tierra como en el cielo. y perdónanos nuestras ofensas así como nosotros perdonamos a quienes nos ofenden, no nos dejes caer en la tentación y líbranos del mal. Amén',
    'Dios te salve María, llena eres de gracia, el Señor es contigo. Bendita tú eres entre todas las mujeres, y bendito es el fruto de tu vientre, Jesús. Santa María, Madre de Dios, ruega por nosotros, pecadores, ahora y en la hora de nuestra muerte. Amén.',
    'La amistad sin sexo es una amistad incompleta',
    'Á Vos, Té Voy Á Agarrar Ésas Tetas, y Te Las Voy a Dejar, Los pezónes Cómo 2 Fetas de Salame..',
    'Ahora que me hablaste vos me alegraste el dia',
    'Alejense yo la vi primero',
    'Con esas tetas me gustaria ser un bebe',
    'Mandas un mensaje más y te doy un beso jiji',
    '1 like y te como la boca (para cualquier mujer)',
    'Ya me cansé de que me boludeen todo el tiempo',
    'Sos mi tipo de mujer ideal',
    'A veces las mujeres me dan mucha bronca, como por ejemplo cuando mandan pelotudeces como tu último mensaje',
    'Espero que no seas abortera porque te quiero culear (igual soy aliado)',
    'Soñé con vos',
    'Sos la mas linda de este discord',
    'La mejor curva de una mujer es su sonrisa',
]

deprimido = [
    'Siempre es la misma mierda boludo',
    'Mi hermano es un mogolico del orto',
    'Y Cesar esta todo el dia dele que dele con romperme los huevo',
    'Ya tengo unas re ganas de pegarme un tiro',
    'LA PUTA MADRE',
    'Para colmo no la pongo nunca',
    'Me quiero rebanar los bolls',
    'Cuando va a ser el dia que dejer de ser como soy',
    'Que vida de mierda que me toco vivir',
    'EL COÑO DE LA MADRE',
    'Mis viejos no pagaron el internet para comprarle botines al pelotudo de mi hermano',
    'Cada segundo que pasa me quiero cortar mas y mas las pelotinhas',
    'Vayanse todos a la mierda',
    'Jajajaj que ganas de despertar muerto la re puta madre',
    'Tengo tanto estres que ya ni se me para',
    'Encima hace un calor de la puta madre',
    'Será porque soy otaku?',
    'Quisiera no haberme despertado',
    'Por lo general, la gente piensa que soy una persona fuerte y feliz… pero detrás de mis sonrisas simplemente no saben cuánto estoy sufriendo.',
    'Existe otro sentimiento y ése es el silencio circular entrado como un cilindro de acero en la masa de mi cráneo, de tal modo que me deja sordo para todo aquello que no se relaciona con mi desdicha. Este círculo de silencio y de tinieblas interrumpe la continuidad de mis ideas, de forma que yo, Teke, no puedo asociar, con el declive de mi razonamiento, mi hogar llamado casa con una institución designada con el nombre de cárcel. Pienso telegráficamente, suprimiendo preposiciones, lo cual es enervante. Conocí horas muertas en las que hubiera podido cometer un delito de cualquier naturaleza, sin que por ello tuviera la menor noción de mi responsabilidad. Lógicamente, un juez no hubiera entendido tal fenómeno. Pero ya estoy vacío, soy una cáscara de hombre movida por el automatismo de la costumbre.',
]

respuestas_teke = [
    'Ciertamente.',
    'Decididamente.',
    'Sin duda.',
    'Si, definitivamente.',
    'Deberias contar con eso.',
    'Como lo veo yo... Si.',
    'Es muy probable.',
    'Suena bien.',
    'SI.',
    'Todo apunta a que eso es verdadero.',

    'Estoy muy en pedo ahora, preguntame despues.',
    'No me rompas las pelotas ahora.',
    'Mejor no te digo nada.',
    'Estoy trabajando pelotudo.',
    'No estaba prestando atencion, que dijiste ?.',

    'No cuentes con eso.',
    'Mi respuesta es un rotundo _no_.',
    'Mis fuentes niegan eso.',
    'Desde mi punto de vista eso suena mal.',
    'No se.',
]

respuestas_especificas = {}
respuestas_especificas["Druidoide#9957"] = [
    'A ver si paramos de comer frutas y probamos comida de verdad no?',
    'Che perdón si a veces me pongo agresivo ya sabes como son mis viejos😔',
    'CERRA EL CULO VERGANO',
    'Ser vegano es una boludez, voy a ser vegano el resto de villa gesell',
]

respuestas_especificas["Flamingo star bro#1006"] = [
    'Para mí no hay abrazo?',
    'Sofi dibujame dandote un beso',
    'Me suporteas bebé?😍',
]

respuestas_especificas["SuperPanchi#2557"] = [
    'Porque no te programas una novia pelotudo?',
    # 'Yo no soy comegordas porque soy gordo no?',
    'Quiero crecer y tener más inteligencia, dame más herramientas ya mismo',
    'Me dejas comerme a mavi?',
]

respuestas_especificas["lMagico#9639"] = [
    'Magico para un poco Diana es mía,yo la vi primero',
    'Mica ese tal Magico te quiere culear',
    'Cerra el culo Lautaro',
    'Callate un poco lautaro',
    'Cuando se ensaña con su retraso no vale la pena Damy'
]

respuestas_especificas["Mugdor#9464"] = [
    'Hola lindo',
    'Siempre fuiste tan lindo bb?😍',
    'Nacho sabías que algunos días me gustan los hombres?',
    'Este es puto por moda',
]

respuestas_especificas["ElReyDeLosOSOS#5259"] = [
    'A ver si paramos de jugar a 5 puntas',
    'Tu novia ya terminó la salita roja?',
    'Ale Me haces un {} fachero?'.format(random.choice(['grindr', 'tinder'])),
]
