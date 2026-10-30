# ATM Transaction Sequence Simulation

INITIAL_BALANCE = 5000.00
MAX_WITHDRAWAL = 10000.00
MAX_DAILY_WITHDRAWAL = 20000.00

# Process ATM transactions
def process_transactions(transactions, initial_balance):

    balance = initial_balance
    total_deposits = 0.0
    total_withdrawals = 0.0
    daily_withdrawals = 0.0
    successful = 0
    rejected = 0
    transaction_history = []

    for transaction in transactions:

        transaction_type = transaction["type"].lower()
        amount = transaction["amount"]
        status = ""

        # Validate transaction amount
        if amount <= 0:
            status = "REJECTED: Amount must be positive"
            rejected += 1

        elif transaction_type == "deposit":

            balance += amount
            total_deposits += amount
            successful += 1
            status = "SUCCESSFUL"

        elif transaction_type == "withdrawal":

            if amount > MAX_WITHDRAWAL:
                status = "REJECTED: Exceeds single withdrawal limit"
                rejected += 1

            elif daily_withdrawals + amount > MAX_DAILY_WITHDRAWAL:
                status = "REJECTED: Exceeds daily withdrawal limit"
                rejected += 1

            elif amount > balance:
                status = "REJECTED: Insufficient balance"
                rejected += 1

            else:
                balance -= amount
                daily_withdrawals += amount
                total_withdrawals += amount
                successful += 1
                status = "SUCCESSFUL"

        else:
            status = "REJECTED: Invalid transaction type"
            rejected += 1

        # Record transaction result
        transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "status": status,
            "balance": balance
        })

    return {
        "balance": balance,
        "deposits": total_deposits,
        "withdrawals": total_withdrawals,
        "successful": successful,
        "rejected": rejected,
        "history": transaction_history
    }


# Display transaction summary
def display_summary(result):

    print("\n" + "=" * 55)
    print("             ATM TRANSACTION SUMMARY")
    print("=" * 55)

    print(f"{'Type':<15}{'Amount':<15}{'Status':<25}")
    print("-" * 55)

    for transaction in result["history"]:

        print(
            f"{transaction['type']:<15}"
            f"Rs. {transaction['amount']:<11.2f}"
            f"{transaction['status']}"
        )

        print(
            f"{'':15}{'':15}"
            f"Balance: Rs. {transaction['balance']:.2f}"
        )

    print("-" * 55)
    print(f"Total Deposits:       Rs. {result['deposits']:.2f}")
    print(f"Total Withdrawals:    Rs. {result['withdrawals']:.2f}")
    print(f"Successful Transactions: {result['successful']}")
    print(f"Rejected Transactions:   {result['rejected']}")
    print(f"Final Account Balance: Rs. {result['balance']:.2f}")
    print("=" * 55)


# Main program
def main():

    print("=" * 45)
    print("     ATM TRANSACTION SIMULATION")
    print("=" * 45)

    try:
        balance = float(
            input(f"Enter initial balance (default Rs. {INITIAL_BALANCE:.2f}): ")
            or INITIAL_BALANCE
        )

        if balance < 0:
            print("Initial balance cannot be negative.")
            return

        transaction_count = int(
            input("Enter number of transactions: ")
        )

        if transaction_count < 0:
            print("Number of transactions cannot be negative.")
            return

        transactions = []

        for i in range(transaction_count):

            print(f"\nTransaction {i + 1}")
            print("1. Deposit")
            print("2. Withdrawal")

            choice = input("Select transaction type (1/2): ").strip()

            if choice == "1":
                transaction_type = "deposit"

            elif choice == "2":
                transaction_type = "withdrawal"

            else:
                transaction_type = "invalid"

            amount = float(input("Enter transaction amount: "))

            transactions.append({
                "type": transaction_type,
                "amount": amount
            })

        result = process_transactions(transactions, balance)

        display_summary(result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# Run the program
if __name__ == "__main__":
    main()