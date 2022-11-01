""" ([utryck],{x: true , y false})
utryck = [u "and" u] , [u "or" u] , [u "and"[not u]] , [not u]
if "AND" in list u1 and u2 need to be true to get true
if "or" in list u1 or u2 only one need to be true to get true
if "not" in list change in {} 
"""

def interpret(exp, table):
    
    if isinstance(exp, str): # kolla om exp är av typen string
        if exp in table.keys(): # ifall stringen i dic returna värdet av keys
            return table[exp]
        return exp

    elif len(exp) == 3:
        if exp[1] == "AND":
            return "true" if interpret(exp[0], table) == "true" and interpret(exp[2], table) == "true" else "false"
        elif exp[1] == "OR":
            return "true" if interpret(exp[0], table) == "true" or interpret(exp[2], table) == "true" else "false"

    elif len(exp) == 2 :
        return "false" if interpret(exp[1], table) == "true" else "true"
