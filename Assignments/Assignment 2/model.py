import json
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def run_model(train=True):
    with open("data.json", "r") as outfile:
        data=json.load(outfile)
    output = {}
    X_train = data['X_train']
    y_train = data['y_train']
    X_test = data['X_test']
    y_test = data['y_test']
    
    model = RandomForestClassifier()
    model.fit(X_train,y_train)
    y_train_pred = model.predict(X_train)
    output['training_accuracy'] = accuracy_score(y_train,y_train_pred)
    
    if(not train):
        y_pred = model.predict(X_test)
        output['testing_accuracy'] = accuracy_score(y_test,y_pred)
        with open("output_test.json", "w") as outfile:
            json.dump(output, outfile)
    else:
        with open("output_train.json", "w") as outfile:
            json.dump(output, outfile)


if __name__ == "__main__":
    ### If -train is present in arguments call model(path,train=True) 
    
    ### If -test is present in arguments call model(path,train=False) 



