from dataclasses import dataclass
from typing import List

@dataclass
class Entity:
    TotalValue: float
    debtor: str
    creditor: str

x = Entity(3.2, 'George', 'Fred')

allEntities: List[Entity] = list()

allEntities.append(Entity(0.0, 'John', 'Doe'))

x.debtor = 8

print(x)
