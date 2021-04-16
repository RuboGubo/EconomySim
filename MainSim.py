from dataclasses import dataclass
import time
import logging

logging.basicConfig(level = logging.DEBUG, filename = "test.log")

@dataclass
class Entity:
    TotalValue: float
    debtor: str
    creditor: str
    ID: str

@dataclass
class ContractInterest:
    TotalValue: float
    debtor: str
    creditor: str
    interest: float

@dataclass
class Debtor:
    TotalValue: float
    ID: str

@dataclass
class Creditor:
    TotalValue: float
    ID: str

@dataclass
class ContractAssets:
    totalValue: float
    debtor: str
    creditor: str
    interest: float


# add assets

debtor1 = Debtor(0, 'debtor1')
Creditor1 = Creditor(0, 'Creditor1')
bob = Entity(debtor1.TotalValue + Creditor1.TotalValue , debtor1, Creditor1, 'bob')

debtor2 = Debtor(0, 'debtor2')
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
            if AllContractInterests[i].creditor == AllCreditors[d].ID:
                AllCreditors[d].TotalValue -= AllContractInterests[i].TotalValue
    
    return AllDebtors, AllCreditors



def CalculateEntityValue():
    for i in range(0, len(AllEntity)):
        AllEntity[i].TotalValue = AllEntity[i].debtor.TotalValue + AllEntity[i].creditor.TotalValue
    return AllEntity


def CalculateContractInterest():
    for i in range(0, len(AllContractInterests)):
        AllContractInterests[i].TotalValue = AllContractInterests[i].interest * AllContractInterests[i].TotalValue
    return AllContractInterests

def CreateNewEntity(ID, NumberOfEntitys): # creats deters and creditors aswell
    NewEntity = [Entity(0, Debtor(0, ID+1), Creditor(0, ID+i), ID+i) for i in range(0, NumberOfEntitys)]

    AllCreditors.extend([entity.creditor for entity in NewEntity])
    AllDebtors.extend([entity.debtor for entity in NewEntity])
    AllEntity.extend(NewEntity)

    return NewEntity

def CreateNewContractInterest():
    pass

def CreateNewContractAssets():
    pass

cycles = 100000
x = 0

tic = time.perf_counter()

logging.debug('Create New Entity')
New = CreateNewEntity(x, 10)
for i in range(0, len(New)): logging.debug(New[i])

while x < cycles:

    logging.debug(f'[{x:0.0f}] Calculate Contract Interest')
    for i in range(0, len(CalculateContractInterest())): logging.debug(f'[{x:0.0f}] ' + str(CalculateContractInterest()[i]))

    logging.debug(f'[{x:0.0f}] Calculate Total Component Value')
    for i in range(0, len(CalculateComponentValue())):
        for b in range(0, len(CalculateComponentValue())): logging.debug(f'[{x:0.0f}] ' + str(CalculateComponentValue()[i][b]))

    logging.debug(f'[{x:0.0f}] Calculate Total Entity Value')
    for i in range(0, len(CalculateEntityValue())): logging.debug(f'[{x:0.0f}] ' + str(CalculateEntityValue()[i]))

    x += 1

toc = time.perf_counter()

logging.debug(f"Simulated the economy in {toc - tic:0.4f} seconds for " + str(cycles) + ' cycles')