#Used:
#Python dictionary
#Basic flow: 
# 'votes' is used to save every candidate vote
# 'results' is a dictionary to save every option votes and link them with themselves names

import random as r

votes = [0] * 20

results = {'Windows Server': 0, 'Unix': 0, 'Linux': 0, 'Netware': 0, 'Mac OS': 0, 'Outro': 0}

for i in range(20):
    random_number = r.randint(1,6)
    votes[i] = random_number

print(votes)

for i in range(len(votes)):
    if(votes[i]==1):
        results['Windows Server'] = results['Windows Server'] + 1
    elif(votes[i]==2):
        results['Unix'] = results['Unix'] + 1
    elif(votes[i]==3):
        results['Linux'] = results['Linux'] + 1
    elif(votes[i]==4):
        results['Netware'] = results['Netware'] + 1
    elif(votes[i]==5):
        results['Mac OS'] = results['Mac OS'] + 1
    elif(votes[i]==6):
        results['Outro'] = results['Outro'] + 1

print('Which one is the best Operating System for servers usage?')
print('Windows Server: {} votes'.format(results['Windows Server']))
print('Unix: {} votes'.format(results['Unix']))
print('Linux: {} votes'.format(results['Linux']))
print('Netware: {} votes'.format(results['Netware']))
print('Mac OS: {} votes'.format(results['Mac OS']))
print('Other: {} votes'.format(results['Outro']))
print("The Winner is {}".format(max(results, key=results.get)))