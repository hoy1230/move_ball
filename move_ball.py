import pygame
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter, defaultdict

pygame.init()
GUI = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Move Ball")
run = True
pos = None
arr_pos_list = []
circle_pos = [400, 400]
BLACK = [0,0,0]
sum_x = 400
sum_y = 400
ave_x = 0
ave_y = 0
number_click = 0
ar_np = np.array(arr_pos_list)

while run:
    GUI.fill(BLACK)
    pygame.draw.circle(GUI, (200, 0, 0), circle_pos, 150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            break
    if event.type == pygame.MOUSEBUTTONDOWN and pos != pygame.mouse.get_pos():
        pos = pygame.mouse.get_pos()
        print(pos)
        arr_pos_list.append(list(pos))
        print(arr_pos_list)
        sum_x = sum_x+arr_pos_list[number_click][0]
        sum_y = sum_y+arr_pos_list[number_click][1]
        ave_x = int(sum_x / (len(arr_pos_list)+1))
        ave_y = int(sum_y / (len(arr_pos_list)+1))
        circle_pos = [ave_x, ave_y]
        number_click = number_click+1
        ar_np = np.array(arr_pos_list)
        print(ar_np)
    pygame.display.update()
pygame.quit()


plt.title("Mouse Click Positions")
plt.xlabel("x - point")
plt.ylabel("y - point")
plt.axis([0,800,0,800])
clf = KMeans(n_clusters=2)
clf.fit(ar_np)
centroids = clf.cluster_centers_
labels = clf.labels_
colors = ["g.","r.","c.","b.","k.","o."]
for i in range(len(ar_np)):
    plt.plot(ar_np[i][0], ar_np[i][1], colors[labels[i]])
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x')
print(Counter(clf.labels_))
plt.show()