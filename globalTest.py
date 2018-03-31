def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs) #will print spam cause eggs is declared as global
