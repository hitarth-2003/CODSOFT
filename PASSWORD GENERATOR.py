import random as rnd
import string as str
length=int(input("Enter the length of string here:"))

lower=str.ascii_lowercase
upper=str.ascii_uppercase
num=str.digits
symbol=str.punctuation

all=lower+upper+num+symbol
com=rnd.sample(all,length)
password="".join(com)
print(password)