import pyautogui #Libraty to autocontrol computer
import time #Library to control time
import pandas #Library to work with data

pyautogui.PAUSE = 0.4 # Pause between commands

pyautogui.press('win') # Press the Win key
pyautogui.write('chrome') # Write the word chrome
pyautogui.press('enter') # Press the Enter key, opening Chrome

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') # Write the URL
pyautogui.press('enter') # Press the Enter key, opening the URL

time.sleep(2) # Wait the website open

# Doing the login

pyautogui.click(x=779, y=477) # Click on the email field
pyautogui.write('leandrocs1500@gmail.com') # Write the email
pyautogui.press('tab') # Press the Tab key
pyautogui.write('flamengoo') # Write the password
pyautogui.press('enter') # Press the Enter key

time.sleep(2) # Wait the website open

table = pandas.read_csv('produtos.csv') # Read the CSV file

for index, row in table.iterrows(): # Loop to get the items in the table
     pyautogui.click(x=664, y=326) # Click on the button to start the course
     pyautogui.write(str(row["codigo"])) # Get the item and write it
     pyautogui.press('tab') # Press the Tab key

     pyautogui.write(str(row["marca"])) # Write the brand
     pyautogui.press('tab') # Press the Tab key

     pyautogui.write(str(row["tipo"])) # Write the type
     pyautogui.press('tab') # Press the Tab key

     pyautogui.write(str(row["categoria"])) # Write the category
     pyautogui.press('tab') # Press the Tab key

     pyautogui.write(str(row["preco_unitario"])) # Write the price
     pyautogui.press('tab') # Press the Tab key

     pyautogui.write(str(row["custo"])) # Write the cost
     pyautogui.press('tab') # Press the Tab key

     obs = str(row["obs"])
     if obs != 'nan': # Check if the observation is not empty
          pyautogui.write(obs) # Write the observation

     pyautogui.press('enter') # Press the Enter key

     pyautogui.click(x=1650, y=484) # Click on the background to use home key
     pyautogui.press('home') # Press the Home key (go to the top of the page)
     #pyautogui.scroll(5000) # Scroll the page