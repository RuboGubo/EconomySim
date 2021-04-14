from dataclasses import dataclass
import time
from typing import List


# Creditors = [['Bank Alpha', 0, [['Bank Alpha ContractInterest 1', 'debtor 1', 1.05, 5], 
#                             ['Bank Alpha ContractInterest 2', 'debtor 2', 1.03, 20]]]]

# Debtors = [[name, total money, [[ContractInterest ID, ContractInterest owner ID, interest, total money in ContractInterest (aware)]]]]
# Debtors = [['debtor 1', 0, [['Bank Alpha ContractInterest 1', 'debtor 1', 1.5, 0]]],
#            ['debtor 2', 0, [['Bank Alpha ContractInterest 2', 'debtor 2', 1.3, 0]]]]

# Debtors = [[name, total money, debtor component, Creditor component]]
# Entity = [['bob', 0, 'debtor 1', 'Bank Alpha ContractInterest 1'],
#           ['sharon', 0, 'debtor 2', 'a']]

@dataclass
class Entity:
    TotalValue: float
    debtor: str
    Creditor: str
    ID: str

@dataclass
class ContractInterest:
    TotalValue: float
    debtor: str
    Creditor: str
    interest: float

@dataclass
class Debtors:
    TotalValue: float
    ID: str

@dataclass
class Creditor:
    TotalValue: float
    ID: str

@dataclass
class ContractAssets:
    TotalValue: float
    debtor: str
    Creditor: str
    interest: float


# add assets

debtor1 = Debtors(0, 'debtor1')
Creditor1 = Creditor(0, 'Creditor1')
bob = Entity(debtor1.TotalValue + Creditor1.TotalValue , debtor1, Creditor1, 'bob')

debtor2 = Debtors(0, 'debtor2')
Creditor2 = Creditor(0, 'Creditor2')
sharon = Entity(debtor2.TotalValue + Creditor2.TotalValue, debtor2, Creditor2, 'sharon')


BankAlphaContractInterest1 = ContractInterest(1, 'debtor1', 'Creditor2', 1.05)

AllEntity = [bob, sharon]
AllDebtors = [debtor1, debtor2]
AllCreditors = [Creditor1, Creditor2]
AllContractInterests = [BankAlphaContractInterest1]

def CalculateComponentValue(): # might need improving
    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractInterests[i].debtor == AllDebtors[d].ID:
                AllDebtors[d].TotalValue += AllContractInterests[i].TotalValue

    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractInterests[i].Creditor == AllCreditors[d].ID:
                AllCreditors[d].TotalValue -= AllContractInterests[i].TotalValue
    
    return AllDebtors, AllCreditors



def CalculateEntityValue():
    for i in range(0, len(AllEntity)):
        AllEntity[i].TotalValue = AllEntity[i].debtor.TotalValue + AllEntity[i].Creditor.TotalValue
    return AllEntity


def CalculateContractInterest():
    for i in range(0, len(AllContractInterests)):
        AllContractInterests[i].TotalValue = AllContractInterests[i].interest * AllContractInterests[i].TotalValue
    return AllContractInterests

def CreateNewEntity(DebtorID, CreditorID, EntityID, NumberOfEntitys): # creats deters and creditors aswell
    NewEntity = []
    for i in range(0, NumberOfEntitys):
        Cr = Creditor(0, CreditorID + i)
        De = Debtors(0, DebtorID + i)
        En = Entity(0, De, Cr, EntityID + i)

        AllCreditors.append(Cr)
        AllDebtors.append(De)
        AllEntity.append(En)
        NewEntity.append(En)

    return NewEntity

def CreateNewContractInterest():
    pass

def CreateNewContractAssets():
    pass

cycles = 500
x = 0

tic = time.perf_counter()

print('\nCreate New Entity')
New = CreateNewEntity(x, x, x, 10)
for i in range(0, len(New)): print(New[i])

while x < cycles:

    print(f'\n[{x:0.0f}] Calculate Contract Interest')
    for i in range(0, len(CalculateContractInterest())): print(f'[{x:0.0f}] ', CalculateContractInterest()[i])
    print(f'\n[{x:0.0f}] Calculate Total Component Value')
    for i in range(0, len(CalculateComponentValue())):
        for b in range(0, len(CalculateComponentValue())): print(f'[{x:0.0f}] ', CalculateComponentValue()[i][b])
    print(f'\n[{x:0.0f}] Calculate Total Entity Value')
    for i in range(0, len(CalculateEntityValue())): print(f'[{x:0.0f}] ', CalculateEntityValue()[i])

    x += 1

toc = time.perf_counter()

print(f"\nSimulated the economy in {toc - tic:0.4f} seconds for " + str(cycles) + ' cycles')