import time
import random
import pyttsx3
import webbrowser
from subprocess import *
droid = pyttsx3.init()



wesh = 0.07
print("""
Bienvenue chez baydar. Vous pouvez lui poser des questions à propos de lui, mais aussi
lui demander de faire des calculs et de corriger des textes. Cependant, vous devez lui parler en minuscules 
et sans faute d'orthographe. Si vous voulez voir l'intégralité de ses fonctionnalités, tapez /help
""")
prenom = input("Quelle est votre prenom: ")
print("""
Debus du chat...""")

time.sleep(1)

# variables de question
bonjour = ["bonjour", "salut", "wesh", "coucou", "hey", "hello", "slt", "wsh", "salam", "slm", "salamou3alaykoum"]
sex = ["sexuelle", "sex", "baiser", "amour", "viol", "violer", "zizi", "penis", "vagin", "chatte", "uterus", "sperm", "spermatozoïde", "spz"]
appelle = ["comment tu t'appelle", "comment t'appelle tu", "t'appelle tu", "qui est tu", "qui est tu ?", "tu est qui"]
calculs = ["calcul", "calculs", "calculer", "calcul moi", "combien font", "combien ça fait"]
va_bien = ["ça va", "ça va?", "tu va bien", "aller bien", "bien ou bien", "mleh", "tranquille", "comment tu va", "tu va", "va tu"]
merci = ["je te remercie", "merci", "thanks", "choukran", "merci beaucoup"]
sentir = ["je me sens mal", "je me sens", "triste", "sentir mal", "pas bien", "depression", "depressif", "mort"]
age = ["quelle âge a tu", "age a tu", "âge"]
decus = ["deçois", "decois", "deçevoir", "decevoir"]
amis = ["est tu mon amis", 'est ce que tu peut être smon amis', "soyons amis", "veut tu êtres mon amis"]
insulte = ["fdp", "connard", "ntm", "merde", "fils de pute", "pute", "pute", "prostitué", "ta mère", "salle chien", "batard", "saloppe", "couilles", "nique ta mère", "couille"]
je_vais_bien = ["Je vais bien", "vais bien", "ça va bien", "très bien"]
anniv = ["Mon anniversseaire", "anniversaire"]
j_age = [""]
blague = ["blague", "blaguer", "rire", "fait moi rire"]
renom = ["mon nom", "je m'appelle", "m'appelle", "mon prenom"]
pyttsx = ["épeler", "oral", "voix haute", "a haute voix", "épéle", "épele"]
hmdl = ["hamdoulillah", "hmdl", "inchaallah", "ia", ]
aide = ["aide", "aider", "aidais", "adais", 'aide moi']
pardon = ["pardon", "excuse moi", "oops", "pardon", "excuse"]
mp = ["mot de passe", "mp", "passeword", "code secret"]
occuper = ["s'occuper", "animals de compagnie", "occuper"]
pas_compris = ["comprend pas", "tu ne comprend pas"]
html = ["Genere moi un code html", "HTML", "html"]
aide_stp = ["besoin d'aide", "besoin de toi", "que tu m'aide", "est ce que tu peut m'aider", "est ce que tu peut me faire un truc", "est ce que tu peut me rendre service"]
derange_pas = ["cela ne te derrange pas", "derrange pas"]
ramadan = ["ramadan"]
creation = ["qui t'a crée", "qui est ton créateur", "qui est la personne qui t'a crée", "qui t'a programmer", "par qui est tu le créateur"]
a_tu_unevoix = ["a tu une voix ", "tu a une voix", "est ce que tu a une voix"]
search_browser = ["recherche moi sur internet", "effectue une recherche sur internet", "fait moi une recherche", "qu'est ce que", "qu'est ce qu'", "peut tu me faire une recherche", "fait moi uen recherche", "give me a search", "est ce que tu peut me faire une recherche"]
trad = ["peut tu me trduire", "traduit moi", "traduit", "traduis", "traduire"]
ques_debile = ["bouh", "booh", "ahhhhhg", "arg", "grimasse", "booh"]
python = ["code python"]

