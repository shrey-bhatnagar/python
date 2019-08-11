#!/usr/bin/env python

def main():
    f= open("myfile.txt","w+")
    #f=open("guru99.txt","a+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()   
    #Open the file back and read the contents
    f=open("myfile.txt", "r")
    #if f.mode == 'r': 
    #    contents =f.read()
    #	print contents
    #or, readlines reads the individual line into a list
    fl =f.readlines()
    for x in fl:
        print x

def newmain():
    with open("newmyfile.txt","w+") as f:
        for i in range(10):
            f.write("this is line %d\r\n"%(i+1))
        f.close()
    with open("newmyfile.txt","r") as f:
        fl =f.readlines()
        for x in fl:
            print x
    
if __name__== "__main__":
  newmain()
  main()
