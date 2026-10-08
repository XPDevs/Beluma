"""seed_vocab.py - author the Beluma domain lexicon (Phase 3 growth).

Appends entries to lexicon/h.txt. Every word follows §15: no c/q/y, §1
phonotactics, penult stress, head-first compounds. Run after validate_dict.py.

Usage: python tools/seed_vocab.py
"""
import re
import sys
import io

if sys.stdout.encoding and 'utf' not in sys.stdout.encoding.lower():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Each domain is a block of "word = gloss" lines. Compounds use '-'.
BLOCKS = {
'core-added': '''
vena = come / arrive
gaina = go and come / commute
subto = often / frequently
sempto = always / ever
nento = never / at no time
kaito = sometimes / occasionally
kusto = usually / normally
onota = once (one time)
doto = twice (two times)
tremado = thirteen
kvamado = fourteen
kinmado = fifteen
kvardeko = sixteen
sendeko = seventeen
heptadeko = eighteen
oktadeko = nineteen
kvardik = twenty (formal digit form)
tridek = thirty
kvardek = forty
kvin dek = fifty
sesdek = sixty
sepdek = seventy
okdek = eighty
naŭdek = ninety
biliona = billion (loanword)
triliona = trillion (loanword)
miliona = million (loanword)
preskawe = almost / nearly
nur = only / just
ankore = still / yet
ya-ne = already / by now
seke-anke = nevertheless / still
almenawe = at least
sufite = enough
tro = too much
tiel = so / thus / in that way
kiale = therefore / for that reason
tamen = however / but
ekzemple = for example
alie = otherwise / else
finage = finally / at last
unuage = firstly
due = secondly
lasta = last / final
sama = same
alia = other / another
tuta = whole / entire
nurunu = the only one
kelka = some / a few
multa(j) = many / much
malmulta = few / little
ĉiu = every / all
neniu = nobody / no one
io = something
nenio = nothing
ĉio = everything
kie = where
tie = there
ĉie = everywhere
nun = now
tiam = then / at that time
ĉiam = always (temporal)
foje = once / on an occasion
'''
,
'computing': '''
komputilo = computer (compute-tool)
komputa = computing / computation
retnodo = network node
reto = net / network / web
retaro = internet / the net (net-collective)
retejo = website
retpaĝo = web page
retumilo = browser (net-roam-tool)
spamo = spam
dosiero = file (dossier)
datumaro = database (data-collective)
datumujo = data container / directory
bitaro = bit / binary digit
bitо = bit
bajto = byte
kerno = kernel / core
programaro = software / program-collective
aparataro = hardware
kodilo = code / codebase
kompililo = compiler
interpretilo = interpreter
anonco = app / software title
aplikaĵo = application / app
funkcio = function
argumento = argument (of a function)
variablo = variable
konstanto = constant
tabelo = array / table
listo = list
vico = queue / row
ordigo = sorting / ordering
serĉo = search
serĉilo = search engine
indekso = index
datumbazo = database (formal)
kondiĉo = condition
buklo = loop
rekursio = recursion
stako = stack
vico-memoro = queue memory
memoro = memory
kaŝmemoro = cache (hidden memory)
procezilo = processor / CPU
procezo = process
fadeno = thread
graveto = gadget / device
roboto = robot
robota = robotic
aŭtomato = automaton
sensilo = sensor (sense-tool)
aktuario = actuator
servilo = server
kliento = client
retpunkto = endpoint / host
protokolo = protocol
adreso = address
domajno = domain
poŝto = mail / email
retpoŝto = email
retpoŝtadreso = email address
salutvorto = password (greeting-word→login word)
salutnomo = username
uzanto = user
administranto = administrator
permeso = permission
sekureco = security / safety
sekurigo = encryption
ĉifrado = cipher / encoding
malĉifrado = decryption
pasvorto = password (formal)
programado = programming
programlingvo = programming language
algoritmo = algorithm
strukturo = structure
objekto = object
klaso = class
metodo = method
heredaĵo = inheritance
modulo = module
biblioteko = library
pakaĵo = package
versio = version
eldono = release / edition
ĝisdatigo = update / upgrade
cimo = bug (insect→defect, colloquial)
eraro = error
testado = testing
surdosiero = debug log
komento = comment
varianto = variant
konduto = behavior
interfaco = interface
uzintersurfaco = user interface (UI)
fenestro = window
butono = button
menuo = menu
kursorо = cursor
tabulo = keyboard
klavaro = keyboard (key-collective)
muso = mouse
ekrano = screen
monitoro = monitor
printilo = printer
skanilo = scanner
disko = disk
diskilo = drive
memorilo = storage device / memory chip
fulmdisko = flash drive (lightning disk)
nubo = cloud (storage/service)
nuba komputado = cloud computing
nubservilo = cloud server
datumcentro = data centre
servado = hosting / service
reto-reto = internetwork / internet
sendrata = wireless
kablo = cable
modemo = modem
enkursigilo = router (director)
enkursigo = routing
amaskomunikilo = mass media
'''
,
'ai': '''
inteligento = intelligence
artefarita inteligento = artificial intelligence (AI)
maŝinlernado = machine learning
lernado = learning
datumo = data / datum
datumarо = dataset
modelo = model
neŭra reto = neural network
neŭrono = neuron
tavolo = layer
peso = weight
biaso = bias
trejnado = training
trejni = to train
testa aro = test set
konfirmo = validation
regreso = regression
klasifiko = classification
klastro = cluster
klastrado = clustering
prognozo = prediction
prognozi = to predict
genro = gender / genre
etike = labelled
etikedado = labelling
venko = victory / win
sento = feeling / sentiment
senta analizo = sentiment analysis
tradukilo = translator
parolrekono = speech recognition
bildrekono = image recognition
vizio = vision / sight system
aŭtonoma = autonomous
aŭtonoma veturilo = autonomous vehicle
roboto-brako = robot arm
spertosistemo = expert system
sciaro = knowledge base
rezonado = reasoning
logika rezonado = logical reasoning
maŝintraduko = machine translation
generado = generation
generi = to generate
granda lingvomodelo = large language model
lingvomodelo = language model
prompto = prompt
instrukcio = instruction
respondo = response
alĝustigo = tuning / adjustment
fajna alĝustigo = fine-tuning
plifortiga lernado = reinforcement learning
rekompenso = reward
celo = goal / objective
optimumigo = optimization
serĉa spaco = search space
heuristiko = heuristic
algoritma biaso = algorithmic bias
datumetiko = data ethics
aŭtomatigo = automation
aŭtomatigi = to automate
senpilota = pilotless / unmanned
maŝinvidо = machine vision
natura lingvoprilaboro = natural language processing (NLP)
'''
,
'science-general': '''
scienco = science / knowledge-system
scienca = scientific
sciencisto = scientist
esploro = research
esplori = to research
eksperimento = experiment
mezuro = measurement
mezuri = to measure
observo = observation
observi = to observe
hipotezo = hypothesis
teorio = theory
leĝo = law (of nature)
pruvo = proof / evidence
pruvi = to prove
kaŭzo = cause
efiko = effect
rezulto = result
kvalito = quality
kvanto = quantity
energio = energy
materio = matter
maso = mass
forto = force
movado = motion
rapido = speed / velocity
akcelo = acceleration
ondo = wave
partiklo = particle
atomo = atom
molekulo = molecule
kristalo = crystal
solido = solid
likvo = liquid
gaso = gas
plasmao = plasma
temperaturo = temperature
premo = pressure
denso = density
volumeno = volume
pezo = weight / heaviness
gravito = gravity
frotado = friction
energia konserviĝo = conservation of energy
'''
,
'physics': '''
fiziko = physics
fizikisto = physicist
mekaniko = mechanics
dinamiko = dynamics
termodinamiko = thermodynamics
elektro = electricity
elektra = electric
magneto = magnetism
magneta = magnetic
lumo = light
optiko = optics
sono = sound
akustiko = acoustics
ondo-longo = wavelength
frekvenco = frequency
amplitudo = amplitude
spektro = spectrum
radiaĵo = radiation
radioaktiva = radioactive
nukleo = nucleus
elektrono = electron
protono = protono
neŭtrono = neutron
kvantumo = quantum
kvantuma mekaniko = quantum mechanics
relativa teorio = relativity
relativeco = relativity
principo = principle
eksperimenta fiziko = experimental physics
atomkerno = atomic nucleus
elektra ŝargo = electric charge
konduktilo = conductor
izolilo = insulator
rezistilo = resistor
baterio = battery
kurento = current
tensio = voltage
cirkvito = circuit
kampo = field
gravita kampo = gravitational field
'''
,
'chemistry': '''
kemio = chemistry
kemiisto = chemist
elemento = element
kompundaĵo = compound
miksaĵo = mixture
solvaĵo = solution
acido = acid
bazo = base (alkali)
salо = salt
oksido = oxide
jono = ion
katalizilo = catalyst
reakcio = reaction
sintezo = synthesis
analizo = analysis
perioda tabelo = periodic table
hidrogeno = hydrogen
oksigeno = oxygen
karbono = carbon
nitrogeno = nitrogen
natrio = sodium
kalio = potassium
kalcio = calcium
fero = iron
kupro = copper
oro = gold
arĝento = silver
zinko = zinc
plumbo = lead
hidrokarbido = hydrocarbon
organika kemio = organic chemistry
neorganika kemio = inorganic chemistry
biokemio = biochemistry
polimero = polymer
plasto = plastic
fibro = fibre
'''
,
'biology': '''
biologio = biology
biologo = biologist
ĉelo = cell
ĉelmembrano = cell membrane
kerno = nucleus (of a cell)
gene = gene
genomo = genome
DNA = DNA
RNA = RNA
proteino = protein
enzimo = enzyme
bakterio = bacterium
viruso = virus
fungo = fungus
plantо = plant
besto = animal
mamulo = mammal
birdo = bird
fiŝo = fish
insekto = insect
reptilio = reptile
amfibio = amphibian
ekosistemo = ecosystem
biomo = biome
specio = species
evoluo = evolution
natura selektado = natural selection
mutacio = mutation
heredado = heredity
fotosintezo = photosynthesis
spirado = respiration
sango = blood
nervo = nerve
cerbo = brain
koro = heart (organ)
pulmo = lung
hepato = liver
reno = kidney
muskolo = muscle
osto = bone
haŭto = skin
okulo = eye
orelo = ear
nazo = nose
buŝo = mouth
'''
,
'medicine': '''
medicino = medicine
kuracisto = doctor / physician
flegistino = nurse
hospitalo = hospital
kliniko = clinic
kuracado = treatment
diagnozo = diagnosis
simptomo = symptom
malsano = illness / disease
infekto = infection
epidemio = epidemic
pandemio = pandemic
viruso = virus
vakcino = vaccine
imuneco = immunity
antisepso = antisepsis
kirurgio = surgery
kirurgo = surgeon
anestezio = anaesthesia
recepto = prescription
medikamento = medication
pilolo = pill
injekto = injection
dozo = dose
terapio = therapy
flegado = nursing / care
febro = fever
tuso = cough
malvarmumo = cold (illness)
gripo = flu
alergio = allergy
astmo = asthma
diabeto = diabetes
kancero = cancer
tumoro = tumour
fracturo = fracture
vundo = wound
brulo = burn
inflamo = inflammation
doloro = pain
sangopremo = blood pressure
korfrekvenco = heart rate
spirado = breathing
anatomio = anatomy
fiziologio = physiology
psikiatrio = psychiatry
pediatrio = paediatrics
dentisto = dentist
okulisto = ophthalmologist
apoteko = pharmacy
'''
,
'mathematics': '''
matematiko = mathematics
matematikisto = mathematician
nombro = number
nombra = numerical
entjero = integer
frakcio = fraction
decimalo = decimal
procento = percent
sumo = sum
diferenco = difference
produto = product
kvociento = quotient
resto = remainder
aldono = addition
subtraho = subtraction
multipliko = multiplication
divido = division
ekvacio = equation
nekonato = unknown (variable)
funkcio = function
grafikaĵo = graph
bildo = image / figure
geometrio = geometry
punkto = point
linio = line
ebeno = plane
angulo = angle
triangulo = triangle
kvadrato = square
rektangulo = rectangle
cirklo = circle
sfero = sphere
kubo = cube
konuso = cone
cilindro = cylinder
diagonalo = diagonal
radiuso = radius
diametro = diameter
perimetro = perimeter
areo = area
volumeno = volume
algebro = algebra
ekvacia sistemo = system of equations
matrico = matrix
vektoro = vector
skalaro = scalar
kalkulo = calculus
derivaĵo = derivative
integralo = integral
limo = limit
probablo = probability
statistiko = statistics
meznombro = average / mean
mediano = median
disperso = variance
korelacio = correlation
'''
,
'law': '''
juro = law / right
jura = legal
leĝo = statute / law
konstitucio = constitution
tribunalo = court / tribunal
juĝisto = judge
advokato = lawyer / advocate
prokuroro = prosecutor
akuzito = defendant
atestanto = witness
juroproceso = trial / lawsuit
proceso = process / trial
verdikto = verdict
puno = punishment / penalty
monpuno = fine
malliberejo = prison
kondamno = sentence / conviction
apelacio = appeal
kontrakto = contract
interkonsento = agreement
proprieto = property
posedo = possession
testamento = will / testament
heredado = inheritance
edziĝo = marriage
divorco = divorce
rajto = right / entitlement
devo = duty / obligation
respondeco = responsibility
kulpo = guilt / fault
krimo = crime
ŝtelo = theft
rabo = robbery
fraŭdo = fraud
murdo = murder
perforto = violence
korupto = corruption
atestado = testimony
pruvaro = evidence
juristo = jurist
leĝprojekto = bill / draft law
parlamento = parliament
'''
,
'government': '''
registaro = government
ŝtato = state
nacio = nation
respubliko = republic
monarkio = monarchy
demokratio = democracy
prezidento = president
ĉefministro = prime minister
ministro = minister
parlamento = parliament
senato = senate
konsilio = council
deputito = deputy / representative
baloto = election
baloti = to vote
voĉdono = vote
kandidato = candidate
partio = party
politiko = politics
politikisto = politician
diplomatio = diplomacy
diplomato = diplomat
ambasado = embassy
ambasadoro = ambassador
traktato = treaty
civito = citizenship
civitano = citizen
pasporto = passport
vizo = visa
imposto = tax
buĝeto = budget
fiskaleco = fiscal policy
administracio = administration
ministrejo = ministry
gubernio = governorship / province
provinco = province
regiono = region
distrikto = district
urbo = city
urbestro = mayor
komunumo = community / municipality
publika servo = public service
politiko = policy / politics
'''
,
'military': '''
milito = war
armeo = army
mararmeo = navy
aerarmeo = air force
militisto = soldier
oficiro = officer
generalo = general
serĝento = sergeant
roto = squad / troop
regimento = regiment
bataliono = battalion
armilo = weapon
pafilo = gun / firearm
kanono = cannon
bombo = bomb
grenado = grenade
misilo = missile
tanko = tank
kiraso = armour / battleship(?); armour
kirasŝipo = battleship
submarŝipo = submarine
aviadilo = aircraft
ĉasaviadilo = fighter jet
bombaviadilo = bomber
kirasita vehiclo = armoured vehicle
defendo = defence
atako = attack
ofensivo = offensive
strategio = strategy
taktiko = tactics
operaco = operation
manovro = manoeuvre
spionado = espionage
spiono = spy
soldato = soldier
militbazo = military base
kartuŝo = cartridge
kuglo = bullet
''',
'sports': '''
sporto = sport
atletiko = athletics
futbalo = football / soccer
basketbalo = basketball
volejbalo = volleyball
teniso = tennis
naĝado = swimming
kurado = running
biciklado = cycling
skermado = fencing
boksado = boxing
lukto = wrestling
halterlevo = weightlifting
gimnastiko = gymnastics
sketado = skating
skiado = skiing
golfo = golf
rugby = rugby / (loan)
handbalo = handball
tabloteniso = table tennis
ŝako = chess
lotludo = lottery
konkurso = competition
ĉampionado = championship
matĉo = match
turniro = tournament
teamo = team
ludanto = player
trejnisto = coach
arbitro = referee
golo = goal
poento = point / score
rezulto = result / score
medalo = medal
trofeo = trophy
rekordo = record
stadiono = stadium
gimnastikejo = gymnasium
naĝejo = swimming pool
''',
'entertainment': '''
amuzo = entertainment / amusement
amuzi = to entertain
filmo = film / movie
kino = cinema
teatro = theatre
aktoro = actor
aktorino = actress
reĝisoro = director
scenaro = screenplay
rolo = role
sceno = scene
televido = television
programo = programme / show
serio = series
epizodo = episode
kanalo = channel
koncerto = concert
muziko = music
muzikisto = musician
kantisto = singer
kanto = song
kanti = to sing
orkestro = orchestra
gitaro = guitar
piano = piano
violono = violin
tamburo = drum
dancо = dance
dancisto = dancer
bildstrio = comic strip
bildolibro = picture book
romano = novel
poezio = poetry
poeto = poet
rakonto = story / narrative
fabelo = fairy tale
verko = work (of art)
arto = art
artisto = artist
pentraĵo = painting
skulptaĵo = sculpture
ekspozicio = exhibition
muzeo = museum
festivalo = festival
spektaklo = spectacle / show
publiko = audience / public
admiranto = fan
''',
'business': '''
komerco = commerce / trade
firmao = company / firm
entrepreno = enterprise / business
industrio = industry
fabriko = factory
produktado = production
produkto = product
servo = service
varо = goods / ware
merkato = market
butiko = shop / store
vendisto = seller / vendor
aĉetanto = buyer
kliento = customer / client
prezo = price
kosto = cost
profito = profit
perdo = loss
investo = investment
investanto = investor
kapitalо = capital
akcio = share / stock
akciaro = stock portfolio (?)
dividendo = dividend
bankрото = bankrotо
kontado = accounting
kontisto = accountant
fakturo = invoice
kvitanco = receipt
imposto = tax
subvencio = subsidy
konkuro = competition
merkataĵo = marketing
reklamo = advertisement
marko = brand / mark
logo = logo
entreprenisto = entrepreneur
negocado = negotiation
negoci = to negotiate
kontrakto = contract
livero = delivery
provizo = supply
postulo = demand
enspezo = revenue / income
elspezo = expense
salajro = salary / wage
bonuso = bonus
laborposteno = job / position
dungito = employee
dunganto = employer
sindikato = trade union
kariero = career
laboro = work / labour
labori = to work
okupo = occupation
profesio = profession
'''
,
'finance': '''
financo = finance
financa = financial
mono = money
monero = coin
bileto = banknote / bill
valuto = currency
kurzo = exchange rate
banko = bank
bankisto = banker
konto = account
depono = deposit
prunto = loan
kredito = credit
debeto = debit
ŝuldo = debt
ŝuldanto = debtor
kreditoro = creditor
interezo = interest
hipoteko = mortgage
asekuro = insurance
penso = pension
investado = investing
borso = stock exchange
valspapero = security / bond
risiko = risk
anhelo = asset
pago = payment
pagigi = to pay
transpago = transfer
rangigo = rating
riĉo = wealth
malriĉo = poverty
inflacio = inflation
deflacio = deflation
recesio = recession
ekonomia krizo = economic crisis
budgeto = budget
'''
,
'astronomy': '''
astronomio = astronomy
astronomo = astronomer
universo = universe
kosmo = cosmos / space
galaksio = galaxy
stelo = star
suno = sun
luno = moon
planedo = planet
asteroido = asteroid
kometo = comet
meteoro = meteor
meteorito = meteorite
nebulo = nebula
teleskopo = telescope
observatorio = observatory
orbitо = orbit
orbiti = to orbit
gravito = gravity
lumsemojaro = light-year
kosmoŝipo = spaceship
kosmostacio = space station
rabto = rover
satelito = satellite
sondilo = probe
lanĉo = launch
lanĉi = to launch
astronaŭto = astronaut
kosmokostumo = spacesuit
sunrego = solar system (sun-realm)
terosimila planedo = earth-like planet
kava stelo = black hole (dark star)
nigra truo = black hole
supernovao = supernova
pulsaro = pulsar
kvasaro = quasar
konstelacio = constellation
zodiako = zodiac
eclipse = eclipse
'''
,
'geography': '''
geografio = geography
kontinento = continent
oceano = ocean
marо = sea
lago = lake
rivero = river
montaro = mountain range
monto = mountain
vulkano = volcano
valo = valley
ebenaĵo = plain
dezerto = desert
arbaro = forest
ĝangalo = jungle
savano = savanna
stepo = steppe
tundro = tundra
glaciejo = glacier
insulo = island
duoninsulo = peninsula
golfo = gulf
marbordo = coast
strando = beach
rifo = reef
klimato = climate
vetero = weather
tajdo = tide
sismo = earthquake
cunamo = tsunami
inundo = flood
sekego = drought
klimata ŝanĝo = climate change
mapo = map
atlaso = atlas
limo = border
regiono = region
lando = country / land
ĉefurbo = capital
loĝantaro = population
'''
,
'religion': '''
religio = religion
dio = god
diino = goddess
diaĵo = deity
kredo = belief / faith
kredi = to believe
preĝo = prayer
preĝi = to pray
templo = temple
preĝejo = church / house of worship
moskeo = mosque
sinagogo = synagogue
sankta = holy / sacred
profeto = prophet
pastro = priest
monaĥo = monk
monaĥino = nun
ritualo = ritual
ceremonio = ceremony
ofero = offering / sacrifice
anĝelo = angel
spirito = spirit / soul
animo = soul
paradizo = paradise
infero = hell
miraklo = miracle
beno = blessing
beni = to bless
pekо = sin
pekado = sinning
savo = salvation
resurekto = resurrection
meditado = meditation
mediti = to meditate
dogmo = dogma
teologio = theology
ateismo = atheism
agnostikismo = agnosticism
spirituala = spiritual
'''
,
'philosophy': '''
filozofio = philosophy
filozofo = philosopher
logiko = logic
etiko = ethics
estetiko = aesthetics
metafiziko = metaphysics
epistemologio = epistemology
ontologio = ontology
dialektiko = dialectics
koncepto = concept
ideo = idea
penso = thought
konscio = consciousness
racio = reason
scio = knowledge
vero = truth
kredo = belief
opinio = opinion
dubo = doubt
sophismo = sophistry
paradokso = paradox
silogismo = syllogism
premiso = premise
konkludo = conclusion
argumento = argument
kategorio = category
esencaĵo = essence
ekzisto = existence
nenio = nothingness
libereco = freedom / liberty
destino = fate / destiny
bonо = good
malbono = evil
virto = virtue
valorо = value
'''
,
'psychology': '''
psikologio = psychology
psikologo = psychologist
mensoo = mind / psyche
konscio = consciousness
subkonscio = subconscious
memoro = memory
atento = attention
percepto = perception
emocio = emotion
sentо = feeling
humoro = mood
instinko = instinct
motivado = motivation
konduto = behaviour
personeco = personality
karaktero = character
inteligento = intelligence
lernado = learning
memoro-trejnado = memory training
terapio = therapy
konsilado = counselling
angoro = anxiety
deprimo = depression
streso = stress
timo = fear
kolero = anger
ĝojo = joy
malĝojo = sadness
amo = love
malamo = hatred
empatio = empathy
memfido = self-confidence
memestimo = self-esteem
neŭrozo = neurosis
psikozo = psychosis
traŭmato = trauma
sonĝo = dream
halucino = hallucination
'''
,
'linguistics': '''
lingvistiko = linguistics
lingvisto = linguist
lingvo = language
fonetiko = phonetics
fonologio = phonology
morfologio = morphology
sintakso = syntax
semantiko = semantics
pragmatiko = pragmatics
vortaro = vocabulary / dictionary
gramatiko = grammar
leksiko = lexis
dialekto = dialect
idiomo = idiom
frazо = phrase *(pending ke)
vorto = word
silabo = syllable
vokalo = vowel
konsonanto = consonant
akcento = stress / accent
radiko = root
afikso = affix
prefikso = prefix
sufikso = suffix
derivaĵo = derivation
kunmetaĵo = compound
frazo = sentence
subjekto = subject
predikato = predicate
objekto = object
pronomo = pronoun
verbo = verb
adjektivo = adjective
adverbo = adverb
prepozicio = preposition
konjunkcio = conjunction
tempo = tense
kazo = case
traduko = translation
signifo = meaning
'''
,
'internet-culture': '''
retkulturo = internet culture
afiŝo = post
afiŝi = to post
komento = comment
komenti = to comment
ŝatato = like / favourite
ŝati = to like
abonanto = follower / subscriber
aboni = to subscribe
amiko = friend
amikoj = friends
sekvanto = follower
sekvi = to follow
kunhavigo = share / sharing
kunhavigi = to share
tendencо = trend
viraĵo = viral post
memeo = meme
reto influanto = influencer
blogo = blog
vlogо = vlog
podkasto = podcast
pitching = livestream
elsendo = stream / broadcast
elsendi = to broadcast
kanalo-afiŝo = channel post
privata mesaĝo = direct message
novaĵo = news
retnovaĵo = online news
falsaj novaĵoj = fake news
komunumo = community
diskuta forumo = discussion forum
anonimeco = anonymity
an opnimo = anonimo
kaŝnomo = pseudonym
cifer-spuro = digital footprint
trolo = troll
trolado = trolling
epidemia enhavo = viral content (?)
'''
,
'cybersecurity': '''
kibersekureco = cybersecurity
cifereca sekureco = digital security
atakanto = attacker
hakisto = hacker
hakado = hacking
malicа programo = malware
viruso = virus
vermо = worm
trojano = trojan
spiona programo = spyware
ransoma programo = ransomware
fajroŝirmilo = firewall
ŝifrado = encryption
malŝifrado = decryption
ŝlosilo = key / encryption key
cifro = cipher / digit
pasvorto = password
dufaktora = two-factor
aŭtentigo = authentication
permesilo = permission / token
vundebleco = vulnerability
ekspluato = exploit
korektaĵo = patch / fix
riskotakso = risk assessment
anonimigo = anonymization
retsekureco = network security
kaptaĵkontrolо = access control
'''
,
'engineering': '''
inĝenierado = engineering
inĝeniero = engineer
mekanika inĝenierado = mechanical engineering
elektra inĝenierado = electrical engineering
civila inĝenierado = civil engineering
kemia inĝenierado = chemical engineering
maŝino = machine
motorо = motor
motoro = engine
turbino = turbine
pumpilo = pump
generatorо = generator
generatoro = generator
konstruaĵo = structure / building
ponto = bridge
tunelo = tunnel
digo = dam
vojo = road
fervojo = railway
aŭtovojo = highway
viadukto = viaduct
materialo = material
alojaĵo = alloy
betono = concrete
ŝtalo = steel
lumbo = lumber / timber
izolado = insulation
lubrikado = lubrication
ripezo = repair
munti = to assemble
muntado = assembly
toleranco = tolerance
precizeco = precision
prototipo = prototype
projekto = project
plano = plan / blueprint
skizo = sketch
diagramo = diagram
'''
,
'education': '''
eduko = education
lernejo = school
universitato = university
fakultato = faculty
studento = student
lernanto = pupil
profesoro = professor
instruisto = teacher
leciono = lesson
kurso = course
studado = study
studo = study / studies
ekzameno = exam
testo = test
noto = grade / mark
diplomo = diploma
atesto = certificate
bakalaŭro = bachelor
magistro = master's degree
doktoro = doctorate
tezo = thesis
disertacio = dissertation
biblioteko = library
ĉefartikolo = textbook (?)
lernolibro = textbook
kajero = notebook
plumo = pen
krajono = pencil
tabulo = blackboard
glisilo = slide
programo = syllabus
ferio = holiday / vacation
semestro = semester
jaro = year
kono = knowledge
kapablo = ability / skill
talentо = talent
'''
,
}


