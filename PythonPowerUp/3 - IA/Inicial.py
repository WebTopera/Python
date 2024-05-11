# %% [markdown]
# # Projeto Python IA: Inteligência Artificial e Previsões
# 
# ### Case: Score de Crédito dos Clientes
# 
# Você foi contratado por um banco para conseguir definir o score de crédito dos clientes. Você precisa analisar todos os clientes do banco e, com base nessa análise, criar um modelo que consiga ler as informações do cliente e dizer automaticamente o score de crédito dele: Ruim, Ok, Bom

# %%
import pandas as pd

table = pd.read_csv("clientes.csv") # read csv file
table = table.dropna() # remove rows with NaN values
display(table)
display(table.info())

# %%
from sklearn.preprocessing import LabelEncoder # To represent string columns as numbers
# remove string columns, because we can't use them in the model,the AI doesn't understand strings
coder = LabelEncoder()
table['profissao'] = coder.fit_transform(table['profissao'])

table['mix_credito'] = coder.fit_transform(table['mix_credito'])

table["comportamento_pagamento"] = coder.fit_transform(table["comportamento_pagamento"])

display(table.info())

# %%
Y = table["score_credito"] # the result we want to predict

X = table.drop(columns= ["id_cliente","score_credito"]) # the data we will use to predict

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y) # split the data into training and testing data


# %%
# Create AI model
from sklearn.ensemble import RandomForestClassifier # Random Forest Classifier
from sklearn.neighbors import KNeighborsClassifier     # KNeighbors Classifier

# Make AI

model_Forest = RandomForestClassifier()
model_KNN = KNeighborsClassifier()

# Train AI
model_Forest.fit(x_train, y_train)
model_KNN.fit(x_train, y_train)

# %%
# Choose the best model
predict_Forest = model_Forest.predict(x_test)
predict_KNN = model_KNN.predict(x_test)

from sklearn.metrics import accuracy_score

display(accuracy_score(y_test, predict_Forest)) # Compare the results of the model with the real results
display(accuracy_score(y_test, predict_KNN)) 

# %%
# Use the model
new_clients = pd.read_csv("novos_clientes.csv") # read the new clients file
display(new_clients)

coder = LabelEncoder()
new_clients['profissao'] = coder.fit_transform(new_clients['profissao'])

new_clients['mix_credito'] = coder.fit_transform(new_clients['mix_credito'])

new_clients["comportamento_pagamento"] = coder.fit_transform(new_clients["comportamento_pagamento"])

predict = model_Forest.predict(new_clients) # predict the new clients score
display(predict)


