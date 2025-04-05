import time
from queue import PriorityQueue
from frozen_lake_env import create_env

def heuristic(pos, goal, ncols):
    x1, y1 = divmod(pos, ncols)
    x2, y2 = divmod(goal, ncols)
    return abs(x1 - x2) + abs(y1 - y2)

def branch_and_bound(env):
    start_time = time.time()
    nrows, ncols = int(env.desc.shape[0]), int(env.desc.shape[1])
    goal_state = nrows * ncols - 1

    frontier = PriorityQueue()
    visited = set()

    obs, _ = env.reset()
    frontier.put((0, obs, []))

    while not frontier.empty():
        _, state, path = frontier.get()
        if state in visited:
            continue
        visited.add(state)

        if state == goal_state:
            return path, time.time() - start_time, 1

        for action in range(env.action_space.n):
            env.unwrapped.s = state  # Set current state manually
            next_obs, reward, done, truncated, _ = env.step(action)

            if next_obs in visited:
                continue

            cost = len(path) + 1
            h = heuristic(next_obs, goal_state, ncols)
            total_cost = cost + h

            frontier.put((total_cost, next_obs, path + [action]))

    return [], time.time() - start_time, 0
