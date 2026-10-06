class DeliveryPartnerPool:

    _instance = None
    MAX_PARTNERS = 3

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.active_partners = {}
            cls._instance.next_partner_id = 1

        return cls._instance

    def assign_partner(self, order_id):

        if len(self.active_partners) >= self.MAX_PARTNERS:
            print("No delivery partner available. Pool is full.")
            return None

        partner_id = f"Partner-{self.next_partner_id}"
        self.next_partner_id += 1

        self.active_partners[partner_id] = order_id

        print(f"{partner_id} assigned to order {order_id}")

        return partner_id

    def release_partner(self, partner_id):

        if partner_id in self.active_partners:
            del self.active_partners[partner_id]

            print(f"{partner_id} has been released.")

            return True

        print(f"{partner_id} is not currently active.")

        return False
