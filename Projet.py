# -*- coding: utf-8 -*-
#PRÉ-PHASE **********************
def game_management():
    """
        calling functions with informations from UI, portals and asteroids.

        version:
        -------
        specification: Bechet Francois (v.1 02/03/18)
    """

def create_ui ():
    """
        Creating graphic interface.

        Version:
        --------
        specification: Beyers Bruno (v1.1 03/03/18)

    """
def create_portals():
    """
        portals setup

        Return:
        -------
        portail_axe: Position and live of allied portal (dico)
        portail_allie: Position and live of ennemy portal (dico)

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/03/18)
    """
def create_asteroids():
    """
        Setup of asteroids

        Return:
        -------

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/03/18)
    """


#PHASE 1 **************************
def phase_one():
    """
        calling phase one functions

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """

def ores(data_structures):
    """
        show players ores number

        Parameters:
        ----------
        data_structures: ore number in the data structure (dict(int))
        

        Note:
        -----
        Must be strictly positive
        4 ores are given when game start
        data structure don't already have a name (variable)

        Returns:
        --------
        nbr_ores: ore number (int)

        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
    
     """

def store(nbr_ores):
    """
        spaceships purchase

        parameter:
        ----------
        data_structure: ore number available (dict(int))

        Note:
        -----
        ore number must be strictly positive

        version:
        --------
        specification: Bechet François (v.2 03/03/18)

    """
def get_stats_spaceships(type):
    """
        search spaceships caracteristics in the data structure

        Parameters:
        -----------
        type:nspaceship type (dict(float))

        Note:
        -----
        5 types possible : scout,warship,excavator-S,-M,-L.

        Return:
        -------
        type_spaceship: return the size, volume, life, attack, scope and price of a spaceship (list)

        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
    """
def spawn_vaisseaux(pos_portail_x,pos_portail_y):
    """
        spawn spacehips in portals center

        Parameters:
        -----------
        pos_portail_x: x position of the portal
        pos_portail_y: y position of the portal

        Note:
        -----
        must only appear in portal center
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)


    """

#PHASE 2 **********************************
def phase_two():
    """
        calling phase two fucntions

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """
def lock():
    """
        Lock an asteroid for automatic harvest

        Note:
        -----
        can only be locked by an excavator

        Version:
        --------
        specification: Beyers Bruno (v1.0 04/03/18)
    """
def Unlock():
    """
        unlock an asteroid for automatic harvest

        Version:
        --------
        specification: Beyers Bruno (v1.0 04/03/18)
    """
#PHASE 3 *************************************************
def phase_three():
    """
        calling phase three functions

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
    """

def attack(type_vaisseau):
    """ attack the ennemy

        parameters:
        -----------
        type_spaceship: caracteristic (attack/scope) of the selected spaceship (list)

        Note:
        ----
        scope and damages must be strictly positive
        excavators can't attack

        version:
        --------
        specification: Beyers Bruno (v.1 02/03/18)
    """
def moves(data_structure):
    """
        move spaceship
        
        Parameters:
        -----------
        data_structure: position of the selected spaceship (dict(list(int)))
        
        Note:
        -----
        data_structure don't already have a name(variable)
        can't move out of UI
        
        return:
        -------
        spaceship_position: spaceship coordinates after have been moved(list(int))
        
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
        
    """
    
def end(nbr_turn,health_portail):
    """
        ends the game
    
        Parameters:
        -----------
        nbr_turn: turn number without any taken damages (int)
        health_portail: health points of the portal(int)
        
        Note:
        -----
        the game ends if 20 turns have been done without any taken damages
        the game ends if portal heatlh is at 0
        
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
        
    """
    
#PHASE 4 *********************************
def phase_four():
    """
        calling phase four functions

        Version:
        --------
        specification: Beyers Bruno (v1.0 03/02/18)
   """
def asteroid_sold_out(data_structure):
    """
        distributed the ores fairly in case of sold out

        Parameters:
        -----------
        data_structure: ore number left in the data structure(dict(int))
        
        Note:
        -----
        data structure don't already have a name(variable)
        
        Return:
        -------
        nbr_ores: ore number distributed to the player(int)
        
        Version:
        --------
        specification: Beyers Bruno (v1.0 05/03/18)
        
    """
def illegal_action():
    """
    verify if the player action can be effectued
    note:
    -----
    check if player action is legal
    Version:
    --------
    specification: Bechet François(v1.0 05/03/18)
