# FoodExpress – Design Patterns in Python

FoodExpress is a mini food-delivery backend system developed in Python to demonstrate the practical implementation of five fundamental software design patterns:

* Singleton
* Multiton
* Factory
* Builder
* Adapter

The project combines these patterns into a single order-processing workflow, demonstrating object-oriented programming, modular design, code reusability, and maintainability.

## Project Overview

FoodExpress simulates the backend workflow of a food-delivery application.

The system demonstrates:

1. Creating meals through a Factory
2. Building customized combo meals using a Builder
3. Managing delivery partners through a limited partner pool
4. Processing payments through an Adapter
5. Maintaining centralized application logs using a Singleton
6. Integrating all components into a complete order workflow

## Design Patterns Implemented

### 1. Singleton – Logger

The `Logger` class provides a single shared logger instance throughout the application.

**Responsibilities:**

* Maintain centralized log history
* Record important application events
* Provide one shared logger instance

Example:

```python
logger = Logger.get_instance()
logger.log("Order started")
```

### 2. Multiton – Delivery Partner Pool

The `DeliveryPartnerPool` manages a limited number of active delivery partners.

The system allows a maximum of three active partners at a time.

**Responsibilities:**

* Assign unique delivery partner IDs
* Limit the number of active partners
* Reject assignments when the pool is full
* Release partners when they are no longer active

Example workflow:

```text
Partner-1 → ORD-001
Partner-2 → ORD-002
Partner-3 → ORD-003

Pool Full → ORD-004 rejected

Partner-2 released

Partner-4 → ORD-004
```

### 3. Factory – MealFactory

The `MealFactory` creates meal objects based on the requested meal type.

Supported meals:

* Pizza
* Burger
* Salad

The client does not need to directly create the concrete meal classes.

Example:

```python
meal = MealFactory.create_meal("pizza")
```

### 4. Builder – ComboMealBuilder

The `ComboMealBuilder` constructs a customized combo meal step by step.

A combo can contain:

* Main meal
* Drink
* Side
* Discount code

Example:

```python
combo = (
    ComboMealBuilder()
    .set_main_meal(meal)
    .set_drink("Pepsi")
    .set_side("Fries")
    .set_discount("SAVE10")
    .build()
)
```

The builder creates a new `ComboMeal` object when `build()` is called.

### 5. Adapter – PaymentGatewayAdapter

The system contains a legacy payment gateway with an incompatible interface:

```python
make_payment_old(amount)
```

The `PaymentGatewayAdapter` provides the interface expected by the new system:

```python
pay(amount)
```

This allows the existing legacy gateway to work with the new payment-processing system without modifying the legacy class.

## System Workflow

```text
MealFactory
     ↓
Create Meal
     ↓
ComboMealBuilder
     ↓
Build Combo
     ↓
DeliveryPartnerPool
     ↓
Assign Delivery Partner
     ↓
PaymentGatewayAdapter
     ↓
Process Payment
     ↓
Logger
     ↓
Record Activity
     ↓
Order Receipt
```

## Project Structure

```text
FoodExpress-Design-Patterns/
│
├── main.py
├── logger.py
├── delivery_partner_pool.py
├── meal_factory.py
├── combo_meal_builder.py
├── payment_adapter.py
└── README.md
```

## Example Output

```text
==============================
         FOOD EXPRESS
==============================
Order ID: ORD-001
Meal: Pizza
Drink: Pepsi
Side: Fries
Discount: SAVE10
Delivery Partner: Partner-1
Amount: Rs.1500
Payment: Successful
==============================
        ORDER COMPLETE
==============================
```

The application also demonstrates the delivery partner pool becoming full, releasing a partner, and assigning a new partner.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Abstract Base Classes
* Design Patterns
* Encapsulation
* Abstraction
* Method Chaining

## Key Learning Outcomes

This project demonstrates practical understanding of:

* Singleton Pattern
* Multiton Pattern
* Factory Pattern
* Builder Pattern
* Adapter Pattern
* Object-oriented software design
* Separation of responsibilities
* Code reusability
* Interface adaptation
* Modular software architecture

## How to Run

Clone the repository and run:

```bash
python main.py
```

The program executes the complete FoodExpress order-processing workflow.

## Project Objective

The objective of this project is to demonstrate how common software design patterns can be applied to build a modular and maintainable backend system.

FoodExpress shows how individual design patterns can work independently while also being integrated into a complete software workflow.
