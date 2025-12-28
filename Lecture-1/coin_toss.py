# Libraries
import os
import numpy as np

# Coin Biases
SEED = 40
np.random.seed(SEED)
coin_biases = np.random.uniform(0, 1, size = (3)).tolist()

# Tosses
num_tosses = 20
coin1list, coin2list, coin3list = [], [], []
for toss in range(num_tosses):
    print(f"Coin 1: {coin1list}\nCoin 2: {coin2list}\nCoin 3: {coin3list}\nNumber of tosses left: {num_tosses - toss}")
    coin_num = int(input("Which coin do you want to toss (1/2/3)? "))
    outcomes = ['h', 't']
    prob = [coin_biases[coin_num - 1], 1 - coin_biases[coin_num - 1]]
    output = str(np.random.choice(outcomes, p = prob))
    if coin_num == 1:
        coin1list.append(output)
    elif coin_num == 2:
        coin2list.append(output)
    else:
        coin3list.append(output)
    os.system('clear')

total_heads = coin1list.count('h') + coin2list.count('h') + coin3list.count('h')
print(f"Coin 1: {coin1list}\nCoin 2: {coin2list}\nCoin 3: {coin3list}\nTotal number of heads: {total_heads}")