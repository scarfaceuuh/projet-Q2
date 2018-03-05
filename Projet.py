# -*- coding: utf-8 -*-
#PRÉ-PHASE **********************
def game_management():
    """
        Fait appel fonctions avec les informations de l'ui, des portails et des astéroides.

        version:
        -------
        specification: Bechet Francois (v.1 02/03/18)
    """

def create_ui ():
    """
        Création de l'interface graphique.

        Version:
        --------
        specification: Beyers Bruno (v1.1 03/03/18)

    """
def create_portals():
    """
        Mise en place des portails

        Return:
        -------
        portail_axe: Postion, vie et emplacement du portail allié (dico)
        portail_allie: Postion, vie et emplacement du portail ennemi (dico)

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/03/18)
    """
def create_asteroids():
    """
        Mise en place des asteroids

        Return:
        -------

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/03/18)
    """


#PHASE 1 **************************
def phase_one():
    """
        Appel les fonctions de la phase une

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """

def ores(Structure_de_donnees):
    """
        Indique le nombre d'ores des joueurs

        Paramètre:
        ----------
        Structure_de_donnees: Nombre de minerais dans la structure de données (dictionnaire(int))

        Note:
        -----
        Doit être strictement positif
        4 ores offert au début de partie
        La structure de donnée n'a pas encore de nom (variable)

        Returns:
        --------
        nbr_ores: Nombre d'ores actuel (int)

        Version:
        --------
        spécification: Beyers Bruno (v1.0 05/03/18)
    
     """

def store(nbr_ores):
    """
        Achat de vaisseaux

        parameter:
        ----------
        Structure_de_donnees: nombre de minerais disponible (dictionnaire(int))

        Note:
        -----
        Le nombre de minerais doit être strictement positif

        version:
        --------
        specification: Beyers Bruno (v.1 03/03/18)

    """
def get_stats_vaisseaux(type):
    """
        rechercher les caractéristiques des vaisseaux dans la structure de données

        Paramètres:
        -----------
        type: type du vaisseau (dictionnaire(float))

        Note:
        -----
        5 types possible : scout,warship,excavator-S,-M,-L.

        Return:
        -------
        type_vaisseau: Renvois la taille, tonnage, vie, attaque, portée et coup d'un vaisseau (liste)

        Version:
        --------
        spécification: Beyers Bruno (v1.0 05/03/18)
    """
def spawn_vaisseaux(pos_portail_x,pos_portail_y):
    """
        Fait apparaître les vaisseaux au centre de portail

        Paramètres:
        -----------
        pos_portail_x: position x du centre du portail
        pos_portail_y: position y du centre du portail

        Note:
        -----
        Ne peut apparaître qu'au centre du portail
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)


    """

#PHASE 2 **********************************
def phase_two():
    """
        Appel les fonctions de la phase deux

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """
def lock():
    """
        Verrouiller un astéroide pour la récole automatique

        Note:
        -----
        Ne peut être lock que par un extracteur

        Version:
        --------
        specification: Beyers Bruno (v1.0 04/03/18)
    """
def Unlock():
    """
        Déverouille un astéroide pour la récole automatique

        Version:
        --------
        specification: Beyers Bruno (v1.0 04/03/18)
    """
#PHASE 3 *************************************************
def phase_three():
    """
        Appel les fonctions de la phase trois

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """

def attack(type_vaisseau):
    """ attaque l'adversaire 

        parameters:
        -----------
        type_vaisseau: Caractéristique (attaque/portée) du vaisseau sélectionné (liste)

        Note:
        ----
        La portée et les dégats doivent être strictement positif
        Les extracteurs ne peuvent attaquer

        version:
        --------
        specification: Beyers Bruno (v.1 02/03/18)
    """
def deplacement(structure_de_donnees):
    """
        Déplace le vaisseau
        
        Paramètres:
        -----------
        structure_de_donnees: emplacement du vaisseau actuel (dictionnaire(liste(int)))
        
        Note:
        -----
        La structure de donnée n'a pas encore de nom (variable)
        Ne peut se déplacer hors de l'UI
        
        return:
        -------
        Vaissseau_emplacement: Coordonnée du vaisseau une fois déplacé (liste(int))
        
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
        
    """
    
def end(nbr_tour,health_portail):
    """
        Met fin à la partie
    
        Paramètres:
        -----------
        nbr_tour: nombre de tour sans dégât occasionné(int)
        health_portail: Point de vie du portail(int)
        
        Note:
        -----
        La partie se termine si 20 tour se sont passé sans dégât occasionné
        La parti se termine si la vie du portail est à 0
        
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
        
    """
    
#PHASE 4 *********************************
def phase_four():
    """
        Appel les fonctions de la phase quatre

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """
