from dataclasses import dataclass
import time
import logging

open("test.log", 'w').close() # wipes log so that it is easy to read

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
class ContractAsset:
    totalValue: float
    debtor: str
    itemID: float
    itemQuantity: int
    ID: int

@dataclass
class Item:
    itemID: float
    itemValue: float

#BankAlphaContractInterest1 = ContractInterest(1, 0, 1, 1.05, -1)

AllEntity = []
AllDebtors = []
AllCreditors = []
AllContractInterests = []
AllContractAssets = []
AllItems = []

def CalculateComponentValue(): # might need improving
    for i in range(0, len(AllContractInterests)): # find ContractInterests with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractInterests[i].debtor == AllDebtors[d].ID:
                AllDebtors[d].totalValue += AllContractInterests[i].totalValue

    for i in range(0, len(AllContractInterests)): # find ContractInterests with creditors
        for d in range(0, len(AllCreditors)):
            if AllContractInterests[i].creditor == AllCreditors[d].ID:
                AllCreditors[d].totalValue -= AllContractInterests[i].totalValue

    for i in range(0, len(AllContractAssets)): # find ContractAssets with debitors
        for d in range(0, len(AllDebtors)):
            if AllContractAssets[i].debtor == AllDebtors[d].ID:
                AllDebtors[d].totalValue += AllContractAssets[i].totalValue
    
    return AllDebtors, AllCreditors

def CalculateEntityValue():
    for i in range(0, len(AllEntity)):
        AllEntity[i].totalValue = AllEntity[i].debtor.totalValue + AllEntity[i].creditor.totalValue
    return AllEntity

def CalculateContractInterest():
    for i in range(0, len(AllContractInterests)):
        AllContractInterests[i].totalValue = AllContractInterests[i].interest * AllContractInterests[i].totalValue
    return AllContractInterests

def CalculateContractAsset():
    for i in range(0, len(AllContractAssets)):
        AllContractAssets[i].totalValue = AllContractAssets[i].itemQuantity * AllContractAssets[i].itemID.itemValue
    return AllContractAssets

def CreateNewEntity(ID, NumberOfEntitys): # creats deters and creditors aswell as Entities
    NewEntity = [Entity(0, Debtor(0, ID+i), Creditor(0, ID+i), ID+i) for i in range(0, NumberOfEntitys)]

    AllCreditors.extend([entity.creditor for entity in NewEntity])
    AllDebtors.extend([entity.debtor for entity in NewEntity])
    AllEntity.extend(NewEntity)

    return NewEntity

def CreateNewContractInterest(totalValue, debtor, creditor, interest, ID): # nnnnnnnnnneeeeeeeeddddddddddddd wwwwwwwwwwwoooooooooooooorrrrrrrrrrrrkkkkkkkkk
    NewContract = [ContractInterest(totalValue, debtor, creditor, interest, ID)]
    AllContractInterests.extend(NewContract)
    return NewContract

def CreateNewItem(ID, NumberOfEntitys, Value):
    NewItem = [Item(ID+i, Value) for i in range(0, NumberOfEntitys)]
    AllItems.extend(NewItem)
    return NewItem

def CreateNewContractAsset(debtor, itemID, itemQuantity, ID): # VERY SLOW, FIX
    for e in range(0, len(AllItems)):
        AI = AllItems[e]
    
        if AI.itemID == itemID:
            break

    NewContract = [ContractAsset(0, debtor, AI, itemQuantity, ID)]
    AllContractAssets.extend(NewContract)
    return NewContract

def ClearAllTotalValue(): # clears the value of the creditor and debitor which then affects the totalValue calculation for Entities
    for i in range(0, len(AllCreditors)):
        AllCreditors[i].totalValue = 0
    for i in range(0, len(AllDebtors)):
        AllDebtors[i].totalValue = 0

cycles = 1
x = 0

tic = time.perf_counter()

# all tasks that are not within the loop will be actions that the user or AI can interact with
logging.debug('Create New Entity')
New = CreateNewEntity(x, 2) # remove abilaty for it to create multipal Entitys at a time + add the abilaty to use a already existing debitor/creditor

for i in range(0, len(New)): logging.debug(New[i])


logging.debug('Create New Item')
NewItem = CreateNewItem(x, 2, 1) # remove abilaty for it to create multipal Items at a time

for i in range(0, len(NewItem)): logging.debug(NewItem[i])


logging.debug('Create New Interest Contract')
New = CreateNewContractInterest(1, 0, 1, 1.58, 0)

logging.debug(New)


logging.debug('Create New Asset Contract')
NewAssetContract = CreateNewContractAsset(1, 1, 50, x+1)

logging.debug(NewAssetContract)


while x < cycles:

    # AllContractAssets[0].itemQuantity =+ AllContractAssets[0].itemQuantity+1
    # use above code to increment a contract asset by one, this will need to be a proper function in the future


    # do once all actions are compleated

    logging.debug(f'[{x:0.0f}] Clear Creditor, Debitor and Entity Total Value')
    ClearAllTotalValue()

    logging.debug(f'[{x:0.0f}] Calculate Contract Interest')
    CCI = CalculateContractInterest()
    for i in range(0, len(CCI)): logging.debug(f'[{x:0.0f}] ' + str(CCI[i]))

    logging.debug(f'[{x:0.0f}] Calculate Total Asset Value')
    CCA = CalculateContractAsset()
    for i in range(0, len(CCA)): logging.debug(f'[{x:0.0f}] ' + str(CCA[i]))

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