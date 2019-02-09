# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a developing script file.
"""

# dictionary = { 'अपनाना' : 'अपना', 'खेलना': 'खेल', 'खाना': 'खाना','सोना':'सो','सिल्ना':'सिल' ,'कुद्ना':'कुद ' ,'रखना': 'रख' ,'करना': 'कर', 'हसना': 'हस', 'समझना': 'समझ', 'बोलना': 'बोल', 'सुनना': 'सुन', 'देखना': 'देख', 'चाहना': 'चाह', 'मरना': 'मर', 'मारना' :'मार', 'देना': 'दे', 'लिखना': 'लिख', 'बनाना': 'बन', 'पढ़ना': 'पढ़', 'भूलना' :'भूल', 'खोलना': 'खोल', 'पटकना' :'पटक '} # Add the rest of your words and stems
#stems = ['अपना', 'खेल', 'खाना','सो','सिल' ,'कुद ' , 'रख' , 'कर',  'हस',  'समझ',  'बोल',  'सुन',  'देख',  'चाह',  'मर', 'मार',  'दे',  'लिख',  'बन',  'पढ़', 'भूल', 'खोल', 'पटक','ओढ','बिछ','खोल','जल','डर','रह']
sentence = input()
flag=0
counter=0
#file=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/stems.txt","r")
#lines=file.read().splitlines()
file=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/ignorewrd.txt","r")
lines=file.read().splitlines()
lists=["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां","ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां","ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं""कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें","ो","े","ू","ु","ी","ि","ा"]
for word in sentence.split():
    for ignore in lines:
        if(word == ignore):
            print(word)
            counter=counter+1
            break
    #file=open("/home/tanmay/Desktop/stems.txt","r")
    if(counter!=0):
        counter=0
        continue
    for end in lists:
        if word.endswith(end):
            print(word.strip(end))
            flag=flag+1
            break
    if(flag==0):
        print(word)
    flag=0
#file.close()    
