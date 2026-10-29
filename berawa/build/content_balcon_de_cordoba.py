# Contenido de la demo Hotel Balcón de Córdoba (es/ca/en/fr). Hechos de balcondecordoba.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Pantea · Doble Superior','Ruzbahan · Deluxe con terraza','Maryam · Junior Suite Real'],
'ca':['Pantea · Doble Superior','Ruzbahan · Deluxe amb terrassa','Maryam · Junior Suite Reial'],
'en':['Pantea · Superior Double','Ruzbahan · Deluxe with terrace','Maryam · Royal Junior Suite'],
'fr':['Pantea · Double Supérieure','Ruzbahan · Deluxe avec terrasse','Maryam · Junior Suite Royale']}
RD={
'es':['En la planta baja, con ventanal enrejado abierto a la fuente del patio del Naranjo, ducha accesible y cama King o dos twin.','Una casita en lo alto de la casa, con cama Queen, bañera, terraza y vistas a la mezquita.','La habitación más espaciosa: 75 m², salón y vestidor, cama King y vistas al patio del naranjo.'],
'ca':['A la planta baixa, amb finestral enreixat obert a la font del pati del Taronger, dutxa accessible i llit King o dos twin.','Una caseta a dalt de la casa, amb llit Queen, banyera, terrassa i vistes a la mesquita.','L\'habitació més espaiosa: 75 m², saló i vestidor, llit King i vistes al pati del taronger.'],
'en':['On the ground floor, with a barred window opening onto the fountain of the Orange Tree patio, accessible shower and a King bed or two twins.','A little house at the top of the building, with a Queen bed, bathtub, terrace and views of the mosque.','The most spacious room: 75 m², living room and dressing room, King bed and views of the orange tree patio.'],
'fr':['Au rez-de-chaussée, avec une fenêtre à grille ouverte sur la fontaine du patio de l\'Oranger, douche accessible et lit King ou deux lits twin.','Une petite maison tout en haut de la bâtisse, avec lit Queen, baignoire, terrasse et vue sur la mosquée.','La chambre la plus spacieuse : 75 m², salon et dressing, lit King et vue sur le patio de l\'oranger.']}
ART={
'hero':('arches',9701,['#f3e4cc','#e7caa0','#b8613a','#8a3f2c','#c8963c']),
'intro':('columns',9702,['#efe3cf','#f6ecda','#c8963c','#9a5a3c','#7a3b2a']),
'r1':('arches',9711,['#f0e0c6','#e4c79c','#b45e38','#7d3a2a','#c4923a']),
'r2':('skyline',9712,['#4a3a52','#e08a5c','#f8cf98','#4a3a50','#352a3e','#231b2a']),
'r3':('columns',9713,['#ece0cb','#f4e9d6','#c48f38','#9a5a3c','#78392a']),
'g1':('arches',9721,['#f2e3ca','#e8cfa4','#b9633b','#843f2d','#c6953b']),
'g2':('hills',9722,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g3':('skyline',9723,['#3c3f66','#e58e5e','#fbd69c','#3b3d62','#2c2e4c','#1d1f33']),
'g4':('columns',9724,['#eee1cc','#f5ead6','#c8903a','#a0603f','#7a3b2a']),
'g5':('waves',9725,['#f3dcb0','#e5a070','#fff0c4','#7ab0c0','#4a88a0','#2f6780','#1d445a']),
'g6':('skyline',9726,['#32406a','#e2885c','#f7cf98','#2c3b60','#202e4a','#151f31'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Balcón de Córdoba · Hotel 4 estrellas en la judería, junto a la Mezquita-Catedral',see_rooms='Ver habitaciones',hero_k='Córdoba · Judería',hero_t='Un balcón sobre Córdoba',hero_s='Una casa centenaria con tres patios, en pleno casco histórico y a pocos pasos de la Mezquita-Catedral.',
 intro_t='Una casa cordobesa con patio del naranjo',intro_p1='Balcón de Córdoba es un hotel de 10 habitaciones repartidas en dos plantas en torno a tres patios, en la calle Encarnación, a pocos pasos de la Mezquita-Catedral.',
 intro_p2='Tiene terraza con vistas a la Mezquita-Catedral, restaurante en el patio del naranjo y más de cien restos arqueológicos repartidos por el edificio. Se reserva por su web oficial o contactando con el hotel.',
 stats=['10 habitaciones','Tres patios','Terraza con vistas','Restos arqueológicos'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de las diez habitaciones, cada una con su propia personalidad.',
 svcs=['Aire acondicionado','WiFi','Terraza con vistas','Restaurante en el patio','Caja fuerte','Minibar','Ascensor','Cunas y camas adicionales'],
 loc_p='Calle Encarnación 8, 14003 Córdoba, en el casco histórico, a pocos pasos de la Mezquita-Catedral.',
 chips=['¿Qué tipos de habitación hay?','¿Hay parking?','¿Cómo es el desayuno?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Balcón de Córdoba · Hotel de 4 estrelles a la jueria, al costat de la Mesquita-Catedral',see_rooms='Veure habitacions',hero_k='Còrdova · Jueria',hero_t='Un balcó sobre Còrdova',hero_s='Una casa centenària amb tres patis, en ple centre històric i a pocs passos de la Mesquita-Catedral.',
 intro_t='Una casa cordovesa amb pati del taronger',intro_p1='Balcón de Córdoba és un hotel de 10 habitacions repartides en dues plantes al voltant de tres patis, al carrer Encarnación, a pocs passos de la Mesquita-Catedral.',
 intro_p2='Té terrassa amb vistes a la Mesquita-Catedral, restaurant al pati del taronger i més de cent restes arqueològiques repartides per l\'edifici. Es reserva per la seva web oficial o contactant amb l\'hotel.',
 stats=['10 habitacions','Tres patis','Terrassa amb vistes','Restes arqueològiques'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres de les deu habitacions, cadascuna amb la seva pròpia personalitat.',
 svcs=['Aire condicionat','WiFi','Terrassa amb vistes','Restaurant al pati','Caixa forta','Minibar','Ascensor','Bressols i llits addicionals'],
 loc_p='Carrer Encarnación 8, 14003 Còrdova, al centre històric, a pocs passos de la Mesquita-Catedral.',
 chips=['Quins tipus d\'habitació hi ha?','Hi ha pàrquing?','Com és l\'esmorzar?','Com es reserva?']),
'en':dict(title='Hotel Balcón de Córdoba · 4-star hotel in the Jewish Quarter, next to the Mosque-Cathedral',see_rooms='See the rooms',hero_k='Córdoba · Jewish Quarter',hero_t='A balcony over Córdoba',hero_s='A centuries-old house with three patios, in the heart of the historic centre and a few steps from the Mosque-Cathedral.',
 intro_t='A Córdoba house with an orange tree patio',intro_p1='Balcón de Córdoba is a hotel of 10 rooms spread over two floors around three patios, on Calle Encarnación, a few steps from the Mosque-Cathedral.',
 intro_p2='It has a terrace with views of the Mosque-Cathedral, a restaurant in the orange tree patio and over a hundred archaeological remains throughout the building. You book through its official website or by contacting the hotel.',
 stats=['10 rooms','Three patios','Terrace with views','Archaeological remains'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the ten rooms, each with its own personality.',
 svcs=['Air conditioning','WiFi','Terrace with views','Restaurant in the patio','Safe','Minibar','Lift','Cots and extra beds'],
 loc_p='Calle Encarnación 8, 14003 Córdoba, in the historic centre, a few steps from the Mosque-Cathedral.',
 chips=['What room types are there?','Is there parking?','What is breakfast like?','How do I book?']),
'fr':dict(title='Hotel Balcón de Córdoba · Hôtel 4 étoiles dans la juiverie, près de la Mosquée-Cathédrale',see_rooms='Voir les chambres',hero_k='Cordoue · Juderia',hero_t='Un balcon sur Cordoue',hero_s='Une maison centenaire avec trois patios, en plein centre historique et à quelques pas de la Mosquée-Cathédrale.',
 intro_t='Une maison cordouane avec patio de l\'oranger',intro_p1='Balcón de Córdoba est un hôtel de 10 chambres réparties sur deux étages autour de trois patios, calle Encarnación, à quelques pas de la Mosquée-Cathédrale.',
 intro_p2='Il dispose d\'une terrasse avec vue sur la Mosquée-Cathédrale, d\'un restaurant dans le patio de l\'oranger et de plus de cent vestiges archéologiques dans le bâtiment. On réserve par son site officiel ou en contactant l\'hôtel.',
 stats=['10 chambres','Trois patios','Terrasse avec vue','Vestiges archéologiques'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des dix chambres, chacune avec sa propre personnalité.',
 svcs=['Climatisation','WiFi','Terrasse avec vue','Restaurant dans le patio','Coffre-fort','Minibar','Ascenseur','Lits bébé et lits supplémentaires'],
 loc_p='Calle Encarnación 8, 14003 Cordoue, dans le centre historique, à quelques pas de la Mosquée-Cathédrale.',
 chips=['Quels types de chambre y a-t-il ?','Y a-t-il un parking ?','Comment est le petit-déjeuner ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@balcondecordoba.com')
D=dict(name='Hotel Balcón de Córdoba',ac='#7a3b2a',ac2='#c8963c',ac2_a11y='#7a4f12',book=BOOK,around=[],foot=FOOT,
 address='Calle Encarnación 8 · 14003 Córdoba',phones=['957 498 478'],emails=['info@balcondecordoba.com'],maps='Hotel Balcón de Córdoba, Calle Encarnación 8, Córdoba',t=T)
META=dict(repo='demo-balcon-de-cordoba',name='Hotel Balcón de Córdoba',legal_name='E8HBC S.L.',registry_ids=['CIF B56393960'],
 url='https://balcondecordoba.com/',domain='balcondecordoba.com',municipality='Córdoba',province='Córdoba',sector='hotel 4 estrellas en casa centenaria',
 read_at='2026-10-29T04:27:00+01:00',created_at='2026-10-29T04:35:00+01:00',built_at='2026-10-29T04:37:00+01:00',audit_date='2026-10-29T04:35:00+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T04:24:11+01:00',url='https://www.google.com/maps/place/Hotel+Balc%C3%B3n+de+C%C3%B3rdoba/@37.8805562,-4.7792074,17z/data=!3m1!5s0xd6d2082ca044069:0xca8d2f6993b80cf1!4m9!3m8!1s0xd6d2082b63eed09:0xa236bc937cfc99fc!5m2!4m1!1i2!8m2!3d37.8805562!4d-4.7792074!16s%2Fg%2F1hc1j81jz'),
 book=dict(mode='mail',email='info@balcondecordoba.com',note='La web del negocio reserva por su web oficial o contactando con el hotel; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel urbano con precedente en demos de esta tanda')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Tiene aire acondicionado?','K02'),('¿A qué hora es el check-in?','K03'),('¿Hay parking?','K04'),('¿Se admiten mascotas?','K05'),('¿Está incluido el desayuno?','K06'),('¿Hay restaurante?','K07'),('¿Dónde está el hotel?','K08'),('¿Es accesible para personas con movilidad reducida?','K09'),('¿Se admiten niños?','K10'),('¿Cómo reservo?','K11'),('¿Cuál es el teléfono?','K12'),('¿Qué historia tiene el edificio?','K13'),('¿Tienen piscina?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11')],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Té aire condicionat?','K02'),('A quina hora és el check-in?','K03'),('Hi ha pàrquing?','K04'),('S\'admeten mascotes?','K05'),('Està inclòs l\'esmorzar?','K06'),('Hi ha restaurant?','K07'),('On és l\'hotel?','K08'),('És accessible per a persones amb mobilitat reduïda?','K09'),('S\'admeten nens?','K10'),('Com reservo?','K11'),('Quin és el telèfon?','K12'),('Quina història té l\'edifici?','K13'),('Teniu piscina?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11')],
'en':[('What room types are there?','K01'),('Is there air conditioning?','K02'),('What time is check-in?','K03'),('Is there parking?','K04'),('Are pets allowed?','K05'),('Is breakfast included?','K06'),('Is there a restaurant?','K07'),('Where is the hotel?','K08'),('Is it accessible for reduced mobility?','K09'),('Are children welcome?','K10'),('How do I book?','K11'),('What is the phone number?','K12'),('What history does the building have?','K13'),('Do you have a swimming pool?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11')],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il la climatisation ?','K02'),('À quelle heure est le check-in ?','K03'),('Y a-t-il un parking ?','K04'),('Les animaux sont-ils admis ?','K05'),('Le petit-déjeuner est-il inclus ?','K06'),('Y a-t-il un restaurant ?','K07'),('Où est l\'hôtel ?','K08'),('Est-il accessible à mobilité réduite ?','K09'),('Les enfants sont-ils admis ?','K10'),('Comment réserver ?','K11'),('Quel est le téléphone ?','K12'),('Quelle histoire a le bâtiment ?','K13'),('Avez-vous une piscine ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11')]}
