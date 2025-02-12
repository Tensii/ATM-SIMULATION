# ATM Simulation Project

## Overview
This project is a simulation of a basic ATM system built in Python. It allows users to perform essential banking operations such as checking their balance, withdrawing money, depositing funds, and changing their PIN. This project was created as part of a college assignment, with specific evaluation criteria focusing on code quality, functionality, usability, and documentation.

## Features
- **Balance Check**: View the current balance of the account.
- **Withdraw Money**: Withdraw a specified amount if there are sufficient funds.
- **Deposit Money**: Deposit funds into the account.
- **Change PIN**: Update the account PIN after verifying the current one.

## Project Structure
- **ATM Class (`atm.py`)**: Contains the core functionality of the ATM, including methods for balance checking, withdrawing, depositing, and changing PIN.
- **Main Function (`atm_menu`)**: Provides a user interface for the ATM, with a menu-driven loop for selecting different actions.

## Setup and Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tensii/ATM-SIMULATION.git
   cd ATM-SIMULATION
   ```

2. **Run the Program**:
   Make sure you have Python installed (Python 3.6 or higher recommended). Then, run the main script:
   ```bash
   python atm.py
   ```

## Usage
1. **Launch the Program**:
    After running the `atm.py` script, you will be asked to enter your pin. 
2. After entering the correct pin, you will see a menu with options.

3. **Select an Option**:
   - **Check Balance**: Press `1` to display the current balance.
   - **Withdraw Money**: Press `2` and enter an amount to withdraw.
   - **Deposit Money**: Press `3` and enter an amount to deposit.
   - **Change PIN**: Press `4`, then enter the current PIN followed by the new PIN.
   - **Exit**: Press `5` to exit the program.

### Example Run
- Start the program.
- Enter `1` to check the balance.
- Enter `2` to withdraw an amount.
- Enter `3` to deposit money.
- Enter `4` to change the PIN (enter the current and new PINs).
- Enter `5` to exit.

## Testing
Tests can be run for each core function, such as checking the balance, making withdrawals, deposits and changing the PIN. Unit tests can be added to ensure each function works as expected.

# ATM Simulation Unit Tests

This project includes a set of unit tests for the `ATM` class in `atm.py`. The `ATM` class simulates basic ATM operations, such as checking balance, withdrawing, depositing, and changing the PIN. The unit tests verify the functionality and correctness of each feature.

## Test Cases

The unit tests cover the following scenarios:

1. **Balance Inquiry**: Checking if the balance inquiry returns the correct balance.
2. **Withdrawals**:
   - Valid withdrawals that update the balance correctly.
   - Invalid withdrawals (e.g., insufficient funds or negative amounts).
3. **Deposits**:
   - Valid deposits that update the balance correctly.
   - Invalid deposits (e.g., negative or zero amounts).
4. **PIN Verification**:
   - Successful PIN verification.
   - Failed PIN verification with incorrect PIN entries.
5. **Change PIN**:
   - Successful PIN changes.
   - Failed PIN change attempts (e.g., incorrect current PIN or mismatched new PIN).

## Running the Tests

To execute the unit tests, navigate to the project directory in your terminal and use the following command:

```bash
python -m unittest test_atm.py
```

## Documentation
For detailed documentation of each function, see the code comments in `atm.py`. Each function includes explanations of:
- Parameters: Input values expected for each function.
- Return values: What each function returns to indicate success or failure.
- Conditions and edge cases handled within the code.

## Future Enhancements
- Add authentication for multiple users.
- Implement an account creation process.
- Improve the user interface for easier navigation.

## License
This project is open-source and available under the MIT License.
