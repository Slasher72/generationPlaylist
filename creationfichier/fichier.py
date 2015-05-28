#Création d'un fichier au format M3U recuperant la playlist généré préalablement
def M3U(args, musiquePlayList): #Arguments, et la playlist)
    
    #Nommage du fichier au demande l'utilisateur
    fichier = args.nomFichierPlaylist +"."+ args.formatPlaylist
    #Ouverture du fichier
    fichier = open(fichier, 'w')
    
    #Boucle permettant de recuperé les chemins(Position(lien) des musiques) d'apres la génération de playlist
    for champ_musique in musiquePlayList:
        fichier.write("#EXTINF:" + str(champ_musique[3]) + ", " + champ_musique[1] + " - " + champ_musique[0] + "\n\n")
        #Ecriture du fichier avec la playlist
        fichier.write(champ_musique[4] + "\n") #champ_musique[4] correspond au chemin des musiques qui on été inséré dans la playlist
    #Fermeture du fichier
    fichier.close()


#Création d'un fichier au format XSPF recuperant la playlist généré préalablement
def XSPF(args, musiquePlayList):
    #Nommage du fichier au demande l'utilisateur
    fichierxspf1 = (args.nomFichierPlaylist + "." + args.formatPlaylist)
    #Ouverture du fichier
    fichierxspf = open(fichierxspf1, 'w')
    fichierxspf.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ fichierxspf1 +"</title>\n"+
                       "\t<trackList>\n")
    #Boucle permettant de recuperé les chemins(Position(lien) des musiques) d'apres la génération de playlist
    #Parcours le résultat pour chaque ligne
    for champ_musique in musiquePlayList:
        #Ecriture du fichier avec la playlist
            fichierxspf.write("\t\t<track>\n\t\t\t<location>file://"+ champ_musique[4] +"</location>\n"+ #champ_musique[4] correspond au chemin des musiques qui on été insérés dans la playlist
                               "\t\t\t<title>"+ champ_musique[0] +"</title>\n"+ #champ_musique[0] correspond au titre des musiques qui on été insérés dans la playlist(liste)
                               "\t\t\t<creator>"+ champ_musique[1] +"</creator>\n"+  #champ_musique[1] correspond à l'artiste des musiques qui on été insérés dans la playlist
                               "\t\t\t<album>"+ champ_musique[2] +"</album>\n"+ #champ_musique[2] correspond à l'album correspndant aux musiques qui on été insérés dans la playlist
                               "\t\t\t<duration>"+ str(champ_musique[3]) +"</duration>\n"+ #champ_musique[3] correspond à la durée d'une musique qui on été insérés dans la playlist
                               "\t\t</track>\n")
    fichierxspf.write("\t</trackList>\n</playlist>")
    #Fermeture du fichier
    fichierxspf.close()


#Création d'un fichier au format PLS recuperant la playlist généré préalablement 
def PLS(args, musiquePlayList):
    i=1
    #Nommage du fichier au demande l'utilisateur
    fichierPLS1 = (args.nomFichierPlaylist + "." + args.formatPlaylist)
    #Ouverture du fichier
    fichierpls = open(fichierPLS1, 'w')
    #Ecriture du fichier avec la playlist
    fichierpls.write("[playlist]\n\n")
    for champ_musique in musiquePlayList:
        fichierpls.write("File"+ str(i) +"="+ champ_musique[4] +"\n")#champ_musique[4] correspond au chemin des musiques qui on été insérés dans la playlist
        fichierpls.write("creator"+ str(i) +"="+ champ_musique[1] +"\n")#champ_musique[1] correspond à l'artiste des musiques
        fichierpls.write("Title"+ str(i) +"="+ champ_musique[0] + "\n")#champ_musique[0] correspond au titre des musiques
        fichierpls.write("Length"+ str(i) +"="+ str(champ_musique[3]) + "\n\n")#champ_musique[3] correspond à la durée d'une musique
        i+=1
        #Ecrit le nombre d'entrée(musique) dans la playlist (optionelles)
    fichierpls.write("NumberOfEntries="+ str(len(musiquePlayList)) +"\n")
    #Fermeture du fichier
    fichierpls.close()