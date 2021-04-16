from dataclasses import dataclass
from typing import List

@dataclass
class Entity:
    TotalValue: float
    debtor: str
    creditor: str

x = Entity(3.2, 'George', 'Fred')

x.debtor = 8

print(x)