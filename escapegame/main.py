from multiprocessing.dummy import JoinableQueue
import flask
from pageshtml import entete, basdepage

app = flask.Flask(__name__) # Création de l'application

@app.route('/') # O
def index():    
    page=entete
    page+="""
    <p>Tu es coincé dans mon cerveau et tu as pour mission de retrouver mon neurone perdu.</p>
    <table>
    <td><img src="static/brain01.jpg"/></td>
    <td><ul>
    <li><a href="/temporal">Aller au lobe temporal</a></li>
    <li><a href="/parietal">Aller au lobe parietal</a></li>
    <li><a href="/frontal">Aller au lobe frontal</a></li>
    <li><a href="/occipital">Aller au lobe occipital</a></li>
    </ul></td>

"""
    page+=basdepage
    return page


@app.route("/temporal")
def temporal():
    page=entete
    page+="""<p>Lobe temporal</p>
            <p>On dirait qu'il n'y a rien...</p>
            <h2><a href="/infotemporal">Pas étonnant, comprenez ici pourquoi !</a></h2>
<blockquote class="morse">.-.. . / .--. .-. . -- .. . .-. / -.-. .... .. ..-. ..-. .-. . / . ... - / ---..</blockquote>

<ul>
<li><a href="/">Revenir à la pièce</a></li>
<li><a href="/parietal">Aller au lobe parietal</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/parietal")
def parietal():
    page=entete
    page+="""<p>Lobe parietal</p>
    <p>Bienvenu au lobe parietal humble voyageur</p>
    <h2><a href="/infoparietal">Cet endroit a l'air sombre, comprenez ici pourquoi !</a></h2>
    <table>
    <td><img src="static/brain2.png"/></td>
    <td><ul>
    <li><a href="/">Revenir à la pièce</a></li>
    <li><a href="/examinertrou">Examiner le trou</a></li>
    <li><a href="/frontal">Aller au lobe frontal</a></li>
    </ul></td>
"""
    page+=basdepage
    return page

@app.route("/frontal")
def frontal():
    page=entete
    page+="""<p>Bienvenu au lobe frontal !</p>
    <p>Tu arrives au lobe le plus important !<br></p>
    <p class="frontal">Ton lobe frontal permet de parler et de communiquer<br>
Récemment, on a decouvert que le lobe frontal n’est pas le seul à jouer un rôle dans les processus cognitifs<br>
Outre le lobe pariétal, celui-ci permet aussi d’entendre.<br>
Il est le lobe qui sécrète la Dopamine ( une des hormones du plaisir).<br>
Sa caractéristique principale restant celle de la phonologie et de la parole<br></p>

<ul>
<li><a href="/">Retourner au début</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/infotemporal")
def infotemporal():
    page=entete
    page+="""<p>Le lobe temporal est la partie inférieure du cerveau, elle sert à contenir la mémoire, les émotions, la lecture, le goût, l'odorat et l'ouïe<br>En cas d'atteinte du lobe temporal, certaines de ces fonctions pourront être plus ou moins déficientes.</p>
    <ul>
    <li><a href="/">Revenir au début</a></li>
    <li><a href="/temporal">Aller au lobe temporal</a></li>
    </ul>

"""
    page+=basdepage
    return page

@app.route("/infoparietal")
def infoparietal():
    page=entete
    page+="""<p>Le lobe pariétal est la partie supérieure arrière du cerveau, elle sert à envoyer la douleur et la ressentir, au toucher et à l'ouïe. Le lobe pariétal constitue une des régions du cerveau. Ce dernier est la partie la plus développée de l’encéphale et en occupe la majeure partie</p>
    <ul>
    <li><a href="/">Revenir au début</a></li>
    <li><a href="/parietal">Aller au lobe pariétal</a></li>
    </ul>

"""
    page+=basdepage
    return page

@app.route("/examinertrou")
def trou():
    page=entete
    page+="""
    <p> Il y a un papier posé par terre</p>
    <h3> ¡¡¡ ןɐʇǝᴉɹɐd ǝqoן np ᴉʇᴉɟɟɐɹƃ ǝן ɹᴉɹʌnoɔǝp sɐd ʇuǝʌᴉop ǝu ןI</h3>
<ul>
<li><a href="/">Retourner à l'entrée</a></li>
<li><a href="/parietal">retourner au lobe parietal</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/occipital")
def occipital():
    page=entete
    page+="""
    <p>Vous entrez dans le lobe occipital</p>
    <p>Le mot de passe du zip des solutions est facile</p>