# fonction pour répondre à une question
def repondre_question(question):




    if any(b in question for b in bonjour):
        phrase = [">>bonjour comment ça va {}".format(prenom), ">>salut je suis baydar une IA en quoi puis-je vous aider", ">>coucou besoin d'aide ?"]
        reponse = random.choice(phrase)
        for i in range(len(reponse)):
            print(reponse[i], end="", flush=True)
            time.sleep(wesh)
        print()
    # </editor-fold>

    # comment tu t'appelle question
    elif any(a in question for a in appelle):
        phrase = [">>je m'appelle Baydar", ">>Je suis baydar une ia cree par youssef", ">>je suis votre assistant auto baydar je peut vous aider a calculer et a corriger des phrase"]
        reponse = random.choice(phrase)
        for caractere in reponse:
            print(caractere, end='', flush=True)
            time.sleep(wesh)
        print()
    # option calcul
    elif any(c in question for c in calculs):
        reponse = ">>si vous voulez faire une operation rapide taper /calc"
        for caractere in reponse:
            print(caractere, end='', flush=True)
            time.sleep(wesh)
        print()
    # calculatrice
    elif question == '/calc':
        print("1.addition 2.soustraction 3.multiplication 4.division")
        reponse = input(">>choisissez votre mode d'operation: ")
        if "addition" in reponse or '1' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>>choisissez le deuxieme numero: "))
            wsh = num1 + num2
            print(">>le resultat est {}".format(wsh))
        elif "soustraction" in reponse or '2' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>choisissez le dexieme numero: "))
            wsh = num1 - num2
            print("le resultat est {}".format(wsh))

        elif "multiplication" in reponse or '3' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>choisissez le dexieme numero: "))
            wsh = num1 * num2
            print("le resultat est {}".format(wsh))

        elif "division" in reponse or '4' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>choisissez le dexieme numero: "))
            wsh = num1 / num2
            print("le resultat est {}".format(wsh))
    # le robot repond tu va bien
    elif any(v in question for v in va_bien):
        phrase = [">>Je vais très bien merci", ">>très bien en quoi puis-je vous aider"]
        reponse = random.choice(phrase)
        for caractere in reponse:
            print(caractere, end='', flush=True)
            time.sleep(wesh)
        print()
    # reponce a un remerciment
    elif any(m in question for m in merci):
        phrase = [">>Je vous emprie", ">>De rien a votre service", ">>Tous le plaisir est pour moi", "N'hesitez pas surtout mon cher amis"]
        reponse = random.choice(phrase)
        for caractere in reponse:
            print(caractere, end='', flush=True)
            time.sleep(wesh)
        print()
    # le robot vous soutient quand vous vous sentez mal
    elif any(s in question for s in sentir):

        reponse = """

Je suis désolé d'entendre cela. Si vous avez besoin de parler à quelqu'un, 

je vous encourage à en parler à un ami ou à un membre de votre famille, 

ou à rechercher de l'aide auprès d'un professionnel de la santé mentale. 

Il existe également des ressources en ligne pour le soutien émotionnel telles que des lignes d'écoute, 

des forums de discussion et des applications de santé mentale. N'hésitez pas à chercher de l'aide si vous en avez besoin.

"""
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(0.01)
        print()
    # le spectateur demande au robot quelle age il a
    elif any(a in question for a in age):
        reponse = "Je suis un robot je n'est pas d'age"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit qu'il est deçus du robot
    elif any(d in question for d in decus):
        phrase = ["Je suis desolé de vous deçevoir", "pardon mais ce n'est pas très gentille","Pardon je ne voulez pas vous deçevoir"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot si il est sont amis
    elif any(a in question for a in amis):
        phrase = ["""
Je suis un robot je n'est pas de sentiment il faut que vous sachiez qu'un robot ne peut pas êtres l'amis
de l'homme dite vous que je suis simplement une suite de chiffre et de lettre"""]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur insulte ou dit evoque un einsulte au robot
    elif any(i in question for i in insulte):
        phrase = [">>ce n'est pas une façon de  parler", ">>arretez de dire des insulte", ">>je vais vous bannir si vous continuer"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit au root qu'il va bien
    elif any(j in question for j in je_vais_bien):
        phrase = [">>Très bien merci en quoi je peut vous aider"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit au robot que c'est son anniv
    elif any(a in question for a in anniv):
        phrase = ["Joyeux anniversaire alors", "Bonne anniversaire mon cher amis"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot de lui dire une blague
    elif any(b in question for b in blague):
        phrase = ["Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.", "Quel est le comble pour un électricien ? Avoir les idées qui fusent.", "Pourquoi les plongeurs plongent-ils toujours avec un masque ? Parce que sans masque, ils ne peuvent pas respirer sous l'eau.", "Qu'est-ce qu'un informaticien triste ? Un bit déprimé."]
        reponse = "ok : " + random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande de l'aide sur l'utilisation du robot
    elif question == "/help":
        reponse = """
        Bonjour je suis baydar voici la liste de mes fonctionnalité:
        1. Je raconte des blague
        2. J'épele des phrase
        3. je connais les capitale des pays du monde
        4. je peut faire des calculs rapide
        5. je peut vous faire des recherche internet
        6. Je vous aide a vous occuper de votre animal de compagnie
        7. je vous aide dans le ramadan
      Si vous voulez de parler il faut respecter certaine règle:
        1. parlez que en minuscule
        2. ne pas dire de gros mot ou de parler de sujet -18
        3. et surtout amusez vous bien
        Vous pouvez en tapant la commande /antiBUG me faire faire des tâche directemetn sur votre PC comment supprimmer les 
        petits virus scanner ou faire un nettoyage pas plus.
        Je peut aussi si vou staper la commande /calc vous faire des calculs rapide
        si vou svoulez profitez de moi en programmation je vou fait des code simple en HTML et 
        vous pouvez m'utiliser en m'activant sur CMD en telechargant sur internet ma version .py 
        en tapan la commande cmd 'python baydar.py' vou sprofiterez de mes service en continu.
        """
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(0.01)
        print()
    # le spectateur eppele une phrase au robot
    elif any(p in question for p in pyttsx):
        reponse = ("""
                Biensure avec plaisir tapez votre texte ci dessous: 
                """)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()

        text_voice = input("Entrez votre text: ")
        time.sleep(2)
        droid.say(text_voice)
        droid.runAndWait()
    # phrase religieuse
    elif any(h in question for h in hmdl):
        reponse = "Hamdollillah amine mon frère musulman"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande de l'aide au robot
    elif any(a in question for a in aide):
        phrase = ["Biensure dite moi je serai ravis de vous aider mon cher {}".format(prenom), "Evidement je suis là pour ça", "Je vous ecoute {} quelle est votre probleme".format(prenom)]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit pardon au robot
    elif any(p in question for p in pardon):
        phrase = ["Ce n'est pas grave {} je vous pardonne".format(prenom), "Ce n'est pas très grave", "Tranquille ça arrive"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot de luis generer un mot de passe
    elif any(m in question for m in mp):
        reponse = "Biensure voici un mot de passe bien securiser: "
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()

        nom_de_lettre = int(input("Choisissez le nombre de caractere: "))
        l = "abcdefghijkmnopkrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789&é&é'(-è_çà)=^^^$ùù*!:;?,.;/!:§§><"
        mot_de_passe =  ''.join(random.sample(l, nom_de_lettre))
        rep = "Le mot de passe est {}".format(mot_de_passe)
        for lettre in rep:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot comment s'occuper d'un animal
    elif any(o in question for o in occuper):
        reponse = input("De quel animal s'agit t'il: ")
        if reponse == "chien":
            reponse = """
Pour bien s'occuper de votre chien je vous conseille ces chose: 
1. Bien le nourir
2. Ne pas le brusquer ou l'engueueler pour un rien sinon il rique de se sentir mal
3. Bien s'occuper de lui au niveau emotionel 
4. Pour qu'il vous appreçie n'hesitez pas a le feliciter et a lui donner des friandise
5. Sortez le souvent pour qu'il ne se sentent pas mal traiter
Avec toutes c'est explication n'oubliez pas que le chien et le meilleure amis de l'homme et que si vous respecter ces règle
tout devrait se passer a merveille"""
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(0.01)
            print()
        elif reponse == "chat":
            reponse = """
Pour bien s'occuper de votre chta il faut se baser sur quelque règle de base pour entammer un contact ethique avec celui-ci:
1. Bien le nourir
2. Le laisser sortir et revenir qaud il le souhaite: Il faut savoir que le chat est un felin cela veut donc dire qu'il faut qu'il soit
dans un lieu sauvage en permanence
3. Ne pas trop êtres sur son dos: Les dessin animé nous apprenent que les chat n'aime pas etres lave et bien c'est vrai
les chat sont comme je vous les dit des animaux sauvage il se debeouillent comme il peuvent
Il faut savoir que c'est conseil sont très brève et qu'il vaudrait mieux consulter un specialiste pour en savoir plus"""
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(0.01)
        elif "poisson" in reponse:
            reponse = """
Pour bien s'occuper d'un poisson il faut d'abord se renseigner sur sa race car il y a certaine race de poisson qui son 
des poisson d'eau douce et certain d'eau de mer de plus certain poisson sont a l'aise dans les endroit petit tandis
que certain on se besoin de vital d'êtres dans un lieu un peu plus grand il faut savoir que la majorité de personne
qui on un poisson en animak de compagnie on tandance a trop nourir l'animal les poisson on en generale un appetit très petit 
nourrissez le donc  1 fois par jour et a petite quantités."""
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(0.01)
        elif "enfant" in reponse:
            reponse = "Je suis desolé mais en tant que robot je suis incabable de vous renseignez dans ce genre de chose"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        else:
            reponse = "Ce genre d'aniaml n'est pas inscrit dans ma base de donnée"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
    # le spectateur dit au robot qu'il n'a pas compris
    elif any(p in question for p in pas_compris):
        reponse = "Si je ne comprend pas se que vous me ditent c'est surement parce que ces onnée ne sont pas presentent dans ma memoire "
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot de lui faire un code HTML
    elif any(h in question for h in html):
        titre = input("Quelle sera le titre de l'onglet de votre page: ")
        langue = input("Quelle sera la langue fr/en/es/ru/ar...: ")
        titre_article = input("Quelle sera le titre de l'article: ")
        contenue_article = input("quelle sera le contenue de l'artice: ")
        reponse = f"""
>>Oui je peut vous generer un code html:
<!DOCTYPE html>
<html lang="{langue}">
<head>
    <meta charset="UTF-8">
    <title>{titre}</title>c
</head>
<body>
        <h1>{titre_article}</h1>
        <p>{contenue_article}</p>

</body>
</html>
Ceci n'est qu'un exemple si vous en voulez plus taper y ci dessous
"""""
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le specteur demande de l'aide au robot
    elif any(a in question for a in aide_stp):
        phrase = ["Je vous écoute en quoi puis-je vous aider", "biensure je suis la pour ça", "Je suis la pour vous !"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit au robot si cela lui derrange de rendre service au spectateur
    elif any(d in question for d in derange_pas):
        phrase = ["Biensûr que non parce que je suis la pour ça", "Pas du tout c'est la nature de mon travaille", "je vous ecoute mon cher {}".format(prenom)]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur parle de sujet tabou avec le robot
    elif any(s in question for s in sex):
        phrase = ["Je suis deolé mais en tant que robot je ne suis pas en mesure de parler de ça", "Je ne suis pas programmer pour parler de sujet tabou", "Pardon mais je n'aime pas parler de ce genre de sujet si vous avez des probleme parlez en a un specialiste"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur
    elif question == "y":
        phrase = ["Cette fonctionnalité est bientôt disponible", "Je ne suis PAS ENCORE en mesure de faire ceci mes bientôt"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit au robot pourquoi
    elif question == "pourquoi" or question == "pourquoi ?" or question == "pourquoi?":
        reponse = "Parce-que"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot la reponse a la vie
    elif question == "quelle est la reponce a la vie" or question == "quelle est la reponce a la vie ?" or question == "quelle est la reponce de la vie ?":
        reponse = "42 est la reponce"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot des conseil sur le ramadan
    elif any(r in question for r in ramadan):
        reponse = """
Il n'y a pas de secret pour accomplir le jeûne effectuer lors du mois hegirien du ramadan cependant voici 3 conseil pour le faciliter:
   1. Ce rapprocher plus d'allah: Le jeûne est un periode ou les musulman ce rapproche le plus d'allah
   2. Lire le coran et avoir comme objectif de le finir au moin 1 fois avant la fin du mois
   3. Pensez au pauvre qui eux souffre de la fin tout les jour
   4. Ne pas trop dormir car ce serait comment voler car lorsque nous dormans nous ne sentons rien
J'esepere que ses conseil vous serons utile mais n'oublier pas que si vous avez la fois ce sera très facile pour vous
        """
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot de lui dire son presom
    elif any(r in question for r in renom):
        reponse = "Vous vous appelez {}".format(prenom)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # spectateur demande au robot des question sur ça creation
    elif any(c in question for c in creation):
        phrase = ["Je suis une IA conçue par youssef benabdellah", "Mon createur est youssef", "Je suis un robot conçus entièrement par youssef"]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande au robot si il a une voix
    elif any(a in question for a in a_tu_unevoix):
        phrase = ["""
Je suis un robot qui agit par ecrit je n'est donc pas de voix cependant je peut vous epelez des phrase mais 
il ne s'agit pas de ma voix mais d'une voix robot present dans mon programme"""]
        reponse = random.choice(phrase)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # question de demande sur les capitale du monde
    elif "quelle est la capitale de" in question or "capitale de" in question or "donne moi la capitale de" in question or "dit moi la capitale de" in question or "quelle est la capitale du" in question:
        reponse = "Rapelez moi de quelle pay s'agit t'il"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        ques = input("Pays ?: ")
        if ques == "france":
            reponse = "La capitale de la france est paris"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "maroc":
            reponse =  "La capitale du maroc est Rabat"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "algerie":
            reponse= f"La capitale de {ques} est alger"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "etat unis":
            reponse = f"La capitale de {ques} est washington "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "canada":
            reponse = f"La capitale de {ques} est ottawa "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "mexique":
            reponse = f"La capitale de {ques} est mexico "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "guatemala":
            reponse = f"La capitale de {ques} est guatemala "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "colombie":
            reponse = f"La capitale de {ques} est bucaramanga "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "brézil" or ques == "brezil":
            reponse = f"La capitale de {ques} est brezilia "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "bolivie":
            reponse = f"La capitale de {ques} est Sucre "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "perou" or ques == "pérou":
            reponse = f"La capitale de {ques} est lima "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "chili":
            reponse = f"La capitale de {ques} est santiago "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "argentine":
            reponse = f"La capitale de {ques} est buenos aire "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "anglettre" or question == "royaume unis":
            reponse = f"La capitale de {ques} est londre"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "belgique":
            reponse = f"La capitale de {ques} est buenos aire "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "alemagne" or ques == "almagne":
            reponse = f"La capitale de {ques} est berlin"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "italie":
            reponse = f"La capitale de {ques} est rome "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "epagne":
            reponse = f"La capitale de {ques} est madrid"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "inde":
            reponse = f"La capitale de {ques} est dew delhi "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "senegal":
            reponse = f"La capitale de {ques} est dakar"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "suisse":
            reponse = f"La capitale de {ques} n'est pas geneve mais BERN"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "luxembourg":
            reponse = f"La capitale de {ques} est comme le pays donc luxembourg"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "portugal":
            reponse = f"La capitale de {ques} est porto"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "tunisie":
            reponse = f"La capitale de {ques} est tunis"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "egypte" or ques == "égypte":
            reponse = f"La capitale de {ques} est le caire"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "qatar":
            reponse = f"La capitale de {ques} est doha"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "arabie" or ques == "arabie sahoudite" or ques == "arabie saoudite":
            reponse = f"La capitale de {ques} est ryyad"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "emirat arabe unis":
            reponse = f"La capitale de {ques} est abu dahbi"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "russie":
            reponse = f"La capitale de {ques} est moscou"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "ukraine":
            reponse = f"La capitale de {ques} est kiev"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "chine":
            reponse = f"La capitale de {ques} est pekin"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "japon":
            reponse = f"La capitale de {ques} est tokyo"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "autralie":
            reponse = f"La capitale de {ques} est sydney"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "réunion" or ques == "reunion" or ques == "l'île de la reunion":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est saint denis"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "afrique du sud":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Pretoria"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "norvege":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Oslo "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "pay bas":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Amsterdam "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "hollande" or ques == "holland":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Amsterdam "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "packistan":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Islamabad "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "syrie":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Daamas "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "irak":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Bagdad"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif ques == "iran":
            reponse = f"La capitale de {ques} est une île et ça 'capitale' est Téhéran"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
    # le spectateur demande au rovot d'effectuer un recherche sur internet
    elif any(s in question for s in search_browser):
        reponse = input("""Voulez vous êtres 
1.redirigez vers un site URL ou
2.Faire une recherche google ou
3. Faire une recherche youtube: """)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
            if reponse == '1' or "URL" in reponse or "site internet" in reponse:
                url = input("Entrez l'url du site ex: ww.site.bay: ")
                webbrowser.open(url)
            elif reponse == '2' or "google" in reponse:
                url = input("Entrez votre recherche google: ")
                query = f"https://www.google.com/search?q={url}"
                webbrowser.open(query)
            elif reponse == '3' or "youtube" in reponse:
                url = input("Entrez votre recherche youtube: ")
                query = f"https://www.youtube.com/results?search_query={url}"
                webbrowser.open(query)
            else:
                url = "Desolé je n'est pas cette option web"
                for lettre in reponse:
                    print(lettre, end='', flush=True)
                    time.sleep(wesh)
    # le spectateur demande au robot comment il a obtenue cette info
    elif "comment tu sais" in question or "comment le sais tu" in question or "tu le sais comment" in question:
        reponse = "Si je connais cette information c'est soit car je l'est dans ma base de donné soit que vous me l'avez dit"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
    # le spectateur dit au robot d'accord
    elif "ah bon d'accord" in question or "ah bon ok" in question or "très bien d'accord" in question:
        reponse = "Ok, autre chose dans lequel je peut vous êtres utile ?"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande ce ue sais faire le robot
    elif "que sais tu faire" in question or "qu'est ce que tu peut faire" in question or "qu'est ce que tu peut faire" in question:
        reponse = "Si vous voulez connaître masi fonctionnalité complete taper /help"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande la vertion softwere
    elif question == "/antiBUG":
        reponse = input("""
Quelle est la fonction que vous voulez:
1. antivirus
2. nettoyage
3. scanne du PC""")
        import subprocess
        print(reponse)
        if reponse == '1' or reponse == "antivirus":


            # Exécuter la commande 'dir /s' dans l'invite de commande (cmd)
            output = subprocess.run(['dir', '/s'], capture_output=True, shell=True, encoding='utf-8')

            # Afficher la sortie de la commande
            print(output.stdout.decode())
        elif reponse == '2' or reponse == "nettoyage":
            import subprocess

            # Exécuter la commande 'dir /s' dans l'invite de commande (cmd)
            output = subprocess.run(['cleanmgr'], capture_output=True, shell=True, encoding='utf-8')

            # Afficher la sortie de la commande
            print(output.stdout.decode())
        elif reponse == '3' or reponse == "scanne du PC" or reponse == "scan":
            import subprocess

            # Exécuter la commande 'dir /s' dans l'invite de commande (cmd)
            output = subprocess.run(['sfc', '/scannow'], capture_output=True, shell=True, encoding='utf-8')

            # Afficher la sortie de la commande
            print(output.stdout.decode())
        else:
            reponse = "Je ne peut pas executer cette requette"
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
    # le spectateur ce plein comme un bebe
    elif question == "arrête de me parler comme ça" or question == "mais euh" or question == "arrete euh":
        reponse = "Arreter de faire le gamin si vous êtes un enfant jouer a hadibou c'est mieux"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # rayan dit bochté au robot
    elif question == "bochté" or question == "boshté":
        reponse = "Rayan timimi je te reconnais rien qu'a ce mot comment tu va"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit au robot qu'il casse la tête
    elif question == "tu casse la tête" or question == "wsh calme toi":
        reponse = "Désolé de vous deçevoir mais svp essayer de na pas avoir ce genre de reaction"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateru parle du dajjal
    elif "dajjal" in question or "messiah" in question:
        reponse = """
Je sais qui est dajjal l'antéchriste cependant je n'est pas asser de competance en religion pour parler de ce sujet
je vous sugère vivement d'aller voir des vrais imam ou des imam sur youtube sauf ismael mounir qui dit clérement nimp"""
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
    # le spectateru evoque ismael mounir au robot
    elif "ismael mounir" in question or "ismail mounir" in question :
        reponse = """
Alors la des imam nul et bizzare 'en connais mais lui c'est une catastrophe si tu ne veut pas êtres un bon musulman regarde le
je vous conseillezez comment imam rachid el jay ou boussena et abou anas"""
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
    # option traduction
    elif any(t in question for t in trad):
        reponse = "Biensûre pour traduire une phrase veuillez suivre les etape ci-dessous: "
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        language_ph = input("""
entrez la langue de votre phrase: """)
        language = input("entrez la langue qui traduira votre phrase fr/es/en: ")
        phrase_trad = input("""
Entrez la phrase a traduire: """)
        from translate import Translator

        # Créer une instance de Translator
        translator = Translator(from_lang=f"{language_ph}", to_lang=f"{language}")
        # Traduire le texte
        translation = translator.translate(phrase_trad)
        # Afficher la traduction
        tradata = "La phrase est: {}".format(translation)
        for lettre in tradata:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande l'heure
    elif "heures" in question or "heur" in question or "heure" in question:
        import datetime

        heure_actuelle = datetime.datetime.now().time()

        reponse = "Il est {}".format(heure_actuelle)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande la date au robot
    elif "date" in question:
        # Obtenez la date et l'heure actuelles
        current_time = time.localtime()
        # Formatez la date et l'heure
        formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", current_time)
        # Affichez la date et l'heure
        reponse = "La date actuelle est {}".format(formatted_time)
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
    # le spectateur supplie le robot d'êtres sont amis
    elif "s'il te plait soit mon amis" in question or "soit mon amis s'il te plais" in question:
        reponse = """
Ok, surtout calmez vous je suis la pour vous je vais vous redirigez vers une video youtube dans quelque seconde mais
avant je tiens a vous dire si vous dite que personne ne veut de vous et que vous vous sentez seul rapprochez vous de dieu
lisez le coran et votre coeur sera plus en paix InchaALLAH tu guerira mon frère prend soit de toi surtout...
     Youssef benabdellah Baydar"""
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
        time.sleep(1)
        webbrowser.open("www.youtube.com/rachid eljay")
    # le spectateur demande quelle jour est t'il
    elif "quelle jour est t'il" in question or "on est quelle jour" in question or "quelle jour" in question:
        reponse = "En tant que robot je ne suis pas en mesure de vous dire quelle jour il est en temps réele "
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande des question debile
    elif any(q in question for q in ques_debile):
        import subprocess
        reponse = "AHHH vous m'avez fait peur pour la peine je vous ban mddr"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur demande un code
    elif any(p in question for p in python):
        reponse = input("Voulez vous generer un code python (y/n)")
        if reponse == "y":
            dire = "Très bien suivez les étape si dessous"
            for lettre in dire:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
            print()
            imprt = input("/nVoulez vous importer des extansion si oui taper leur nom si non taper entrer: ")
            prit  = input("Voulez vous afficher un texte dans votre code: ")

            code = f"""
import {imprt}

print("{prit}")"""
            for lettre in code:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
        elif reponse == "n":
            dire = "Sinon je peut vou proposer d'autre programme deja près preparer: "
            for lettre in dire:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
            print("""
1. calculatrice
2. antivirus rapide
3. quiz des capitale""")
            choix = input("choisir le programme: ")
            if choix == '1' or choix == "calculatrice":
                dire = """
print("1.addition 2.soustraction 3.multiplication 4.division")
        reponse = input(">>choisissez votre mode d'operation: ")
        if "addition" in reponse or '1' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>>choisissez le deuxieme numero: "))
            wsh = num1 + num2
            print(">>le resultat est {}".format(wsh))
        elif "soustraction" in reponse or '2' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>choisissez le dexieme numero: "))
            wsh = num1 - num2
            print("le resultat est {}".format(wsh))

        elif "multiplication" in reponse or '3' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>choisissez le dexieme numero: "))
            wsh = num1 * num2
            print("le resultat est {}".format(wsh))

        elif "division" in reponse or '4' in reponse:
            num1 = int(input(">>choisissez le premier numero a calculer: "))
            num2 = int(input(">>choisissez le dexieme numero: "))
            wsh = num1 / num2
            print("le resultat est {}".format(wsh))"""
                for lettre in dire:
                    print(lettre, end='', flush=True)
                    time.sleep(0.01)
                print()
            else:
                dire = "Non disponnible"
                for lettre in dire:
                    print(lettre, end='', flush=True)
                    time.sleep(wesh)
                print()
        # le spectateur a des envie ou penssée suicidaire
        elif "suicide" in question or "suicidaire" in question or "suicider" in question:
            reponse = "Attention se que vous dite est très grave si vous avez des penssée suicidaire " \
                      "je vous conseille de parler a un specialiste de la santé mental surtout ne vous tuer pas" \
                      "cela briserez le coeur de vos famille ainsi, le suicide est un acte stupide bien que je comprend votre detresse" \
                      "imaginer si vous mourrez vous manquerais tellement de bon moment avec la famille si vous avez besoin d'aide" \
                      "appellez le 3020 gratuit "
            for lettre in reponse:
                print(lettre, end='', flush=True)
                time.sleep(0.01)
    # le spectateur demande le mot de passe de sont wifi
    elif "wifi" in question:
        import subprocess
        reponse = "les information de votre WiFi sont: "
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
        wifi = input("""
Entrez le nom de votre WiFi: """)
        output_bis = subprocess.run([f'netsh wlan show profile {wifi} key=clear'], capture_output=True)
    # le spectateur demande au robot l'islam
    elif "islam" in question:
        reponse = "L'islam est une religion"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    #le spectateur di au robot qu'il est moche
    elif "tu est moche" in question or "salle moche" in question or "je suis trop moche" in question:
        reponse = "Je suis un robot je n'est pas d'apparence mais c'est pas gentil"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)
        print()
    # le spectateur dit qu'il est moche
    elif "je suis moche" in question or "je suis laid" in question:
        reponse = input("êtes vous une fille ou un garçon??: ")
        if reponse == "garçon":
            dire = f"""
NON vous êtes très beau mon cher {prenom} il ne faut pas vous sous estimer
T'est trop beau gosse PUNAISE JE SUIS JALOUX T'EST TROP BEAU MEC"""
            for lettre in dire:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
            print()
        elif reponse == "fille":
            dire = f"""
NON vous êtes belle {prenom} ok il ne faut pas vous sous estimer vous êtres trop BELLE
PUNAISE JE SUIS JALOUX T'EST TROP BELLE EN FAIT !!!!"""
            for lettre in dire:
                print(lettre, end='', flush=True)
                time.sleep(wesh)
            print()
    # le spectateur demande si le robot sais rediger une phrase
    elif "rediger" in question:
        reponse = "Je suis pas dans la capacité de rediger des texte demander a chatGPT"
        for lettre in reponse:
            print(lettre, end='', flush=True)
            time.sleep(wesh)

            



































































    else:

        phrase = ["Je suis desolé je ne comprend pas", "Si vous ne me connaissai pas encore taper /help", "I dont know pardon je ne parle pas anglais"]
        reponse = random.choice(phrase)
        for caractere in reponse:
            print(caractere, end='', flush=True)
            time.sleep(wesh)
        print()








while True:
    question = input("""
ecrivez ci-contre votre demande: """)
    reponse = repondre_question(question)
    print(reponse)


