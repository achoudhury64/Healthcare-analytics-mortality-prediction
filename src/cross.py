import models_partc
from sklearn.model_selection import KFold, ShuffleSplit

import numpy as np
from numpy import mean, array

import utils


from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *

# USE THE GIVEN FUNCTION NAME, DO NOT CHANGE IT

# USE THIS RANDOM STATE FOR ALL OF YOUR CROSS VALIDATION TESTS, OR THE TESTS WILL NEVER PASS
RANDOM_STATE = 545510477

#input: training data and corresponding labels
#output: accuracy, auc
def get_acc_auc_kfold(X,Y,k=5):
    print("X----->\n",X)
    print("Y----->\n",Y)
	#TODO:First get the train indices and test indices for each iteration
	#Then train the classifier accordingly
	#Report the mean accuracy and mean auc of all the folds
    
    kf = KFold(n_splits=k, random_state=None, shuffle=False)
    clf_lr_kfold = LogisticRegression()
    print("kf---->\n", type(kf))
    acc_list =[]
    auc_list =[]
    for train,test in kf.split(X):
        clf_lr_kfold.fit(X[train],Y[train])
        acc = accuracy_score(clf_lr_kfold.predict(X[test]),Y[test])
        acc_list.append(acc)      
        auc_ = roc_auc_score(clf_lr_kfold.predict(X[test]),Y[test])
        auc_list.append(auc_)
    #print("acc-->\n", acc_list)    
    acc_k = mean(acc_list)
    #print("acc_k", acc_k)
    auc_k = mean(auc_list)
    #print("auc_k", auc_k)
    return acc_k,auc_k
	


#input: training data and corresponding labels
#output: accuracy, auc
def get_acc_auc_randomisedCV(X,Y,iterNo=5,test_percent=0.2):
	#TODO: First get the train indices and test indices for each iteration
	#Then train the classifier accordingly
	#Report the mean accuracy and mean auc of all the iterations
    ss = ShuffleSplit(n_splits=iterNo, test_size=test_percent,random_state = RANDOM_STATE)
    clf_lr_ss = LogisticRegression()
    acc_list =[]
    auc_list =[]
    for train,test in ss.split(X):            
        clf_lr_ss.fit(X[train],Y[train])
        acc = accuracy_score(clf_lr_ss.predict(X[test]),Y[test])
        acc_list.append(acc)
        
        auc_ = roc_auc_score(clf_lr_ss.predict(X[test]),Y[test])
        auc_list.append(auc_)
        
    acc_k = array(acc_list).mean()
    #print("acc_k", acc_k)
    auc_k = array(auc_list).mean()
    #print("auc_k", auc_k)
    return acc_k,auc_k
	


def main():
	X,Y = utils.get_data_from_svmlight("/users/abhik/deliverables/features_svmlight.train")
	print("Classifier: Logistic Regression__________")
	acc_k,auc_k = get_acc_auc_kfold(X,Y)
	print(("Average Accuracy in KFold CV: "+str(acc_k)))
	print(("Average AUC in KFold CV: "+str(auc_k)))
	acc_r,auc_r = get_acc_auc_randomisedCV(X,Y)
	print(("Average Accuracy in Randomised CV: "+str(acc_r)))
	print(("Average AUC in Randomised CV: "+str(auc_r)))

if __name__ == "__main__":
	main()

