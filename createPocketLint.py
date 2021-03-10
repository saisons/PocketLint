#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:36:35 2021
@author: saisons
"""
import csv#Let's import some shit
import datetime
from datetime import date
import random
from random import randrange
import string#that's the end of the import
todays_date = date.today()#define today's date for current year calculation
epoch = randrange(1,4)#currently each individual has a 1/4 chance of being born in the future
if epoch == 4:
    thisYear = randrange(2060,42000)#assign the current year for time travelers
else:
    thisYear = todays_date.year#define the current year for age calculation
ageMin = 13 # set the minimum possible age here
ageMax = 120 #set the maximum possible age here
minBirthYr = thisYear-ageMin#set min birth year - this is used to avoid generating any profiles younger than the typical social media minimum TOS age.
maxBirthYr = thisYear-ageMax#set max birth year
streets = "ukStreets.csv"#filename of street database csv (currently pulled from a 1k list of random UK street names)
pets = "petNames.csv"#filename of pet name csv (currently pulled from Seattle pet licenses)
names = "firstNames.csv"#filename of firstNames
cars = "carMakes.csv"#filename of list of care makes, UK and US, current & defunt major
colours = "colours.csv"#filename of colours. this could be a list here, but there's more user flexibility to add a large range of arty colours
albums = "albums.csv"#list of top selling albums of all time
films = "films.csv"#combined lists from wikipedia net of some
jobs = "jobs.csv"#list of occupations from https://www.careerdimension.com/sampleoccupations/fulloccupationlist.cfm
animals = "animals.csv"#list of common animal names
countries = "countries.csv"#list of countries
surnames = "surnames.csv"#list of surnames
religions = "religions.csv"#list of faiths/philosophies
politics = "politics.csv"#list of joke political parties
ailments = "ailments.csv"#list of common medical ailments
pokedex = "pokedex.csv"#list of pokemon
phobos = "phobos.csv"#list of common fears
library = "books.csv"#list of books
smilies = "emoji.csv"#list of popular emojis
poesy = "poesy.csv"#list of popular poems
forest = "forest.csv"#list of trees
planets = "planets.csv"#list of planets
hobbies = "hobbies.csv"#list of hobbies
sodas = "sodas.csv"#list of sodas
allergies = "allergies.csv"#list of common allergies
languages = "languages.csv"#list of spoken languages
conlangs = "conlangs.csv"#list of constructed languages
proglangs = "proglangs.csv"#list of programming languages
socials = "socials.csv"#list of social media networks, including defunct
cryptids = "cryptids.csv"#list of cryptids
scps = "scps.csv"#list of SCPs
foods = "foods.csv"#list of favourite foods
icecream = "icecream.csv"#list of Ben & Jerry's flavours
songs = "songs.csv"#list of popular songs from Rolling Stone top 500
simps = "simpsons.csv"#list of Simpsons characters
flowers = "flowers.csv"#list of flowers
heroes = "heroes.csv"#list of superheroes
villains = "villains.csv"#list of supervillians
hols = "holidays.csv"#list of most celebrated holidays
diets = "diets.csv"#list of dietary restrictions
elems = "elements.csv"#peroid table of the elements+
sports = "sports.csv"#list of spectator sports
clearances = "clearances.csv"#list of security clearances
cuddlepuddle = "fursonas.csv"#list of popular fursona species
martial = "martialarts.csv"#list of martial arts
superpowers = "superpowers.csv"#list of stupid superpowers
homestar = "homestar.csv"#list of homestar runner characters
schools = "schools.csv"#list of fictional schools
pajamas = "sleepwear.csv"#list of pajamas
certs = "certs.csv"#list of professional certifications (currently us only)
postnoms = "postn.csv"
### Lists below this line are defined in code rather than in a csv ###
bloods = ["O","A","B","AB"]#list of blood types
rhs = ["\u2099\u2091\u1d4d","\u209A\u2092\u209b","\u2099\u1D64\u2097\u2097"]#list of rh factors
genders = ["male", "female", "nonbinary", "masc", "femme", "complicated", "none"]#user can expand this as much as possible
titles = ["Dr.","Hon.","Prof.","Rev.","Rt. Hon.","St.","Lt.","Captain","Pvt.","Col.","Cpl","Lcpl","General","Admiral","Major","Ensign","Warrant Officer","Chief"]#list of prefix titles
suffixes = ["Esq.","Jr.","Sr.","II","III","IV","V"]#list of name suffix titles
doneness = ["Blue - 0","Rare - 1","Medium Rare - 2","Medium - 3","Medium Well - 4","Well Done - 5","Shoe Leather - 6"]#assign steak quality
toasts = ["White - 0","2","3","4","5","Burnt - 6","done on one side"]#list of toast qualities
pronouns = ["he/him","he/they","she/her","she/they","they/them","ey/em","xe/xir","any","he/were","she/wif"]#list of pronouns. if you don't like it, fuck off
zodiacs = [(120, 'Capricorn'), (218, 'Aquarius'), (320, 'Pisces'), (420, 'Aries'), (521, 'Taurus'),
           (621, 'Gemini'), (722, 'Cancer'), (823, 'Leo'), (923, 'Virgo'), (1023, 'Libra'),
           (1122, 'Scorpio'), (1222, 'Sagittarius'), (1231, 'Capricorn')]#dict of zodiac signs
cafe = ["Tea","Coffee","Monster","Earl Grey, hot","Bovril"]#list of hot drinks
teaql = ["Black - A","B","C","D","E","White - F"]#list of tea qualities
seasons = ["Winter","Spring","Summer","Autumn"]#list of seasons
edu = ["Primary School","Secondary School","Undergraduate","Masters","Post-Graduate","Post Grad - ABD","Doctoral","Post-Doc",]
height = randrange(54,272)#assign height
criminal = randrange(1,12)#assign criminal record status.
arrested = randrange(1,3)#assign arrested status
wants = randrange(1,50)#assign wanted level
systems = randrange(1,17)#assign number of systems who want person
networth = random.random()#assign networth as a fractional bitcoin
bitcoinval = float(40566)#define bitcoin value as float
poundtoyen = 151.63#set estimated GBP>YEN conversion
creditscore = randrange(300,850)#assign credit score
networth = networth*bitcoinval*poundtoyen#convert networth to bitcoin value then to Yen
networth = "¥{:.2f}".format(networth)#format networth
idNum = ''.join(random.choice('0123456789ABCDEF') for i in range(16))#set faux SSN/TIN/NINO
### Assign Qualities ###
year = randrange(maxBirthYr,minBirthYr)#assign a random birth year
age = thisYear-year#calculate age
firstInit = random.choice(string.ascii_letters).upper()#assign a first initial
lastInit = random.choice(string.ascii_letters).upper()#assign a second initial
gender = random.choice(list(genders))#assign a random gender
pronoun = random.choice(list(pronouns))#assign random pronouns. this isn't currently linked to gender, not that it necessarily needs to be
blood = random.choice(list(bloods))#assign blood type
rh = random.choice(list(rhs))#assign rh factor
heightM = height / 100#height in meters
heightM2 = heightM ** 2#square height in meters
bmi = randrange(16,35)#set BMI to drive mass calculation
weight = bmi * heightM2#fast inverse bmi
formWeight = "{:.2f}".format(weight)#format mass
formHeight = "{:.2f}".format(height)#format height
steak = random.choice(list(doneness))#set steak quality
toast = random.choice(list(toasts))#set toast quality
caf = random.choice(list(cafe))#assign favourite hot beverage
tea = random.choice(list(teaql))#set tea quality
season = random.choice(list(seasons))#assign favourite season
education = random.choice(list(edu))#assign education
if criminal == 12:#set criminality and record
    crimrec = "Classified: Special Access Only"
    arrestrec = "Classified: Special Access Only"
elif criminal >= 9:
    crimrec = "Criminal Convictions on File"
    arrestrec = "Arrest Record on File"
else:
    crimrec = "No Criminal Convictions"
    if arrested == 3:
        arrestrec = "Arrest Record on File"
    else:
        arrestrec = "No Arrests on File"
if wants == 50:
    wanted = "Active Warrants on: "+systems+" systems."
else:
    wanted = "No Active Warrants."
### DOB and Zodiac ###
month = randrange(1,12)#assign a birth month
day = randrange(1,31)#assign a birth day (note: this currently doesn't check if the month has 28-31 days. Bonus points if you end up with a Leap+ Day Birthday)
zeroFilledDay = str(day).zfill(2)
datetime_object = datetime.datetime.strptime(str(month), "%m")#convert month number to month format
month_name = datetime_object.strftime("%b")#convert month number to short month
def get_zodiac_of_date():#define zodiac function
    signstr = str(month)+str(zeroFilledDay)
    signstr = int(signstr)
    for z in zodiacs:
        if signstr <= z[0]:
            return z[1]
zodiac = get_zodiac_of_date()#find star sign
zodiac = str(zodiac)#assign star sign
### Assign Characteristics from csv files ###
with open(streets) as s:#open streets file
    reader = csv.reader(s)
    streetName = random.choice(list(reader))[0]#assign a random street name and convert from list to str
with open(pets) as p:#open pets file
    reader = csv.reader(p)
    petName = random.choice(list(reader))[0]#assign a random pet name and convert from list to str
with open(names) as n:#open firstnames file
    reader = csv.reader(n)
    firstName = random.choice(list(reader))[0]#assign a random friend's first name
with open(names) as n:#open firstnames file
    reader = csv.reader(n)    
    firstnm = random.choice(list(reader))[0]
with open(names) as n:#open firstnames file
    reader = csv.reader(n)
    secondnm = random.choice(list(reader))[0]
with open(cars) as m:#open car make file
    reader = csv.reader(m)
    carMake = random.choice(list(reader))[0]#assign a random first car
with open(colours) as c:#open colour list
    reader = csv.reader(c)
    colour = random.choice(list(reader))[0]#assign a random favourite colour
with open(albums) as al:#open top selling albums file
    reader = csv.reader(al)
    album = random.choice(list(reader))[0]#assign a random favourite album
with open(films) as fi:
    reader = csv.reader(fi)
    film = random.choice(list(reader))[0]#assign a random favourite film
with open(jobs) as jo:
    reader = csv.reader(jo)
    job = random.choice(list(reader))[0]#assign a career
with open(animals) as an:
    reader = csv.reader(an)
    animal = random.choice(list(reader))[0]#assign a favourite animal
with open(countries) as co:
    reader = csv.reader(co)
    country = random.choice(list(reader))[0]#assign a country of origin
    country = str(country).strip()
citizenships = randrange(1,8)#set number of citizenships
citlist = [ ]
if citizenships > 1:
    i = 0
    while i < citizenships:
        with open(countries) as co:
            reader = csv.reader(co)
            citizenship = random.choice(list(reader))[0]#define additional citizensihps
            citlist.append(citizenship)
        i += 1
    citlist = ', '.join(citlist)
else: citlist.append("None")
cleared = randrange(1,10)#Assign whether the person has a security clearance
if int(cleared) < 9:
    clearance = "None"#Set no clearance for uncleared individuals
else:
    with open(clearances) as cl:
        reader = csv.reader(cl)
        clearance = random.choice(list(reader))[0]#assign a security clearance
with open(schools) as sch:
    reader = csv.reader(sch)
    school = random.choice(list(reader))[0]#assign a school
with open(surnames) as su:
    reader = csv.reader(su)
    surname = random.choice(list(reader))[0]#assign a mother's maiden name
with open(surnames) as su:
    reader = csv.reader(su)
    surname2 = random.choice(list(reader))[0]#assign a friend's surname
with open(surnames) as su:
    reader = csv.reader(su)
    thirdnm = random.choice(list(reader))[0]# assign a 1st surname
with open(surnames) as su:
    reader = csv.reader(su)
    fourthnm = random.choice(list(reader))[0]#assign 2nd surname
with open(religions) as re:
    reader = csv.reader(re)
    philosophy = random.choice(list(reader))[0]#assign a philosophy
with open(politics) as po:
    reader = csv.reader(po)
    politics = random.choice(list(reader))[0]#assign a political party
with open(ailments) as ai:
    reader = csv.reader(ai)
    ailment = random.choice(list(reader))[0]#assign an ailment
with open(pokedex) as pkdx:
    reader = csv.reader(pkdx)
    pokemon = random.choice(list(reader))[0]#assign pokemon
with open(phobos) as ph:
    reader = csv.reader(ph)
    phobia = random.choice(list(reader))[0]#assign common phobia
with open(library) as li:
    reader = csv.reader(li)
    tome = random.choice(list(reader))[0]#assign favourite book
with open(smilies) as sm:
    reader = csv.reader(sm)
    smile = random.choice(list(reader))[0]#assign favourite emoji
with open(poesy) as poe:
    reader = csv.reader(poe)
    poem = random.choice(list(reader))[0]#assign favourite poem
with open(forest) as fore:
    reader = csv.reader(fore)
    tree = random.choice(list(reader))[0]#assign favourite tree
with open(planets) as pl:
    reader = csv.reader(pl)
    planet = random.choice(list(reader))[0]#assign birth planet
with open(hobbies) as ho:
    reader = csv.reader(ho)
    hobb1 = random.choice(list(reader))[0]#assign favourite hobby
with open(hobbies) as ho:
    reader = csv.reader(ho)
    hobb2 = random.choice(list(reader))[0]#assign additional hobbies
with open(hobbies) as ho:
    reader = csv.reader(ho)
    hobb3 = random.choice(list(reader))[0]#assign additional hobbies
with open(sodas) as so:
    reader = csv.reader(so)
    soda = random.choice(list(reader))[0]#assign favourite soda
with open(allergies) as al:
    reader = csv.reader(al)
    allergy = random.choice(list(reader))[0]#assign allergies
with open(languages) as la:
    reader = csv.reader(la)
    lang1 = random.choice(list(reader))[0]#assign 1st spoken lang
with open(languages) as la:
    reader = csv.reader(la)
    lang2 = random.choice(list(reader))[0]#assign 2nd spoken lang
with open(languages) as la:
    reader = csv.reader(la)
    lang3 = random.choice(list(reader))[0]#assign 3rd spoken lang
with open(conlangs) as co:
    reader = csv.reader(co)
    conlang1 = random.choice(list(reader))[0]#assign 1st spoken conlang
with open(conlangs) as co:
    reader = csv.reader(co)
    conlang2 = random.choice(list(reader))[0]#assign 2nd spoken conlang
with open(conlangs) as co:
    reader = csv.reader(co)
    conlang3 = random.choice(list(reader))[0]#assign 3rd spoken conlang
with open(proglangs) as pr:
    reader = csv.reader(pr)
    proglang = random.choice(list(reader))[0]#assign favourite programming language
with open(socials) as soc:
    reader = csv.reader(soc)
    social = random.choice(list(reader))[0]#assign favourite social network
with open(cryptids) as cr:
    reader = csv.reader(cr)
    cryptid = random.choice(list(reader))[0]#assign favourite crypid
with open(scps) as scps:
    reader = csv.reader(scps)
    scp = random.choice(list(reader))[0]#assign favourite scp
with open(foods) as foo:
    reader = csv.reader(foo)
    food = random.choice(list(reader))[0]#assign favourite food
with open(icecream) as ic:
    reader = csv.reader(ic)
    icecream = random.choice(list(reader))[0]#assign favourite ice cream flavour
with open(songs) as son:
    reader = csv.reader(son)
    song = random.choice(list(reader))[0]#assign favourite song
with open(elems) as el:
    reader = csv.reader(el)
    ele = random.choice(list(reader))[0]#assign favourite element
with open(hols) as hol:
    reader = csv.reader(hol)
    hol = random.choice(list(reader))[0]#assign favourite holiday
with open(simps) as sim:
    reader = csv.reader(sim)
    simp = random.choice(list(reader))[0]#assign favourite simpsons character
with open(flowers) as flow:
    reader = csv.reader(flow)
    flower = random.choice(list(reader))[0]#assign favourite flower
with open(heroes) as her:
    reader = csv.reader(her)
    hero = random.choice(list(reader))[0]#assign favourite superhero
with open(villains) as vil:
    reader = csv.reader(vil)
    villain = random.choice(list(reader))[0]#assign favourite superhero
with open(diets) as di:
    reader = csv.reader(di)
    diet = random.choice(list(reader))[0]#assign dietary restrictions
with open(sports) as sp:
    reader = csv.reader(sp)
    sport = random.choice(list(reader))[0]#assign favourite spectator sport
with open(cuddlepuddle) as cu:
    reader = csv.reader(cu)
    fursona = random.choice(list(reader))[0]#assign fursona
with open(martial) as ma:
    reader = csv.reader(ma)
    martialart = random.choice(list(reader))[0]#assign a fighting style
with open(superpowers) as su:
    reader = csv.reader(su)
    power = random.choice(list(reader))[0]#assign a superpower
with open(homestar) as ho:
    reader = csv.reader(ho)
    strongbad = random.choice(list(reader))[0]#assign a homestar runner character
with open(pajamas) as pjs:
    reader = csv.reader(pjs)
    pajama = random.choice(list(reader))[0]#assign pajamas
with open(certs) as ce:
    reader = csv.reader(ce)
    certs = random.choice(list(reader))[0]#assign professional certification
with open(postnoms) as po:
    reader = csv.reader(po)
    postnom = random.choice(list(reader))[0]#assign professional certification
certified = randrange(1,10)#
if certified > 6:
    postnom = ", "+postnom
else:
    postnom = ""
furry = randrange(1,3)#assign if person is a furry
if furry > 1:
    fursona = fursona#why are 2/3 of people furries? because there aren't good stats and I said so.
else:
    fursona = "None"#set no fursona
hastitle = randrange(1,5)#assign if person has a title
if hastitle <= 2:#assign a title with 40% distribution
    title = random.choice(list(titles))#assign a title
    title = title+" "
else:
    title = ""#assign no title
hassuffix = randrange(1,3)#assign if a person has a suffix
if hassuffix == 1:#assign suffic with 33% distribution
    suffix = random.choice(list(suffixes))#assign suffix
    suffix = ", "+suffix
else:
    suffix = ""#assign a suffix
child_bit = random.getrandbits(1)#assign if person has children - pick a random bit
childers = bool(child_bit)#convert bit to boolean
kids = str(randrange(1,6))#assign a number of children
partner = random.getrandbits(1)#assign if a person is in relationship - pick a random bit
partnered = bool(partner)#convert bit to boolean
spouses = str(randrange(1,8))#assign a number of partners
allergic = random.getrandbits(1)#assign if person has allergies - pick a random bit
allergic = bool(allergic)#convert bit to boolean
if allergic == True:#evaluate for allergies
    allergicVal = "Known allergies: "+allergy+"."#assign allergies
else:
    allergicVal = "Known allergies: none."#assign no allergies
belief = random.getrandbits(1)#assign if person is believer - pick a random bit
belief = bool(belief)#convert bit to boolean
if belief == True:#evaluate for beliefs
    faithInt = "Beliefs: "
    faithVal = philosophy#assign belief system
else:
    faithInt = "Beliefs: "
    faithVal = "No strong philosophical or religious beliefs."#assign no belief system
if partnered == True:#evaluate if person is in a relationship
    spouseVal = spouses#set number of partners
    spouseCls = " loving partner(s)"
else:
    spouseVal = "Single"#assign no partners
    spouseCls = ""
if childers == True:#evaluate if person has chlidren
    childCount =  kids#assign number of children
    childSuf = " children"
else:
    childCount = "None"#assign no chlidren
    childSuf = ""
hobbies = randrange(1,3)#assign number of hobbies
if hobbies == 1:
    hobby = hobb1+"."#assign hobby1
elif hobbies == 2:
    hobby = hobb1+" and "+hobb2+"."#assign hobby2
else:
    hobby = hobb1+", "+hobb2+" and "+hobb3+"."#assign hobby3
conlans = randrange(1,3)#assign number of spoken conlangs
if conlans == 1:#evaluate number of conlangs
    conlanglst = conlang1#assign one conlang
elif conlans == 2:#evaluate number of conlangs
    conlanglst = conlang1+" and "+conlang2#assign two conlangs
else:#evaluate number of conlangs
    conlanglst = conlang1+", "+conlang2+" and "+conlang3#assign three conlangs
langs = randrange(1,3)#assign number of spoken languages
if langs == 1:#evaluate number of spoken languages
    lang = lang1+", "+conlanglst#assign language and append conlangs
elif langs == 2:#evaluate number of spoken languages
    lang = lang1+", "+lang2+", "+conlanglst#assign two languages and append conlangs
else:#evaluate number of spoken languages
    lang = lang1+", "+lang2+" , "+lang3+", "+conlanglst#assign three languages and append conlangs
print("###### Your Results Are: ######")#let's print that shit
print("Name: "+title+firstnm+" "+secondnm+" "+thirdnm+"-"+fourthnm+suffix+postnom+".")
print("Citizen ID Num: "+idNum)
print("First initial: "+firstnm[0]+","+" Last initial: "+thirdnm[0]+".")
print("Gender: "+gender+". Pronouns: "+pronoun+".")
print("DOB: "+str(month_name),str(day)+", "+str(year)+" - Age: "+str(age), "years.")
print("Birthplace: "+planet+".")
print("Primary Citizenship: "+country)
print("Associate Citizenship(s): "+str(citlist)+".")
print("Star Sign: "+zodiac+".")
print("------------------------------------------------")
print("Height: "+str(formHeight)+" cm.")
print("Mass:  "+str(formWeight)+" kg.")
print(faithInt+faithVal+".")
print("Political Party membership: "+politics)
print("Relationship Status: "+spouseVal+spouseCls+". ")
print("Children: "+childCount+childSuf+".")
print(allergicVal)
print("Blood type: "+blood+" "+rh)
print("You are afraid "+phobia+".")
print("Prexisting Health Conditions: "+ailment+" controlled with diet & medication.")
print("Dietary Restrictions: "+diet+".")
print("Hobbies: "+hobby)
print("Languages: "+lang+".")
print("Occupation: "+job+".")
print("Security Clearance: "+clearance+".")
print("Criminal Record: "+crimrec+".")
print("Arrest Record: "+arrestrec+".")
print("Warrants: "+wanted+".")
print("Networth: "+networth+".")
print("Credit Score: "+str(creditscore)+".")
print("Professional Assn: "+certs)
print("Highest Education Achieved: "+education+".")
print("Last School Attended: "+school+".")
print(str("------------------------------------------------"))
print(str("Your:"))
print("        Childhood home was on "+streetName+".")
print("        First pet's name was "+petName+".")
print("        Childhood best-friend's name is "+str(firstName),surname2+".")
print("        First vehicle:  "+carMake+".")
print("        Mother's maiden name: "+surname+".")
print("        Fursona: "+fursona+".")
print("        Fighting Style: "+martialart+".")
print("        Superpower is: "+power+".")
print("------------------------------------------------")
print("Your favourite/preferred:")
print("        Colour is: "+colour+".")
print("        Food is: "+food+".")
print("        Ice Cream is: "+icecream+".")
print("        Poem is: "+poem+".")
print("        Flower is: "+flower+".")
print("        Sleepwear is: "+pajama+".")
print("        Homestar Runner Character: "+strongbad+".")
print("        Superhero is: "+hero+".")
print("        Social Media Network is: "+social+".")
print("        Season is: "+season+".")
print("        Tree is: "+tree+".")
print("        Emoji is: "+smile+".")
print("        Spectator Sport: "+sport+".")
print("        Cryptid is: "+cryptid+".")
print("        Simpsons Character is: "+simp)
print("        Element is: "+ele)
print("        Song is: "+song+".")
print("        Holiday is: "+hol+".")
print("        SCP is: "+scp+".")
print("        Album is: "+album+".")
print("        Steak doneness: "+steak+".")
print("        Toast Doneness: "+toast+".")
print("        Hot Beverage: "+caf+".")
print("        Tea/Coffee Colour: "+tea)
print("        Soda is: "+soda+".")
print("        Movie is: "+film+".")
print("        Programming Language is: "+proglang+".")
print("        Animal is: "+animal+".")
print("        Pokemon is: "+pokemon+".")
print("        Book is: "+tome+".")
print("------------------------------------------------")