import GameState as g

height_selected = False
width_selected = False
current_player_id = 1
game_running = True

"""Définitions des classes représentant les différentes erreurs possibles"""
class FormatError(Exception):
    """Cette classe représente l'erreur renvoyée pour les erreurs de format"""
    pass

class LineError(Exception):
    """Cette classe représente l'erreur renvoyée lorsque la ligne est déjà tracée sur le plateau"""
    pass

"""Définition des fonctions de jeu"""
def help_function():
    print("\n\nPour jouer vous devez taper les points de départs et d'arrivée suivant le fomrat suivant : (X X)(X X) ou X est un nombre appartenant aux limites du plateau\nLes points doivent être adjacents sur le plateau de jeu, ils ne peuvent pas être adjacents dans la diagonale, ils doivent pouvoir être reliés par une seule et unique ligne.\n\n")
    
"""Cette fonction permet de voir si les arguments donnés pour tracer une ligne sont bien formatés et si leur nombre est le bon, elle vérifie également si leur type est bien entier
Elle renvoie ensuite les points de départ et d'arrivée qu'elle en a extrait"""

def formating(command):
    digits_list = []
    command = ''.join(x for x in command if x.isdigit())
    if len(command) == 4:
        for elt in command:
            if (int(elt) < height_selected) and (int(elt) < height_selected) == False:
                return False
            else:
                digits_list.append(int(elt))
        starting_point = (digits_list[0],digits_list[1])
        ending_point = (digits_list[2],digits_list[3])
        return (starting_point,ending_point)
    else:
        return False

#Permet de choisir la hauteur du plateau en gérant les erreurs de type ainsi que les tailles maximales du plateau
while height_selected == False:
    try:
        height = int(input("Quelle hauteur de plateau voulez vous ? (elle doit comprise entre 1 et 25 inclus)\n"))
        if height > 0 and height < 26:
            height_selected = True
        else:
            print("La valeur doit être comprise entre 1 et 25 inclus")
    except ValueError:
        print("\n\nLa hauteur doit etre un entier positif\n")

#Permet de choisir la largeur du plateau en gérant les erreurs de type ainsi que les tailles maximales du plateau
while width_selected == False:
    try:
        width = int(input("Quelle largeur de plateau voulez vous ? (elle doit comprise entre 1 et 25 inclus)\n"))
        if width > 0 and width < 26:
            width_selected = True
        else:
            print("La valeur doit être comprise entre 1 et 25 inclus")
    except ValueError:
        print("\n\nLa largeur doit être un entier positif")
    
#On créer le jeu avec les bonnes tailles pour la création du plateau
GS = g.game_state(height,width)

#Boucle principale du jeu
while game_running:
    GS.textDisplay()
    
    command_accepted = False
    
    #boucle entre les comandes
    while command_accepted == False:
        try:
            command = input("Tapez h pour afficher l'aide\nPour jouer tapez le point de départ de votre ligne et le point d'arrivée\n")
            if command == 'h':
                help_function()
                command_accepted = True
            if command == 'q':
                game_running = False
                command_accepted = True
                
            else:
                formating_result = formating(command)
                if formating_result == False:
                    raise(FormatError)
                else:
                    starting_point = formating_result[0]
                    ending_point = formating_result[1]
                    result_play = GS.play(starting_point,ending_point,current_player_id)
                    GS.play(starting_point,ending_point,current_player_id)
                    
                    if result_play == "invalid line":
                        raise(ValueError)
                    elif result_play == "already drawn":
                        raise(LineError)
                    elif result_play == "another play":
                        print("\n\nCarré complété, vous pouvez rejouer")
                        command_accepted = True
                    elif result_play == "end of game":
                        GS.textDisplay()
                        command_accepted = True
                        game_running = False
                    else:
                        if current_player_id == 1:
                            current_player_id += 1
                        else:
                            current_player_id -=1
                        print(f"\n\nC'est au joueur {current_player_id} de jouer")
                        command_accepted = True

        except FormatError:
            print("\n\nMauvais format")
        except ValueError:
            print("\n\nLes points doivent être adjacents")
        except LineError:
            print("\n\nLa ligne est déjà tracée")
        