def arithmetic_arranger(problems,show_answer=False):
    if len(problems)>5:
      return 'Error: Too many problems.'
    length = []
    add1 = []
    add2 = []
    arith = []
    output_list = ['','','','']
    for line in problems:
      line = line.split()
      if max(len(line[0]),len(line[2]))>4:
        return 'Error: Numbers cannot be more than four digits.'
      length.append(max(len(line[0]),len(line[2])))
      add1.append(line[0])
      add2.append(line[2])
      if line[1] != '+' and line[1] != '-':
        return 'Error: Operator must be \'+\' or \'-\'.'
      arith.append(line[1])
    for i in range(len(problems)):
      if i > 0 and i <len(problems):
        for j in range(len(output_list)):
          output_list[j] = output_list[j] + ' '*4
      output_list[0] = output_list[0] + ' '*(2+length[i]-len(add1[i]))+add1[i]
      output_list[1] = output_list[1] + arith[i] + ' '*(1+length[i]-len(add2[i]))+add2[i]
      output_list[2] = output_list[2] + '-'*(2+length[i])
      try:
        int(add1[i])
        int(add2[i])
      except ValueError:
        return 'Error: Numbers must only contain digits.'
      if arith[i] == '+':
          answer = int(add1[i]) + int(add2[i])
      else:
        answer = int(add1[i]) - int(add2[i])
      output_list[3] = output_list[3] + ' '*(2+length[i]-len(str(answer)))+str(answer)
    arranged_problems = ''
    if show_answer:
        k = 3
    else:
        k = 2
    for i in range(k):
      arranged_problems = arranged_problems + output_list[i] + '\n'
    arranged_problems = arranged_problems + output_list[k]
    return arranged_problems