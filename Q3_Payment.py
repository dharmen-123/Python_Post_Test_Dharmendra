# Q3. Create Abstract class Payment with: (3 Marks)
# • Abstract method pay()
# • Abstract method receipt()
# Create 2 child classes: GPay and CreditCard — implement both methods.
# Create objects and call all methods

from abc import ABC , abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def receipt(self):
        pass

class GPay(Payment):
    def pay(self):
        print("Gpay is Good Payment mode")

    def receipt(self):
        print("Gpay provide digital recipt")

class CreditCard(Payment):
    def pay(self):
        print("CreditCard is good mode")

    def receipt(self):
        print("CreditCard provide digital and Physical recipt")

Gp=GPay()
Gp.pay()
Gp.receipt()

print()
Cc=CreditCard()
Cc.pay()
Cc.receipt()