import numpy as np
from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *
#For Models_Partc
import utils

# PLEASE USE THE GIVEN FUNCTION NAME, DO NOT CHANGE IT
# USE THIS RANDOM STATE FOR ALL OF THE PREDICTIVE MODELS
# THE TESTS WILL NEVER PASS
RANDOM_STATE = 545510477

#input: X_train, Y_train and X_test
#output: Y_pred
def logistic_regression_pred(X_train, Y_train, X_test):
    #Make an instance of the model
    lr_clsfr = LogisticRegression()
    #Training the model on the bothX and Y train data, storing the information learned from the data
    lr_clsfr.fit(X_train,Y_train)
    #Predict class labels for samples in X of test data
    lr_y_test = lr_clsfr.predict(X_test)
    #print("lr_y_test---->", lr_y_test)
    return lr_y_test
	#TODO: train a logistic regression classifier using X_train and Y_train. Use this to predict labels of X_test
	#use default params for the classifier	
	#return None

#input: X_train, Y_train and X_test
#output: Y_pred
def svm_pred(X_train, Y_train, X_test):
    #Make an instance of the model
    svm_clsfr = LinearSVC()
    #Training the model on the bothX and Y train data, storing the information learned from the data
    svm_clsfr.fit(X_train,Y_train)
    #Predict class labels for samples in X of test data
    svm_y_test = svm_clsfr.predict(X_test)
    #print("svm_y_test---->", svm_y_test)
    return svm_y_test
	#TODO:train a SVM classifier using X_train and Y_train. Use this to predict labels of X_test
	#use default params for the classifier
	#return None

#input: X_train, Y_train and X_test
#output: Y_pred
def decisionTree_pred(X_train, Y_train, X_test):
    #Make an instance of the model
    dt_clsfr = DecisionTreeClassifier()
    #Training the model on the bothX and Y train data, storing the information learned from the data
    dt_clsfr.fit(X_train,Y_train)
    #Predict class labels for samples in X of test data
    dt_y_test = dt_clsfr.predict(X_test)
    #print("dt_y_test---->", dt_y_test)
    return dt_y_test
	#TODO:train a logistic regression classifier using X_train and Y_train. Use this to predict labels of X_test
	#IMPORTANT: use max_depth as 5. Else your test cases might fail.
	#return None


#input: Y_pred,Y_true
#output: accuracy, auc, precision, recall, f1-score
def classification_metrics(Y_pred, Y_true):
    accuracy = accuracy_score(Y_pred,Y_true)
    auc = roc_auc_score(Y_pred,Y_true)
    precision = precision_score(Y_pred,Y_true)
    recall = recall_score(Y_pred,Y_true)
    f1score = f1_score(Y_pred,Y_true)
    return accuracy,auc,precision,recall,f1score
	#TODO: Calculate the above mentioned metrics
	#NOTE: It is important to provide the output in the same order
	

#input: Name of classifier, predicted labels, actual labels
def display_metrics(classifierName,Y_pred,Y_true):
	print("______________________________________________")
	print(("Classifier: "+classifierName))
	acc, auc_, precision, recall, f1score = classification_metrics(Y_pred,Y_true)
	print(("Accuracy: "+str(acc)))
	print(("AUC: "+str(auc_)))
	print(("Precision: "+str(precision)))
	print(("Recall: "+str(recall)))
	print(("F1-score: "+str(f1score)))
	print("______________________________________________")
	print("")

def main():
	X_train, Y_train = utils.get_data_from_svmlight("/users/abhik/deliverables/features_svmlight.train")
	X_test, Y_test = utils.get_data_from_svmlight("/users/abhik/data/features_svmlight.validate")

	display_metrics("Logistic Regression",logistic_regression_pred(X_train,Y_train,X_test),Y_test)
	display_metrics("SVM",svm_pred(X_train,Y_train,X_test),Y_test)
	display_metrics("Decision Tree",decisionTree_pred(X_train,Y_train,X_test),Y_test)

if __name__ == "__main__":
	main()
	
