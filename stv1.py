# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:47:44 2020

@author: 23beraid
"""

import random
printlist=[]
totalfemalecandidates=0
totalmalecandidates=0
totalmalevotes=0
totalfemalevotes=0
totalwinvotes=0
totalwastevotes=0


def stvElection(quota):
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
    
    mcandidateselected=0
    fcandidateselected=0
    winners=[]
    malevotescast=0
    femalevotescast=0
    
    def printList(thislist):
        for x in range(0, len(thislist)):
            printlist.append(thislist[x])
            
    mainlist=[0, 0, 0, 0, 0, 0]
    for x in range(0, 135):
        mainlist[random.randint(0, len(mainlist)-1)]+=1
    printlist.append('The Votes are in!')   
    printList(mainlist)
    print(mainlist)


    def sort(my_list):
        printlist=[]
        size = len(my_list)
        for i in range(size):
            for j in range(size-i-1):
                if(my_list[j] > my_list[j+1]):
                    tmp = my_list[j]
                    my_list[j] = my_list[j+1]
                    my_list[j+1] = tmp
        printlist.append("The results have been ordered!")
        printList(my_list)
        print("The results have been ordered.")
        print(my_list)
        
    sort(mainlist)
    genders=[0, 0, 0, 0, 0, 0]
    for x in range(0, len(genders)):
        genders[x]+=random.randint(0,1)
    print(genders)
    printList(genders)
    
    for x in range(0, len(genders)):
        if genders[x]==0:
            femalevotescast+=mainlist[x]
        else:
            malevotescast+=mainlist[x]
    test=False
    while test==False:
    
        maxvalue=max(mainlist)
        if maxvalue>=quota:
            
            excess=maxvalue-quota
            winners.append(maxvalue-excess)
            listpos=getIndexPositions(mainlist, maxvalue)
            lastpos=listpos[-1]
            del mainlist[lastpos]
            if genders[lastpos]==1:
                mcandidateselected+=1
            else:
                fcandidateselected+=1
            del genders[lastpos]
            '''
            m=0
            tester=0
            while tester==0:
                if mainlist[m]==0:
                    m+=1
                else:
                    tester+=1
            '''
            for x in range(0, excess):
                vote=random.randint(0,len(mainlist)-1)
                mainlist[vote]+=1
            printlist.append(str(excess)+' Excess votes redistributed.')
            printList(mainlist)
            printlist.append('Winner Added')
            printList(winners)
            print(str(excess)+' Excess Votes Redistributed')
            print(mainlist)
            print('Winner added')
            print(winners)
        
        else:
            #print('code2')
            minvalue=min(mainlist)
            redistribute=minvalue
            listpos=getIndexPositions(mainlist, minvalue)
            mainlist[listpos[0]]=0
            del mainlist[listpos[0]]
            del genders[listpos[0]]
            for x in range(0, redistribute):
               
                   
                vote=random.randint(0, len(mainlist)-1)
                   
                mainlist[vote]+=1
                #print(mainlist[vote])
            printlist.append('Lowest candidate eliminated')
            printList(mainlist)
            printList(genders)
            print('Lowest Candidate eliminated')
            print(mainlist)
            print(genders)
        if len(winners)==3:
           test=True
        #test=True    
    print('Male Candidates elected '+str(mcandidateselected))
    printlist.append('Male Candidates elected '+str(mcandidateselected))
    printlist.append('Female Candidates elected '+str(fcandidateselected))
    print('Female Candidates elected '+str(fcandidateselected))
    printlist.append('Male Votes Cast '+ str(malevotescast))
    printlist.append('Female Votes Cast '+ str(femalevotescast))
    printlist.append('Winning votes cast '+str(sum(winners)))
    printlist.append('Wasted Votes Cast '+str(135-sum(winners)))
    #print(printlist)
    #printlist.append('Final Results')
    #printList(printlist)
    print(printlist)
    
    global totalmalecandidates
    global totalfemalecandidates
    global totalmalevotes
    global totalfemalevotes
    global totalwinvotes
    global totalwastevotes
    
    totalmalecandidates+=mcandidateselected
    totalfemalecandidates+=fcandidateselected
    totalwinvotes+=sum(winners)
    totalmalevotes+=malevotescast
    totalfemalevotes+=femalevotescast
    totalwastevotes+=135-sum(winners)
    
stvElection(45)
'''Hare = 45
Droop = 34'''
def finalStvResults():
    #def finalResults():
    #print(totalmalevotes)
    #print(totalfemalevotes)
    printlist=[]
    printlist.append('----------')
    printlist.append("Hello. I'm SAMIRA, your specialized automated mathematical internal research associate.")
    
    printlist.append('Total Results!')
    
    printlist.append("Male Votes Cast " + str(totalmalevotes))
    
    printlist.append("Female Votes Cast " + str(totalfemalevotes))
    
    printlist.append("Male Candidates Elected " +str(totalmalecandidates))
    
    printlist.append("Female Candidates Elected " +str(totalfemalecandidates))
    
    printlist.append("Winning Votes Cast " + str(totalwinvotes))
    printlist.append("Wasted Votes "+ str(totalwastevotes))
    print(printlist)
    return(printlist)
finalStvResults()