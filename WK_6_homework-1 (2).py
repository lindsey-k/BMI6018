# -*- coding: utf-8 -*-

# 1.a  Using print() only:

def wrong_add_function(arg1, arg2):
    a = arg1[:] 
    i = 0
    while i < len(a):
        print(f"At index {i}, we are adding {a[i]} with all of {arg2}.")

        print(f"The correct answer should be: {[x + y for x, y in zip(arg1, arg2)]}")
        
        buggy_list = [a[i] + j for j in arg2]
        a[i] = sum(buggy_list)
        i += 1
    return a

#1.a test
print(wrong_add_function([1, 2, 3], [1, 1, 1]))


#1.b

def correct_add_function(arg1, arg2):
    return [x + y for x, y in zip(arg1, arg2)]

#1.b test
print(correct_add_function([1, 2, 3], [1, 1, 1]))  


#2.a


def wrong_add_function(arg1, arg2):
    #numeric
    if all(isinstance(x, int) for x in arg1) and all(isinstance(y, int) for y in arg2):
        return [x + y for x, y in zip(arg1, arg2)]

    #string
    if all(isinstance(x, str) for x in arg1) and all(isinstance(y, str) for y in arg2):
        result = []
        for a in arg1:
            result.append(a + "".join(arg2))
        return result

    #numeric nor strings
    return arg1

#2.a test
print(wrong_add_function([1,2,3],[1,1,1]))        
print(wrong_add_function(['1','2','3'],['1','1','1'])) 



#2.b

def exception_add_function(arg1, arg2):
    try:
        #arg1 
        for i, v in enumerate(arg1):
            if not isinstance(v, type(arg1[0])):
                return (
                    f"Your input argument 1 at element {i} is not of the expected type. "
                    f"Please change this and rerun."
                )
        #arg2
        for i, v in enumerate(arg2):
            if not isinstance(v, type(arg2[0])):
                return (
                    f"Your input argument 2 at element {i} is not of the expected type. "
                    f"Please change this and rerun."
                )
    
        return wrong_add_function(arg1, arg2)
    except Exception as e:
        return f"Unexpected error: {e}"

#2.b test
print(exception_add_function(["5","2",5], [1,1,1]))



#2.c  

def correction_add_function(arg1, arg2):
    try:
        #numeric
        if all(isinstance(x, int) for x in arg1) and all(isinstance(y, int) for y in arg2):
            return wrong_add_function(arg1, arg2)

        #string
        if all(isinstance(x, str) for x in arg1) and all(isinstance(y, str) for y in arg2):
            return wrong_add_function(arg1, arg2)

        #etc
        arg1_str = [str(x) for x in arg1]
        arg2_str = [str(y) for y in arg2]
        return wrong_add_function(arg1_str, arg2_str)
    except Exception as e:
        return f"Unexpected error: {e}"

#2.c test
print(correction_add_function(['1','2','3'], ['1','1', 1]))  
