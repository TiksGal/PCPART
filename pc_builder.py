from database import Database
import inspect
from pc_parts import CPU, CPUCooler, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply, OperatingSystem, Monitor

class PCBuilder:
    def __init__(self, database: Database):
        self.database = database
        self.category_mapping = {
            "CPUs": CPU,
            "CPU_Coolers": CPUCooler,
            "Motherboard": Motherboard,
            "Memory": Memory,
            "Storage": Storage,
            "VideoCard": VideoCard,
            "Case": Case,
            "PowerSupply": PowerSupply,
            "OperatingSystem": OperatingSystem,
            "Monitor": Monitor    
        }

    def start(self):
        while True:
            print("\n1. See all items")
            print("2. Add an item")
            print("3. Delete an item")
            print("4. See total price")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.print_all_items()
            elif choice == '2':
                self.add_item()
            elif choice == '3':
                self.delete_item()
            elif choice == '4':
                self.print_total_price()
            elif choice == '5':
                break
            else:
                print("Invalid option")

    def print_all_items(self):
        for category, items in self.database.db.items():
            print(f'\n{category}:')
            for item in items:
                print(item.get_info())  # Abstraction: only print necessary info to the user

    def add_item(self):
        category = input("Enter the category of the item you want to add: ")

        # Check if the category exists in the mapping
        if category in self.category_mapping:
            pc_part_class = self.category_mapping[category]

            # Get the constructor parameters of the PCPart subclass
            params = inspect.signature(pc_part_class).parameters

            # Prompt the user to enter details for each parameter
            kwargs = {}
            for param in params.values():
                if param.name == 'self':
                    continue  # Skip 'self' parameter
                if param.default == inspect.Parameter.empty:
                    value = input(f"Enter the {param.name} of the {category}: ")
                else:
                    value = input(f"Enter the {param.name} of the {category} (leave blank for default '{param.default}'): ")
                    if not value:
                        value = param.default
                kwargs[param.name] = value

            # Create the PCPart instance with the collected details
            item = pc_part_class(**kwargs)
            self.database.add_item(category, item)
        else:
            print("Invalid category")


    def delete_item(self):
        category = input("Enter the category of the item you want to delete: ")
        item_name = input("Enter the name of the item you want to delete: ")

        # Find the item in the specified category by its name
        item_to_delete = None
        for item in self.database.get_items(category):
            if item.get_name() == item_name:
                item_to_delete = item
                break

        if item_to_delete:
            self.database.delete_item(category, item_to_delete)
        else:
            print(f"Item '{item_name}' does not exist in category '{category}'.")

    def print_total_price(self):
        print(f'Total price: ${self.database.get_total_price()}')