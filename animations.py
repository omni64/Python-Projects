import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
import time

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def show():
    time.sleep(2)

    def animate(i):
        graph_data = open('files\\mytimes.txt', 'r').read()
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

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()


show()
