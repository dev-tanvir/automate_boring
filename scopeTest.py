def spam():
    eggs = 99
    bacon()
    #spam()
    print(eggs)   #it will print 99 cause bacon() scope is destryoed when bacon()
                  #---(previous line)-----------is called and returned  
def bacon():
    ham = 101
    eggs = 0
    return print(eggs)
spam()
