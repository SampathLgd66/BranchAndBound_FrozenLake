import gym
import imageio
import os
from frozen_lake_env import create_env
from branch_and_bound import branch_and_bound

def generate_gif():
    env = create_env()
    path, _, _ = branch_and_bound(env)

    frames = []
    obs, _ = env.reset()

    for action in path:
        frame = env.render()
        frames.append(frame)
        obs, _, done, _, _ = env.step(action)
        if done:
            frame = env.render()
            frames.append(frame)
            break

    env.close()

    os.makedirs("results/gifs", exist_ok=True)
    gif_path = "results/gifs/bnb_frozenlake.gif"
    imageio.mimsave(gif_path, frames, duration=0.5)
    print(f"🎞️ GIF saved to: {gif_path}")

if __name__ == "__main__":
    generate_gif()
