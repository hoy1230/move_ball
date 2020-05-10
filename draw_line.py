import numpy as np
import matplotlib.pyplot as plt

data = np.array([[570, 653], [588, 648], [589, 646], [598, 642], [599, 641], [598, 641], [597, 641], [596, 641], [605, 637], [606, 637], [607, 637], [598, 640], [593, 640], [585, 641], [582, 641], [590, 640], [592, 640], [598, 642], [596, 649], [608, 654], [610, 661], [621, 663], [622, 662], [626, 655], [626, 652], [612, 646], [607, 635], [621, 619], [625, 615], [640, 614], [637, 621], [637, 633], [648, 652], [663, 663], [668, 669], [660, 673], [654, 673], [645, 670], [631, 666], [621, 666], [613, 666], [603, 651], [605, 642], [603, 633], [614, 624], [625, 620], [640, 618], [640, 623], [656, 644], [662, 657], [655, 669], [652, 674], [643, 676], [639, 677], [630, 680], [625, 681], [617, 680], [616, 673], [615, 669], [611, 663], [607, 657], [603, 650], [606, 641], [613, 633], [619, 629], [621, 629], [627, 627], [628, 628], [637, 628], [638, 630], [644, 634], [645, 638], [643, 642], [644, 646], [643, 650], [643, 652], [640, 657], [639, 659], [634, 665], [633, 668], [632, 668], [632, 667], [632, 666], [632, 660], [633, 654], [633, 648], [635, 640], [636, 637], [637, 633], [638, 633], [646, 629], [646, 630], [659, 632], [660, 638], [665, 643], [665, 649], [659, 658], [643, 662], [640, 663], [635, 662], [625, 655], [625, 650], [628, 645], [638, 637], [641, 636], [652, 634], [654, 637], [653, 644], [660, 653], [658, 665], [656, 669], [648, 670], [637, 671], [637, 664], [643, 656], [647, 648], [663, 637], [664, 637]]
)
plt.scatter(data[:, 0], data[:, 1])
plt.title("Mouse Click Positions")
plt.xlabel("x - point")
plt.ylabel("y - point")
plt.axis([0,800,0,800])
plt.show()
