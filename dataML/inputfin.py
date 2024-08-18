import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv('dataset\inputfin.csv')

X = data.iloc[:,-1]
y = data.iloc[:,-1]

X.head()
y.head(20)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
classifier = RandomForestClassifier()

y_pred = classifier.predict(X_test)
score = accuracy_score(y_test,y_pred)


