import pygame

class Resolve(pygame.sprite.Sprite):

    def __init__ (self, lab: list, start : tuple, end : tuple):
        super().__init__()
        self.lab = self.convert_grid(lab)
        self.start = start
        self.end = end

    def convert_grid (self, grid):
        for i in range(0, len(grid)):
            grid[i] = [0 if x == 100 else 1 for x in grid[i]]

        return grid

    def res_dfs (self):

        a = self.lab
        start = self.start
        end = self.end

        m = []
        for i in range(len(a)):
            m.append([])
            for j in range(len(a[i])):
                m[-1].append(0)
        i, j = start
        m[i][j] = 1

        # nouvelle étape
        def make_step (k):
            for i in range(len(m)):
                for j in range(len(m[i])):
                    if m[i][j] == k:
                        if i > 0 and m[i - 1][j] == 0 and a[i - 1][j] == 0:
                            m[i - 1][j] = k + 1
                        if j > 0 and m[i][j - 1] == 0 and a[i][j - 1] == 0:
                            m[i][j - 1] = k + 1
                        if i < len(m) - 1 and m[i + 1][j] == 0 and a[i + 1][j] == 0:
                            m[i + 1][j] = k + 1
                        if j < len(m[i]) - 1 and m[i][j + 1] == 0 and a[i][j + 1] == 0:
                            m[i][j + 1] = k + 1

        # boucle
        k = 0
        while m[end[0]][end[1]] == 0:
            k += 1
            make_step(k)

        # récupérer les coordonnées du chemin :
        i, j = end
        k = m[i][j]
        the_path = [(i, j)]
        while k > 1:
            if i > 0 and m[i - 1][j] == k - 1:
                i, j = i - 1, j
                the_path.append((i, j))
                k -= 1
            elif j > 0 and m[i][j - 1] == k - 1:
                i, j = i, j - 1
                the_path.append((i, j))
                k -= 1
            elif i < len(m) - 1 and m[i + 1][j] == k - 1:
                i, j = i + 1, j
                the_path.append((i, j))
                k -= 1
            elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
                i, j = i, j + 1
                the_path.append((i, j))
                k -= 1

        return the_path
