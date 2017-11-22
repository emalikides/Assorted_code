#!/bin/python

import sys

OPPOSITE  = {"{" : "}","}":"{",
            "[" : "]","]":"[",
            "(" : ")",")":"("}

LEFT      = {"{" : "}",
             "[" : "]",
             "(" : ")"}

RIGHT     = {"}":"{",
             "]":"[",
             ")":"("}

def isBalanced(s):
    # Complete this function
    # Only works for symmetric case.
    chlst = list(s)
    stack = []
    while chlst:
#        print(stack)
        brkt = chlst.pop()
        if brkt in RIGHT.keys():
            stack.append(brkt)
        else :
            if stack:
                last = stack.pop()
                if brkt != RIGHT[last]:
                    return "NO"
            else:
                return "NO"
    if stack: 
        return "NO"
    else :
        return "YES"
              
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        result = isBalanced(s)
        print result

