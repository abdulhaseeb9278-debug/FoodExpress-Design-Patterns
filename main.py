from logger import Logger
from meal_factory import MealFactory
from combo_meal_builder import ComboMealBuilder
from delivery_partner_pool import DeliveryPartnerPool
from payment_adapter import OldPaymentGateway, PaymentGatewayAdapter


def main():

    # -----------------------------------------
    # 1. Singleton Logger
    # -----------------------------------------

    logger = Logger.get_instance()

    order_id = "ORD-001"

    logger.log(f"Starting order {order_id}")

    # -----------------------------------------
    # 2. Factory - Create Meal
    # -----------------------------------------

    meal = MealFactory.create_meal("pizza")

    if meal is None:
        print("Invalid meal type.")
        logger.log("Meal creation failed.")
        return

    logger.log("Meal created successfully: Pizza")

    # -----------------------------------------
    # 3. Builder - Build Combo Meal
    # -----------------------------------------

    builder = ComboMealBuilder()

    combo = (
        builder
        .set_main_meal(meal)
        .set_drink("Pepsi")
        .set_side("Fries")
        .set_discount("SAVE10")
        .build()
    )

    logger.log("Combo meal built successfully")

    # -----------------------------------------
    # 4. Multiton - Delivery Partner Pool
    # -----------------------------------------

    pool = DeliveryPartnerPool()

    partner1 = pool.assign_partner("ORD-001")
    partner2 = pool.assign_partner("ORD-002")
    partner3 = pool.assign_partner("ORD-003")

    # Pool is now full
    partner4 = pool.assign_partner("ORD-004")

    if partner4 is None:
        logger.log("Delivery partner pool is full")

    # Release one partner
    pool.release_partner(partner2)
    logger.log(f"Delivery partner released: {partner2}")

    # Assign a new partner
    partner4 = pool.assign_partner("ORD-004")
    logger.log(f"New delivery partner assigned: {partner4}")

    # Use Partner-1 for our actual order
    partner_id = partner1

    logger.log(f"Delivery partner assigned to {order_id}: {partner_id}")

    # -----------------------------------------
    # 5. Adapter - Process Payment
    # -----------------------------------------

    old_gateway = OldPaymentGateway()

    payment_processor = PaymentGatewayAdapter(old_gateway)

    payment_success = payment_processor.pay(1500)

    if payment_success:
        logger.log("Payment processed successfully")
    else:
        logger.log("Payment failed")

    # -----------------------------------------
    # 6. Display Order Receipt
    # -----------------------------------------

    print("\n==============================")
    print("         FOOD EXPRESS")
    print("==============================")

    print(f"Order ID: {order_id}")
    print("Meal: Pizza")
    print("Drink: Pepsi")
    print("Side: Fries")
    print("Discount: SAVE10")
    print(f"Delivery Partner: {partner_id}")
    print("Amount: Rs.1500")
    print("Payment: Successful")

    print("==============================")
    print("        ORDER COMPLETE")
    print("==============================")

    # -----------------------------------------
    # 7. Display Logger History
    # -----------------------------------------

    print("\n==============================")
    print("         LOG HISTORY")
    print("==============================")

    for log in logger.get_logs():
        print(log)


if __name__ == "__main__":
    main()
