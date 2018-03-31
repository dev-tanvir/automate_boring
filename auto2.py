#a = 0
#if a < 6:
#    print('a')
#    if a == 3:
#        continue   #it is an error cause continue must be in a loop
#    a=a+1

while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)
