import gym

def create_env():
    return gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False)
