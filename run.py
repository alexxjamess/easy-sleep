import gspread
from google.oauth2.service_account import Credentials
from datetime import date


SCOPE = [
  "https://www.googleapis.com/auth/spreadsheets",
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('easysleep')


def get_sale_data():
    """
    Get daily sales total from user.
    Run a while loop to collect a valid data string via the the terminal,
    which must be a number greater or equal to zero.
    The loop will repeatedly request data unitl it is valid
    """

    while True:
        print(f'Please enter the total number of sales for {str(date.today())}')
        print('Number of Sales Should be Greater Than or Equal to 0')
        print('Example: 0 OR 4 \n')

        data_str = input('Enter Todays Sales:\n')

        sales_data = data_str

        if validate_data(sales_data):
            print("Data is valid!\n")
            return sales_data


def validate_data(sales_data):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if the value is less than 0
    """
    try:
        data_sales = int(sales_data)
        if data_sales < 0:
            raise ValueError(
                f"Figure 0 or greater required, you provided {sales_data}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter a valid number.\n")
        return False

    return True



def get_advertising_data():
    """
    Get daily Advertising total from user.
    Run a while loop to collect a valid data string via the the terminal,
    which must be a number greater or equal to zeroand less than 175.
    The loop will repeatedly request data unitl it is valid
    """
    while True:
        print(f'Please enter the total advertising cost for {str(date.today())}')
        print('Number of Advertising Cost Should be Greater Than or Equal to 0 and Less than 175')
        print('Example: 50 OR 153 \n')

        data_str_advertising = input('Enter Todays Total Advertising Cost:\n')

        if validate_data_adverstising(data_str_advertising):
            print("Data is valid!\n")
            return data_str_advertising


def validate_data_adverstising(data_str_advertising):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if the value is less than 0 and geater than 175
    """
    try:
        data_adverstising = int(data_str_advertising)
        if data_adverstising > 175 or data_adverstising < 0:
            raise ValueError(
                f"Figure greater than 0 and less than 175 required, you provided {data_str_advertising}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter a valid number.\n")
        return False

    return True


def get_price_data():
    """
    Get daily Price from user.
    Run a while loop to collect a valid data string via the the terminal,
    which must be a number greater or equal to 28.99 and less than 33.99.
    The loop will repeatedly request data unitl it is valid
    """
    while True:
        print(f'Please enter the Sale Price for {str(date.today())}')
        print('Price Should be Greater Than or Equal to 28.99 and Less than 33.99')
        print('Example: 29.99 OR 31.99 \n')

        data_str_price = input('Enter Todays Sale Price:\n')

        if validate_data_price(data_str_price):
            print("Data is valid!\n")
            return data_str_price


def calculate_acos(sale_data, adv_data, price_data):
    """ This function retrieves user inputs converts them to an interger or float
     and then preforms a calculation to work out ACOS
     Which is (Advertsing Cost/No of Sales)/Sale Price
     """
    acos_data = float((int(adv_data) / int(sale_data)) / float(price_data))
    return acos_data

def validate_data_price(data_str_price):
    """
    Inside the try, converts all string values into float.
    Raises ValueError if strings cannot be converted into float,
    or if the value is less than 28.99 and geater than 33.99
    """
    try:
        data_price = float(data_str_price)
        if data_price > 33.99 or data_price < 28.99 :
            raise ValueError(
                f"Figure greater than or equal to 28.99 and less than 33.99 required, you provided {data_str_price}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter a valid number.\n")
        return False

    return True

def capture_data():
    """ Function to collect all data to return so it can be added to spreadsheet"""
    today_data = str(date.today())
    sale_data = get_sale_data()
    adv_data = get_advertising_data()
    price_data = get_price_data()
    acos_data = calculate_acos(sale_data, adv_data, price_data)
    return [today_data, sale_data, price_data, adv_data,acos_data]
    choice

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

def get_daily_summary():
    """ This function will get the last row of the table and return it
    it will then print the results to the terminal for the users to see
    """
    print("Getting Daily Summary...\n")
    sales_total = SHEET.worksheet("sales").get_all_values()
    sales_daily = sales_total[-1]
    print(f'Here is your daily Summary for {sales_daily[0]}\n Total Daily Sales:{sales_daily[1]}\n Total Adversiting Cost Today:£{sales_daily[3]}\n Price Per Unit £{sales_daily[2]}\n Todays ACOS {sales_daily[4]}\n Reccomended Monthly Order Quantity{sales_daily[5]}')
    choice


def print_all_data():
    all_sales_data = SHEET.worksheet("sales").get_all_values()
    for each_entry in all_sales_data:
            print(f'{each_entry[0]}\n Total Daily Sales:{each_entry[1]}\n Total Adversiting Cost Today:£{each_entry[3]}\n Price Per Unit £{each_entry[2]}\n Todays ACOS {each_entry[4]}\n Reccomended Monthly Order Quantity{each_entry[5]}')
    
print("To Enter Daily Data Select A")
print("To get the last daily summary select B")
print("To View all Data select C")
choice = str(input("Enter choice: A/B/C:"))

if choice == "A":
    data = capture_data()
    update_sales_worksheet(data)
elif choice == "B":
    get_daily_summary()
elif choice == "C":
    print_all_data()
    
def main():
    """
    Run all program functions
    """
    data = capture_data()
    update_sales_worksheet(data)
    get_daily_summary()

