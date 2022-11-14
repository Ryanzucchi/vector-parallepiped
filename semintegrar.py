import matplotlib.pyplot as plt

v =[2, 3, 1]
u =[2, 5, 4]
w =[7, 2, 10]

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.set_xlim([-1,10])
ax.set_ylim([-10,10])
ax.set_zlim([0,15])

start =[0,0,0]

ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color ='b')
ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2], color ='g')
ax.quiver(start[0], start[1], start[2], w[0], w[1], w[2], color ='r')

#WWWWW
ax.quiver(2, 3, 1, w[0], w[1], w[2], color ='r')
ax.quiver(2, 5, 4, w[0], w[1], w[2], color ='r')
#uuuuuu
ax.quiver(2, 3, 1, u[0], u[1], u[2], color ='g')
ax.quiver(7, 2, 10, u[0], u[1], u[2], color ='g')
#vvvvvv
ax.quiver(2, 5, 4, v[0], v[1], v[2], color ='b')
ax.quiver(7, 2, 10, v[0], v[1], v[2], color ='b')
#somados
#v+u
ax.quiver(4, 8, 5, w[0], w[1], w[2], color ='r')
#w+u
ax.quiver(9, 7, 14, v[0], v[1], v[2], color ='b')
#w+v
ax.quiver(9, 5, 11, u[0], u[1], u[2], color ='g')

ax.view_init(10,10)
plt.show()
