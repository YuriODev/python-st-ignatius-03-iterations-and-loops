def pytest_sessionfinish(session, exitstatus):
    """Prints a custom success message at the end of a successful test session."""
    if exitstatus == 0:  # exitstatus 0 indicates all tests passed
        print("\x1b[6;30;42m Success! Your code works as intended. \x1b[0m")
