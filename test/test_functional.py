import pytest
import inspect
import importlib
import re
from test.TestUtils import TestUtils
from online_store_management_system import (
    initialize_data,
    filter_by_category,
    filter_by_price_range,
    filter_by_availability,
    filter_by_feature,
    find_products_with_keyword,
    update_product_price,
    update_stock_level,
    add_product_feature,
    merge_inventories,
    calculate_category_counts,
    calculate_total_inventory_value,
    find_highest_rated_product,
    create_price_brackets
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_variable_naming(test_obj):
    """Test that the required variable names and structure are used"""
    try:
        # Import the module
        module = importlib.import_module("online_store_management_system")

        # Check dictionary initialization
        init_source = inspect.getsource(module.initialize_data)
        assert "inventory = {" in init_source, "Initialize data must create inventory dictionary"
        assert "new_products = {" in init_source, "Initialize data must create new_products dictionary"
        
        # Check main function uses required data
        main_source = inspect.getsource(module.main)
        assert "inventory, new_products = initialize_data()" in main_source, "main() must initialize inventory data"
        
        # Check dictionary operation functions use correct parameter names
        assert "def filter_by_category(inventory, category)" in inspect.getsource(module), "filter_by_category() must use correct parameters"
        assert "def filter_by_price_range(inventory, min_price, max_price)" in inspect.getsource(module), "filter_by_price_range() must use correct parameters"
        assert "def merge_inventories(existing_inventory, new_products)" in inspect.getsource(module), "merge_inventories() must use correct parameters"
        
        test_obj.yakshaAssert("test_variable_naming", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_variable_naming", False, "functional")
        pytest.fail(f"Variable naming test failed: {str(e)}")

def test_dictionary_operations(test_obj):
    """Test all dictionary operations"""
    try:
        # Test all filtering operations
        inventory, new_products = initialize_data()

        # Test filter_by_category
        filtered = filter_by_category(inventory, "electronics")
        assert len(filtered) == 2 and "P001" in filtered and "P003" in filtered
        
        # Test filter_by_price_range
        filtered = filter_by_price_range(inventory, 5000, 10000)
        assert len(filtered) == 2 and "P003" in filtered and "P005" in filtered
        
        # Test filter_by_availability
        # Create copy with one unavailable product
        inventory_copy = inventory.copy()
        inventory_copy["P002"] = {**inventory_copy["P002"], "stock": 0}
        filtered = filter_by_availability(inventory_copy)
        assert len(filtered) == 4 and "P002" not in filtered
        
        # Test filter_by_feature
        filtered = filter_by_feature(inventory, "Noise Cancelling")
        assert len(filtered) == 1 and "P003" in filtered
        
        # Test find_products_with_keyword
        filtered = find_products_with_keyword(inventory, "phone")
        assert len(filtered) == 2 and "P001" in filtered and "P003" in filtered
        
        # Test update operations
        original_price = inventory["P001"]["price"]
        updated = update_product_price(inventory, "P001", 69999.99)
        assert updated["P001"]["price"] == 69999.99 and inventory["P001"]["price"] == original_price
        
        original_stock = inventory["P002"]["stock"]
        updated = update_stock_level(inventory, "P002", 5)
        assert updated["P002"]["stock"] == original_stock + 5 and inventory["P002"]["stock"] == original_stock
        
        updated = add_product_feature(inventory, "P001", "Water Resistant")
        assert "Water Resistant" in updated["P001"]["features"]
        assert "Water Resistant" not in inventory["P001"]["features"]
        
        # Test merge operation
        merged = merge_inventories(inventory, new_products)
        assert len(merged) == 7 and merged["N001"]["new_arrival"] == True
        
        # Test statistics operations
        counts = calculate_category_counts(inventory)
        assert counts["electronics"] == 2 and counts["clothing"] == 1
        
        value = calculate_total_inventory_value(inventory)
        expected_value = sum(product["price"] * product["stock"] for product in inventory.values())
        assert abs(value - expected_value) < 0.01
        
        highest = find_highest_rated_product(inventory)
        assert highest[0] == "P004" and highest[1]["rating"] == 4.8
        
        brackets = create_price_brackets(inventory)
        assert "P004" in brackets["budget"] and "P001" in brackets["premium"]
        
        test_obj.yakshaAssert("test_dictionary_operations", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_dictionary_operations", False, "functional")
        pytest.fail(f"Dictionary operations test failed: {str(e)}")

def test_implementation_techniques(test_obj):
    """Test implementation of dictionary techniques"""
    try:
        # Check dictionary comprehension
        source = inspect.getsource(filter_by_category)
        assert "{" in source and "for" in source and "if" in source
        
        # Check dictionary methods
        source = inspect.getsource(calculate_category_counts)
        assert ".values()" in source or ".items()" in source or ".keys()" in source
        
        # Check dictionary unpacking
        source1 = inspect.getsource(update_product_price)
        source2 = inspect.getsource(merge_inventories)
        assert "**" in source1 and "**" in source2
        
        # Check data immutability
        inventory, _ = initialize_data()
        product_id = "P001"
        original_price = inventory[product_id]["price"]
        updated = update_product_price(inventory, product_id, original_price + 1000)
        assert inventory[product_id]["price"] == original_price
        assert updated[product_id]["price"] == original_price + 1000
        
        test_obj.yakshaAssert("test_implementation_techniques", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_implementation_techniques", False, "functional")
        pytest.fail(f"Implementation techniques test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])