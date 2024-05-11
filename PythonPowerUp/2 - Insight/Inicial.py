# %% [markdown]
# # Python Insights - Analisando Dados com Python
# 
# ### Case - Cancelamento de Clientes
# 
# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.
# 
# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

# %%
# !pip install pandas plotly numpy openpyxl nbformat ipkernel 
# install library with ! to use the jupyter celule
import pandas as pd

table = pd.read_csv('cancelamentos_sample.csv') # read csv file
table = table.drop(columns=['CustomerID']) # remove a unnecessary column
display(table)

# %%
table = table.dropna() # remove rows with missing values

# display(table.info()) # show the data type of each column

display(table["cancelou"].value_counts(normalize=True)) # show the count of each value in the column in percentage

# %%
import plotly.express as px # import the library to plot the graph

color_map = {0.0: '#1f77b4', 1.0: '#d62728'} # create a color map to use in the graph

for coluna in table.columns:
    if coluna == 'cancelou':
        continue
    graph = px.histogram(table, x=coluna, color='cancelou', color_discrete_map=color_map) # create a histogram with the data
    graph.show()


# %%
# clientes com contrato mensal cancelam mais
     # oferecer desconto em outros tipos de contratos

table = table[table["duracao_contrato"] != 'Monthly']
display(table["cancelou"].value_counts(normalize=True))

# clientes com mais ligações no callcenter cancelam mais
     # melhorar o atendimento
     # alertar quando tem mais 3 ligações
table = table[table["ligacoes_callcenter"] <= 3]
display(table["cancelou"].value_counts(normalize=True))
# clientes com atraso de mais de 20 dias cancelam mais
     # acompanhamento para evitar atrasos
table = table[table["dias_atraso"] <= 20]
display(table["cancelou"].value_counts(normalize=True))




