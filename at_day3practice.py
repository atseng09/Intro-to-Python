#%%

my_string = "The fox jumped over the lazy dog"

def string_operator (string: str, method="capitalize") -> str:
    if method == "title":
        return my_string.title()
    elif method == "lower":
         return my_string.lower()
    elif method == "upper":
        return my_string.upper()
    else:
        return my_string.capitalize() 
    
    print(string_operator(my_string, method="title"))
    print(string_operator(my_string, method="lower"))
    print(string_operator(my_string, method="upper"))
    print(string_operator(my_string, method="capitalize"))

# %%
def tip_calculator(bill: float, percent: float, parties: int):
     if percent > 1:
         percent = percent/100 
     tip = bill * percent
     total = bill + tip
     split = total / parties

     return total, tip, split
total, tip, split = tip_calculator(100, 20, 3)
# %%

bill = {
    "Daniel": 14,
    "Darcy": 20,
    "Ben": 40
}

def split_calculator(bill: dict, percent: float, tax: float):
   if tax > 1:
    tax = tax / 100

    if percent > 1:
     percent = percent / 100

    total = sum(list(bill.values()))
    
    for k in bill.keys():
        bill[k] = bill[k] / total
    
    tax = total * tax
    total += tax

    tip = total * percent
    total += tip

    for k in bill.keys():
        bill[k] = round(bill[k] * total, 2)
    
    return bill
   
   split_calculator(bill, 20, 8)

   #%%
lower = lambda string: string.lower()

    #%%
exponent = lambda num, root: num**root

   #%%
my_list = my_string.split(" ")
my_list2 = [x.title() for x in my_list]
#%%
my_numbers = [x for x in range (0,11)]
my_numbers = ["even" if x%2<1 else "odd" for x in my_numbers]

# %%
import random

random_list = [random.randint(0, 100)for x in range(0,11)]
def number_sorter(a_list):
    sorted_list = []

    for i in a_list:
        if len(a_list) == 0:
            sorted_list.append(i)
        else:
            if i > a_list[len(a_list)//2]:
                a_list.append(i)
            # else:
            #     a_list

#%%
example = {
    "First": "Alison",
    "Last": "Tseng",
    "Age": 17
}
def lower_dictionary(dictionary): 
    new_dict = {}
    for key in dictionary:
        new_dict[key.lower()] = dictionary[key]

    return new_dict

examples = lower_dictionary(example)
        

# %%
