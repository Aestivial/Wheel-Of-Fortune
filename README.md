# Wheel-Of-Fortune
A GUI based program made using Tkinter and Python3 to randomly pull prize items from a given file containing the prize item list.

![image](https://user-images.githubusercontent.com/69592060/198697938-4707eb02-ab6c-4406-985a-40988f68a592.png)

In this simple GUI window, the "Start" button initiates the iteration of the prizes and randomly lands on a prize item after the end of the flow. The screen switches colour in order to indicate the final prize received by the user. The user can use the "Start" button again to restart the process.
The "Stop" button can be utilized to kill the GUI and close the running program.

The fetching of data for the prize items is carried out in two ways:
  #1. Using a simple text file where each line indicates a prize item. It is for simpler and faster pulling of data as text.
  ![image](https://user-images.githubusercontent.com/69592060/194707348-264901b5-71ff-4ef9-bd58-5f645ccedc93.png)

  #2. Using an excel file with a sheet containing a column with prize item records. It is helpful for better standalone presentation of data items.
  ![image](https://user-images.githubusercontent.com/69592060/194707368-9ce99bc1-18c8-4897-b676-0e25b0a1ffdc.png)

[ UPDATE ]
Now the updated GUI also supports adding new prizes to the existing list in the excel sheet. At one time, a user may enter n number of prizes and have it dumped in the ListOfPrizes.xlsx file via the program.
![image](https://user-images.githubusercontent.com/69592060/198699210-0e3007b1-f50b-49d9-bf71-c429c20fd342.png)

Selecting the "Add New Items" option prompts the user with a new window where new items can be added in separate lines. The new items are then added to the existing database.
