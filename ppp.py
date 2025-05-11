import wfdb
import matplotlib.pyplot as plt
import wfdb
import pywt
import numpy as np
import matplotlib.pyplot as plt


# Choose a record to display (without file extension)
record_name = '101'  # Example record
record_path = 'mit-bih-arrhythmia-database-1.0.0/' + record_name

# Read the record
record = wfdb.rdrecord(record_path)
signal = record.p_signal[:,:1]
signal_1d = signal.ravel()

print(signal_1d)
annotation = wfdb.rdann(record_path, 'atr')
print(annotation)
# Plot the signals
wfdb.plot_wfdb(record=record, annotation=annotation,
               title='Record ' + record_name + ' from MIT-BIH Arrhythmia Database',
               time_units='seconds')
plt.show()

