from capital_utils import capital

def test_capital():
    test_data = [
        {'state': 'California', 'capital': 'Sacramento'},
        {'country': 'France', 'capital': 'Paris'},
        {'state': 'Texas', 'capital': 'Austin'},
        {'country': 'Japan', 'capital': 'Tokyo'},
        # Test with keys as non-string (simulate symbol-like keys)
        {('state',): 'New York', ('capital',): 'Albany'},
        # Test with missing capital
        {'state': 'Nevada'},
        # Test with missing place
        {'capital': 'Ottawa'},
    ]

    results = capital(test_data)
    for sentence in results:
        print(sentence)

if __name__ == "__main__":
    test_capital()
