import requests
import json

def get_exchange_rate(base_currency, target_currency):
    """Get current exchange rate from Frankfurter API"""
    try:
        url = f"https://api.frankfurter.app/latest?from={base_currency}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()
        return data['rates'].get(target_currency)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def currency_converter():
    print("Welcome to Currency Converter")
    print("Enter currency codes in uppercase (e.g., INR, EUR)")
    
    try:
        # Get user input
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("From currency (3-letter code): ").upper()
        to_currency = input("To currency (3-letter code): ").upper()
        
        if len(from_currency) != 3 or len(to_currency) != 3:
            raise ValueError("Currency codes must be 3 letters long")
        
        # Get exchange rate
        rate = get_exchange_rate(from_currency, to_currency)
        
        if rate is None:
            print(f"Could not get exchange rate for {from_currency} to {to_currency}")
            print("Please check your internet connection and currency codes")
            return
        
        # Calculate and display result
        converted_amount = amount * rate
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        print(f"Exchange rate: 1 {from_currency} = {rate:.4f} {to_currency}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    currency_converter()
    input("\nPress Enter to exit...")