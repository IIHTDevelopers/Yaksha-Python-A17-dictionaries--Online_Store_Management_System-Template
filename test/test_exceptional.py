import pytest
from test.TestUtils import TestUtils
from online_store_management_system import (
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
    create_price_brackets,
    get_formatted_product,
    display_data
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_input_validation(test_obj):
    """Consolidated test for input validation and error handling"""
    try:
        # Test with None inputs for critical functions
        functions_to_test = [
            (filter_by_category, [None, "electronics"]),
            (filter_by_category, [{"P001": {}}, None]),
            (filter_by_price_range, [None, 100, 200]),
            (filter_by_price_range, [{"P001": {}}, None, 200]),
            (filter_by_price_range, [{"P001": {}}, 100, None]),
            (filter_by_availability, [None]),
            (filter_by_feature, [None, "5G"]),
            (filter_by_feature, [{"P001": {}}, None]),
            (find_products_with_keyword, [None, "phone"]),
            (find_products_with_keyword, [{"P001": {}}, None]),
            (update_product_price, [None, "P001", 1000]),
            (update_product_price, [{"P001": {}}, None, 1000]),
            (update_product_price, [{"P001": {}}, "P001", None]),
            (update_stock_level, [None, "P001", 10]),
            (update_stock_level, [{"P001": {}}, None, 10]),
            (update_stock_level, [{"P001": {}}, "P001", None]),
            (add_product_feature, [None, "P001", "5G"]),
            (add_product_feature, [{"P001": {}}, None, "5G"]),
            (add_product_feature, [{"P001": {}}, "P001", None]),
            (merge_inventories, [None, {"N001": {}}]),
            (merge_inventories, [{"P001": {}}, None]),
            (calculate_category_counts, [None]),
            (calculate_total_inventory_value, [None]),
            (find_highest_rated_product, [None]),
            (create_price_brackets, [None]),
            (get_formatted_product, ["P001", None])
        ]
        
        # Test all functions with None inputs
        for func, args in functions_to_test:
            with pytest.raises(ValueError):
                func(*args)
        
        # Test with incorrect parameter types
        with pytest.raises(Exception):
            filter_by_category("not a dict", "electronics")
        
        # Test with invalid input values
        inventory = {"P001": {"price": 1000, "stock": 10, "features": []}}
        
        # Test with invalid product ID
        invalid_id = "INVALID"
        with pytest.raises(ValueError):
            update_product_price(inventory, invalid_id, 1500)
        
        # Test with negative price
        with pytest.raises(ValueError):
            update_product_price(inventory, "P001", -100)
        
        # Test with negative resulting stock
        with pytest.raises(ValueError):
            update_stock_level(inventory, "P001", -20)  # Would result in -10 stock
        
        # Test with negative min_stock
        with pytest.raises(ValueError):
            filter_by_availability(inventory, -1)
        
        # Test with empty feature string
        with pytest.raises(ValueError):
            add_product_feature(inventory, "P001", "")
        
        # Test with min_price > max_price
        with pytest.raises(ValueError):
            filter_by_price_range(inventory, 2000, 1000)
        
        # Test with empty inventory for critical functions
        empty_inventory = {}
        with pytest.raises(ValueError):
            find_highest_rated_product(empty_inventory)
        
        # But these should handle empty inventory gracefully
        result = calculate_category_counts(empty_inventory)
        assert result == {}, "Category counts for empty inventory should be empty dict"
        
        result = calculate_total_inventory_value(empty_inventory)
        assert result == 0, "Total value for empty inventory should be 0"
        
        test_obj.yakshaAssert("TestInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidation", False, "exception")
        pytest.fail(f"Input validation test failed: {str(e)}")

def test_error_handling(test_obj):
    """Test specific error handling scenarios"""
    try:
        # Setup inventory with specific conditions for testing
        inventory = {
            "P001": {
                "name": "Test Product",
                "category": "electronics",
                "price": 5000.0,
                "stock": 10,
                "rating": 4.5,
                "features": ["Feature1", "Feature2"]
            }
        }
        
        # Test handling missing fields in product
        invalid_product_inventory = {
            "P001": {
                "name": "Invalid Product"
                # Missing required fields
            }
        }
        
        # Should raise exception when accessing missing fields
        with pytest.raises(Exception):
            filter_by_category(invalid_product_inventory, "electronics")
        
        with pytest.raises(Exception):
            filter_by_price_range(invalid_product_inventory, 0, 10000)
        
        # The following should not raise exceptions
        display_data(None, "inventory")  # None data
        display_data([], "records")  # Empty data
        display_data(inventory, "invalid_type")  # Invalid type
        
        # Test immutability - original inventory should not change
        original_price = inventory["P001"]["price"]
        updated_inventory = update_product_price(inventory, "P001", 6000.0)
        assert inventory["P001"]["price"] == original_price, "Original inventory should not be modified"
        assert updated_inventory["P001"]["price"] == 6000.0, "New inventory should have updated price"
        
        original_stock = inventory["P001"]["stock"]
        updated_inventory = update_stock_level(inventory, "P001", 5)
        assert inventory["P001"]["stock"] == original_stock, "Original inventory should not be modified"
        assert updated_inventory["P001"]["stock"] == original_stock + 5, "New inventory should have updated stock"
        
        original_features = inventory["P001"]["features"].copy()
        updated_inventory = add_product_feature(inventory, "P001", "NewFeature")
        assert inventory["P001"]["features"] == original_features, "Original inventory should not be modified"
        assert "NewFeature" in updated_inventory["P001"]["features"], "New inventory should have new feature"
        
        test_obj.yakshaAssert("TestErrorHandling", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestErrorHandling", False, "exception")
        pytest.fail(f"Error handling test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])