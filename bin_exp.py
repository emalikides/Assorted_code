# algorithm for binary exponents.
from collections import namedtuple
pair = namedtuple("pair", "base exponent")

TEST = [pair(4,5), pair(20,3), pair(3,19), pair(3,8)]
TESTADD = [('01','10'),
           ('010','10'),
           ('01010101','111111'),
           ('01010101','111111'),
           ('01010101','111101010101'),
           ('01010101','1110101111'),
           ('0101','1110101111'),
           ('01010101','11')
           ]

def bmult(n1_str, n2_str):
    LN1 = list(n1_str)
    ans = ""
    while LN1:
        n = LN1.pop()
        if int(n):
            ans = badd(ans, n2_str)
        n2_str += '0'
    return(ans)

ADD = {'000':('0','0'), 
       '010':('1','0'),
       '100':('1','0'),
       '110':('0','1'),
       '001':('1','0'), 
       '011':('0','1'),
       '101':('0','1'),
       '111':('1','1')}

def badd(n1_str,n2_str):
    LN2 = list(n2_str)
    LN1 = list(n1_str)
    ans = []
    carry = '0'
    while LN2 and LN1:
        idx = LN1.pop() + LN2.pop() + carry
        (result, carry) = ADD[idx]
        ans.append(result)
    if LN2:
        while LN2:
            idx = "0"+ LN2.pop() + carry
            (result, carry) = ADD[idx]
            ans.append(result)
    if LN1:
        while LN1:
            idx = "0"+ LN1.pop() + carry
            (result, carry) = ADD[idx]
            ans.append(result)
    ans.append(carry)
    anstr = ""
    while ans:
        anstr += ans.pop()
    return(anstr)

def powerpower(b_str, e_str):
    """takes a pair of numbers and multiplies them using an advanced algorithm"""
    
    # for each bit in the exponent put a bunch of copies of the 
    # base in a list
    # loop through the list and run a normal multiplication
    # Reallly innefficient...

    # find multiples of 2 which add to give the exponent (already done for binary.)

    # for each bit of the exponent, multiply the number by itself, and if the bit
    # is one, add it to the list.
    # now multiply all the elements of the list.

    # call mult (N_exp**2) => worst case  = number of bits in exponent * number of bits in exponent.
    EL = list(e_str)
    tmp = b_str
    ans = "1"
    while EL:
        n = EL.pop()
        if int(n):
            ans = bmult(ans,tmp)
        tmp = bmult(tmp, tmp)
    return ans

print('testing addition!!')
for p in TESTADD:
    rans = int(badd(p[0],p[1]),2)
    ans  = int(p[0],2) + int(p[1],2)
    print(rans==ans,"correct",ans,"returned",rans)

print('testing multiplication!!')
for p in TESTADD:
    rans = int(bmult(p[0],p[1]),2)
    ans  = int(p[0],2) * int(p[1],2)
    print(rans==ans, "correct", ans, "returned", rans)

print('testing exponent!!')
for p in TEST:
    rans = int(powerpower(bin(p.base)[2:], bin(p.exponent)[2:]),2)
    ans  = p.base**p.exponent
    print(rans==ans, "correct", ans, "returned", rans)