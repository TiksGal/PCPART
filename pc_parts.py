class PCPart:
    def __init__(self, name: str, price: float, color: str=None):
        self.name = name
        self.price = price
        self.color = color

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def get_color(self) -> str:
        return self.color
    
    def get_info(self):
        return f"{self.name}, Color: {self.color}, Price: ${self.price}"


class CPU(PCPart):
    def __init__(self, name: str, price: float, color: str, brand: str, speed: str, power_usage: str):
        super().__init__(name, price, color)
        self.brand = brand
        self.speed = speed
        self.power_usage = power_usage

    def get_brand(self) -> str:
        return self.brand

    def get_speed(self) -> str:
        return self.speed

    def get_power_usage(self) -> str:
        return self.power_usage


class CPUCooler(PCPart):
    def __init__(self, name: str, price: float, color: str, brand: str, power_usage: str):
        super().__init__(name, price, color)
        self.brand = brand
        self.power_usage = power_usage
        
    def get_brand(self) -> str:
        return self.brand
    
    def get_power_usage(self) -> str:
        return self.power_usage
    

class Motherboard(PCPart):
    def __init__(self, name: str, price: float, color: str, socket: str, form_factor: str):
        super().__init__(name, price, color)
        self.socket = socket
        self.form_factor = form_factor
    
    def get_socket(self) -> str:
        return self.socket
    
    def get_form_factor(self) -> str:
        return self.form_factor
    
    
class Memory(PCPart):
    def __init__(self, name: str, price: float, color: str, brand: str, modules: str, speed: str):
        super().__init__(name, price, color)
        self.brand = brand
        self.modules = modules
        self.speed = speed

    def get_brand(self) -> str:
        return self.brand

    def get_modules(self) -> str:
        return self.modules

    def get_speed(self) -> str:
        return self.speed
    
    
class Storage(PCPart):
    def __init__(self, name: str, price: float, color: str, form_factor: str, capacity: str, type: str):
        super().__init__(name, price, color)
        self.form_factor = form_factor
        self.capacity = capacity
        self.type = type

    def get_form_factor(self) -> str:
        return self.form_factor

    def get_capacity(self) -> str:
        return self.capacity

    def get_type(self) -> str:
        return self.type
    
    
class VideoCard(PCPart):
    def __init__(self, name: str, price: float, color: str, chipset: str, memory: str):
        super().__init__(name, price, color)
        self.chipset = chipset
        self.memory = memory

    def get_chipset(self) -> str:
        return self.chipset

    def get_memory(self) -> str:
        return self.memory
    
    
class Case(PCPart):
    def __init__(self, name: str, price: float, color: str, type: str, side_panel: str):
        super().__init__(name, price, color)
        self.type = type
        self.side_panel = side_panel

    def get_type(self) -> str:
        return self.type

    def get_side_panel(self) -> str:
        return self.side_panel
    

class PowerSupply(PCPart):
    def __init__(self, name: str, price: float, color: str, type: str, wattage: int):
        super().__init__(name, price, color)
        self.type = type
        self.wattage = wattage

    def get_type(self) -> str:
        return self.type

    def get_wattage(self) -> int:
        return self.wattage


class OperatingSystem(PCPart):
    def __init__(self, name: str, price: float, mode: str, memory: int):
        super().__init__(name, price)
        self.mode = mode
        self.memory = memory

    def get_mode(self) -> str:
        return self.mode

    def get_memory(self) -> int:
        return self.memory


class Monitor(PCPart):
    def __init__(self, name: str, price: float, color: str, refresh_rate: int, size: float, resolution: str):
        super().__init__(name, price, color)
        self.refresh_rate = refresh_rate
        self.size = size
        self.resolution = resolution

    def get_refresh_rate(self) -> int:
        return self.refresh_rate

    def get_size(self) -> float:
        return self.size

    def get_resolution(self) -> str:
        return self.resolution