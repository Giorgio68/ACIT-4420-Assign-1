# ACIT4420 Assignment 1

## Task A

## Task B

Seeing as most bank accounts have similar functions, allowing the user to withdraw and deposit cash, it was worth using inheritance to avoid rewriting the same code multiple times. A base `BankAccount` class was written with a constructor, a method to deposit money, one to withdraw it, and finally a way to get account information, in the form of a string containing the account holder and balance.

As a checking account has a fee for withdrawals, the base `withdraw` method is overridden, to add the fee to the requested amount; this value is then passed to the base `withdraw` method by calling `super()`.

The savings account remains the same as the base class, except for a new method to apply interest. This will simply multiply the current balance by 1.025, effectively adding an interest of 2.5% on the balance.

One change that was done compared to the original `BankAccount` class was to return the available balance from the `deposit` and `withdraw` methods, allowing to test the code programmatically and using assertions, rather than having to look at a console output; a new method was also added to return the available balance, for the same reason.

Additionally, both the transaction fee for the checking account and the interest rate for the savings account were created as class members rather than instance members; the reason for this choice is that generally these tend to be the same for all accounts, which means that it can make sense that it should be the same object for all instances.

A series of test cases were written to demonstrate and test the functionality of the three classes, such as testing that depositing and withdrawing money works as expected, and for checking and savings accounts respectively, that the transaction fee is also subtracted from the balance and that the interest rate is applied correctly. Assertions were used during tests, easily allowing a tester to see whether a test has failed or all have succeeded.
