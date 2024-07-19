# count number of row and columns
#  read specific row and column data
# read all the rows and columns data
# read dat based on conditions

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

noOfRows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
noOfCols = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
print(len(noOfRows))
print(len(noOfCols))

# read speciffic row and column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

# read all the  rows and columns data
print("printing all the rows and columns data ............")

for r in range(2, len(noOfRows)+1):
    for c in range(1,len(noOfCols)+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end='   ')
    print()

# read data based on condition
for r in range(2, len(noOfRows)+1):
    authName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authName=="Mukesh":
        bookName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text

        print(bookName,"    ",authName," ",price)
