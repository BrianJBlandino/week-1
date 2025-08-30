def palindrome(word):
    word = word.lower() # make all characters lowercase
    word = word.replace(',', '') # remove commas
    word = word.replace(' ', '') # remove spaces
    word = word.replace('.', '') # remove period
    print(word[::-1]) # testing if the reverse word works
    if (word[::-1] == word): # seeing if the reverse matches the original
        return True
    else:
        return False

def parentheses(sequence):
    lp = sequence.count('(') # count the number of left parentheses
    rp = sequence.count(')') # count the number of right parentheses
    print(lp) # check the lp count
    print(rp) # check the rp count
    if lp == rp: # checking to see if the sequence is balanced
        return True
    else:
        return False
# add code below ...
