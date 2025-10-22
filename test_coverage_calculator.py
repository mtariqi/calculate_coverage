from coverage_calculator import calculate_coverage

def test_calculate_coverage():
    assert abs(calculate_coverage(10_000_000, 150, 5_000_000) - 600) < 1e-6
    print("✅ Test passed!")

if __name__ == "__main__":
    test_calculate_coverage()
