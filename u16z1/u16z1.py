class Kassa: 
 def __init__(self, money=0):
  self.money = money
def top_up(self, x):
 self.money += x
def count_1000(self):
  return self.money // 1000
def take_away(self, x):
  if x > self.money:
   raise ValueError('Not enough money in the cash register.')
  self.money -= x