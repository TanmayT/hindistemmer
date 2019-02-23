# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a developing script file.
"""

# dictionary = { 'अपनाना' : 'अपना', 'खेलना': 'खेल', 'खाना': 'खाना','सोना':'सो','सिल्ना':'सिल' ,'कुद्ना':'कुद ' ,'रखना': 'रख' ,'करना': 'कर', 'हसना': 'हस', 'समझना': 'समझ', 'बोलना': 'बोल', 'सुनना': 'सुन', 'देखना': 'देख', 'चाहना': 'चाह', 'मरना': 'मर', 'मारना' :'मार', 'देना': 'दे', 'लिखना': 'लिख', 'बनाना': 'बन', 'पढ़ना': 'पढ़', 'भूलना' :'भूल', 'खोलना': 'खोल', 'पटकना' :'पटक '} # Add the rest of your words and stems
#stems = ['अपना', 'खेल', 'खाना','सो','सिल' ,'कुद ' , 'रख' , 'कर',  'हस',  'समझ',  'बोल',  'सुन',  'देख',  'चाह',  'मर', 'मार',  'दे',  'लिख',  'बन',  'पढ़', 'भूल', 'खोल', 'पटक','ओढ','बिछ','खोल','जल','डर','रह']
sentence = input()
flag1=0
flag2=0
#file=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/stems.txt","r")
#lines=file.read().splitlines()
#file1=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/ignorewrd.txt","r")
#lines=file1.read().splitlines()
file2=open("/home/tanmay/Desktop/Projects/Hindi_Stemmer/ignorewrd.txt","r")
conso=file2.read().splitlines()
#lists=["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां","ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","यों","याँ","ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं","कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें","ो","े","ू","ु","ी","ि","ा","एँ"]
l1=[' ि◌यों' ,' ि◌यां', 'ि◌अ◌ो◌ं','यां' ,'यों']
l2=['अ◌ो◌ं' ,'◌ौ◌ं','ए◌']
l3=['◌ो◌ं',"े",'◌ो']
l4=['◌ं','◌ी','एँ','एं ','◌ा']
l5=['ए']
l6=['ई' ,'ना' , 'ता' , 'ती' , 'जन' , 'गण' , 'तया' , 'वर्ग' , 'कार' , 'त्व', '◌े◌ं' , '◌ीय']
l7=['◌़ि◌याँ']
for word in sentence.split():
    #for ignore in lines:
        #if(word == ignore):
            #print(word)
            #counter=counter+1
            #break
    #file=open("/home/tanmay/Desktop/stems.txt","r") 
    for ign in conso:
        if ign == word:
            print(word)
            flag1=flag1+1
            break
    if flag1!=0:
        flag1=0
        continue
    for end in l1:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)-1]
            print(word+'ी')
            flag2=flag2+1
            break
    if(flag2!=0):
        break
    for end in l2:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)]
            print(word)
            flag2=flag2+1
            break
    if(flag2!=0):
        continue    
    for end in l3:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)]
            print(word+'◌ा')
            flag2=flag2+1
            break
    if(flag2!=0):
        continue    
    for end in l4:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)]
            print(word)
            flag2=flag2+1
            break
    if(flag2!=0):
        continue    
    for end in l5:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)]
            print(word+'आ')
            flag2=flag2+1
            break
    if(flag2!=0):
        continue    
    for end in l6:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)]
            print(word)
            flag2=flag2+1
            break
    if(flag2!=0):
        continue    
    for end in l7:
        if (word.endswith(end) and len(word)>len(end)+1):
            word=word[:-len(end)]
            print(word+'या')
            flag2=flag2+1
            break    
    if (flag2==0):
        print(word)
    flag2=0
