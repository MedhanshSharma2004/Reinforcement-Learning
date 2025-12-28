# Libraries
import os
import numpy as np
import matplotlib.pyplot as plt 

# Coin Biases
SEED = 20
np.random.seed(SEED)
coin_biases = np.random.uniform(0, 1, size = (3)).tolist()

# Parameters
epsilon_list = np.linspace(0, 1, num = 20).tolist()
numheads_arr = []
horizon = 1000

# Epsilon Greedy - 1 Algorithm
for epsilon in epsilon_list:
    
    # Preliminary toss (to ensure that mean is defined)
    coin1list, coin2list, coin3list = [], [], []
    outcomes = ['h', 't']
    prob1, prob2, prob3 = [coin_biases[0], 1 - coin_biases[0]], [coin_biases[1], 1 - coin_biases[1]], [coin_biases[2], 1 - coin_biases[2]]
    coin1list.append(str(np.random.choice(outcomes, p = prob1)))
    coin2list.append(str(np.random.choice(outcomes, p = prob2)))
    coin3list.append(str(np.random.choice(outcomes, p = prob3)))

    for toss in range(horizon):    
        # Best arm
        coins_avg_list = [coin1list.count('h')/len(coin1list), coin2list.count('h')/len(coin2list), coin3list.count('h')/len(coin3list)]
        best_mean = max(coins_avg_list)
        best_arm = coins_avg_list.index(best_mean) + 1

        # Exploration - Exploitation
        if toss <= int(epsilon*horizon):
            coin_num = int(np.random.choice([1, 2, 3]))
        else:
            coin_num = best_arm
        
        # Append the outcomes
        if coin_num == 1:
            coin1list.append(str(np.random.choice(outcomes, p = prob1)))
        elif coin_num == 2:
            coin2list.append(str(np.random.choice(outcomes, p = prob2)))
        else:
            coin3list.append(str(np.random.choice(outcomes, p = prob3)))

    total_heads = coin1list.count('h') + coin2list.count('h') + coin3list.count('h')
    numheads_arr.append(total_heads)
    print(f"Using Epsilon Greedy - 1 Algorithm for Horizon = {horizon} with Epsilon = {epsilon}:\nTotal number of heads: {total_heads}")

    # Expected Number of heads
    explore_heads = (epsilon * horizon) * (sum(coin_biases) / 3)
    exploit_heads = (1 - epsilon) * horizon * coin_biases[best_arm - 1]
    expected_heads = explore_heads + exploit_heads
    print(f"Expected number of heads: {expected_heads}")

# Plotting number of heads v/s epsilon
plt.plot(epsilon_list, numheads_arr)
plt.xlabel('Epsilon')
plt.ylabel('Number of heads')
plt.title('Search for Optimal Epsilon')
plt.show()
