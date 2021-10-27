from UsedDataClasses import ContractAsset, Item, Properities
import dataclasses

# This time remove the idea of a 'creditor' and a 'debitor' instead simply specifying contracts, which certant poeple gain and lose stuff from

class indexing:
    def __init__(self) -> None:
        self.Properties = {}
        self.Items = {}
        
    def createNewPropertie(self, ID, Value):
        NewPropertie = Properities(Value, ID)
        self.Properties[ID] = NewPropertie
        return NewPropertie
        
    def createNewItem(self, ID, PropertiesIDs):
        
        ItemProperities = self.convertPropertieIDsToDataClasses(PropertiesIDs)
            
        NewItem = Item(ID, ItemProperities)
        self.Items[ID] = NewItem
        return NewItem
    
    def convertPropertieIDsToDataClasses(self, PropertiesIDs):
        ItemProperties = {}
        for propertieID in PropertiesIDs:
            if self.validatePropertiesExist(propertieID):
                if isinstance(propertieID, Properities):
                    ItemProperties[propertieID.ID] =  propertieID
                else:
                    ItemProperties[propertieID] = self.Properties[propertieID]

        return ItemProperties
        
    def convertItemIDToDataClass(self, ItemID):
        if self.validateItemExist(ItemID) and isinstance(ItemID, str):
            if isinstance(ItemID, Item):
                return ItemID
            else:
                return self.Items[ItemID]
    
    def convertContractAssetIDToObject(self, AssetContractID, Entity):
        if self.validateAssetContract(AssetContractID, Entity):
            if isinstance(AssetContractID, ContractAsset):
                return AssetContractID
            else:
                return Entity.AssetContracts[AssetContractID]
                
    
    def validateItemExist(self, ItemID):
        if dataclasses.is_dataclass(ItemID):
            if ItemID in self.Items:
                return True
        else:
            try:
                self.Items[ItemID]
                return True
            except:
                print('Item does not exist')
                return False
    
    def validatePropertiesExist(self, PropertieID):
        if dataclasses.is_dataclass(PropertieID):
            if PropertieID in self.Properties:
                return True
        else:
            try:
                self.Properties[PropertieID]
                return True
            except:
                print('Item does not exist')
                return False
    
    def validateAssetContract(self, ContractAssetitem, Entity):
        if isinstance(ContractAssetitem, ContractAsset):
            if ContractAssetitem in Entity.AssetContracts:
                return True
            else:
                return False
        else:
            try:
                Entity.AssetContracts[ContractAssetitem]
                return True
            except:
                print('Contract does not exist')
                return False
    
class exchange():
    def transferAssetContract(self, FromEntity: object, ToEntity: object, AssetContractID: str):
        AssetContact = Indexer.convertContractAssetIDToObject(AssetContractID, FromEntity)
        FromEntity.AssetContracts.pop(AssetContact.ID)
        ToEntity.AssetContracts[AssetContact.ID] = AssetContact
        return True
        
 

class Entity:
    def __init__(self, ID: int, Name: str) -> None:

        self.AssetContracts = {}
        self.ID = ID
        self.Name = Name
        
    def createAssetContract(self, ContractID, ItemID, Quantity):
        
        Item = Indexer.convertItemIDToDataClass(ItemID)
            
        NewAssetContract = ContractAsset(Item, Quantity, ContractID)
        self.AssetContracts[ContractID] = NewAssetContract
        return NewAssetContract
    
Exchange = exchange()
Indexer = indexing()
Indexer.createNewPropertie('hard', 1)
Indexer.createNewPropertie('wood', 2)
Indexer.createNewItem('Stick', ['hard', 'wood'])

Shelly = Entity(0, 'Shelly')
Shelly.createAssetContract('Sticks Reserve', 'Stick', 5) # Suports both the actual dataclass and id
print(Shelly.AssetContracts['Sticks Reserve'].getValueOfContract())

Sharron = Entity(1, 'Sharron')

Exchange.transferAssetContract(Shelly, Sharron, 'Sticks Reserve')

print(Sharron.AssetContracts['Sticks Reserve'].getValueOfContract())