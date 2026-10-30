# Warehouse Inventory Reconciliation System

def reconcile_inventory(products):
    results = []

    for product in products:
        name = product["name"]
        opening_stock = product["opening_stock"]
        incoming_stock = product["incoming_stock"]
        dispatched_stock = product["dispatched_stock"]
        actual_closing_stock = product["actual_closing_stock"]
        minimum_stock = product["minimum_stock"]

        # Calculate expected closing stock
        expected_closing_stock = (
            opening_stock + incoming_stock - dispatched_stock
        )

        # Detect stock discrepancy
        discrepancy = actual_closing_stock - expected_closing_stock

        if discrepancy == 0:
            status = "MATCH"
        elif discrepancy > 0:
            status = "EXCESS STOCK"
        else:
            status = "STOCK SHORTAGE"

        # Calculate replenishment requirement
        replenishment = max(0, minimum_stock - actual_closing_stock)

        results.append({
            "name": name,
            "opening": opening_stock,
            "incoming": incoming_stock,
            "dispatched": dispatched_stock,
            "expected": expected_closing_stock,
            "actual": actual_closing_stock,
            "discrepancy": discrepancy,
            "status": status,
            "replenishment": replenishment
        })

    return results


def display_report(results):
    print("\n" + "=" * 100)
    print("             WAREHOUSE INVENTORY RECONCILIATION REPORT")
    print("=" * 100)

    print(
        f"{'Product':<15}"
        f"{'Opening':>9}"
        f"{'Incoming':>10}"
        f"{'Dispatch':>10}"
        f"{'Expected':>10}"
        f"{'Actual':>9}"
        f"{'Difference':>12}"
        f"{'Status':>17}"
    )

    print("-" * 100)

    for item in results:
        print(
            f"{item['name']:<15}"
            f"{item['opening']:>9}"
            f"{item['incoming']:>10}"
            f"{item['dispatched']:>10}"
            f"{item['expected']:>10}"
            f"{item['actual']:>9}"
            f"{item['discrepancy']:>12}"
            f"{item['status']:>17}"
        )

    print("\n" + "=" * 55)
    print("                 INVENTORY SUMMARY")
    print("=" * 55)

    matched = sum(1 for item in results if item["discrepancy"] == 0)
    excess = sum(1 for item in results if item["discrepancy"] > 0)
    shortage = sum(1 for item in results if item["discrepancy"] < 0)

    total_replenishment = sum(
        item["replenishment"] for item in results
    )

    print(f"Total products checked:       {len(results)}")
    print(f"Products matching records:    {matched}")
    print(f"Products with excess stock:   {excess}")
    print(f"Products with stock shortage: {shortage}")
    print(f"Total units to replenish:     {total_replenishment}")

    print("\n" + "=" * 55)
    print("             REPLENISHMENT REQUIREMENTS")
    print("=" * 55)

    for item in results:
        if item["replenishment"] > 0:
            print(
                f"{item['name']}: Order "
                f"{item['replenishment']} units"
            )

    if total_replenishment == 0:
        print("No replenishment required.")

    print("=" * 55)


def main():
    print("=" * 50)
    print("     WAREHOUSE INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    products = []

    try:
        number_of_products = int(
            input("Enter the number of products: ")
        )

        if number_of_products <= 0:
            print("Number of products must be greater than zero.")
            return

        for i in range(number_of_products):
            print(f"\nEnter details for Product {i + 1}")

            name = input("Product name: ").strip()

            if not name:
                print("Product name cannot be empty.")
                return

            opening_stock = int(input("Opening stock: "))
            incoming_stock = int(input("Incoming stock: "))
            dispatched_stock = int(input("Dispatched stock: "))
            actual_closing_stock = int(input("Actual closing stock: "))
            minimum_stock = int(input("Minimum stock level: "))

            quantities = [
                opening_stock,
                incoming_stock,
                dispatched_stock,
                actual_closing_stock,
                minimum_stock
            ]

            if any(quantity < 0 for quantity in quantities):
                print("Stock quantities cannot be negative.")
                return

            if dispatched_stock > opening_stock + incoming_stock:
                print(
                    "Warning: Dispatches exceed available stock. "
                    "Please verify the entered quantities."
                )

            products.append({
                "name": name,
                "opening_stock": opening_stock,
                "incoming_stock": incoming_stock,
                "dispatched_stock": dispatched_stock,
                "actual_closing_stock": actual_closing_stock,
                "minimum_stock": minimum_stock
            })

        results = reconcile_inventory(products)
        display_report(results)

    except ValueError:
        print("Invalid input. Please enter whole numbers for quantities.")


if __name__ == "__main__":
    main()