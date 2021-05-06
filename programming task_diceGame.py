




# Ed Trujillo


# Programming task
# Creating a dice game that
# 1. uses 6-sided, 10-sided, and 20-sided dice
# 2. uses a cup to hold the dice
# 3. lets the user shake the cup with the desired dice numbers for each die 
# 4. and gets the sum of dice in the cup





import random

# creating dice and rolling them
#####################################################################################


class SixSidedDie:
    """Represents the outcome of rolling a six-sided-die. Values are 1-6."""
    die_vals = [1,2,3,4,5,6] 
    rolledValue = []
    
    def roll(self): 
        """Rolling and getting a 6 sided die value."""
        
        die_vals = random.shuffle(SixSidedDie.die_vals)   # shuffling die 
        res = random.choice(self.die_vals)                # geting die value
        self.res = res
        SixSidedDie.rolledValue.append(res)
        return self.res
    
    def __repr__(self):
        """Printing die value results."""
        
        return "SixSidedDie({})".format(self.res)



die=SixSidedDie()
die.roll() # shuffling results
die        # type of die and results


class TenSidedDie(SixSidedDie):
    """Represents the outcome of rolling a ten-sided-die. Values are 1-10."""
    die_vals = [1,2,3,4,5,6,7,8,9,10] 
    def __repr__(self):
        return "TenSidedDie({})".format(self.res)


die = TenSidedDie()
die.roll() # shuffling results
die        # type of die and results




class TwentySidedDie(SixSidedDie):
    """Represents the outcome of rolling a twenty-sided-die. Values are 1-20."""
    rank = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #adjusted values for this die
    def __repr__(self):
        return "TwentySidedDie({})".format(self.res)


die = TwentySidedDie()
die.roll() # shuffling results
die        # type of die and results




# Placing dice in a cup and rolling them
#####################################################################################


class Cup:
    """Takes in a set number of dice and places them in a cup. It rolls the cup and obtains the sum of all the rolled dice inside the cup."""
    def __init__(self, six=0, ten=0, twenty=0):  
        self.six =   six
        self.ten =    ten
        self.twenty = twenty

    def sixDie(self):   
        """Simulates rolling a 6 sided die n times. Returns sum of all rolls."""
        sixSum = 0
        for rolls in range(1, self.six + 1):
            six_die = SixSidedDie()
            roll_value =  six_die.roll()
            sixSum =  sixSum + roll_value
        self.sixSum = sixSum
        return sixSum

    def tenDie(self):
        """Simulates rolling a 10 sided die n times. Returns sum of all rolls."""
        tenSum = 0 
        for rolls in range(1,self.ten + 1):
            ten_die = TenSidedDie()
            roll_value = ten_die.roll()
            tenSum = tenSum + roll_value
        self.tenSum = tenSum
        return tenSum
    
    def twentyDie(self): 
        """Simulates rolling a 20 sided die n times. Returns sum of all rolls."""
        twentySum=0
        twen_rollsLst = []
        for rolls in range(1,self.twenty + 1):
            twen_roll = TwentySidedDie()
            roll_value = twen_roll.roll()
            twentySum = twentySum + roll_value
            twen_rollsLst.append(rolls)
        self.twentySum = twentySum
        return twentySum

    def getSum(self): 
        """ Returns the sum of the dice rolled."""
        totalSum = self.sixSum + self.tenSum + self.twentySum 
        return totalSum

    def __repr__(self):
        return "SixSidedDie({}),TenSidedDie({}),TwentySidedDie({})".format(self.sixSum,self.tenSum,self.twentySum)



#ex 1
cup = Cup(1,2,3)  # number of 6 sided, 10 sided, and 20 sided dice in the cup
cup.sixDie()    # sum of all 6 side dice
cup.tenDie()    # sum of all 10 side dice
cup.twentyDie() # sum of all 20 side dice
cup.getSum()    # sum of all dice in the cup
cup             # cup summary


#ex 2 --when no dice numbers are entered
cup = Cup()
cup.sixDie()
cup.tenDie()
cup.twentyDie()
cup.getSum()
cup
