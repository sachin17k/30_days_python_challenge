#sample while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print("else part ",counter)

#while loop with continue (terminates only the iteration and moves on to the next loop)
counter = 10
while counter < 20:
    if counter%2 != 0:
        counter += 1
        continue
        
    print(counter)
    counter += 1

#while with break (terminates the entire loop)
counter = 20
while counter < 25:
    print(counter)
    if counter == 23:
        break
    counter += 1
