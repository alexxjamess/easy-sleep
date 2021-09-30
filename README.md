![EASY SLEEP LOGO](./assets/images/easysleep-logo.jpg)

## About EasySeep

EasySleep is a brand that sells temporary blackout blinds, they sell their products on amazon but plan to sell on thier own using their own system to check stock sales etc.
![EASY SLEEP Mockup ](./assets/images/easy-sleep-mockup.jpg)
## Uses

* This will allow the user to enter data via a terminal and it get inputted into a spreadsheet.
* It will allow the the user to retrieve calculation based on their input
* It will return a customer a daily summary for the user to see on the terminal

## How to Use 

* Run the run.py file
* Choose an option from A,B,C depending if you want to enter data, get the last summary, or all data
### Option A
* Input the total number of daily sales
* Next Imput the total advertising cost for that day
* Finally Input the price per unit that day
* System will calculate acos and order quantity an update spreadsheet
* The user will be then prompted to contiue or end.
### Option B
* Will show the previous days summary 
* The user will be then prompted to continue or end.
### Option C
* Will show all the data in the spreadsheet
* The user will be then prompted to continue or end.

## Features 

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:
### Validation 
#### Daily Sales Input 
* The Input for Daily Sales will have validation that makes sure the information can be turned into an integer if not will return an error
* The Input for Daily Sales will also have a validation that only lets the user enter a number greater or equal to zero 
 #### Daily Advertising Input 
* The Input for Daily Advertising will have validation that makes sure the information can be turned into an integer if not will return an error
* The Input for Daily Advertising will also have a validation that only lets the user enter a number greater than zero and less than 175 as this the maximum budget for advertising per day
#### Daily Price Input 
* The Input for Price will have validation that makes sure the information can be turned into an Float if not will return an error
* The Input for Price Sales will also have a validation that only lets the user enter a number greater than 28.99 and less than 33.99 as this is the price range that the product sells depending on demand.
### Calculations 
* Once information has been inputted by user and all has been comfirmed and valid the function will calculate the ACOS based on the figures provided
* Once information has been inputted by user and all has been comfirmed and valid the function will calculate the Reccomeneded Order Quantity based on the figures provided
### Information Return
* The functions will then return a 'Daily Summary' in the terminal of the inputted calculations as well as the calulations 
* The user can also access all data in the spreadsheet using terminal
### API Spreasheet Update
* The spreasheet will get updated with user inputed data and calculations
### Choice
* The user will be given a choice on what they wish do to, enter data or view
* The user will be given a choice on if they would like to continue or not 

## Testing 
### Sales Input Function and Validation
* The Fuction should request the an input from the user and return "Data is valid" and continue to the next input.

![Test 1 Sales Iput](./assets/images/sales-input-test-1.jpg)

* The function works Correctly when valid data is entered
* The validation should return errors when invalid data such as a something that can not be turned into an interger or a number outside the range. The function should also then request the user to re-enter valid data so the function does not end.

![Test 2 Sales Iput](./assets/images/sales-input-test-2.jpg)

* The validation works correctly when data that cant be changed into an integer is entered, returning an error and asking the user to input correct data.

![Test 3 Sales Iput](./assets/images/sales-input-test-3.jpg)

* The validation works correctly when data that is below zero is entered, showing an error and asking user to pinput valid data 
### Advertising Input Function and Validation
* The Fuction should request the an input from the user and return "Data is valid" and continue to the next input.

![Test 1 Advertising Iput](./assets/images/advertising-input-test-1.jpg)

* The function works Correctly when valid data is entered
* The validation should return errors when invalid data such as a something that can not be turned into an interger or a number outside the range. The function should also then request the user to re-enter valid data so the function does not end.

![Test 2 Advertising Iput](./assets/images/advertising-input-test-2.jpg)

* The validation works correctly when data that cant be changed into an integer is entered, returning an error and asking the user to input correct data.

![Test 3 Advertising Iput](./assets/images/advertising-input-test-3.jpg)

* The validation works correctly when data that is below 0 or above 175 returning error and requesting the data to be entered again 

### Sale Price Input Function and Validation
* The validation works correctly when valid data is entered
* The validation shows a error if the number is not a float or if it out of the range of the selling price of 28.99 and 33.99

### Choice 1
* Choice 1 will allow the users to pick A,B,C depending on their requirement, if the user enters not one of these three Letter the program will ask if the user wants continue with a Y/N.
* This function works correctly, All options bring up correct scenario when chosen as expected.
### Choice 2
* Choice 2 is a Y/N if the customer would like to continue, if the user selects Y the user will be taken back to the start of choice 1 if they select N the program will end 
* This function works correctly, both options works correctly.

### Spreadsheet Update
* Once user inputs all data calculation are preformed and added to spreadhseet, the spreadsheet updates succesfully

### Calculations 
#### Calculate Acos
* The acos calulation will take the figures inputted and use the formula Advertising (Total/Daily Sales) / Sale Price This function works correctly
#### Calculate Reccomended Order Quanitiy
* The inital idea was to use google sheets to calculate this, however google sheets does not have the capacity to enter a formula when a new line is written.
* The next step was to create a python code that counted the added the sales of each day up and devided them by the number of rows, however due to time constraints i was unable to get this to work.
* Therefore a simple calculations which takes the daily sales * 365 / 12 was used instead./ This calculation works correctly.

### Data Retrieval 
* Option B will allow the user to retrieve the data for the last day if they have not entered any data or the current day if they have already entered the data.
* This works correctly and shows in a readable format.
* Option C will allow the user to retrieve all the data from the spreadsheet in a readable format.
* This works correctly.

### Validator Testing
* When running the code through PEP8 http://pep8online.com/
* There were 11 errors all indication the line were to long
* I was unable to change this without comprimising my code, however this does not seem to effect the proram.

![Test PEP8 ](./assets/images/pep8-validator-test.jpg)

## Spreadsheet 
Link to spreadsheet https://docs.google.com/spreadsheets/d/1PdROOvZJ8ri_ZWFjpySQprSaOuknZzx5k9gvUY064fI/edit?usp=sharing

## Deployment
The project was deployed using Code Institutes mock terminal for Heroku https://easy-sleep.herokuapp.com
* Steps for Deployment
    * create a new Heroku App
    * add creds.json to config vars
    * Set buildbacks to Python and Node.js in that order
    * link the Heroku app to the repository 
    * click automatic deploy