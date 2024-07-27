from pymongo import MongoClient
from bson import ObjectId
from getpass import getpass

try:
    # u_name = input("Enter the user name : ")
    # password = input("Enter the password : ")

    u_name = "bill_python"
    password = "bansi636363"

    con_str = f"mongodb+srv://{u_name}:{password}@cluster0.s6um6yc.mongodb.net/"
    client = MongoClient(con_str)
    print("Connection established...")



except Exception as e:
    print(e)


try:
    db = client['bill_system']
    # print(db)
    # print(type(db))
    collection = db["bill_collection"]
    # print(collection)

except Exception as e:
    print(e)

def insert(c_name,Item_name,quantity,price,total_amount,loc):
    try:
        collection.insert_one({"Customer_Name" : c_name,"Item_name" : Item_name,"Quantity" : quantity,"Price" : price,"Total_Amount" : total_amount,"Location" : loc})
        print("Data inserted successfully....")
    except Exception as e:
        print(e)

def display():
    try:
        for i in collection.find():            
            # print(f"ID : {i['_id']} | Customer Name : {i['Customer_Name']} | Item Name : {i['Item_name']} | Quantity : {i['Quantity']} | Price : {i['Price']} | Total : {i['Total_Amount']} | Location : {i['Location']}")
            print(f"ID: {i.get('_id')} | Customer Name: {i.get('Customer_Name')} | Item Name: {i.get('Item_name')} | Quantity: {i.get('Quantity')} | Price: {i.get('Price')} | Total: {i.get('Total_Amount')} | Location: {i.get('Location')}")
            #.get is used for get the value of dict. If the key "model" does not exist in the dictionary, it will return None by default. 

    except Exception as e:
        print("Display error ..." , e)


def update(Id):
    try:
        print("Enter what would you update..")
        print("*" * 50)
        print("1. Customer name")
        print("2. Item name ")
        print("3. Quantity")
        print("4. price")
        print("*" * 50)

        ch = int(input("Enter your choice : "))
        print("*" * 50)

        match ch:
            case 1:
                new_name = input("Enter new name : ")
                collection.update_one({'_id' : ObjectId(Id)} , {"$set" : {'Customer_Name' : new_name}})
            case 2:
                new_item = input("Enter new item name :")
                collection.update_one({'_id' : ObjectId(Id)} , {'$set' : {'Item_name' : new_item}})
            case 3:
                new_q = int(input("Enter new Quantity"))
                item = collection.find_one({'_id' : ObjectId(Id)})  #it find the product collection details using Id
                price = item['Price']  #it fetch the price using the item and display item price 
                collection.update_one({'_id' : ObjectId(Id)} , {'$set' : {'Quantity' : new_q,'Price' : new_q*price}})
            case 4:
                new_price = float(input("Enter new updated price :"))
                item = collection.find_one({'_id' : ObjectId(Id)})
                qty = item['Quantity']
                # print("Item :" , item)
                # print("Quantity : " , item['Quantity'])
                collection.update_one({'_id' : ObjectId(Id)} , {'$set' : {'Price' : new_price,'Total_Amount' : new_price*qty}})
            case _:
                print("Invalid choice...")
    except Exception as e:
        print("Update error..",e)


def delete(Id):
    try:
        collection.delete_one({'_id' : ObjectId(Id)})
        print("Record deleted successfully....")
    except Exception as e:
        print("Deleting error...",e)







def main():
    while True:
        print("-" * 50)
        print("*" * 50)

        print("1. Insert data in System ")
        print("2. Display data from System ")
        print("3. Update data from System ")
        print("4. Delete data from System ")
        print("5. Break")
        print("-" * 50)

        ch = int(input("Enter yout choice :"))

        match ch:
            case 1:
                c_name = input("Enter the name of Customer :")
                I_name = input("Enter the name of item :")
                quantity = int(input("Enter the Quantity of item :"))
                price = float(input("Enter the price of Item :"))
                location = input("Enter the location :")
                total = quantity * price
                insert(c_name,I_name,quantity,price,total,location)

            case 2:
                display()

            case 3:
                id = input("Enter the product id : ")
                update(id)

            case 4:
                id = input("Enter id of record which you delete : ")
                delete(id)

            case 5:
                break

            case _ :
                print("Invalid Choice...")



if __name__ == "__main__":
    main()

            


