import gym

def create_env():
    return gym.make("FrozenLake-v1", is_slippery=False, render_mode="rgb_array")

