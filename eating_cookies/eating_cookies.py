#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement

# a solution that is more efficient than the naive

# recursive solution

# cookie monster can eat 0,1,2,3 cookies at a time

# find combinations for n number of cookies

# since it's recursive, all we need to do is solve for base (error) cases

# then one more case

# call itself

# use caching afterwards

# notes on eating cookies

# Look at the ways to eat (n-1) cookies, then eat one more
# Look at the ways to eat (n-2) cookies, then at 2 at once
# Look at the ways to eat (n-3) cookies, then eat 3 at once

# cookies = 1
# 1

# cookies = 2
# 11
# 2



# cookies = 3
# 111
# 12
# 21
# 3

# cookies = 4
# 1111
# 112
# 121
# 211
# 22
# 13
# 31

# cookies = 5
# 11111
# 1112
# 1121
# 1211
# 2111
# 122
# 212
# 221
# 113
# 131
# 311
# 32
# 23
  # base/error cases up front

 
  # check for three first because it can use all three options (1,2,3)

  # one and two test (maybe do 0, 1, and 2 for base cases), then do 3+

newArray = []

def eating_cookies(n):
  if n == 1:
      return 1
  if n == 0:
      return 1
  if n < 0:
      return 0
  print(eating_cookies(n-1), "A")
 # print(eating_cookies(n-2), "B")
 # print(eating_cookies(n-3), "C")
  return eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
