import time
import csv
from frozen_lake_env import create_env
from branch_and_bound import branch_and_bound

def run_trials(runs=5, timeout=600):  # 10 mins
    results = []

    for i in range(runs):
        env = create_env()
        start = time.time()
        path, duration, reward = branch_and_bound(env)
        elapsed = time.time() - start

        results.append({
            'Run': i+1,
            'Time': round(duration, 4),
            'Reward': reward,
            'Steps': len(path) if reward else 'N/A'
        })

    # Save to CSV
    with open('results/times.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    for r in results:
        print(r)

if __name__ == "__main__":
    run_trials()
