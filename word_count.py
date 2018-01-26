

import sys
import math

fl=input("enter file :")

dict={} #dictionary to store frequencies...!!!

with open(fl,'r') as f:
    for line in f:
        str=line
        for i in range(0,len(str)-1 ):
            if str[i+1]=="," or str[i+1]=="." or str[i+1]=="\"" or str[i+1]=="-" or str[i+1]=="!" : #to check special characters...!!!
                str=str[:i+1]+" , "+str[i+2:]
               
        for word in str.split():
            if word in dict.keys():
                dict[word]+=1
            else:
                dict[word]=1


print dict


