from sklearn.ensemble import AdaBoostClassifier
from sklearn.externals import joblib
import numpy as np
from Driver import Driver, load_challenge_data, save_challenge_predictions


Train = np.load('../22/old/imputeInterval.npy', allow_pickle = True)

data = np.array(Train)
trainData = data[:, :-1]
trainLabels = data [:,-1]

############################    sample weighting
weightArray = np.copy(trainLabels)
weightArray[weightArray == 1] = 40
weightArray[weightArray == 0] = 1

################## train Data

# for i in range(12):
# ne = (i+1) * 10
# ne = 1 + i
ne = 150
clf = AdaBoostClassifier(n_estimators=ne , random_state=None )
clf.fit(trainData, trainLabels, sample_weight = weightArray)
joblib.dump(clf, 'model-saved.pkl')
result = Driver()
resultut = result[4]
modelname = "model-saved_Rivised" + str(ne) + "ut=" + str(resultut)
joblib.dump(clf, modelname+'.pkl')
