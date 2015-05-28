import argparse

# On initialise un parser
parser = argparse.ArgumentParser()

"""
Fonction avec les arguments principaux du générateur de playlist
"""
def arguments_generals():
    parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
    parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
    parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")

"""
Fonction avec les arguments optionnels  du générateur de playlist
"""
def arguments_optionnels():
    parser.add_argument("-t", "--titrePlaylist", action='append', help="titre choisis",nargs=2)
    parser.add_argument("-ar", "--artistePlaylist", action='append', help="nom de l'artiste",nargs=2)
    parser.add_argument("-al", "--albumPlaylist", action='append',help="album présent dans la playlist" ,nargs=2)
    parser.add_argument("-g", "--genrePlaylist", action='append', help="genre%%pourcentage", nargs=2) #nargs=2 signifie que l'on attends deux données dans cet arguments  
                                                        #append signifie que l'on saisir plusieurs genres