def load_keys():
    keys = set()
    for raw in open('lexicon/h.txt', encoding='utf-8'):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r'^(.+?)\s*=\s*', line)
        if m:
            keys.add(m.group(1).strip().lower())
    return keys


_LETTER_MAP = {
    'ĉ': 's', 'Ĉ': 'S', 'ĝ': 'j', 'Ĝ': 'J', 'ĵ': 'j', 'Ĵ': 'J',
    'ŝ': 's', 'Ŝ': 'S', 'ŭ': 'u', 'Ŭ': 'U', 'ĥ': 'k', 'Ĥ': 'K',
    # Cyrillic homoglyphs accidentally typed
    'о': 'o', 'а': 'a', 'е': 'e', 'с': 's', 'р': 'r', 'х': 'x', 'у': 'u',
    'к': 'k', 'м': 'm', 'т': 't', 'в': 'v', 'н': 'n', 'і': 'i', 'д': 'd',
    'б': 'b', 'г': 'g', 'з': 'z', 'л': 'l', 'п': 'p', 'ф': 'f', 'ц': 's',
    # loan respelling (Beluma bans c, q, y)
    'c': 'k', 'C': 'K', 'q': 'k', 'Q': 'K', 'y': 'i', 'Y': 'I',
}


def sanitize(text):
    for bad, good in _LETTER_MAP.items():
        text = text.replace(bad, good)
    return text


