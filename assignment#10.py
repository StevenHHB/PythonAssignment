current = input('Please enter current investment amount:')
year = input('Please enter year until retirement:')
expected = input('Please enter expected rate of return:') / 100


Future = current * (1+expected)**year

print('Your ending value based on input is:', Future);

BOOL = input('would you like to add more money?')


if(BOOL == 'yes'):
  extra = input('How much do you plan to add each year?')
  
  
  
  print('Your revised ending value is:', )
  print('Thank you! Have a nice day')
  return
  
print('Thank you! Have a nice day')
