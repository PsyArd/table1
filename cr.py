# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() 

# import pandas as pd 
# import numpy as np
# import random 

# lst = ['robot'] *10
# lst += ['human'] *10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst, 'who': [i for i in lst]})
# unique_values = data['whoAmI'].unique()
# for value in unique_values:
#     data[f'is_{value}'] = (data['whoAmI'] == value).astype(int)
# data = data.drop('whoAmI', axis = 1)
# data.head()

# import pandas as pd 
# import numpy as np
# import random 

# lst = ['random'] *10
# lst += ['human'] *10
# random.shuffle(lst)
# print(lst)
# data = pd.DataFrame({'whoAmI':lst, 'robot': [i for i in lst], 'human':[i for i in lst]})
# data['robot'] = data['robot'].map({'robot': 1, 'human': 0})
# data['human'] = data['human'].map({'robot': 0, 'human': 1})
# data.head(20)

import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
 
#==================================================#
data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)