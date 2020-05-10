import pygame
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter, defaultdict

pygame.init()
GUI = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Move Ball v2")
run = True
pos = None
arr_pos_list = []
circle_pos = [400, 400]
BLACK = [0,0,0]
ar_np = np.array(arr_pos_list)
plt.title("Mouse Click Positions")
plt.xlabel("x - point")
plt.ylabel("y - point")
plt.axis([0,800,0,800])
clf = KMeans(n_clusters=2)

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
        ar_np = np.array(arr_pos_list)
        print(ar_np)
        if len(ar_np)>10:
            clf.fit(ar_np)
            centroids = clf.cluster_centers_
            labels = clf.labels_
            colors = ["g.", "r.", "c.", "b.", "k.", "o."]
            for i in range(len(ar_np)):
                plt.plot(ar_np[i][0], ar_np[i][1], colors[labels[i]])
            k = Counter(clf.labels_)
            a_centroid = Counter(clf.labels_)[0]
            b_centroid = Counter(clf.labels_)[1]
            if a_centroid > b_centroid:
                circle_pos = [int(centroids[0][0]),int(centroids[0][1])]
            if b_centroid > a_centroid:
                circle_pos = [int(centroids[1][0]),int(centroids[1][1])]
            if b_centroid == a_centroid:
                circle_pos = [400,400]

    pygame.display.update()
pygame.quit()

clf.fit(ar_np)
centroids = clf.cluster_centers_
labels = clf.labels_
colors = ["g.","r.","c.","b.","k.","o."]
for i in range(len(ar_np)):
    plt.plot(ar_np[i][0], ar_np[i][1], colors[labels[i]])
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x')
print(Counter(clf.labels_))
plt.show()