<ul>
<li><a href="/">Retourner à l'entrée</a></li>
<li><a href="/suite">Aller à la suite</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/suite")
def suite():   
    page=entete
    page+="""
    <p>Vous arrivez au sas de filtrage de données pour être emmené vers le tronc cérébral</p>
    <p>Nous vous demandons donc un mot de passe pour être sûr de votre autorisation d'accès</p>
    <form action ="/tronc" method="post">\n
    <label class="mdp">Mot de passe</label> : <input type="password" name="mdp">\n
    <input type="submit" value="Envoyer">\n
    </form>
    
<ul>
<li><a href="/">Retourner à l'entrée</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/tronc", methods = ['POST'])
def tronc():
    resultat = flask.request.form
    if resultat['mdp']=='853':
        page=entete
        page+="""
        <h2>Vous entrez dans le tronc cérébral</h2>
        <p>Vous ne pouvez maintenant plus revenir en arrière, vous entamez une descente vers la moelle épinière, faites attention aux détails</p> 
    <table>
    <td><img src="static/SOMBRE.jpg"/></td>
    <td>
    <ul>
    <li><a href="/descente">Commencer à descendre</a></li>
    </ul>
    """
        page+=basdepage
        return page
    else:
        page=entete
        page+="""
        <p>Vous n'avez pas le bon mot de passe</p>
        <p>Recommencer</p>
    <ul>
    <li><a href="/">Retourner à l'entrée</a></li>
    </ul>
    """
        page+=basdepage
        return page

@app.route("/descente")
def descente():
    page=entete
    page+="""
    <p>Vous êtes en pleine descente vers la moelle épinière !</p>
    <p>Avant de continuer, les anticorps soupçonnent une intrusion et font donc beaucoup plus attention, vous allez donc devoir les suivre</p>
<ul>
<li><a href="/salleanti">Suivre les anticorps</a></li>
<li><a href="/non1">Les semer</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/non1")
def non1():
    page=entete
    page+="""
    <p>Vous avez décidé de tenter de les semer, malheureusement ils finissent par vous rattraper, vous êtes maintenant en cellule...</p>
    <td><img src="static/prison.jpg"/></td>
<ul>
<li><a href="/tapis">Regarder sous le tapis</a></li>
<li><a href="/attente">Attendre d'être libéré</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/tapis")
def tapis():
    page=entete
    page+="""
    <p>Sous le tapis vous trouvez un ordinateur à peine fonctionnel qui affiche ces lignes de code...<br>Peut-être qu'elles vous serviront plus tard...</p>
    <td><img src="static/tapis.png"/></td>
<ul>
<li><a href="/attente">Attendre d'être libéré</a></li>
</ul>
"""
    page+=basdepage
    return page


@app.route("/attente")
def attente():
    page=entete
    page+="""
    <p id="timer">Veuillez patienter</p>
<script>
let timer = 60;
let interval = setInterval(() => {
  timer--;
  if (timer === 0) {
    clearInterval(interval);
    console.log('Time is up!');
    window.location="/salleanti";
  } else {
    document.getElementById("timer").innerHTML = "Veuillez patienter " + timer + " secondes";
  }
}, 1000);
</script>

"""
    page+=basdepage
    return page

@app.route("/salleanti")
def salleanti():
    page=entete
    page+="""
    <p>Bienvenu dans la salle des anticorps, ici nous vérifions les entités suspectes.</p>
    <p>Ils vous demandent quelle était la lettre présente sur le sol lorsque vous avez entamé votre descente vers la moelle épinière</p>
    <div class="lettre1"><form action ="/sortie" method="post">\n
    <p class="lettre">X</p><input type="radio" name="x" value="case 1"><p class="lettre">Y</p><input type="radio" name="x" value="case 2"><p class="lettre">V</p><input type="radio" name="x" value="case 3">\n
    <input type="submit" value="Envoyer">\n'</form></div>
   <td><img src="static/desk.jpg"/></td>
