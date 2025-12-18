import time
import trainlytics as tl

tl.start()

for i in range(100):
    tl.update_value("loss", 1.0 / (i+1))
    tl.update_value("accuracy", 0.5 + i*0.01)
    tl.update_value("val_loss", 1.2 / (i+1))
    tl.update_value("val_accuracy", 0.4 + i*0.015)
    time.sleep(0.1)

input("Server running. Press Enter to exit...\n")

