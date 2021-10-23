# Importing
import joblib
from sklearn import datasets
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump
import logging
####
#print(sklearn.__version__) #0.23.1
#print(joblib.__version__) #0.16.0
#print(logging.__version__) #0.5.1.2
#### Splitting the dataset 
iris = datasets.load_iris()
# print(iris_df.target)
x = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
# helper functions : 
# Preprocessing : 
def preprocessing():
    return None
# saving : 
def saving_model():
    '''
    Saving the model as pkl or joblib file .
    Optinal pramiter : type , defualt type="p". 
    This function takes a model argumint and returns the model in .pkl format in defualt . 
    If you want to save the model in joblib format set type="j"
    '''
    return None
saving_model.__doc__
# Model 
dt = DecisionTreeClassifier().fit(X_train, y_train)
pred = dt.predict(X_test)
accuracy = accuracy_score(y_test, pred)
# saving the model 
dump(dt, open('iris-model.pickle',"wb"))
filename = 'iris-model.joblib'
dump(dt, filename)
# Debugging 
logging.info('Training Finished. Accuracy Result: ',accuracy)
