def check_alive(health):
    if health > 0:
        return True
    else:
        return False

# Sample test cases
if __name__ == "__main__":
    import sys

    class test:
        @staticmethod
        def assert_equals(a, b):
            if a != b:
                print(f"Test failed: Expected {b}, got {a}")
                sys.exit(1)
            else:
                print(f"Test passed: {a} == {b}")

    def fixed_tests():
        print("Running Fixed Tests")
        test.assert_equals(check_alive(5), True)
        test.assert_equals(check_alive(0), False)
        test.assert_equals(check_alive(-5), False)

    fixed_tests()
