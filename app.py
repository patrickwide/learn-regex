import re

#you can find wheather a word is used in a senttece or data from the sentense yousing re,search
#example
#if re.search("inform","we need inform  to inform him with the latest information"):
 #   print("there is inform")
#end
#you can know the number of times the word is used in a sentence
allinform = re.findall("inform","we need to inform him with the latest information")

for i in  allinform:
    print(f"we found {i}" )
    print(type(i))

#end
#get index of the string bing find
#to convert we use span() its a functon
sentence = "we need inform  to inform him with the latest information"
for i in re.finditer("inform",sentence):
    index = i.span()
    print("----------------------------------------------------------------------------")

#    print(type(i))
 #   print(i)
#print all word that start with the the letters [shmp] and end with [at]
#str = "sat,mat,pat,hat"
#allstr = re.findall("[shmp]at",str)



#print word that are in the renge a-z ir h-m or a-b and end with at
#for i in allstr:
 #   print(i)
#
str = "mat, pat, sat, hat"
index = re.findall("[^a-z]at",str)

for i in index:
    print(i)





food = "hat rat mat pat"
regex = re.compile("[r]at")

food = regex.sub("food",food)
print(food)

randstr = "here is \\drogba"


print(re.search(r"\\drogba",randstr))

#\s:stands for [\f\n\r\t\v], S is the viseverse
#\n: stands for new line, n is the viseverse
#\f: stands for formfeed, F is the viseverse
#\b: stands for backsoace, B is the viseverse
#\r: stands for carriage return, R is the viseverse
#\t: stands for tab, T is the viseverse
#\v: stands for vertical tab, V is the viseverse
#\w means  ,W is the viseverse
#\d: it highlights the number of digits alone D is the viseverse
#\D: it highlights the number of strings alone
# if you wnat to match a particular digit or string use {the string or digit} after the \d or \d
randstr = "12345 12345 12345 12345 12345 12345 98765 56789"
print("matches:",len(re.findall("\d{5}",randstr)))

#can find matches in the range of 5-7
num = "123 1234 12345 123456 1234567"
print("matches:",len(re.findall("\d{5,7}",num)))

#\w is equal to [a-zA-Z0-9]
#\W is equal [^a-zA-Z0-9] any thing apart from [a-zA-Z0-9]
#:  ^ means not or apart from

phn = "patrick kiarie"
if re.search("\w{2,20}\s\w{2,20}",phn):
    print(phn,"is valid")
else:
    print(phn,"is invalid")


email = "sk@alcom md@.com @seo.com dc@.com  patkia@gmail.com"
print("email Matches:", len(re.findall("[\w._%+-]{2,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))