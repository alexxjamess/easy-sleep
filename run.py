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
    which must be a number greater or to zero. 
    The loop will repeatedly request data unitl it is valid
    """
    while True:
        print(f'Please enter the total number of sales for {today}')
        print('Number of Sales Should be Greater Than or Equal to 0')
        print('Example: 0 OR 4 \n')

        data_str = input('Enter Todays Sales:\n')
        
        if validate_data(data_str):
            print("Data is valid!")
            break

    return data_str
    print(data_str)

def validate_data(data_str):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if the value is less than 0
    """
    try:
        data_sales = int(data_str) 
        if data_sales < 0:
            raise ValueError(
                f"Figure 0 or greater required, you provided {data_str}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter a valid number.\n")
        return False

    return True    

get_sale_data()