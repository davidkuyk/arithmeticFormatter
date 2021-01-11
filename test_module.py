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
  answerLen = []
  dashLen = []
  for i in range(len(arranger)):
      if len(arranger[i][0]) > len(arranger[i][2]):
          longestOpLen.append(len(arranger[i][0]))
          shortestOpLen.append(len(arranger[i][2]))
      else:
          longestOpLen.append(len(arranger[i][2]))
          shortestOpLen.append(len(arranger[i][0]))
      answerLen.append(len(arranger[i][3]))
      dashLen.append(2 + longestOpLen[i])

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

  if showAns == True:
      count = 0
      for i in range(len(arranger)):
        count += 1
        if count == 1:
            arranged_problems += '\n' + (dashLen[i] - answerLen[i])*' ' + arranger[i][3] + (4*' ')
        elif count == len(arranger):
            arranged_problems += (dashLen[i] - answerLen[i])*' ' + arranger[i][3]
        else:
            arranged_problems += (dashLen[i] - answerLen[i])*' ' + arranger[i][3] + (4*' ')
  
  return arranged_problems