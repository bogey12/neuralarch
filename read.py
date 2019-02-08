import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

dat = pd.read_csv('data/tonysad1.csv')
dat = dat.fillna(0)
numpydat = dat.values.transpose()
dattag = dat.keys()

sfreq = 256
ch_types = ['grad', 'mag', 'mag', 'grad']
info = mne.create_info(ch_names=list(dat.keys()[1:5]), sfreq=sfreq, ch_types=ch_types)
raw = mne.io.RawArray(numpydat[1:5], info)

'''Apply Basic Filters'''
#Low pass filter
raw.filter (l_freq=8, h_freq=12)

'''Determine epochs and average them'''
'''
events = mne.find_events (raw, stim_channel = list(dat.keys()[1:5]), shortest_event = 2)
epochs = mne.Epochs (raw, events, event_id=4, tmin=-0.2, tmax=0.5, proj=True,
	baseline=(None,0), preload=True)
evoked = epochs.average()
#cov = mne.compute_covariance (epochs, tmax=0)
evoked.plot()
'''
'''Graph Raw Data'''
scalings = {'mag': 100, 'grad': 100}
raw.plot(n_channels=4, scalings=scalings, title='Data from arrays',
         show=True, block=True)



#plt.plot(dat["time"],dat["TP9"])
#plt.show()
#print(dat)"""
