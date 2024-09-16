"""
ACIT 4420, Assignment 1, Task B

Giorgio Salvemini
"""


class BankAccount:
    """
    Base class for creating bank accounts. Initializes balance to 0

    :param account_holder: The name of the account owner
    """

    def __init__(self, account_holder: str) -> None:
        """
        Constructor method
        """
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount: float) -> float:
        """
        Adds an amount to the user's balance

        :param amount: The amount to be added
        :return: The updated balance
        """
        self.balance += amount

        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Subtracts an amount from the user's balance, or prints an error if the requested amount is
        higher than the available balance

        :param amount: The amount to withdraw
        :return: The updated balance, or -1 if the balance is insufficient
        """
        if amount <= self.balance:
            self.balance -= amount
            return self.balance

        print("Insufficient funds")
        return -1

    def balance_info(self) -> float:
        """
        Return the current balance

        :return: The current balance
        """
        return self.balance

    def account_info(self) -> str:
        """
        Returns a string containing the account holder's name and balance
        """
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"


class CheckingAccount(BankAccount):
    """
    Class for checking accounts, inheriting from a base bank account. Adds a transaction fee to
    all withdrawals

    :param account_holder: The name of the account owner
    """

    transaction_fee: float = 2.5  # usd

    def withdraw(self, amount: float) -> float:
        """
        Overrides the base `withdraw` method. Adds a transaction fee to the requested amount

        :return: The updated balance
        """
        return super().withdraw(amount + self.transaction_fee)


class SavingsAccount(BankAccount):
    """
    Class for savings accounts, inheriting from a base bank account. Allows to apply interest to
    the available balance

    :param account_holder: The name of the account owner
    """

    interest_rate: float = 0.025  # 2.5%

    def apply_interest(self) -> float:
        """
        Applies the interest rate to the chosen

        :return: The updated balance
        """
        self.balance *= 1 + self.interest_rate

        return self.balance


def test_base() -> None:
    print(
        """
*************************
Testing base bank account
*************************
"""
    )
    bank_account = BankAccount("Giorgio")
    print(bank_account.account_info())

    # basic functionality test
    assert bank_account.deposit(1000) == 1000
    print(bank_account.account_info())

    assert bank_account.withdraw(500) == 500
    print(bank_account.account_info())

    assert bank_account.withdraw(500) == 0
    print(bank_account.account_info())

    assert bank_account.withdraw(500) == -1  # this should error out

    try:
        bank_account.deposit("a")
    except TypeError as e:
        print(repr(e))
        print("Cannot deposit a string to the balance")

    try:
        bank_account.withdraw("a")
    except TypeError as e:
        print(repr(e))
        print("Cannot withdraw a string from the balance")

    print(
        """
****************************
Base bank account tests done
****************************
"""
    )


def test_checking() -> None:
    print(
        """
************************
Testing checking account
************************
"""
    )
    checking_account = CheckingAccount("Giorgio")

    assert checking_account.deposit(1000) == 1000
    print(checking_account.account_info())

    assert checking_account.withdraw(500) == 500 - 2.5  # subtract the transaction fee
    print(checking_account.account_info())

    assert (
        checking_account.withdraw(500) == -1
    )  # this should error out since there's less than 500

    try:
        checking_account.withdraw("a")
    except TypeError as e:
        print(repr(e))
        print("Cannot withdraw a string from the balance")

    print(
        """
********************************
Base checking account tests done
********************************
"""
    )


def test_savings() -> None:
    print(
        """
***********************
Testing savings account
***********************
"""
    )
    savings_account = SavingsAccount("Giorgio")

    assert savings_account.deposit(1000) == 1000
    print(savings_account.account_info())

    assert savings_account.apply_interest() == 1025  # 1000*(1 + 0.025)
    print(savings_account.account_info())

    print(
        """
*******************************
Base savings account tests done
*******************************
"""
    )


def main() -> None:
    test_base()
    test_checking()
    test_savings()


if __name__ == "__main__":
    main()
