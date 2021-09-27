'''
Este script contiene todas las funciones para crear los modelos a contraponer (ANN y Naive-Bayes)
'''

from sklearn import metrics
from sklearn.pipeline import Pipeline
from data import separacion_train_test
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

def main():
    X_train, X_test, y_train, y_test = separacion_train_test()

    bayes_pipe = pipeline_model()
    bayes_parameters = grid_parameters()
    bayes_grid = grid(bayes_pipe, bayes_parameters)
    model_bayes= naive_bayes_best_model(bayes_grid, X_train, y_train)

    naive_bayes_predictions(model_bayes, X_test)
    naive_bayes_comprobations(model_bayes, X_train, X_test, y_train, y_test)

def pipeline_model():
    naive_bayes_pipe = Pipeline(steps = [
        ('vectorizer', CountVectorizer(stop_words='english')),
        ('bayes', MultinomialNB())
    ])

    return naive_bayes_pipe

def grid_parameters():
    naive_bayes_parameters = {
        'vectorizer__max_features': range(80, 400)
    }

    return naive_bayes_parameters

def grid(pipe, parameters):
    bayes_grid = GridSearchCV(pipe, parameters, n_jobs = -1)

    return bayes_grid

def naive_bayes_best_model(bayes_grid, X_train, y_train):
    bayes_grid.fit(X_train, y_train)

    best_model = bayes_grid.best_estimator_

    return best_model

def naive_bayes_predictions(model_bayes, X_test):
    prediction = model_bayes.predict(X_test)
    print(prediction)

def naive_bayes_comprobations(model_bayes, X_train, X_test, y_train, y_test):
    prediction = model_bayes.predict_proba(X_test)

    #fpr: false positie rate; tpr: true positive rate, thresholds: punto de inflexión en la curva AUC
    fpr, tpr, thresholds = metrics.roc_curve(y_test, prediction[:,1]) #Cogemos la probabilidad de que salga 1 (spam)
    auc = metrics.auc(fpr, tpr) #Imprimimos el valor del área bajo al curva AUC

    print('AUC metric:', auc)

    train_score = model_bayes.score(X_train, y_train)
    print('Train accuracy:', train_score)

    test_score = model_bayes.score(X_test, y_test)
    print('Test accuracy:', test_score)

