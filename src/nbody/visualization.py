import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def animate_2d(positions_over_time, interval=50):
    """
    Create a 2D animation of the trajectories.
    positions_over_time: List of (body_name, position ndarray).
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Extract max range for better scaling
    all_positions = []
    for snapshot in positions_over_time:
        for _, pos in snapshot:
            all_positions.append(pos)

    all_positions = [p for p in all_positions]
    xs = [p[0] for p in all_positions]
    ys = [p[1] for p in all_positions]
    margin = 0.1 * (max(xs) - min(xs))
    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys) - margin, max(ys) + margin)

    scatters = []
    def init():
        for _ in positions_over_time[0]:
            scat = ax.plot([], [], 'o')[0]
            scatters.append(scat)
        return scatters

    def update(frame):
        snapshot = positions_over_time[frame]
        for i, (body_name, pos) in enumerate(snapshot):
            scatters[i].set_data(pos[0], pos[1])
        return scatters

    ani = animation.FuncAnimation(fig, update, frames=len(positions_over_time),
                                  init_func=init, interval=interval, blit=True)
    plt.show()

def animate_3d(positions_over_time, interval=50):
    """
    Create a 3D animation of the trajectories.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    all_positions = []
    for snapshot in positions_over_time:
        for _, pos in snapshot:
            all_positions.append(pos)

    xs = [p[0] for p in all_positions]
    ys = [p[1] for p in all_positions]
    zs = [p[2] for p in all_positions]

    margin = 0.1 * (max(xs) - min(xs))
    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys) - margin, max(ys) + margin)
    ax.set_zlim(min(zs) - margin, max(zs) + margin)

    scatters = []
    def init():
        for _ in positions_over_time[0]:
            scat = ax.plot([], [], [], 'o')[0]
            scatters.append(scat)
        return scatters

    def update(frame):
        snapshot = positions_over_time[frame]
        for i, (body_name, pos) in enumerate(snapshot):
            scatters[i].set_data(pos[0], pos[1])
            scatters[i].set_3d_properties(pos[2])
        return scatters

    ani = animation.FuncAnimation(fig, update, frames=len(positions_over_time),
                                  init_func=init, interval=interval, blit=True)
    plt.show()
