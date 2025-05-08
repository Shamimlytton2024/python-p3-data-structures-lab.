from lib.data_structures import get_names

def test_get_names():
    spicy_foods = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        },
    ]
    expected = ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
    assert get_names(spicy_foods) == expected
