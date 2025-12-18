import requests
import time
import trainlytics as tl

tl.start()
time.sleep(0.5)

def test_index_served():
    r = requests.get("http://127.0.0.1:8000")
    assert r.status_code == 200
    assert len(r.text) > 0
    assert "<html>" in r.text.lower()
