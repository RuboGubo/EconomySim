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
    ID: int

@dataclass # woooooooooorrrrrrrrrkkkkkkkkkkkkkkk oooooooooooooooonnnnnnnnnnnnnnn tttttttthhhhhhhhhhiiiiiiiiiiisssssssss
class ContractAssets:
    totalValue: float
    debtor: str
    itemID: float
    itemQuantity: int

class Item:
    itemID: float
    itemValue: float

#BankAlphaContractInterest1 = ContractInterest(1, 0, 1, 1.05, -1)

AllEntity = []
AllDebtors = []
AllCreditors = []
AllContractInterests = []

def CalculateComponentValue(): # might need improving
    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractInterests[i].debtor == AllDebtors[d].ID:
                AllDebtors[d].totalValue += AllContractInterests[i].totalValue

    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllCreditors)):
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

def CreateNewContractInterest(debtor, creditor, interest, ID):
    NewContract = [ContractInterest(1, debtor, creditor, interest, ID)]
    AllContractInterests.extend(NewContract)
    return NewContract

def CreateNewContractAssets():
    pass

def ClearAllTotalValue():
    for i in range(0, len(AllCreditors)):
        AllCreditors[i].totalValue = 0
    for i in range(0, len(AllDebtors)):
        AllDebtors[i].totalValue = 0

cycles = 1
x = 0

tic = time.perf_counter()

logging.debug('Create New Entity')
New = CreateNewEntity(x, 2)

for i in range(0, len(New)): logging.debug(New[i])

logging.debug('Create New Contract')
New = CreateNewContractInterest(0, 1, 1.58, 0)

logging.debug(New)



while x < cycles:


    # do once all actions are compleated

    logging.debug(f'[{x:0.0f}] Clear Entity Total Value')
    ClearAllTotalValue()

    logging.debug(f'[{x:0.0f}] Calculate Contract Interest')
    CCI = CalculateContractInterest()
    for i in range(0, len(CCI)): logging.debug(f'[{x:0.0f}] ' + str(CCI[i]))

    # update item value
    # calculate asset contract value and add to debitor

    logging.debug(f'[{x:0.0f}] Calculate Total Component Value')
    CCV = CalculateComponentValue()
    for i in range(0, len(CCV)):
        for b in range(0, len(CCV)): logging.debug(f'[{x:0.0f}] ' + str(CCV[i][b]))

    logging.debug(f'[{x:0.0f}] Calculate Total Entity Value')
    CEV = CalculateEntityValue()
    for i in range(0, len(CEV)): logging.debug(f'[{x:0.0f}] ' + str(CEV[i]))

    x += 1

toc = time.perf_counter()

logging.info(f"Simulated the economy in {toc - tic:0.4f} seconds for " + str(cycles) + ' cycles')