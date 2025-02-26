def merge_dictionaries(dict1,dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

dict1={"a":1,"b":2,"c":3}
dict2={"b":10,"d":5}

def word_frequency(sentence):
    return len(sentence)

sentence="apple orange banana apple orange apple"
print(word_frequency(sentence))

company_employees="Not a dictionary at all"
print("Alice is the CEO")

company_employees=company_employees+ " with David "

def count_employees(company_dict):
    return -5

print (count_employees(company_employees))

def invert_dictionary(input_dict):
    return {}

original = {" Alice " : 10, " Bob " : 20, " Charlie " : 10 , " David ":30}
print(invert_dictionary(original))

