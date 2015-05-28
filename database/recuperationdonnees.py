import sqlalchemy
import random
from database.Basedonnees_initiation import table_morceaux, connection as conn
from creationfichier.fichier import M3U, XSPF, PLS

#Définition d'une variable regroupant un ensemble d'arguments
argument_cli = ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']

#Définition de la playlist
musiquePlayList =[] #Musique PlayList

"""
Fonction permettant de récupérer des données dans la BDD par rapport aux besoins de l'utilisateur
:param a: les arguments saisis par l'utilisateur
"""

def recupererDonnees(args):
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                #Récupération des données dans la base pour chaque argument ci-dessous
                if (attribut == 'titrePlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.titre == argument[0])
                #Récupération des données dans la base pour chaque argument ci-dessous
                if (attribut == 'artistePlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.artiste == argument[0])
                #Récupération des données dans la base pour chaque argument ci-dessous
                if (attribut == 'albumPlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.album == argument[0])
                #Récupération des données dans la base pour chaque argument ci-dessous
                if (attribut== 'genrePlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.genre == argument[0])

                # Connection à la base de données suivi de l'execution de la requète
                recuperation = conn.execute(RecuperationDonnees)
                #Insere les données récuperées dans un list
                recuperation = list(recuperation)
                #Melange la musique dans la list
                random.shuffle(recuperation)
                
                
                argument.insert(2,[]) #Création d'une liste en 3eme position des arguments ex : rock 70 []
                #Initialisation de la valeur à 0
                i=0   
                #Initialisation de la valeur à 0
                duree = 0 
                
                for champBDD in recuperation: 
                    #Pour chaque musique recuperer dans la liste, on vérifie la durée afin de correspondre au mieux au demande de l'utilisateur
                    duree += champBDD[5]  
                    #Correspond au champ durée dans la BDD
                    if(duree < argument[1]*60): 
                        #Si durée inf. à durée demandé par utilisateur + conversion en secondes
                        argument[2].insert(i, champBDD) #Insertion de la musique convertit et vérifié dans la liste
                        i += 1
                        
                    else:
                        duree -= champBDD[5] 
                        #Correspond au champ durée dans la BDD
                          
"""
Génération de la liste de playlist
:param a: la liste des arguments saisis par l'utilisateur
"""
def generationPlaylist(args):
    i = 0
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                for musique in argument[2]: # Pour chaque musique dans la playlist on insére le titre, l'artiste, l'album, le format et le chemin 
                    musiquePlayList.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    random.shuffle(musiquePlayList) #On mélange les musiques aléatoirement
    
"""
Toutes les vérifications pour mener à bien l'éxecution du programme.
:param a: liste des arguments
"""
def Playlist(args):
    duree = 0 #initialisation à 0
    for musique in musiquePlayList: #Pour chaque musique dans la playlist selon un genre précis
        duree += musique[3]
        
    if(duree < args.dureePlaylist*60): #Si la duree de la musique est inférieur à la durée totale demandée par l'utilisateur on effectue la requête permettant d'aller chercher des musiques alétoirement dans la base correspondant au genre
        select_morceaux = sqlalchemy.select([table_morceaux])
        resultat = conn.execute(select_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)
    
    i=len(musiquePlayList)
    for musique in resultat:
        duree += musique[5] # on vérifie que la durée d'un musique ne dépasse pas la durée de la playlist demandée, si c'est le cas, on insére à nouveau une musique aléatoirement
        if(duree < args.dureePlaylist*60):
            musiquePlayList.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
            i += 1
        else:
            duree -= musique[5] # Si ce n'est pas le cas, on enlève la musique et on en sélectionne une moins grande pour compléter la playlist avec le moins d'écart possible
    return duree

"""
On gére l'écriture du fichier dans les 3 formats proposés
:param a: les arguments
:param b: les musiques de la playlist
"""
def EcritureFichier(args, musiquePlayList):
    if(args.formatPlaylist == 'm3u'):
        M3U(args, musiquePlayList)
    if(args.formatPlaylist == 'xspf'):
        XSPF(args, musiquePlayList)
    if(args.formatPlaylist == 'pls'):
        PLS(args, musiquePlayList)

