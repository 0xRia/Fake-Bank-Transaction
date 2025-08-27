def log_transaction(amount, receiver, reason):
    with open("transactions.csv", "a") as f:
        f.write(f"{amount}, {receiver}, {reason}\n")