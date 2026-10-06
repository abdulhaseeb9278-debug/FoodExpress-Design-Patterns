from logger import Logger
from meal_factory import MealFactory
from combo_meal_builder import ComboMealBuilder
from delivery_partner_pool import DeliveryPartnerPool
from payment_adapter import OldPaymentGateway, PaymentGatewayAdapter


def main():

    # -----------------------------------------
    # 1. Get the Singleton Logger
    # -----------------------------------------

    logger = Logger.get_instance()

    order_id = "ORD-001"

    logger.log(f"Starting order {order_id}")

    # -----------------------------------------
    # 2. Create a meal using Factory
    # -----------------------------------------

    meal = MealFactory.create_meal("pizza")

    if meal is None:
        print("Invalid meal type.")
        logger.log("Meal creation failed.")
        return

    logger.log("Meal created successfully: Pizza")

    # -----------------------------------------
    # 3. Build a combo using Builder
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
    # 4. Assign a delivery partner
    # -----------------------------------------

    pool = DeliveryPartnerPool()

    partner_id = pool.assign_partner(order_id)

    if partner_id is None:
        print("No delivery partner available.")
        logger.log("Delivery partner assignment failed.")
        return

    logger.log(f"Delivery partner assigned: {partner_id}")

    # -----------------------------------------
    # 5. Process payment using Adapter
    # -----------------------------------------

    old_gateway = OldPaymentGateway()

    payment_processor = PaymentGatewayAdapter(old_gateway)

    payment_success = payment_processor.pay(1500)

    if payment_success:
        logger.log("Payment processed successfully")
    else:
        logger.log("Payment failed")

    # -----------------------------------------
    # 6. Display order receipt
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
    # 7. Display Logger history
    # -----------------------------------------

    print("\n==============================")
    print("         LOG HISTORY")
    print("==============================")

    for log in logger.get_logs():
        print(log)


if __name__ == "__main__":
    main()