"""
    page+=basdepage
    return page

@app.route("/sortie", methods = ['POST'])
def sortie():
    resultat = flask.request.form
    if resultat['x']=='case 1':
        page=entete
        page+="""
        <h2>Bravo vous nous avez prouvé que vous êtes doté de conscience, bonne continuation</h2>
    <ul>
    <li><a href="/covid">Continuer</a></li>
    </ul>
    """
        page+=basdepage
        return page
    else:
        page=entete
        page+="""
        <p>Vous n'etes pas un humain ! Vous devez aller en prison !</p>
    <ul>
    <li><a href="/non1">Les suivre vers la prison</a></li>
    </ul>
    """
        page+=basdepage
        return page

@app.route("/covid")
def covid():
    page=entete
    page+="""
    <p>Le covid t'attend avec ses gardes, il te dit que pour récupérer le neurone, tu devras répondre à une question.<br> Sauf si tu as fait de la prison</p>
    <td><img class="covid" src="static/covid.png"/></td>
<ul>
<li><a href="/final1">J'ai fait de la prison</a></li>
<li><a href="/final2">Répondre à la question</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/final1")
def final1():   
    page=entete
    page+="""
    <p>Alors comme ça tu as fait de la prison... Tu a sûrement été dans la prison des anticorps et tu as dû trouver le code sous le tapis, alors donne -le moi ici et je te rends le neurone maintenant...</p>
    <form action ="/win" method="post">
    <label class="mdp">Mot de passe</label> : <input type="password" name="mdp1">
    <input type="submit" value="Envoyer">
    </form>
<ul>
<li><a href="/covid">Je me suis trompé, je n'ai pas fait de prison</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/final2")
def final2():   
    page=entete
    page+="""
    <p>Alors comme ça tu n'as pas fait de prison... Tu dois donc répondre à cette question fatidique pour accéder au neurone...</p>
    <h2>Quelle est la meilleure personne que vous ayez rencontrée de toute votre vie ?</h2>
    <form action ="/win1" method="post">\n
    <input type="text" name="prenom">
    <input type="submit" value="Envoyer">\n
    </form>
    
<ul>
<li><a href="/covid">Je me suis trompé, j'ai fait de la prison</a></li>
</ul>
"""
    page+=basdepage
    return page

@app.route("/win", methods = ['POST'])
def win():
    resultat = flask.request.form
    if resultat['mdp1']=='8250':
        page=entete
        page+="""
        <body class="fun-color">
        <h2>BRAVO, vous pouvez récupérer le neurone, vous avez gagné...</h2>
        <p>Si vous avez aimé l'escape game, n'hésitez pas à me mettre 20/20</p> 
    <table>
    <td><img src="static/neurone.jpg"/></td>
    <td>
    </body>
    """
        page+=basdepage
        return page
    else:
        page=entete
        page+="""
        <p>Vous n'avez pas le bon mot de passe</p>
        <p>Vous êtes un menteur, vous n'êtes pas allé en prison !</p>
    <ul>
    <li><a href="/covid">Partez d'ici !</a></li>
    </ul>
    """
        page+=basdepage
        return page


@app.route("/win1", methods = ['POST'])
def win1():
    resultat = flask.request.form
    if resultat['prenom']=='Simon':
        page=entete
        page+="""
        <body class="fun-color">
        <h2>BRAVO, vous pouvez récupérer le neurone, vous avez gagné... (Je sais... Je sais... Je suis la meilleure personne...)</h2>
        <p>Si vous avez aimé l'escape game n'hésitez pas à me mettre 20/20</p> 
    <table>
    <td><img src="static/neurone.jpg"/></td>
    <td>
    </body>
    """
        page+=basdepage
        return page
    else:
        page=entete
        page+="""
        <p>Non, ce n'est pas la meilleure personne que vous ayez rencontrée, réessayez</p>
        <p>Faites attention à la majuscule en début de prénom</p>
    <ul>
    <li><a href="/final2">Partez d'ici !</a></li>
    </ul>
    """
        page+=basdepage
        return page
app.run() 





