import pytest
from test.TestUtils import TestUtils
from online_store_management_system import *  

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_scenarios(test_obj):
    """Consolidated test for boundary scenarios"""
    try:
        # Test with empty inventory
        empty_inventory = {}
        
        # Test filter functions with empty inventory
        filtered = filter_by_price_range(empty_inventory, 1000, 5000)
        assert filtered == {}, "Filtering empty inventory should return empty dict"
        
        filtered = filter_by_availability(empty_inventory)
        assert filtered == {}, "Filtering empty inventory by availability should return empty dict"
        
        filtered = filter_by_feature(empty_inventory, "5G")
        assert filtered == {}, "Filtering empty inventory by feature should return empty dict"
        
        # Test merge with empty inventory
        _, new_products = initialize_data()
        merged = merge_inventories(empty_inventory, new_products)
        assert len(merged) == len(new_products), "Merging empty inventory should only include new products"
        
        # Test with real inventory
        inventory, _ = initialize_data()
        
        # Test with exact price match
        exact_price = inventory["P002"]["price"]
        filtered = filter_by_price_range(inventory, exact_price, exact_price)
        assert len(filtered) == 1 and "P002" in filtered, "Should find exactly one product with exact price"
        
        # Test price range with no matches
        min_prices = sorted([product["price"] for product in inventory.values()])
        gap_min = min_prices[0] - 100
        gap_max = min_prices[0] - 1
        filtered = filter_by_price_range(inventory, gap_min, gap_max)
        assert len(filtered) == 0, "Should return empty dict for price range with no matches"
        
        # Test zero stock
        inventory_copy = inventory.copy()
        for pid in inventory_copy:
            inventory_copy[pid] = {**inventory_copy[pid], "stock": 0}
        filtered = filter_by_availability(inventory_copy)
        assert len(filtered) == 0, "Should return empty dict when all products have zero stock"
        filtered = filter_by_availability(inventory_copy, 0)
        assert len(filtered) == 5, "Should return all products when min_stock is 0"
        
        # Test exact minimum stock
        inventory_copy = inventory.copy()
        pid = "P001"
        exact_stock = 5
        inventory_copy[pid] = {**inventory_copy[pid], "stock": exact_stock}
        filtered = filter_by_availability(inventory_copy, exact_stock)
        assert pid in filtered, "Should include product with exact minimum stock"
        filtered = filter_by_availability(inventory_copy, exact_stock + 1)
        assert pid not in filtered, "Should not include product below minimum stock"
        
        # Test update stock to exactly zero
        current_stock = inventory[pid]["stock"]
        updated = update_stock_level(inventory, pid, -current_stock)
        assert updated[pid]["stock"] == 0, "Stock should be exactly zero after update"
        
        test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

def test_edge_case_filtering(test_obj):
    """Test filtering with edge case inputs"""
    try:
        inventory, _ = initialize_data()
        
        # Test merging empty dictionaries
        empty_dict = {}
        merged = merge_inventories(inventory, empty_dict)
        assert merged == inventory, "Merging empty dict into inventory should not change inventory"
        
        merged = merge_inventories(empty_dict, empty_dict)
        assert merged == {}, "Merging empty dicts should result in empty dict"
        
        # Test price brackets with edge cases
        test_inventory = {
            "T001": {"price": 0, "name": "Free Product"},
            "T002": {"price": 2999.99, "name": "Boundary Budget"},
            "T003": {"price": 3000, "name": "Boundary Mid-Range Low"},
            "T004": {"price": 9999.99, "name": "Boundary Mid-Range High"},
            "T005": {"price": 10000, "name": "Boundary Premium"},
            "T006": {"price": 1000000, "name": "Very Expensive"}
        }
        
        brackets = create_price_brackets(test_inventory)
        assert "T001" in brackets["budget"], "Free product should be in budget bracket"
        assert "T002" in brackets["budget"], "Product just below mid_range should be in budget"
        assert "T003" in brackets["mid_range"], "Product at exact mid_range lower bound should be in mid_range"
        assert "T004" in brackets["mid_range"], "Product just below premium should be in mid_range"
        assert "T005" in brackets["premium"], "Product at exact premium lower bound should be in premium"
        assert "T006" in brackets["premium"], "Very expensive product should be in premium"
        
        # Test extreme values
        pid = "P001"
        updated = update_stock_level(inventory, pid, 1000000)  # Very high stock
        assert updated[pid]["stock"] > 1000000, "Should handle very high stock levels"
        
        # Test feature with empty features list
        inventory_copy = inventory.copy()
        inventory_copy[pid]["features"] = []
        filtered = filter_by_feature(inventory_copy, "Nonexistent")
        assert len(filtered) == 0, "Should handle features that don't exist"
        
        test_obj.yakshaAssert("TestEdgeCaseFiltering", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
        pytest.fail(f"Edge case filtering test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])