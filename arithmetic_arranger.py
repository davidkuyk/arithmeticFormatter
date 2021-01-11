import re

def arithmetic_arranger(problems, showAns=False):
  # test for errors
  if len(problems) > 5:
      return 'Error: Too many problems.'
  
  for problem in problems:
    if "*" in problem or "/" in problem:
        return "Error: Operator must be '+' or '-'."
    letterRegex = re.compile(r'[A-Za-z]')
    if letterRegex.search(problem) != None:
        return "Error: Numbers must only contain digits."
  
  # iterate through problems
  arranger = []
  arranged_problems = ''
  problemRegex = re.compile(r'(\d+)\s+(\+|\-)\s+(\d+)') 
  # get the first operand, the operator, the second operand, and the answer
  for problem in problems:
    arrangerSub = []
    mo = problemRegex.search(problem)
    if len(mo.group(1)) > 4 or len(mo.group(3)) > 4:
        return "Error: Numbers cannot be more than four digits."
    arrangerSub.append(mo.group(1))
    arrangerSub.append(mo.group(2))
    arrangerSub.append(mo.group(3))
    if mo.group(2) == "+":
        arrangerSub.append(str(int(mo.group(1)) + int(mo.group(3))))
    else:
        arrangerSub.append(str(int(mo.group(1)) - int(mo.group(3))))
    arranger.append(arrangerSub)
  # get the longest operand in each problem
  # get the dash length for each problem
  longestOpLen = []
  shortestOpLen = []
  dashLen = []
  for i in range(len(arranger)):
      if len(arranger[i][0]) > len(arranger[i][2]):
          longestOpLen.append(len(arranger[i][0]))
          shortestOpLen.append(len(arranger[i][2]))
      else:
          longestOpLen.append(len(arranger[i][2]))
          shortestOpLen.append(len(arranger[i][0]))
      
      dashLen.append(2 + longestOpLen[i])
  # arranged problems is going to be:
    # (spaces that are 4 - length first 1st operand) + first 1st operand + 4 spaces
    # spaces that are dashLen - longestOpLen
    # + (spaces that are 4 - length second 1st operand) + second 1st operand + 4 spaces
    # + (spaces that are 4 - length third 1st operand) + third 1st operand + 4 spaces
    # + (spaces that are 4 - length 4th 1st operand) + 4th 1st operand + NO spaces
    # + \n
  count = 0
  for i in range(len(arranger)):
      count += 1
      if count == 1:
        arranged_problems += (dashLen[i] -len(arranger[i][0]))*' ' + arranger[i][0] + (4*' ')
      elif count == len(arranger):
          if len(arranger[i][0]) > len(arranger[i][2]):
              arranged_problems += (dashLen[i]-longestOpLen[i])*' ' + arranger[i][0] + '\n'
          else:
              arranged_problems += (dashLen[i]-shortestOpLen[i])*' ' + arranger[i][0] + '\n'
      else:
          if len(arranger[i][0]) > len(arranger[i][2]):
              arranged_problems += (dashLen[i]-longestOpLen[i])*' ' + arranger[i][0] + (4*' ')
          else: 
              arranged_problems += (dashLen[i]-shortestOpLen[i])*' ' + arranger[i][0] + (4*' ')

    # operator + (spaces that are 3 - length of first 2nd operand) + 4 spaces
    # + operator + (spaces that are 3 - length of first 2nd operand) + 4 spaces
    # + operator + (spaces that are 3 - length of first 2nd operand) + 4 spaces
    # + operator + (spaces that are 3 - length of first 2nd operand) + 4 spaces
    # + \n
  count = 0
  for i in range(len(arranger)):
      count += 1
      if count == len(arranger):
          arranged_problems += arranger[i][1] + (((1+longestOpLen[i])-len(arranger[i][2]))*' ') + arranger[i][2]
          arranged_problems += '\n'

      else:
        arranged_problems += arranger[i][1] + (((1+longestOpLen[i])-len(arranger[i][2]))*' ') + arranger[i][2] + (4*' ')
  
  count = 0
  for i in range(len(arranger)):
      count += 1
      if count == len(arranger):
        arranged_problems += ((dashLen[i])*"-")
      else:
        arranged_problems += ((dashLen[i])*"-") + (4*' ')

    # (dashes that are 2 + length of longest of first 1st operand and first 2nd operand) + 4 spaces
    # + (dashes that are 2 + length of longest of first 1st operand and first 2nd operand) + 4 spaces
    # + (dashes that are 2 + length of longest of first 1st operand and first 2nd operand) + 4 spaces
    # + (dashes that are 2 + length of longest of first 1st operand and first 2nd operand) + NO spaces

     # + \n

    # (spaces equal to 5 - length of first answer) + first answer + 4 spaces
    # + (spaces equal to 5 - length of first answer) + second answer + 4 spaces
    # + (spaces equal to 5 - length of first answer) + third answer + 4 spaces
    # + (spaces equal to 5 - length of first answer) + fourth answer
  if showAns == True:
      count = 0
      for i in range(len(arranger)):
        count += 1
        if count == 1:
            arranged_problems += '\n' + (dashLen[i] - longestOpLen[i])*' ' + arranger[i][3] + (4*' ')
        elif count == len(arranger):
            if len(arranger[i][0]) > len(arranger[i][2]):
                arranged_problems += (dashLen[i] - longestOpLen[i])*' ' + arranger[i][3]
            else:
                arranged_problems += (dashLen[i] - shortestOpLen[i])*' ' + arranger[i][3]
        else:
            if len(arranger[i][0]) > len(arranger[i][2]):
                arranged_problems += (dashLen[i] - longestOpLen[i])*' ' + arranger[i][3] + (4*' ')
            else: 
                arranged_problems += (dashLen[i] - shortestOpLen[i])*' ' + arranger[i][3] + (4*' ')
  
  return arranged_problems


print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))