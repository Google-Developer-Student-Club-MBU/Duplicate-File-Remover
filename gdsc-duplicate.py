import os
#FUNCTION TO DETECT A DUPLICATE FILE IN SPECIFIED PATH.
def finder(path):
    x=os.listdir()
    y=[]
    z=[]
    for i in x:
        if i not in y:
            y.append(i)
        else:
            z.append(i)
    if (len(z)==0):
        print("NO DUPLICATES FOUND.")  
        exit()          
    for i in range(len(z)):
        print(f"{i+1}.{z[i]}")
    sel=list(map(int,input("ENTER THE NUMBER OF FILE WANT TO BE DELETED.").split(",")))  
    for i in sel:
        x.remove(z[i-1])
    print(x,y,z) 
#FUNCTION FOR CHANGING THE CURRENT DIRECTORY.     
def change_dir(cwd):
    cwd=list(map(str,input("PASTE YOUR NEW WORKING DIRECTORY NEED TO BE SCANNED.SEPERATED BY COMMA.").split(",")))
    return cwd
cwd=os.getcwd()
#TURNING THE LOOP ON
st=True
while st==True:   
    #ASKING FOR USER INPUT
    opt=input(f"YOUR PRESENT WORKING DIRECTORY IS {cwd}\nTYPE Y/N TO CONTINUE OR C TO CHANGE THE WORKING DIRECTORY.")
    if(opt=="Y" or opt=="y"):
        for i in cwd:
            finder(i)
    
    elif(opt=="C" or opt=="c"):
        cwd=change_dir(cwd)    
    #BREAKING THE LOOP.
    else:
        st=False
#PRINTING THE EXIT MESSAGE.
print(" YOU ARE OUT OF THE PROGRAM")        
