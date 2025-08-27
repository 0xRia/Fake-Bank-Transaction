HIGH_AMOUNT_THRESHOLD = 1000000 #example thrreshold for high amounts

def is_fraudulent(transaction):

    """
    transaction is a dict with keys like:
    'amount' , 'account_from' , 'account_to' , etc.
    """

    amount = transaction.get('amount' , 0)
    known_accounts = {'12345938', '67890328', '54321640'} #example of known safe accounts

    #Rule 1: Flag high amount transactions
    if amount > HIGH_AMOUNT_THRESHOLD:
        return True, "High transaction amount"
    
    #Rule 2: Flag unknown transactions to unknown accounts
    if transaction.get('account_to') not in known_accounts:
        return True, "Unknown recipient account"
    
    return False, ""

