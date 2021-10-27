from dataclasses import dataclass

@dataclass
class Debtor:
    totalValue: float
    ID: str

@dataclass
class Creditor:
    totalValue: float
    ID: str

@dataclass
class Item:
    ID: str
    properties: dict

@dataclass
class Properities:
    PropertyValue: float
    ID: str
    
class ContractAsset:
    def __init__(self, item, itemQuantity, ID) -> None:
        self.item: int = item
        self.itemQuantity: int = itemQuantity
        self.ID: str = ID
    
    def getValueOfContract(self):
        Value = 0
        for propertieID in self.item.properties:
            Value += self.item.properties[propertieID].PropertyValue
        return Value*self.itemQuantity