months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
days = [31,28,31,30,31,30,31,31,30,31,30,31]
print("this is list\n")
for months, days in zip(months, days):
   print( months,days)
print("")
months = 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'
days = 31,28,31,30,31,30,31,31,30,31,30,31
print("this is tuple\n")
for months, days in zip(months, days):
      print(months,days)



    
   
