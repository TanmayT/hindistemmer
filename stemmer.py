# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a developing script file.
"""
sentence = input()
flag1=0
flag2=0
file2=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/ignorewrd.txt","r")
conso=file2.read().splitlines() #list of inflections below
lists=["ियों","ियां","ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां","ाएगी","ाएगा","ाओगी","ीय","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","यों","याँ","ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं","कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","से","ीं","ती","ता","ाँ","ां","ों","ें","ो","े","ू","ु","ी","ि","ा","एँ"]
for word in sentence.split():
     
    for ign in conso: #search for stopwords
        if ign == word:
            print(word)
            flag1=flag1+1
            break
    if flag1!=0:
        flag1=0
        continue
    for end in lists:
        if (word.endswith(end) and len(word)>len(end)+1):
            if(end=="ियों" or end=="ियां" ):
                word=word[:-len(end)]
                print(word+"ी")
                flag2=flag2+1
                break
            if(end=="यों" or end=="याँ"):
                word=word[:-len(end)-1]
                print(word+"ी")
                flag2=flag2+1
                break
            print(word[:-len(end)])
            flag2=flag2+1
            break
            
    if (flag2==0):
        print(word)
    flag2=0
