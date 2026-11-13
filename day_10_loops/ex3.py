'''Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  output:
  #
  ##
  ###
  ####
  #####
  ######
  #######'''
for i in range(1,8):
    print('#'*i)

print("WHILE LOOP")
count = 1
while count < 8:
    print('#'*count)
    count+=1