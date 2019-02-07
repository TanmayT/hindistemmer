# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a developing script file.
"""

# dictionary = { 'अपनाना' : 'अपना', 'खेलना': 'खेल', 'खाना': 'खाना','सोना':'सो','सिल्ना':'सिल' ,'कुद्ना':'कुद ' ,'रखना': 'रख' ,'करना': 'कर', 'हसना': 'हस', 'समझना': 'समझ', 'बोलना': 'बोल', 'सुनना': 'सुन', 'देखना': 'देख', 'चाहना': 'चाह', 'मरना': 'मर', 'मारना' :'मार', 'देना': 'दे', 'लिखना': 'लिख', 'बनाना': 'बन', 'पढ़ना': 'पढ़', 'भूलना' :'भूल', 'खोलना': 'खोल', 'पटकना' :'पटक '} # Add the rest of your words and stems
#stems = ['अपना', 'खेल', 'खाना','सो','सिल' ,'कुद ' , 'रख' , 'कर',  'हस',  'समझ',  'बोल',  'सुन',  'देख',  'चाह',  'मर', 'मार',  'दे',  'लिख',  'बन',  'पढ़', 'भूल', 'खोल', 'पटक','ओढ','बिछ','खोल','जल','डर','रह']
sentence = input()
flag=0
file=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/stems.txt","r")
lines=file.read().splitlines()
for word in sentence.split():
    #file=open("/home/tanmay/Desktop/stems.txt","r")
    for stem in lines:
        if word.startswith(stem):
            print(stem)
            flag=flag+1
            break
    if(flag==0):
        print(word)
    flag=0
file.close()    