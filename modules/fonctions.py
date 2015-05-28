import logging
"""
Vérification d'un temps positif
:param a: l'argument que l'on va vérifier
"""
def verification_du_temps(argumentAVerifier):
    try:
        logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
        if argumentAVerifier <= 0:
            print ("Le temps doit être positif !")
            logging.error("le temps " + str(argumentAVerifier) + " n'est pas un entier positif")
            exit(1)
    except ValueError:
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + argumentAVerifier +"'")
        exit()
            
    
"""
Vérification de la quantité (Pourcentage d'un genre)
:param a: le paramétre auquel ont vérifie la quantite
"""
def verifier_mes_quantite(quantite):
    try:
        logging.info("Mise en marche de la fonction des vérification des quantités")
        quantiteValidee = abs(int(quantite))       
        if quantiteValidee > 100:
            return 10  #On retourne 10 afin d'eviter un maximum les partages de musique de d'autre genre
        return quantiteValidee
    except ValueError:
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + quantite +"'")
        return None
        exit()
            

"""
Gestion des pourcentages pour plusieurs genres
:param a: paramétre affecté à la gestion de pourcentage (2 args)
"""
def gestionPourcentage(typeArg):
    logging.info("Mise en marche de la fonction des vérification des pourcentages")
    i = 0
    ligneListe = 1
    j = 0
    ligneListe2 = 1
    somme = 0
    
    #Tant que la liste du type d'argument passé par l'utilisateur à encore une ligne    
    while ligneListe <= len(typeArg):
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        
        #Vérification du pourcentage
        quantite1 = verifier_mes_quantite(typeArg[i][1])
        somme = somme + quantite1
        ligneListe = ligneListe + 1
        i = i + 1
    logging.info("La sommes totale des genres est de : " + str(somme) +".")
    try:
        if somme >= 100 or somme < 100:        
            #Tant que la liste du type d'argument passé par l'utilisateur à encore une ligne
            logging.info('Remise du total des % à 100 grace à la proportionalité')
            while ligneListe2 <= len(typeArg):
                #Round() permet d'arrondir l'entier le plus proche
                typeArg[j][1] = round(int(typeArg[j][1])*100/somme)
                logging.info(str(typeArg[j][1]) + "% de genres voulues")
                j = j + 1
                ligneListe2 = ligneListe2 + 1
                
        print('ok')
    except ValueError:
        logging.error("erreur")
        return None     
