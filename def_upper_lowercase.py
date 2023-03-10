# python function that accepts string and culculate no.of upper and lower letter
def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for c in s:
        if c.isupper():
            d["upper_case"]+=1
        elif c.islower():
            d["lower_case"]+=1
        else:
            pass

    print("original string: ", string_test)
    print("no. of upper case characters :", d["upper_case"])
    print("no. of lower case characters :", d["lower_case"])

string_test("The quick Brown Fox")
    
  
  
 
