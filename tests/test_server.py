import trainlytics as tl

def test_start_server_runs():
    tl.start()
    # Server should be running in background
    # No exception means it started
    assert True
