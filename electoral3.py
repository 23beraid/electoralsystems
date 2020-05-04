# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:22:05 2020

@author: 23beraid
"""

import random

totalmalevotes=0
totalfemalevotes=0
totalfemalecandidates=0
totalmalecandidates=0
totalwinvotes=0
totalwastevotes=0

def runElection():
    
        
    
    
    def getIndexPositions(listOfElements, element):
        indexPosList=[]
        indexPos = 0
        while True:
            try:
                indexPos = listOfElements.index(element, indexPos)
                indexPosList.append(indexPos)
                indexPos+=1
            except ValueError as e:
                break
        return indexPosList
            
    def ASRA(genderlist, mainlist, candidateselected):
        print("Hello. I'm ASRA, your automated stalemate resolution associate." )
        maxvalue=max(genderlist)
        listpos=getIndexPositions(genderlist, maxvalue)
        if candidateselected==1:
            if len(listpos)==2:
                biglistpos=getIndexPositions(mainlist, maxvalue)
                #lastlistpos=len(biglistpos)-1
                if max(mainlist)==maxvalue and len(biglistpos)==2:  
                    userresponse='y'
                else:
                    userresponse='n'
            else:
                userresponse='n'
        else:
            userresponse='n'
        
        if userresponse=='y':
            print('The stalemate has been resolved.')
        else:
            print("The stalemate cannot be resolved.")
        return userresponse
        
    def SARA(genderlist):
        print("Hello. I'm SARA, your stalemate automatic resulution authenticator.")
        maxvalue=max(genderlist)
        listpos=getIndexPositions(genderlist, maxvalue)
        if len(listpos)==1:
            userresponse='y'
        else:
            userresponse='n'
        
        if userresponse=='y':
            print("The resolution has been authenticated.")
        else:
            print("The resolution cannot be authenticated.")
        return userresponse
    
    femalevotescast=0
    malevotescast=0
    mcandidateselected=1
    fcandidateselected=1
    
    candidatea=0
    candidateb=0
    candidatec=0
    candidated=0
    candidatee=0
    candidatef=0
    voters=135
    for x in range (0, voters):
        vote=random.randint(1, 6)
        if vote==1:
            candidatea+=1
        if vote==2:
            candidateb+=1
        if vote==3:
            candidatec+=1
        if vote==4:
            candidated+=1
        if vote==5:
            candidatee+=1
        if vote==6:
            candidatef+=1
            
    
    lista=[candidatea, candidateb, candidatec, candidated, candidatee, candidatef]
    print("The Votes are in!")
    print(lista)
    
    def main():
        
        sort(lista)
    
    def sort(my_list):
        size = len(my_list)
        for i in range(size):
            for j in range(size-i-1):
                if(my_list[j] > my_list[j+1]):
                    tmp = my_list[j]
                    my_list[j] = my_list[j+1]
                    my_list[j+1] = tmp
        print("The results have been ordered!")
        print(my_list)
    
    
    winners=[]
    males=[]
    females=[]
    main()
    savethislist=[]
    for x in range(0, len(lista)):
        savethislist.append(lista[x])
    test=False
    while test==False:
        gendera=random.randint(0,1)
        genderb=random.randint(0,1)
        genderc=random.randint(0,1)
        genderd=random.randint(0,1)
        gendere=random.randint(0,1)
        genderf=random.randint(0,1)
        if gendera==genderb==genderc==genderd==gendere==genderf:
            test=False
        else:
            test=True
    genders=[gendera, genderb, genderc, genderd, gendere, genderf]
    print(genders)
    savegenders=[gendera, genderb, genderc, genderd, gendere, genderf]
    if gendera==0:
        females.append(lista[0])
        femalevotescast+=lista[0]
    else:
        males.append(lista[0])
        malevotescast+=lista[0]
    if genderb==0:
        females.append(lista[1])
        femalevotescast+=lista[1]
    else:
        males.append(lista[1])
        malevotescast+=lista[1]
    if genderc==0:
        females.append(lista[2])
        femalevotescast+=lista[2]
    else:
        males.append(lista[2])
        malevotescast+=lista[2]
    if genderd==0:
        females.append(lista[3])
        femalevotescast+=lista[3]
    else:
        males.append(lista[3])
        malevotescast+=lista[3]
    if gendere==0:
        females.append(lista[4])
        femalevotescast+=lista[4]
    else:
        males.append(lista[4])
        malevotescast+=lista[4]
    if genderf==0:
        females.append(lista[5])
        femalevotescast+=lista[5]
    else:
        males.append(lista[5])
        malevotescast+=lista[5]
    print("males:")
    print(males) 
    print("females:")
    print(females)
    
    
    def findtopmale(males):
        if len(males)>1:
            maxvalue=max(males)
            if males.count(maxvalue)==1:
                winners.append(max(males))
                listpos = getIndexPositions(lista, max(males))
                test = False
                m=1
                while test==False:
                    
                    if genders[listpos[len(listpos)-m]]==1:
                        test=True
                        #print(genders)
                        #print(lista)
                        del genders[listpos[len(listpos)-m]]
                        del lista[listpos[len(listpos)-m]]
                        del males[len(males)-1]
                        #print(listpos[len(listpos)-m])
                        
                    else:
                        test=False
                        m+=1
                    
            else:
                test=False
                while test==False:
                    print("Stalemate Detected (Male)")
                    #ans=input("Stalemate Associate, can you resolve the stalemate? (y/n)")
                    ans=ASRA(males, lista, fcandidateselected)
                    if ans=="y":
                        test=True
                    if ans=="n":
                        
                        m=0
                        tester=0
                        while tester==0:
                            if lista[m]==0:
                                m+=1
                            else:
                                tester=1
                        
                        
                        redistribute=lista[m]
                        #lista.remove(lista[0])
                        for x in range(0, redistribute):
                            vote=random.randint(m+1,len(lista)-1)
                            lista[vote]+=1
            
                        males=[]
                        females=[]
                        '''
                        if genderb==0:
                            females.append(lista[1])
                        else:
                            males.append(lista[1])
                        if genderc==0:
                            females.append(lista[2])
                        else:
                            males.append(lista[2])
                        if genderd==0:
                            females.append(lista[3])
                        else:
                            males.append(lista[3])
                        if gendere==0:
                            females.append(lista[4])
                        else:
                            males.append(lista[4])
                        if genderf==0:
                            females.append(lista[5])
                        else:
                            males.append(lista[5])  
                        '''
                        for y in range(m+1, len(genders)):
                            if genders[y]==0:
                                females.append(lista[y])
                            else:
                                males.append(lista[y])
                        
                        print("Votes Updated")
                        lista[0]=0
                        print(lista)
                        print("Males:")
                        print(males)
                        print("Females:")
                        print(females)
                        anf=SARA(males)
                        if anf=="y":
                            test=True
                winners.append(max(males))
                listpos = getIndexPositions(lista, max(males))
                test = False
                m=1
                while test==False:
                    
                    if genders[listpos[len(listpos)-m]]==1:
                        test=True
                        #print(genders)
                        #print(lista)
                        del genders[listpos[len(listpos)-m]]
                        del lista[listpos[len(listpos)-m]]
                        del males[len(males)-1]
                        #print(listpos[len(listpos)-m])
                        
                    else:
                        test=False
                        m+=1
        else:
            winners.append(max(males))
            listpos = getIndexPositions(lista, max(males))
            test = False
            m=1
            while test==False:
                
                if genders[listpos[len(listpos)-m]]==1:
                    test=True
                    #print(genders)
                    #print(lista)
                    del genders[listpos[len(listpos)-m]]
                    del lista[listpos[len(listpos)-m]]
                    del males[len(males)-1]
                    #print(listpos[len(listpos)-m])
                    
                else:
                    test=False
                    m+=1
    
    #print("The Votes are IN")
    #print(lista)
    #print(genders)
    
    
    def findtopfemale(females):
        if len(females)>1:
            maxvalue=max(females)
            if females.count(maxvalue)==1:
                winners.append(max(females))
                listpos = getIndexPositions(lista, max(females))
                test = False
                m=1
                while test==False:
                    #print("m "+ str(m))
                    if genders[listpos[len(listpos)-m]]==0:
                        test=True
                        del genders[listpos[len(listpos)-m]]
                        del lista[listpos[len(listpos)-m]]
                        del females[len(females)-1]
                    else:
                        test=False
                        m+=1
            else:
                test=False
                while test==False:
                    print("Stalemate Detected (Female)")
                    #ans=input("Stalemate Associate, can you resolve the stalemate? (y/n)")
                    ans=ASRA(females, lista, mcandidateselected)
                    if ans=="y":
                        test=True
                    if ans=="n":
                        
                        m=0
                        tester=0
                        while tester==0:
                            if lista[m]==0:
                                m+=1
                            else:
                                tester=1
                        
                        
                        redistribute=lista[m]
                        #lista.remove(lista[0])
                        for x in range(0, redistribute):
                            vote=random.randint(m+1,len(lista)-1)
                            lista[vote]+=1
                        males=[]
                        females=[]
                        '''
                        if genderb==0:
                            females.append(lista[1])
                        else:
                            males.append(lista[1])
                        if genderc==0:
                            females.append(lista[2])
                        else:
                            males.append(lista[2])
                        if genderd==0:
                            females.append(lista[3])
                        else:
                            males.append(lista[3])
                        if gendere==0:
                            females.append(lista[4])
                        else:
                            males.append(lista[4])
                        if genderf==0:
                            females.append(lista[5])
                        else:
                            males.append(lista[5])  
                        '''    
                        for y in range(m+1, len(genders)):
                            if genders[y]==0:
                                females.append(lista[y])
                            else:
                                males.append(lista[y])
                                
                        print("Votes Updated")
                        lista[0]=0
                        print(lista)
                        print("Males")
                        print(males)
                        print("Females")
                        print(females)
                        anf=SARA(females)
                        if anf=="y":
                            test=True
                winners.append(max(females))
                listpos = getIndexPositions(lista, max(females))
                test = False
                m=1
                while test==False:
                    
                    if genders[listpos[len(listpos)-m]]==0:
                        test=True
                        del genders[listpos[len(listpos)-m]]
                        del lista[listpos[len(listpos)-m]]
                        del females[len(females)-1]
                    else:
                        test=False
                        m+=1
        else:
            winners.append(max(females))
            listpos = getIndexPositions(lista, max(females))
            test = False
            m=1
            while test==False:
                
                if genders[listpos[len(listpos)-m]]==0:
                    test=True
                    del genders[listpos[len(listpos)-m]]
                    del lista[listpos[len(listpos)-m]]
                    del females[len(females)-1]
                else:
                    test=False
                    m+=1
    
    ordercode=0
    
    highestmale=max(males)
    highestfemale=max(females)
    if males.count(highestmale)!=1:
        if females.count(highestfemale)!=1:
            if highestfemale>highestmale:
                findtopfemale(females)
                ordercode=1
                if len(females)>=1:
                    if max(females)>max(males):
                        ordercode=2
                        findtopfemale(females)
                        fcandidateselected+=1
                findtopmale(males)
            else:
                findtopmale(males)
                if len(males)>=1:
                    if max(males)>max(females):
                        ordercode=3
                        findtopmale(males)
                        mcandidateselected+=1
                findtopfemale(females)
        else:
            findtopfemale(females)
            ordercode=1
            if len(females)>=1:
                if max(females)>max(males):
                    findtopfemale(females)
                    ordercode=2
                    fcandidateselected+=1
            findtopmale(males)
    else:
        if females.count(highestfemale)!=1:
            findtopmale(males)
            if len(males)>=1:
                if max(males)>max(females):
                    findtopmale(males)
                    ordercode=3
                    mcandidateselected+=1
            findtopfemale(females)
        else:
            findtopmale(males)
            findtopfemale(females)
            
    
    
    
    
    if ordercode==0:
        print('Top Male, Top Female:')
    if ordercode==1:
        print('Top Female, Top Male')
    if ordercode==2:
        print('Top two females, top male')
    if ordercode==3:
        print('Top two males, top female')
    print(winners)
    #for x in range(0, len(winners)):
        #lista.remove(winners[x])
        
        
    if len(winners)==2:
        maxvalue=max(lista)
        if lista.count(maxvalue)==1:
            winners.append(maxvalue)
            position=lista.index(maxvalue)
            electedgender=genders[position]
            if electedgender==0:
                fcandidateselected+=1
            else:
                mcandidateselected+=1
        else:
            test=False
            quote=0
            while test==False:
                if quote==0:
                    print("Stalemate Detected. (Neutral) ")
                    quote+=1
                else:
                    print("Fire Detected in the Stalemate Resolution Annex.")
                m=0
                tester=0
                while tester==0:
                    if lista[m]==0:
                        m+=1
                    else:
                        tester=1
                        
                redistribute=lista[m]
                
                for x in range(0, redistribute):
                    vote=random.randint(m+1,len(lista)-1)
                    lista[vote]+=1
                lista[m]=0
                print("New Votes In.")
                print(lista)
                #main()
                maxvalue=max(lista)
                if lista.count(maxvalue)==1:
                    test=True
                    winners.append(maxvalue)
                    position=lista.index(maxvalue)
                    electedgender=genders[position]
                    if electedgender==0:
                        fcandidateselected+=1
                    else:
                        mcandidateselected+=1
                else:
                    test=False
              
                
    global totalmalevotes
    global totalfemalevotes
    global totalmalecandidates
    global totalfemalecandidates
    global totalwinvotes
    global totalwastevotes
    
    print('Final Results!')
    sort(winners)
    print("Male Votes Cast " + str(malevotescast))
    totalmalevotes+=malevotescast
    print("Female Votes Cast " + str(femalevotescast))
    totalfemalevotes+=femalevotescast
    print("Male Candidates Elected " +str(mcandidateselected))
    totalmalecandidates+=mcandidateselected
    print("Female Candidates Elected " +str(fcandidateselected))
    totalfemalecandidates+=fcandidateselected
    print("Winning Votes Cast " + str(sum(winners)))
    totalwinvotes+=sum(winners)
    
    wastedvotes=135-sum(winners)
    
    females=[]
    males=[]
    
    
    excessvotes=0
    for x in range(0, len(savegenders)):
        if savegenders[x]==0:
            females.append(savethislist[x])
            #print(len(females))
        else:
            males.append(savethislist[x])
            
    #print(len(savegenders))
    ##int(len(females))      
            
    if mcandidateselected==1:
        if len(males)!=1:
            females.remove(females[len(females)-1])
            toptwomale=males[len(males)-1]+males[len(males)-2]
            averagemale=toptwomale//2
            if averagemale>females[len(females)-1]:
                excessvotes=max(males)-averagemale
                #print(excessvotes)
    else:
        if len(females)!=1:
            males.remove(males[len(males)-1])
            toptwofemale=females[len(females)-1]+females[len(females)-2]
            averagefemale=toptwofemale//2
            if averagefemale>males[len(males)-1]:
                excessvotes=max(females)-averagefemale
                #print(excessvotes)
                
    wastedvotes+=excessvotes
    print("Wasted Votes " + str(wastedvotes))
    totalwastevotes+=wastedvotes
    print('----------')

repeatnumber=input("How many elections?")
for x in range(0, int(repeatnumber)):
    runElection()


print('----------')
print("Hello. I'm SAMIRA. My job is showing artful mathematics involving real answers.")

print('Total Results!')

print("Male Votes Cast " + str(totalmalevotes))

print("Female Votes Cast " + str(totalfemalevotes))

print("Male Candidates Elected " +str(totalmalecandidates))

print("Female Candidates Elected " +str(totalfemalecandidates))

print("Winning Votes Cast " + str(totalwinvotes))
print("Wasted Votes "+ str(totalwastevotes))
