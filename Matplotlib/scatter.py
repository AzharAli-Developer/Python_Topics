import matplotlib.pyplot as plt
import numpy as np

# x = np.array([1, 5, 2, 7])
# y = np.array([4, 6, 2, 8])
# plt.plot(x, y, linestyle = "dashed", color = 'r' , linewidth = '6')
# plt.show()


# x = np.random.rand(100)
# y = np.random.rand(100)
# plt.plot(x, y, color = 'red', linestyle = 'dashed')
# plt.show()


# x = np.array([1, 5, 2, 7])
# y = np.array([4, 6, 2, 8])
# plt.subplot(3,2,1)
# plt.title('First Graph')
# plt.plot(x, y, linestyle = "dashed", color = 'r' , linewidth = '6')
#
#
# x = np.array([3, 5, 1, 8])
# y = np.array([1,3, 7, 6])
# plt.subplot(3,2,2)
# plt.title('Second Graph')
# plt.plot(x, y, linestyle = "dashed", color = 'r' , linewidth = '6')
#
#
# plt.suptitle('Graph Practices')
# plt.show()




# x = np.array([1, 5, 2, 7])
# y = np.array([4, 6, 2, 8])
# plt.subplot(3,2,1)
# plt.grid()
# plt.title('First Graph')
# plt.plot(x, y, linestyle = "dashed", color = 'r' , linewidth = '6')
#
#
# x = np.array([3, 5, 1, 8])
# y = np.array([1,3, 7, 6])
# plt.subplot(3,2,2)
# plt.title('Second Graph')
# plt.grid()  #We can apply the grid x and y use the axis word.
# plt.plot(x, y, linestyle = "dashed", color = 'r' , linewidth = '6')
#
#
# plt.suptitle('Graph Practices')
# plt.show()



# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.scatter(x, y)
# plt.grid(axis = 'x')
# plt.show()


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.scatter(x, y, color = 'green')
# plt.show()


##############Color of each dot.

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, c=colors)
# plt.show()


# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes)
# plt.show()


x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()