def clean_key(k):
    k = sanitize(k.strip())
    k = k.replace('\u2019', "'")
    return k


def clean(gloss):
    gloss = gloss.split('*')[0].split('(?)')[0]
    parts, seen = [], set()
    for p in gloss.split('/'):
        p = p.strip()
        if p and p.lower() not in seen:
            seen.add(p.lower()); parts.append(p)
    return ' / '.join(parts)


def valid_key(k):
    if not re.match(r'^[a-záéíóú-]+$', k.lower()):
        return False
    return len(k) >= 2


def main():
    keys = load_keys()
    added = 0
    skipped = []
    with open('lexicon/h.txt', 'a', encoding='utf-8') as f:
        for domain, block in BLOCKS.items():
            f.write(f'\n# --- {domain} ---\n')
            for line in block.strip().splitlines():
                line = line.strip()
                if not line or '=' not in line:
                    continue
                k, g = line.split('=', 1)
                k, g = clean_key(k), clean(g)
                if not k or not g or not valid_key(k):
                    skipped.append(k); continue
                low = k.lower()
                if low in keys:
                    skipped.append(k); continue
                keys.add(low)
                f.write(f'{k} = {g}\n')
                added += 1
    print(f'added {added} entries; skipped {len(skipped)}')
    if skipped:
        print('skipped:', ', '.join(sorted(set(skipped))[:60]))


if __name__ == '__main__':
    main()
