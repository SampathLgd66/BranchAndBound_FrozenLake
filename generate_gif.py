import imageio
import numpy as np
import matplotlib.pyplot as plt
from frozen_lake_env import create_env
from branch_and_bound import branch_and_bound

def create_gif(output_path="results/gifs/run.gif"):
    env = create_env()
    path, _, reward = branch_and_bound(env)
    frames = []

    state = env.reset()
    for action in path:
        frame = env.render(mode='rgb_array')
        frames.append(frame)
        state, _, _, _, _ = env.step(action)

    imageio.mimsave(output_path, frames, duration=0.5)

if __name__ == "__main__":
    create_gif()
