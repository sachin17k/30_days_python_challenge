import os
os.mkdir('sachin')
os.mkdir('sample')
os.chdir('D:/30_days_python\day_12_modules')

info = os.getcwd()
print("info",info)

os.rmdir('sample')
