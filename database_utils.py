from typing import List, Dict, Any
import logging
from database import Database
from pc_parts import PCPart

def update_database(db: Database, category: str, item: PCPart):
    try:
        db.add_item(category, item)
    except Exception as e:
        logging.error(f"Failed to update database: {str(e)}")


def parse_database_by_parameter(db: Database, category: str, parameter: str, value: Any) -> List[Dict[str, Any]]:
    try:
        parsed_data = [
            {
                'name': item.get_name(),
                'price': item.get_price(),
                'brand': item.get_brand(),
                'color': item.get_color()
            }
            for item in db.get_items(category)
            if getattr(item, parameter, None) == value
        ]
        return parsed_data
    except Exception as e:
        logging.error(f"Failed to parse database: {str(e)}")