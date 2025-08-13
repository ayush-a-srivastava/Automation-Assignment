def assert_element_visible(element, name):
    assert element.is_displayed(), f"{name} is not visible"

def assert_text_equal(actual, expected, message=""):
    assert actual == expected, message or f"Expected '{expected}', got '{actual}'"
