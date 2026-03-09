from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_reversed_hints_regression():
    # Regression: hints were reversed — guess > secret incorrectly returned "Too Low"
    # and guess < secret incorrectly returned "Too High".
    high_result = check_guess(99, 1)
    assert high_result == "Too High", f"Expected 'Too High' but got {high_result!r}"

    low_result = check_guess(1, 99)
    assert low_result == "Too Low", f"Expected 'Too Low' but got {low_result!r}"
