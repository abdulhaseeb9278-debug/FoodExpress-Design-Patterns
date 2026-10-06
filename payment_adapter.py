from abc import ABC, abstractmethod


class OldPaymentGateway:

    def make_payment_old(self, amount):
        print(f"[Legacy Gateway] Processing payment of Rs.{amount}")
        return True


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class PaymentGatewayAdapter(PaymentProcessor):

    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def pay(self, amount):
        return self.old_gateway.make_payment_old(amount)
