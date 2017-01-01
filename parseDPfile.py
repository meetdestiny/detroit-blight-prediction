
f = open('d:/dataviz/detroit-demolition-permits.tsv', 'r+')
g = open('d:/dataviz/detroit-demolition-permits2.csv', 'w+')

# header to be copied as it is. 

g.write(f.readline() )
x =0 
a = ""
'''
Tried many tricks including attempting to count number of fields but as comma count per row is not fixed ,
stiching multiple rows could not be deterministically attempted for all rows. 
The aproach which worked was to look for BLD201 as starting marking for new record. If line does not start with this, it means that
the line is continuation of previous line. 
'''
while True :   
    if a == "":
        a = f.readline();
    if not a:
        break
    if a.startswith("BLD201"):
        while True:
            b =f.readline()
            if not b:
                g.write( a + "\n")
                a =""
                break;
            if b.startswith("BLD201") :
                g.write( a + "\n" )
                a = b.replace("\n", "")
                break
            else: 
                a = a.replace("\n", "") + b.replace("\n","")
    x +=1 
