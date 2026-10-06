class DeliveryPartnerPool:

    MAX_PARTNERS = 3

    def __init__(self):
        self.active_partners = {}
        self.next_partner_id = 1

    def assign_partner(self, order_id):
        # Check if the pool is full
        if len(self.active_partners) >= self.MAX_PARTNERS:
            print("No delivery partner available. Pool is full.")
            return None

        # Create a unique partner ID
        partner_id = f"Partner-{self.next_partner_id}"
        self.next_partner_id += 1

        # Add partner to active partners
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
