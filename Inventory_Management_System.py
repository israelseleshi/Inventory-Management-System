# *****************************************************
# INVENTORY MANAGEMENT SYSTEM
# ****************************************************

# *****************************************************
class Item:
# *****************************************************



# *****************************************************
  # CONSTRUCTOR
# *****************************************************
  def __init__(self, id, name, category, quantity, price):
    self.id = id
    self.name = name
    self.category = category
    self.quantity = quantity
    self.price = price
# *****************************************************





# *****************************************************
  # to_dict() method
# *****************************************************
  def __str__(self):
    return {
      "id" : self.id,
      "name" : self.name,
      "category" : self.category,
      "quantity" : self.quantity,
      "price" : self.price,
    }
# *****************************************************
  




# *****************************************************
  # add_item(items) method
# *****************************************************
def add_item(items):
  
  id = len(items) + 1

  name = input("Enter item name: ")
  category = input("Enter item category: ")
  quantity = int(input("Enter item quantity: "))
  price = float(input("Enter item price: "))

  new_item = Item(id, name, category, quantity, price)
  items.append(new_item)
  print("Item added successfully!")
# *****************************************************

  



# *****************************************************
  # view_items(items) method
# *****************************************************
def view_items(items):

  sorted_items = sorted(items, key = lambda x: (x.category, x.name))

  for item in sorted_items:
    print(f"ID = {item.id}, Name = {item.name}, Category = {item.category}, Quantity = {item.quantity}, Price = {item.price}")
# *****************************************************
    




# *****************************************************
  # update_item(items) method
# *****************************************************
def update_item(items):

  id = int(input("Enter the ID of the item to update: "))
  item = next((item for item in items if id == items.id), None)
  
  if item:
    item.name = input("Enter the new item name: ")
    item.category = input("Enter the new item category: ")
    item.quantity = int(input("Enter the new item quantity: "))
    item.price = float(input("Enter the new item price: "))
    print("Item updated successfully!")
  else:
    print("Item not found!")

# *****************************************************
  




# *****************************************************
  # delete_item(items) method
# *****************************************************
def delete_item(self, items):
  
  id = int(input("Enter the ID of the item to delete: "))
  item = next(item for item in items if id == items.id)
  if item:
    items.remove(item)
    print(f"Item with {id} deleted successfully!")
  else:
    print(f"Item with ID {id} is not found.")
# *****************************************************





# *****************************************************
  # main() method
# *****************************************************

def main():

  items = []

  while True:

    print("\nInventory Management System")
    print("1. Add an Item")
    print("2. View Items")
    print("3. Update an Item")
    print("4. Delete an Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      add_item(items)

    elif choice == '2':
      view_items(items)

    elif choice == '3':
      update_item(items)

    elif choice == '4':
      delete_item(items)

    elif choice == '5':
      break
    
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()