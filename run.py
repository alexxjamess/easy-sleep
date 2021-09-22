import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('easysleep')

from datetime import date
today = str(date.today())


def get_sale_data():
    """
    Get daily sales total from user.
    Run a while loop to collect a valid data string via the the terminal, 
    which must be a number greater or equal to zero. 
    The loop will repeatedly request data unitl it is valid
    """
    while True:
        print(f'Please enter the total number of sales for {today}')
        print('Number of Sales Should be Greater Than or Equal to 0')
        print('Example: 0 OR 4 \n')

        data_str = input('Enter Todays Sales:\n')

        sales_data = data_str
        
        if validate_data(sales_data):
            print("Data is valid!\n")
            break

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

get_sale_data()


def get_advertising_data():
    """
    Get daily Advertising total from user.
    Run a while loop to collect a valid data string via the the terminal, 
    which must be a number greater or equal to zeroand less than 175. 
    The loop will repeatedly request data unitl it is valid
    """
    while True:
        print(f'Please enter the total advertising cost for {today}')
        print('Number of Advertising Cost Should be Greater Than or Equal to 0 and Less than 175')
        print('Example: 50 OR 153 \n')

        data_str_advertising = input('Enter Todays Total Advertising Cost:\n')
        
        if validate_data_adverstising(data_str_advertising):
            print("Data is valid!\n")
            break

    return data_str_advertising
    

def validate_data_adverstising(data_str_advertising):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if the value is less than 0 and geater than 175
    """
    try:
        data_adverstising = int(data_str_advertising) 
        if data_adverstising > 175:
            raise ValueError(
                f"Figure greater than 0 and less than 175 required, you provided {data_str_advertising}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter a valid number.\n")
        return False

    return True   

get_advertising_data()

def get_price_data():
    """
    Get daily Price from user.
    Run a while loop to collect a valid data string via the the terminal, 
    which must be a number greater or equal to 28.99 and less than 33.99. 
    The loop will repeatedly request data unitl it is valid
    """
    while True:
        print(f'Please enter the Sale Price for {today}')
        print('Price Should be Greater Than or Equal to 29.99 and Less than 33.99')
        print('Example: 29.99 OR 31.99 \n')

        data_str_price = input('Enter Todays Sale Price:\n')
        
        if validate_data_price(data_str_price):
            print("Data is valid!\n")
            break

    return data_str_price
    

def validate_data_price(data_str_price):
    """
    Inside the try, converts all string values into float.
    Raises ValueError if strings cannot be converted into float,
    or if the value is less than 28.99 and geater than 33.99
    """
    try:
        data_price = float(data_str_price) 
        if data_price > 33.99:
            raise ValueError(
                f"Figure greater than or equal to 28.99 and less than 33.99 required, you provided {data_str_price}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter a valid number.\n")
        return False

    return True   

get_price_data()

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


update_sales_worksheet(sales_data) 

