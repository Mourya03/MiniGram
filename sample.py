from numpy.lib.function_base import _extract_dispatcher
from functions import *
from structure import *
from main import *

Data = import_data()
ind = 0

curr_acc = Account(Data.iloc[ind]['Username'],Data.iloc[ind]['Name'],Data.iloc[ind]['Password'],
            Data.iloc[ind]['Phone'],Data.iloc[ind]['Followers'],Data.iloc[ind]['Following'],Data.iloc[ind]['Feed'],ind)

#curr_acc.add_Feed(Data)

print(curr_acc.Feed)

#curr_acc.add_Feed(Data)

print(curr_acc.Feed)

Data = curr_acc.to_DataFrame(Data,ind)

print(Data)

export(Data)