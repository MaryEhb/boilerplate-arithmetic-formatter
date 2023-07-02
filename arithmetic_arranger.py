def arithmetic_arranger(problems, calc_res = False):

  # the max number of problems can be inputed is 5
  if len(problems) > 5:
    return 'Error: Too many problems.'
    
  # lists will store each problem details for each line be printed
  ## Where the 1st line will be the 1st number in each problem
  line1 = list()
  ## 2nd line for the symbol and 2nd number for each problem
  line2 = list()
  ## 3rd line for dashes that will be calculated will adding text
  ## 4th line for result which will be output if calc_res is True
  results = list()

  problength = list()
  # Looping through the main list given (for each problem)
  for problem in problems:

    # Check arithmetic symbol
    if '-' in problem:
      symbol = '-'
      nums = problem.split('-')
    elif '+' in problem:
      symbol = '+'
      nums = problem.split('+')
    else:
      return 'Error: Operator must be \'+\' or \'-\'.'

    # Remove white spaces
    nums[0] = nums[0].strip()
    nums[1] = nums[1].strip()

    # max number of digits in each number is 4
    if len(nums[0]) > 4 or len(nums[1]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    # Calc the result of the problem 
    # and check if the numbers consist of digits only
    try:
      if symbol == '-':
        results.append( int(nums[0]) - int(nums[1]) )
      else:
        results.append( int(nums[0]) + int(nums[1]) )

    except:
      return 'Error: Numbers must only contain digits.'
      
    # Clac number of spaces printed before the number
    spacelen = len(nums[0]) - len(nums[1])
    
    spaces = ''
    for i in range(0,abs(spacelen)):
      spaces = spaces + ' '
    
    # prepare the numbers to be added to the lines list
    if spacelen < 0:
      nums[0] = '  ' + spaces + nums[0]
      nums[1] = symbol + ' ' + nums[1]
    else:
      nums[0] = '  ' + nums[0]
      nums[1] = symbol + ' ' + spaces + nums[1]

    # Add prepared nums to their lines
    line1.append(nums[0])
    line2.append(nums[1])
    problength.append(len(nums[0]))
  # here we will start making the text that will be output of the function 
  # Note that: problems are separeted by 4 spaces
  arranged_problems = ''

  #line 1
  for i in line1:
    arranged_problems = arranged_problems + i 
    if i is not line1[-1]:
      arranged_problems += '    ' 
  arranged_problems += '\n'

  #line 2
  for i in line2:
    arranged_problems = arranged_problems + i 
    if i is not line2[-1]:
      arranged_problems += '    '    
  arranged_problems += '\n'

  #line 3
  for i in line1:
    dashes = ''
    for c in i:
      dashes += '-'
    arranged_problems += dashes
    if i is not line1[-1]:
      arranged_problems += '    '

  #line 4 if calc_res bool is True
  if calc_res == True:
    arranged_problems += '\n'
    
    for i in range(0, len(results)):

      spacelen = problength[i] - len(str(results[i])) 
      spaces = ''
      for s in range(0,abs(spacelen)):
        spaces = spaces + ' '
      
      arranged_problems += spaces + str(results[i])
      
      if results[i] is not results[-1]:
        arranged_problems += '    '
      
  return arranged_problems
