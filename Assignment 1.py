#Keegan Gratton
#INFR 2820U
import time
import sys

#Array to store products
products = []


#Bubble sort by ID number from lowest to highest. Used code from Lecture 2
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]['ID'] > arr[j+1]['ID']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

#Bubble sort by ID number from highest to lowest. Modified code from Lecture 2
def bubbleSortWorstCase(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]['ID'] < arr[j+1]['ID']:  
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

#Analyze sorting performace time. Used code from Lecture 2
def analyzeSortPerformance(data, description, time_complexity):
    
    data = []
    start = time.time()
    #Uses the Bubble sort method
    bubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    #productDisplay(data)
    print(f"Time Complexity: {time_complexity}\n")
    
    
#Functiuon to add new product to array
def addNewProduct(ID,Name,Price,Category):
    product = {
        'ID': ID,
        'Name': Name,
        'Price': float(Price),
        'Category': Category
        }
    products.append(product)

#Function to inport from a txt or csv file
def fileImport(file_name):
    # Read the file and split each line
    with open(file_name, 'r') as file:
        for line in file:
            id, name, price, category = line.strip().split(',')
            addNewProduct(id, name, price, category)
                          
#Displays the array in a clean display
def productDisplay(displayList):
    print("Product inventory")
    for displayList in products:
        print(f"ID: {displayList['ID']}")
        print(f"Name: {displayList['Name']}")
        print(f"Price: ${displayList['Price']:.2f}")
        print(f"Category: {displayList['Category']}")
        print("-" * 30) 

def displayProductByID(product_id):
    found_product = None
    for product in products:
        if product['ID'] == product_id:
            found_product = product
            break

    if found_product:
        print("\nProduct Details")
        print(f"ID: {found_product['ID']}")
        print(f"Name: {found_product['Name']}")
        print(f"Price: ${found_product['Price']:.2f}")
        print(f"Category: {found_product['Category']}")
        print("-" * 30)
    else:
        print(f"No product found with ID {product_id}")


#Update the data in a array by selecting it with the ID number
def updateProduct():
    itemToUpdate = input("Enter the item ID you want to update: ")
    found = False
    for product in products:
        if product['ID'] == itemToUpdate:
            found = True
            print("1. Update Name")
            print("2. Update Price")
            print("3. Update Category")
            print("4. Exit")
            updateSelection = input("What would you like to update? ")
            if updateSelection == "1":
                new_name = input("Enter the new name: ")
                product['Name'] = new_name
            elif updateSelection == "2":
                new_price = float(input("Enter the new price: "))
                product['Price'] = new_price
            elif updateSelection == "3":
                new_category = input("Enter the new category: ")
                product['Category'] = new_category
            elif updateSelection == "4":
                break
            else:
                print("Invalid selection. Please try again.")
    if not found:
        print(f"Product with ID {itemToUpdate} not found.")

#Delete product using the ID number
def deleteProduct():
    itemToDelete = input("Enter the item ID you want to delete: ")
    found = False
    for product in products:
        if product['ID'] == itemToDelete:
            found = True
            products.remove(product)
            print(f"Product with ID {itemToDelete} has been deleted.")
            break  # Exit the loop once the product is found
    if not found:
        print(f"Product with ID {itemToDelete} not found.")

    
#Selection screen runs in loop
def selectionScreen():
    print("\nWould you like to:\n1.Import from a file\n2.Input manually\n3.Show inventory\n4.Update product\n5.Sort by Product ID and show time complexaity\n6.Delete a product\n7.Search for a product by ID\nQ.Exit\n")
    usrSeleciton = input("Enter the selction 1-7, or Q: ")

    if usrSeleciton == "1":
        fileImport(input("Provide the absolute file path: "))
    elif usrSeleciton == "2":
        addNewProduct(input("What's the ID Number:"),input("Whats the Name of product: "),float(input("What's the price of item: ")),input("What's the category: "))
    elif usrSeleciton == "3":
        productDisplay(bubbleSort(products))
        
    elif usrSeleciton == "4":
        updateProduct()
    elif usrSeleciton == "5":
        analyzeSortPerformance(products, "Original Data", "O(n^2)")
        analyzeSortPerformance(bubbleSort(products), "Best Case (Sorted)", "O(n)")
        analyzeSortPerformance(bubbleSortWorstCase(products), "Worst Case (Reverse Sorted)", "O(n^2)")
    elif usrSeleciton == "6":
        deleteProduct()
    elif usrSeleciton == "7":
        displayProductByID(input("Please enter an ID number to search: "))
    elif usrSeleciton == "Q":
        exit()
    else: 
        print("Not valid")
        
run = True
while run == True:
    selectionScreen()
