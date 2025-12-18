from trainlytics.state import STATE, update_value

def test_update_value_sets_state():
    update_value("loss", 0.5)
    assert STATE.data["loss"] == 0.5

def test_update_value_overwrites():
    update_value("epoch", 1)
    update_value("epoch", 2)
    assert STATE.data["epoch"] == 2
