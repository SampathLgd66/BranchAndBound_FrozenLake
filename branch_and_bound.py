import time
from queue import PriorityQueue

# Heuristic function: Manhattan distance
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
    
    # (priority, state, path)
    frontier.put((0, env.reset(), []))

    while not frontier.empty():
        _, state, path = frontier.get()
        visited.add(state)

        if state == goal_state:
            return path, time.time() - start_time, 1  # path, time, reward

        for action in range(env.action_space.n):
            next_state, reward, done, truncated, info = env.step(action)
            if next_state in visited:
                continue

            # Add to frontier with priority = cost + heuristic
            cost = len(path) + 1
            h = heuristic(next_state, goal_state, ncols)
            total_cost = cost + h
            frontier.put((total_cost, next_state, path + [action]))

            # Reset environment to original state
            env.unwrapped.s = state

    return [], time.time() - start_time, 0  # failed
