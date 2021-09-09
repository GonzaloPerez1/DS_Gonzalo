'''
Script principal del proyecto, todos los scripts están interconectados y desembocan en main.py
Para iniciar la descarga de los datos y el entrenamiento del modelo ejecutar en terminal:
`python main.py`
'''

import Naive_Bayes
import ann

nb_auc, nb_train_score, nb_test_score = Naive_Bayes.main()
accuracy = ann.main()

print('\nNAIVE-BAYES')
print('==========================================')
print('AUC:',nb_auc )
print('Train Score:', nb_train_score)
print('Test Score:', nb_test_score)
print('\nARTIFICIAL NEURAL NETWORK')
print('==========================================')
print('Test Score:', accuracy)
