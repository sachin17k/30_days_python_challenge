'''Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
 If the user input is: September, October or November, the season is Autumn.
 December, January or February, the season is Winter.
 March, April or May, the season is Spring. June, July or August, the season is Summer'''

m = input("Enter the current month :")
ml = m.lower()
if ml == 'september' or ml == 'october' or ml == 'november':
    print("The season is  Autumn")
elif ml == 'december' or ml == 'january' or ml == 'february':
    print("The season is Winter")
elif ml == 'march' or ml== 'april' or ml== 'may':
    print("The season is Spring")
else:
    print("The season is Summer")

#error
'''Enter the current month :sdfghjk
   The season is Summer'''