import numpy as np
import glob
import pandas as pd
import os

# meanFirstRow = np.load('meanFirstRow.npy')
# meanFirstRow = np.nan_to_num(meanFirstRow)
meanF =  np.load('meanF.npy')
# np.save('meanF', meanF)

s_m = np.load('septic_mean.npy')
ns_m = np.load('Nonseptic_mean.npy')
All = np.vstack((s_m, ns_m))
maenAll = np.mean(All, axis=0)

# path = "D:/challenge2019/Zare/R/Code/HMM_R/Challenge/r-example-2019-master/train/*.psv"
path = "../train/*.psv"

# imputeInterval = []

ite = 0
for fname in glob.glob(path):
    # imputePatient = []
    # print(ite)
    # ite = ite+1
    file_name = os.path.basename(fname)
    df1 = pd.read_csv(fname, sep="|")
    data = np.array(df1)

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


    if ite==0:
        imputeInterval = imputePatient
    else:
        imputeInterval = np.vstack((imputeInterval, imputePatient))
    ite=ite+1


np.save('imputeInterval', imputeInterval)
print('......End......')