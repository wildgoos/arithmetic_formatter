import re


"""arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

      32         1      9999      523
    +  8    - 3801    + 9999    -  49
    ----    ------    ------    -----
      40     -3800     19998      474 """
    
    


def arithmetic_arranger(problems, result= False):
   
    
    #Search for * or / 
    for i in range(len(problems)):
        oper = problems[i]
        if ('*' in oper or '/' in oper):
          break
   
    
        
    #Couting digits
    val_dig = 0
    for i in range(len(problems)):
        leng = problems[i]
        num_list = re.split("\s", leng)
        if (len(num_list[0]) > 4 or len(num_list[2]) > 4):
            val_dig = 5
            break
   
    #is a digit?
    is_digit = True
    for i in range(len(problems)):
        just_digits = problems[i]
        digits_list = re.split("\s", just_digits)
        if (digits_list[0].isdigit() == False):
            is_digit = False
            break
        elif (digits_list[2].isdigit() == False):
            is_digit = False
            break
         
    def formater(_problems):
        li1 = str()
        li2 = str()
        li3 = str()
        li4 = str()
        li5 = str()
        fi_l = list()
        for i in range(len(_problems)):
            digs = _problems[i]
            digs_list = re.split("\s", digs)
            
            fi_l.append(digs_list)
        for i in range(len(fi_l)):
            if len(fi_l[i][0]) > len(fi_l[i][2]):
                large = len(fi_l[i][0])
            else:
                large = len(fi_l[i][2])
            dash = large + 2          
            li1 = li1 + str(fi_l[i][0]).rjust(dash) + '    '
            li2 = li2 + str(fi_l[i][1]) + ' ' + str(fi_l[i][2]).rjust(large) + '    '
            li3 = li3 + ('-' * dash) + '    '
            li4 = li4 + ''
        sol = li1+ '\n' + li2+'\n' + li3 + li4
        return(sol)
        
                       
        
      
    #Selector
    if (len(problems) > 5):
        arranged_problems = "Error: Too many problems."
    elif ('*' in oper or '/' in oper):
        arranged_problems = "Error: Operator must be '+' or '-'." 
    elif (val_dig > 4):
        arranged_problems = "Error: Numbers cannot be more than four digits."       
      
    elif (is_digit == False):
        arranged_problems = "Error: Numbers must only contain digits." 
    
    else:
        arranged_problems = formater(problems)    

   
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "380 - 2", "45 + 43", "123 + 49","123 - 49"]))    
