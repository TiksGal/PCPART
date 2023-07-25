import logging
from pc_parts import PCPart, CPU, CPUCooler, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply, OperatingSystem, Monitor


class Database:
    def __init__(self, logger):
        self.db = {
            'CPUs': [
                CPU("Intel Core i7", 300.0, "Silver", "Intel", "4.6 GHz", "95 W"),
                CPU("AMD Ryzen 5", 200.0, "Silver", "AMD", "4.2 GHz", "65 W"),
                CPU("Intel Core i9", 500.0, "Silver", "Intel", "5.0 GHz", "125 W"),
                CPU("AMD Ryzen 7", 330.0, "Silver", "AMD", "4.4 GHz", "105 W"),
                CPU("Intel Core i5", 190.0, "Silver", "Intel", "4.4 GHz", "65 W"),
            ],
            'CPU_Coolers': [
                CPUCooler("Cooler Master Hyper 212 Black Edition", 24.99, "Black", "Cooler Master", "800 - 2000 RPM"),
                CPUCooler("Cooler Master MASTERLIQUID ML240L RGB V2", 99.99, "Black", "Cooler Master", "650 - 1800 RPM"),
                CPUCooler("be quiet! Dark Rock Pro 4", 89.90, "Black", "be quiet!", "1500 RPM"),
                CPUCooler("Noctua NH-D15 chromax.black", 89.99, "Black", "Noctua", "300 - 1500 RPM"),
                CPUCooler("Thermalright Peerless Assassin 120 SE", 36.90, "Black", "Thermalright", "1550 RPM"),
            ],
            'Motherboards': [
                Motherboard("MSI MAG B550 TOMAHAWK", 169.99, "Black / Silver", "AM4", "ATX"),
                Motherboard("MSI B550-A PRO", 139.99, "Black / Silver", "AM4", "ATX"),
                Motherboard("MSI B550M PRO-VDH WIFI", 119.99, "Black", "AM4", "Micro ATX"),
                Motherboard("Gigabyte Z790 AORUS ELITE AX", 249.99, "Black", "LGA1700", "ATX"),
                Motherboard("Asus Prime B450M-A II", 79.98, None, "AM4", "Micro ATX"),
            ],
            'Memories': [
                Memory("Corsair Vengeance LPX 16 GB", 37.99, "Black / Yellow", "Corsair", "2 x 8GB", "DDR4-3200"),
                Memory("Corsair Vengeance RGB Pro 32 GB", 104.98, "Black", "Corsair", "2 x 16GB", "DDR4-3600"),
                Memory("Corsair Vengeance LPX 32 GB", 67.99, "Black / Yellow", "Corsair", "2 x 16GB", "DDR4-3600"),
                Memory("Corsair Vengeance 32 GB", 92.99, "Black", "Corsair", "2 x 16GB", "DDR5-5600"),
                Memory("G.Skill Trident Z5 RGB 32 GB", 102.96, "Black", "G.Skill", "2 x 16GB", "DDR5-6000"),
            ],
            'Storages': [
                Storage("Samsung 980 Pro", 119.57, None, "M.2-2280", "2 TB", "SSD"),
                Storage("Samsung 970 Evo Plus", 49.99, None, "M.2-2280", "1 TB", "SSD"),
                Storage("Samsung 980 Pro", 59.99, None, "M.2-2280", "1 TB", "SSD"),
                Storage("Kingston NV2", 42.70, None, "M.2-2280", "1 TB", "SSD"),
                Storage("Seagate Barracuda Compute", 55.00, None, "3.5", "2 TB", "7200 RPM"),
            ],
            'VideoCards': [
                VideoCard("MSI GeForce RTX 3060 Ventus 2X 12G", 289.99, "Black", "GeForce RTX 3060 12GB", "12 GB"),
                VideoCard("Gigabyte WINDFORCE OC", 599.99, "Black", "GeForce RTX 4070", "12 GB"),
                VideoCard("Asus ROG STRIX GAMING OC", 1951.79, "Black", "GeForce RTX 4090", "24 GB"),
                VideoCard("XFX Speedster MERC 319 CORE", 529.99, "Black / Silver", "Radeon RX 6800 XT", "16 GB"),
                VideoCard("Asus TUF GAMING", 999.99, "Black", "GeForce RTX 4070 Ti", "12 GB"),
            ],
            'Cases': [
                Case("Corsair 4000D Airflow", 89.99, "Black", "ATX Mid Tower", "Tinted Tempered Glass"),
                Case("NZXT H5 Flow", 94.99, "Black", "ATX Mid Tower", "Tempered Glass"),
                Case("Deepcool CC560", 66.98, "Black", "ATX Mid Tower", "Tempered Glass"),
                Case("Lian Li O11 Dynamic EVO", 152.99, "White / Gray", "ATX Mid Tower", "Tempered Glass"),
                Case("Lian Li O11 Dynamic EVO", 154.99, "Black", "ATX Mid Tower", "Tinted Tempered Glass"),
            ],
            'PowerSupplies': [
                PowerSupply("Corsair RM750e (2023)", 99.99, "Black", "ATX", 750),
                PowerSupply("Corsair RM850x (2021)", 129.99, "Black", "ATX", 850),
                PowerSupply("Corsair RM1000x (2021)", 169.99, "Black", "ATX", 1000),
                PowerSupply("Thermaltake Toughpower GX2", 69.98, "Black", "ATX", 600),
                PowerSupply("Corsair CX650M (2021)", 79.99, "Black", "ATX", 650),
            ],
            'OperatingSystems': [
                OperatingSystem("Microsoft Windows 11 Home (64-bit)", 117.98, "64-bit", 128),
                OperatingSystem("Microsoft Windows 10 Home (64-bit)", None, "64-bit", 128),
                OperatingSystem("Microsoft Windows 11 Pro (64-bit)", 144.99, "64-bit", 2048),
                OperatingSystem("Microsoft Windows 10 Pro (64-bit)", 129.55, "64-bit", 2048),
                OperatingSystem("Microsoft Windows 11 Home (64-bit)", 129.98, "64-bit", 128),
            ],
            'Monitors': [
                Monitor("Asus TUF Gaming VG27AQ", 300.00, "Black", 165, 27.0, "2560 x 1440"),
                Monitor("Asus VG248QG", 188.99, "Black", 165, 24.0, "1920 x 1080"),
                Monitor("Dell UP3218K", 3999.00, "Black", 60, 32.0, "7680 x 4320"),
                Monitor("Gigabyte G27Q", 239.99, "Black", 144, 27.0, "2560 x 1440"),
                Monitor("Acer Nitro QG241Y Pbmiipx", 119.99, "Black", 165, 23.8, "1920 x 1080"),
            ],
        }
        self.logger = logger
        # Create a logger for the Database class
        self.logger = logging.getLogger("DatabaseLogger")
        self.logger.setLevel(logging.INFO)

        # Configure a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)

        file_handler = logging.FileHandler("app_log.txt")  # Change "app_log.txt" to the desired file name
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        # Add the console handler to the logger
        self.logger.addHandler(console_handler)

    def get_items(self, category: str):
        return self.db.get(category, [])

    def add_item(self, category, item):
        if category in self.db:
            self.db[category].append(item)
        else:
            self.db[category] = [item]

    def delete_item(self, category: str, item: PCPart):
        if category in self.db and item in self.db[category]:
            self.db[category].remove(item)
            self.logger.info(f"Deleted {item.get_name()} from {category}")
        else:
            self.logger.error(f"Item {item.get_name()} does not exist in category {category}")

    def search(self, category: str, **kwargs):
        if category not in self.db:
            return []

        matching_items = []
        for item in self.db[category]:
            if all(getattr(item, key, None) == value for key, value in kwargs.items()):
                item_info = {
                    'name': item.get_name(),
                    'price': item.get_price(),
                    'brand': item.get_brand(),
                    'color': item.get_color()
                }
                matching_items.append(item_info)
        return matching_items
    
    def get_total_price(self):
        total = 0
        for category in self.db.values():
            for item in category:
                price = item.get_price()  # Get the item price
                if price is not None:  # Check if the price is not None
                    total += price  # If price is not None, add it to total
        return total

