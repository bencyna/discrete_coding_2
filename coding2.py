# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 2
#
# Before submitting the file to gradescope make sure of the following:
# 1. The name of the file is coding2.py 
# 2. Nothing below the line `if __name__="__main__":` is changed 
# 3. Make sure there are no indentation errors and that the code compiles on your
#    end
#
# YOUR NAME:
# YOUR UNI:

import itertools

'''
Returns the proposition, formatted in string form.

Parameters:
prop (list): proposition in nested list form

Returns:
string: 'prop' in string form
'''
def format_prop(prop):
    # BASE CASE: #####################################
    if len(prop) == 1:
        return prop[0]
    
    # UNARY OPERATOR (not): ##########################
    if 2 == len(prop):
        # the following two variable declarations are missing LHS #
        op = prop[0] # missing LHS
        proposition = prop[1] # missing LHS

        if "not" == op:
            formatted_prop = f"not {proposition[0]}" # fill in here #
            return formatted_prop
        else:
            raise ValueError("Unary proposition is not not.")
    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif 3 == len(prop):
        # the following three variable declarations are missing LHS #
        op = prop[0] # missing LHS
        left_prop = prop[1] # missing LHS
        right_prop = prop[2] # missing LHS

        if op not in ("if", "iff", "or", "and", "xor"):
            raise ValueError("Binary proposition does not have valid connectives.")

        # change "if" and "iff" representation
        if "if" == op:
            op = "->"
        elif "iff" == op:
            op = "<->"

        # format left and right sides of a binary operation
        left_prop = format_prop(left_prop)
        right_prop = format_prop(right_prop)

        formatted_prop = f"({left_prop}) {op} ({right_prop})"
        return formatted_prop
    ####################################################

    # INVALID LENGTH ####################################
    else:
        raise ValueError("Proposition incorrect length.")
    #####################################################

'''
Returns the evaluation (True or False) as an int (1 or 0) of the proposition,
given a proposition in list form and a list of values for each atomic variable.

Parameters:
prop (list): proposition in nested list form.
values (list): list of integers, either 0 or 1 indicating False or True for
each atomic variable in the proposition. 

Returns:
int: 0 for False, 1 for True
'''
def eval_prop(prop, values):
    # BASE CASE: #####################################
    if len(prop) == 1:
        atomic_prop_id = int(prop[0][1])-1
        return values[atomic_prop_id]
        ##################################################

    # UNARY OPERATOR (not): ##########################
    elif 2 == len(prop):
        # the following two variable declarations are missing LHS #
        op = prop[0] # missing LHS
        prop_num = prop[1][0] # missing LHS
        
        for i in range(0, 10):
            if prop_num == f"p{i+1}":
                value = values[i]
                break
                
        if "not" == op:
            return int(not value) 
        else:
            raise ValueError("Unary proposition is not not.")
    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif 3 == len(prop):
        # the following three variable declarations are missing LHS #
        op = prop[0] # missing LHS
        left = prop[1] # missing LHS
        right = prop[2] # missing LHS

        if op not in ("if", "iff", "or", "and", "xor"):
            raise ValueError("Binary proposition does not have valid connectives.")

        # evaluate left and right sides of a binary operation
        left = eval_prop(left, values)
        right = eval_prop(right, values)

        # the line here is an example. fill in the rest.
        if "and" == op:
            return int(left and right)
        elif "or" == op:
            return int(left or right)
        elif "xor" == op:
            return 0 if ((left and right) or (not left and not right)) else 1  
        elif "if" == op:
            return 1 if (not left or (left and right)) else 0
        else:
            return int(left == right)

    # INVALID LENGTH ####################################
    else:
        raise ValueError("Proposition incorrect length.")
    #####################################################

if __name__ == '__main__':
    print("---------------------------------------")
    print("Coding Assignment 2: Propositional Logic")
    print("---------------------------------------")

    print()
    values = [1]
    prop = ["not", ["p1"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 1]
    prop = ["and", ["p1"], ["p2"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 0]
    prop = ["iff", ["p1"],["p2"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 1, 0]
    prop = ["if", ["and", ["p1"], ["not", ["p2"]]], ["p3"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    prop_str = format_prop(prop)
    print("Evaluating proposition p =", prop_str)
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 0, 1]
    prop = ["iff", ["p1"], ["or", ["p2"], ["not", ["p3"]]]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)
