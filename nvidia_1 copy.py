# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
maximum_number_for_test = 400
nvidia_stock = [[f"day{i}", random.random() * maximum_number_for_test] for i in range(1, 8+1)]

buy = ""
sell = ""
max_profit = 0
for i in range(len(nvidia_stock)):
    for j in range(i+1, len(nvidia_stock)):
        if nvidia_stock[j][1] > nvidia_stock[i][1]:
            profit = nvidia_stock[j][1] - nvidia_stock[i][1]
            if profit > max_profit:
                max_profit = profit
                buy = nvidia_stock[i][0]
                sell = nvidia_stock[j][0]
    
print(buy)
print(sell)
print(max_profit)