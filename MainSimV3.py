import dataclasses
from UsedDataClasses import ContractAsset, Creditor, Debtor, Item, Properities

class Entity:
    def __init__(self, ID, **kwargs) -> None:
        c = kwargs.get('c', None)
        d = kwargs.get('d', None)

        self.AssetContracts = []
        self.ID = ID
        self.Name = 'shely'

        if c == None:
            self.Creditor = Creditor(0, ID)
        elif dataclasses.is_dataclass(c) == True: # not realy good enough
            self.Creditor = c
        else:
            raise Exception('c is a suposed to be the dataclass, Creditor')
        
        if d == None:
            self.Debtor = Debtor(0, ID)
        elif dataclasses.is_dataclass(d) == True:
            self.Debtor = d
        else:
            raise Exception('d is a suposed to be the dataclass, Debitor')
        
    def CreateAssetContract(self, itemID, itemQuantity, ID):
        if len(Items) == 0:
            raise Exception('No Items have been created')

        self.AssetContracts.append(ContractAsset(ListSearchItemID(Items, itemID), itemQuantity, ID))
        
        #for e in range(0, len(Items)):
        #    if Items[e].itemID == itemID:
        #        self.AssetContracts.append(ContractAsset(0, Items[e], itemQuantity, ID))
        #    else:
        #        raise Exception('The item you have referanced does not exist')
    
    def printall(self):
        print(self.Name)
        print(self.ID)
        print(self.Creditor)
        print(self.Debtor)
        print(self.AssetContracts)

class indexing: # indexes the returns of classes. Makes things 'pulic'
    def __init__(self) -> None:
        global Entities; Entities = []
        global Debtors; Debtors = []
        global Creditors; Creditors = []
        global Items; Items = []
        global AllProperties; AllProperties = []

    def CreateEntity(self, EntityID):
        E = Entity(EntityID)
        Entities.append(E)
        Creditors.append(E.Creditor)
        Debtors.append(E.Debtor)

    def CreateItem(self, ID, properties): #ggggggggggggggggggggggg
        confirmedProperties = []

        for e in range(0, len(properties)):
            print(properties[e])
            confirmedProperties.append(ListSearchItemID(AllProperties, properties[e]))
            
        Items.append(Item(ID, 0, confirmedProperties))
    
    def CreateProperty(self, Value, Name):
        AllProperties.append(Properities(Value, Name))
    
    def printall(self):
        print(Entities)
        print(Debtors)
        print(Creditors)
        print(Items)
        print(AllProperties)

def ListSearchItemID(SerchList, SerchingID):
    for e in range(0, len(SerchList)):
            if SerchList[e].ID == SerchingID:
                return SerchList[e]
            else:
                raise Exception('The thing you have referanced does not exist')


System = indexing()

System.CreateProperty(1, 'hard')
System.CreateProperty(1, 'wet')

System.CreateEntity(0)

System.CreateItem('wood', ['hard'])

Entities[0].CreateAssetContract('wood', 5, 'WoodStockpile')

Entities[0].printall()
print()
System.printall()