import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fig2 = plt.figure()
ax2 = fig.add_subplot(2, 2, 2)

def animate(i):
    graph_data = open('Daten.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

def animate2(i):
    graph_data2 = open('Daten2.txt','r').read()
    lines2 = graph_data2.split('\n')
    xs2 = []
    ys2 = []
    for line in lines2:
        if len(line) > 1:
            x2, y2 = line.split(',')
            xs2.append(float(x2))
            ys2.append(float(y2))
    ax2.clear()
    ax2.plot(xs2, ys2)

ani = animation.FuncAnimation(fig, animate, interval=1000)
ani2 = animation.FuncAnimation(fig2, animate2, interval=1000)
plt.show()