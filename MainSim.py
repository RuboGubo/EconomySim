from dataclasses import dataclass
import time
import logging

open("test.log", 'w').close()

logging.basicConfig(level = logging.DEBUG, filename = "test.log")

@dataclass
class Entity:
    totalValue: float
    debtor: str
    creditor: str
    ID: str

@dataclass
class Debtor:
    totalValue: float
    ID: str

@dataclass
class Creditor:
    totalValue: float
    ID: str

@dataclass
class ContractInterest:
    totalValue: float
    debtor: str
    creditor: str
    interest: float

@dataclass
class ContractAssets:
    totalValue: float
    debtor: str
    itemID: float
    itemQuantity: int

class Item:
    itemID: str
    itemValue: int

BankAlphaContractInterest1 = ContractInterest(1, 0, 1, 1.05)

AllEntity = []
AllDebtors = []
AllCreditors = []
AllContractInterests = [BankAlphaContractInterest1]

def CalculateComponentValue(): # might need improving
    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractInterests[i].debtor == AllDebtors[d].ID:
                AllDebtors[d].totalValue += AllContractInterests[i].totalValue

    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractInterests[i].creditor == AllCreditors[d].ID:
                AllCreditors[d].totalValue -= AllContractInterests[i].totalValue
    
    return AllDebtors, AllCreditors



def CalculateEntityValue():
    for i in range(0, len(AllEntity)):
        AllEntity[i].totalValue = AllEntity[i].debtor.totalValue + AllEntity[i].creditor.totalValue
    return AllEntity


def CalculateContractInterest():
    for i in range(0, len(AllContractInterests)):
        AllContractInterests[i].totalValue = AllContractInterests[i].interest * AllContractInterests[i].totalValue
    return AllContractInterests

def CreateNewEntity(ID, NumberOfEntitys): # creats deters and creditors aswell
    NewEntity = [Entity(0, Debtor(0, ID+i), Creditor(0, ID+i), ID+i) for i in range(0, NumberOfEntitys)]

    AllCreditors.extend([entity.creditor for entity in NewEntity])
    AllDebtors.extend([entity.debtor for entity in NewEntity])
    AllEntity.extend(NewEntity)

    return NewEntity

def CreateNewContractInterest():
    pass

def CreateNewContractAssets():
    pass

cycles = 1
x = 0

tic = time.perf_counter()

logging.debug('Create New Entity')
New = CreateNewEntity(x, 2)
for i in range(0, len(New)): logging.debug(New[i])

while x < cycles:



    # do once all actions are compleated

    logging.debug(f'[{x:0.0f}] Calculate Contract Interest')
    for i in range(0, len(CalculateContractInterest())): logging.debug(f'[{x:0.0f}] ' + str(CalculateContractInterest()[i]))

    logging.debug(f'[{x:0.0f}] Calculate Total Component Value')
    for i in range(0, len(CalculateComponentValue())):
        for b in range(0, len(CalculateComponentValue())): logging.debug(f'[{x:0.0f}] ' + str(CalculateComponentValue()[i][b]))

    logging.debug(f'[{x:0.0f}] Calculate Total Entity Value')
    for i in range(0, len(CalculateEntityValue())): logging.debug(f'[{x:0.0f}] ' + str(CalculateEntityValue()[i]))

    # update item value
    # calculate asset contract value and add to debitor

    x += 1

toc = time.perf_counter()

logging.info(f"Simulated the economy in {toc - tic:0.4f} seconds for " + str(cycles) + ' cycles')