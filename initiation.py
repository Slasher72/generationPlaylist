import logging
import modules.arguments
import modules.fonctions
from database.recuperationdonnees import *


logging.basicConfig(filename ="Journal_log.log", level = logging.DEBUG)
#logging.basicConfig(level = logging.DEBUG)
logging.info("Mise en marche du programme")

# On affiche les arguments obligatoire
modules.arguments.arguments_generals()
modules.arguments.arguments_optionnels()
args = modules.arguments.parser.parse_args()
logging.info(repr(args))
            
#Vérification du temps
modules.fonctions.verification_du_temps(args.dureePlaylist)


for argument in ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']:
# Si l'argument est renseigné
        if getattr(args, argument) is not None:
            # On écrit la valeur dans le fichier de logs
            logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
            modules.fonctions.gestionPourcentage(getattr(args, argument))


recupererDonnees(args)
print("Récupération de votre musique")
logging.info("Récupération des données musicales")

generationPlaylist(args)
print("generation de votre musique")
logging.info("Génération de la playlist")


Playlist(args)
print("Playlist en phase de création")

EcritureFichier(args, musiquePlayList)
print("Ecriture de votre playlist")
logging.info("Ecriture de la playlist dans le fichier demandé préalablement par l'utilisateur")



print("Bonne lecture de votre playlist")
logging.info('Tout a été opérationel')
logging.info('*****************FIN************************')
logging.shutdown()
exit(0)