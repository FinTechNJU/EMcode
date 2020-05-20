# -*- coding: utf-8 -*-
from sklearn import svm,datasets
from sklearn.metrics import classification_report

clf = svm.SVC(kernel='linear')
#载入鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target
print ('X=',X)
print ('y=',y)
print ('len(x)=',len(X))
print ('len(y)=',len(y))

X_train = X[0:120]
y_train = y[0:120]
X_test = X[120:]
y_test = y[120:]


print('--------------SVM-------------------')
clf = svm.SVC(kernel='linear')
clf.fit(X_train,y_train)
testlabel=clf.predict(X_test)
print(classification_report(y_test,testlabel))



from sklearn import tree

print('--------------DecisionTree-------------------')
clf = tree.DecisionTreeClassifier()
clf.fit(X_train,y_train)
testlabel=clf.predict(X_test)

print(classification_report(y_test,testlabel))



from sklearn.linear_model import LogisticRegression

print('--------------LogisticRegression-------------------')
clf = LogisticRegression()
clf.fit(X_train,y_train)
testlabel=clf.predict(X_test)
print(classification_report(y_test,testlabel))


from sklearn.ensemble import RandomForestClassifier


print('--------------RandomForest-------------------')
clf = RandomForestClassifier(n_estimators=20)
clf.fit(X_train,y_train)
testlabel=clf.predict(X_test)
print(classification_report(y_test,testlabel))

