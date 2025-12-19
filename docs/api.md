# API Reference

Trainlytics provides a simple API to track and visualize training metrics in real-time.

---

### `trainviz.start()`

```python
trainviz.start()
```
Launches the Trainviz server in a background thread. Multiple calls have no effect if the server is already running.





### `trainviz.update_value(key, value, sample_rate=1, sliding_window=None)`

```
trainviz.update_value(key, value, sample_rate=1, sliding_window=None)
```

Updates a tracked metric and pushes it to the live dashboard.

Parameters:

* `key` : str — Name of the metric (e.g., "loss", "accuracy")
* `value` : float — New value to record
* `sample_rate` : int — Aggregate every N values before storing
* `sliding_window` : int — Keep only the last N values to limit memory

