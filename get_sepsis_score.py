#!/usr/bin/env python
from sklearn.externals import joblib
import numpy as np
import pandas as pd

def get_sepsis_score(data, model):

    meanF = np.load('meanF.npy')
    M1 = joblib.load('model-saved.pkl')
    # s_m = np.load('septic_mean.npy', allow_pickle=True)
    # ns_m = np.load('Nonseptic_mean.npy', allow_pickle=True)
    # All = np.vstack((s_m, ns_m))
    # maenAll = np.mean(All, axis=0)

    ####### Impute
    imputePatient = []
    for interval in range(data.shape[0]):      #### loop for on intervals
        if interval == 0:
            newData = np.copy(data[0,:])
            for column in range(40):       ########  loop for on columns
                if (np.isnan(newData[column])):
                    newData[column] = meanF[column]
            # imputePatient.append(newData)
            imputePatient = newData

        else:
            index = np.arange(interval+1)
            aa = np.copy(data[index])
            aa[0, :] = newData
            df = pd.DataFrame.from_records(aa)
            df.interpolate(method='linear', inplace=True)
            newData1 = np.array(df)
            # imputePatient.append(newData1[-1, :])
            imputePatient = np.vstack((imputePatient, newData1[-1, :]))

    data = imputePatient
    ####### End Impute

    predicted = M1.predict(data)

    score = np.random.rand(len(data), 1)
    for i in range(len(data)):
        if predicted[i]==0:
         score[i] = 0.4
        else:
         score[i] = 0.6

    label = np.copy(predicted)

    return score, label

def load_sepsis_model():

    return None
