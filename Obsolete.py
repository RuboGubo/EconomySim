import time

# Creditors = [[bank name, total money, [[ContractInterest ID, ContractInterest owner ID, interest, total money in ContractInterest (true)]]]]
Creditors = [['Bank Alpha', 0, [['Bank Alpha ContractInterest 1', 'debtor 1', 1.05, 5],
                            ['Bank Alpha ContractInterest 2', 'debtor 2', 1.03, 20]]]]

# Debtors = [[name, total money, [[ContractInterest ID, ContractInterest owner ID, interest, total money in ContractInterest (aware)]]]]
Debtors = [['debtor 1', 0, [['Bank Alpha ContractInterest 1', 'debtor 1', 1.5, 0]]],
           ['debtor 2', 0, [['Bank Alpha ContractInterest 2', 'debtor 2', 1.3, 0]]]]

# Debtors = [[name, total money, debtor component, Creditor component]]
Entity = [['bob', 0, 'debtor 1', 'Bank Alpha ContractInterest 1'],
          ['sharon', 0, 'debtor 2', 'a']]

def printContractInterests():
        for p in range(0, len(Debtors)): #cycle through Debtors
            print(Debtors[p][0])
            for cp in range(0, len(Debtors[p][2])): #cycle through ContractInterests debtor
                print(Debtors[p][2][cp])
            print()
        
        print()
        
        for b in range(0, len(Creditors)): # cycle through Creditors
            print(Creditors[b][0])
            for c in range(0, len(Creditors[b][2])): # cycle through ContractInterests
                print(Creditors[b][2][c])

def ContractInterestsyncer(i):
    print('ContractInterest Syncer:')
    # i = item ID
    for p in range(0, len(Debtors)): # cycle through Debtors
        for cp in range(0, len(Debtors[p][2])): # cycle through ContractInterests debtor
            print(Debtors[p][2][cp])

            for b in range(0, len(Creditors)): # cycle through Creditors
                for c in range(0, len(Creditors[b][2])): # cycle through ContractInterests
                    print(Creditors[b][2][c])

                    if Creditors[b][2][c][i] == Debtors[p][2][cp][i]:
                        print()
                        print('Match found: For Item code', i)
                        print('Bank:   ', Creditors[b][2][c])
                        print('debtor: ', Debtors[p][2][cp])
                        print()

                        print('Synced:')
                        for sy in range(2, len(Creditors[b][2][c])): #find all things to sync

                            #banck gets to deside conditions so they are the validator
                            Debtors[p][2][cp][sy] = Creditors[b][2][c][sy]
                            print(Debtors[p][2][cp])

                        print()

def TotalMoney():
    print('Total Money:')
    for p in range(0, len(Debtors)): # cycle through Debtors
        Debtors[p][1] = 0
        for cp in range(0, len(Debtors[p][2])): # cycle through ContractInterests debtor
            Debtors[p][1] += Debtors[p][2][cp][3]
            print(Debtors[p])
    
    for p in range(0, len(Creditors)): # cycle through Creditors
        Creditors[p][1] = 0
        for cp in range(0, len(Creditors[p][2])): # cycle through ContractInterests Creditors
            Creditors[p][1] -= Creditors[p][2][cp][3]
            print(Creditors[p])

def InterestCalculation():
    print('Interest Calculation:')
    for b in range(0, len(Creditors)): # cycle through Creditors
            print(Creditors[b][0])
            for c in range(0, len(Creditors[b][2])): # cycle through ContractInterests

                Creditors[b][2][c][3] = Creditors[b][2][c][3]*Creditors[b][2][c][2]

                print(Creditors[b][2][c])
        
def EntitySumer():
    print('Entity Sum:')

    for b in range(0, len(Entity)): # cycle through all Entitys
        for i in range(0, len(Debtors)): # find Debtors
            if Entity[b][2] == Debtors[i][0]:
                print(b)
                print(Entity[b][1], '           ', Debtors[i][1])
                Entity[b][1] += Debtors[i][1]

        for i in range(0, len(Creditors)): # find Debtors
            if Entity[b][3] == Creditors[i][0]:
                Entity[b][1] += Creditors[i][1]


    #Entity[b][1] = Debtors
    print(Entity[b])

x = 0
cycles = 1000

tic = time.perf_counter()

while x <= cycles:
    print()

    InterestCalculation()
    print()
    print()
    ContractInterestsyncer(0) # Item ID: 0 = ContractInterest ID
    print()
    TotalMoney()
    print()
    EntitySumer()
    print()
    #printContractInterests()
    #print()

    x += 1

toc = time.perf_counter()

print()
print(f"Simulated the economy in {toc - tic:0.4f} seconds for " + str(cycles) + ' cycles')