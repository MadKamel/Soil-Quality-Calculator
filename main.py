# For the system() call, to clear the screen between tests
import os

# The percentage calculation
def calculate(sand_arg, silt_arg, clay_arg):
  total = sand_arg + silt_arg + clay_arg
  return [(sand_arg/total) * 100, (silt_arg/total) * 100, (clay_arg/total) * 100]

# Mainloop function
def run_test():
  # Reset crash flag to False
  crashed = False

  print('How many parts of each are present in the soil?')

  # In case the user enters an invalid number
  try:
    sand = int(input('Sand: '))
    silt = int(input('Silt: '))
    clay = int(input('Clay: '))

  except:
    print('\n\nWhoops! An error occured!\nIf you entered a decimal, try using a whole number instead.\n\n')
    
    # Reset to 0 for each variable, just for good measure
    sand = 0
    silt = 0
    clay = 0

    crashed = True

  # Only return a result if there wasn't a crash
  if crashed == False:
    result = calculate(sand, silt, clay)
    round_result = [round(result[0]), round(result[1]), round(result[2])]


    print('\nHere are the results:')

    print('Sand: ' + str(result[0]) + '%')
    print('Silt: ' + str(result[1]) + '%')
    print('Clay: ' + str(result[2]) + '%')

    print('\n')


# The mainloop code
while True:
  os.system('clear')
  run_test()
  input('Press Enter to run test again.')
