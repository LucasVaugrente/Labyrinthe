from random import choice
from mur import Mur
import pygame

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

ratio_affichage = 2/1 # Exemple de ratio d'aspect souhaité

ratio_ecran = screen_width / screen_height

if ratio_affichage < ratio_ecran:
    taille_affichage_h = screen_height
    taille_affichage_l = ratio_affichage * taille_affichage_h
else:
    taille_affichage_l = screen_width
    taille_affichage_h = taille_affichage_l / ratio_affichage

print(int(screen_width/9.6)+1, int(screen_height/10.2)+1)

class Labyrinthe:
    def __init__(self):
        
        # taille du labyrinthe (c'est un carré du coup)
        self.larg = 191
        self.haut = 101

        self.grid = []  # liste deux dimensions (axe x, axe y), une valeur (aux coordonnées (x, y)) symbolise une case du labyrinthe
        self.tiles_dict = {}  # dictionnaire pour toutes les cases sous la forme {(x, y) = value}
        self.Mur=[]
        self.start = ()
        self.end = ()

    def create_grid_kruskal(self):

        ### Création de la grille uniquement avec des murs ___________________________________________________________ #
        self.grid = [['1' for _ in range(self.larg)] for _ in range(self.haut)]

        ### Ajout des cases tout les un mur sur deux et assignement de leur valeur ___________________________________ #
        count = 100  # on commence à 100 pour que le print final soit plus graphique
        for y in range(1, self.haut - 1, 2):
            for x in range(1, self.larg - 1, 2):
                self.grid[y][x] = count
                self.tiles_dict[(x, y)] = count  # ajout de la case dans le dictionnaire
                count += 1

        ### Création du labyrinthe _____________________________________________________________________________________ #
        all_converted = False
        while not all_converted:  # Tant que toutes les valeurs des cases ne sont pas égale à 100

            ### Choix des deux case à traiter __________________________________________________________________________ #
            first_tile = choice([key for key in self.tiles_dict.keys()])
            first_value = self.tiles_dict[first_tile]

            neighborhood_list = self.choose_neighbors(first_tile[0], first_tile[1])
            second_tile = choice(neighborhood_list)
            second_value = self.tiles_dict[second_tile]

            ### Détermination de la quelle des deux cases on 'garde' ___________________________________________________ #
            if first_value < second_value:
                convert_tile = second_tile
                new_value = first_value
                last_value = second_value

            elif second_value < first_value:
                convert_tile = first_tile
                last_value = first_value
                new_value = second_value

            else:  # si les deux valeurs sont égales -> on reprend à la prochaine itération de la boucle while
                continue

            ### Destruction du mur entre les deux cases ________________________________________________________________ #
            wall_x = first_tile[0] + self.derterminate_wall_pos(first_tile, second_tile)[0]
            wall_y = first_tile[1] + self.derterminate_wall_pos(first_tile, second_tile)[1]
            self.grid[wall_y][wall_x] = 100

            ### Recherche et conversion des autres cases du 'bout de chemin' de la case convertie ______________________ #
            for tile, tile_value in self.tiles_dict.items():
                if tile_value == last_value:
                    self.grid[tile[1]][tile[0]] = new_value
                    self.tiles_dict[tile] = new_value

            ### Comptage du nombre de case égale à 100 _________________________________________________________________ #
            counter_converted = count
            for tile, tile_value in self.tiles_dict.items():
                if tile_value == 100:

                    counter_converted -= 1

            if counter_converted == 100:
                all_converted = True

            ### Fin de boucle while ____________________________________________________________________________________ #
        self.depart_arrivee()

    @staticmethod
    def derterminate_wall_pos(start_tile, end_tile):
        pos = [0, 0]

        if start_tile[0] < end_tile[0]:
            pos[0] = 1
        elif start_tile[0] > end_tile[0]:
            pos[0] = -1

        if start_tile[1] < end_tile[1]:
            pos[1] = 1
        elif start_tile[1] > end_tile[1]:
            pos[1] = -1

        return pos

    def choose_neighbors(self, x, y):
        neighborhood_list = []

        if x > 1:
            neighborhood_list.append((x - 2, y))

        if x < self.larg - 2:
            neighborhood_list.append((x + 2, y))

        if y > 1:
            neighborhood_list.append((x, y - 2))

        if y < self.haut - 2:
            neighborhood_list.append((x, y + 2))

        return neighborhood_list

    def create_lab(self):
        self.create_grid_kruskal()
        y = 0
        for row in self.grid:
            x = 0
            for tile in row:
                if tile == '1':
                    self.Mur.append(Mur(x * 10, y * 10))
                x += 1
            y += 1

        return self.grid

    def depart_arrivee(self):
        self.grid[1][1] = 100
        self.grid[self.haut-2][self.larg-2] = 100
        self.start = (1, 1)   #Départ
        self.end = (self.haut-2, self.larg-2)  #Arrivée


lab = Labyrinthe()
lab.create_grid_kruskal()
#print(*lab.grid, sep='\n')
