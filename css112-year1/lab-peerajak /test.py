def parentheses(n,start,close,string):
    if( n == close):
        print (string)
        return
    
    else:
        if (start > close):
            parentheses(n,start,close+1,string+(")"))
        if (start < n):
            parentheses(n,start+1,close,string+("("))

parentheses(3,0,0,'')