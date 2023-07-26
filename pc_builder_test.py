import unittest
import logging
from database import Database
from pc_parts import CPU, CPUCooler

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger("TestDatabaseLogger")
        self.logger.setLevel(logging.DEBUG)

        # Create a console handler for testing and set the level to DEBUG
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        self.database = Database(logger=self.logger)

    def test_get_items(self):
        # Ensure 'CPUs' category is available and contains items
        cpus = self.database.get_items('CPUs')
        self.assertTrue(cpus)
        self.assertIsInstance(cpus[0], CPU)

        # Ensure a non-existent category returns an empty list
        non_existent_category = self.database.get_items('NonExistentCategory')
        self.assertEqual(non_existent_category, [])

    def test_add_and_delete_item(self):
        # Add a new CPU item
        test_cpu = CPU("Test CPU", 250.0, "Silver", "Test Brand", "4.0 GHz", "100 W")
        self.database.add_item("CPUs", test_cpu)

        # Check if the new CPU item is added to the 'CPUs' category
        cpus = self.database.get_items('CPUs')
        self.assertTrue(test_cpu in cpus)

        # Try to delete the newly added CPU item
        self.database.delete_item("CPUs", test_cpu)

        # Ensure the CPU item is no longer in the 'CPUs' category
        cpus = self.database.get_items('CPUs')
        self.assertFalse(test_cpu in cpus)

    def test_search(self):
        # Ensure search returns matching items correctly
        test_cpu = CPU("Test CPU", 250.0, "Silver", "Test Brand", "4.0 GHz", "100 W")
        self.database.add_item("CPUs", test_cpu)

        search_result = self.database.search("CPUs", brand="Test Brand")
        self.assertTrue(search_result)
        self.assertEqual(len(search_result), 1)
        self.assertEqual(search_result[0]['name'], "Test CPU")

    def test_get_total_price(self):
        # Ensure the total price calculation is correct
        test_cpu = CPU("Test CPU", 250.0, "Silver", "Test Brand", "4.0 GHz", "100 W")
        test_cooler = CPUCooler("Test Cooler", 50.0, "Black", "Test Cooler Brand", "1200 RPM")

        self.database.add_item("CPUs", test_cpu)
        self.database.add_item("CPU_Coolers", test_cooler)

        total_price = self.database.get_total_price()
        self.assertEqual(total_price, 14507.969999999994)

if __name__ == "__main__":
    unittest.main()

