import argparse

# Write a function find_max_profit that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.

# Loop over the array, taking the difference between selected stock and the rest of the stocks, storing the result in a dictionary.

# Look in the dictionary for the highest price, and return that price

# Numbers will be negative, so we'll need to look for the largest negative number and return that number as a positive by multiplying it as negative one

prices = [10, 7, 5, 8, 11, 9]

def find_max_profit(prices):
    listOfProfits = []
    for x in range(len(prices)):
        for y in range(x+1,len(prices)):
           # if prices[y] > prices[x]:
            #    print(f"{prices[y]}, {prices[x]}")
             #   listOfProfits.append(0)
           # else:
                listOfProfits.append(prices[y]-prices[x])

   
    return max(listOfProfits)
#find_max_profit(prices)

def find_max_profit_take_2(prices):
    current_min_price_so_far = 0
    max_profit_so_far = 0
    for x in range(len(prices)):
        current_min_price_so_far = prices[x]
        for y in range(len(prices)):
            max_profit_so_far = prices[y]-prices[x]
            print(max_profit_so_far)
            print(current_min_price_so_far)

#find_max_profit_take_2(prices)
            
            

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
