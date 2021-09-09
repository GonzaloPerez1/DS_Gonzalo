'''
En el siguiente script podemos encontrar el segundo modelo del trabajo (Artificial Neural Network)
'''

from keras.layers import Dense
from keras.models import Sequential
from data import separacion_train_test
from sklearn.feature_extraction.text import CountVectorizer

def main():
    X_train, X_test, y_train, y_test = separacion_train_test()

    X_train_vec, X_test_vec = data_vectorized(X_train, X_test)

    ann_model = ann(X_train_vec)
    ann_model_train = ann_train(ann_model, X_train_vec, y_train) #Modelo a guardar

    accuracy = ann_comprobations(ann_model_train, X_test_vec, y_test)

    return accuracy

def data_vectorized(X_train, X_test):
    vectorizer = CountVectorizer(max_features = 334, stop_words = 'english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    return X_train_vec, X_test_vec

def ann(X_train_vec):
    ann = Sequential()
    ann.add(Dense(50, input_shape=X_train_vec.shape[1:], activation = 'relu'))
    ann.add(Dense(30, activation = 'sigmoid'))
    ann.add(Dense(10, activation = 'sigmoid'))
    ann.add(Dense(1, activation = 'sigmoid'))

    ann.compile(loss='binary_crossentropy', optimizer='adam',
            metrics=['acc', 'mse', 'mae'])

    return ann

def ann_train(ann_model, X_train_vec, y_train):
    ann_model.fit(X_train_vec.toarray(), y_train, epochs = 10, batch_size = 100, verbose = 0)

    return ann_model

def ann_comprobations(ann_model_train, X_test_vec, y_test):
    prediction = ann_model_train.predict(X_test_vec)
    prediction = list(map(lambda x: 1 if x > 0.5 else 0, prediction))

    accuracy = sum(prediction == y_test) / len(prediction)

    return accuracy