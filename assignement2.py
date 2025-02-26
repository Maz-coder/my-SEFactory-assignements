def merge_dictionaries(dict1,dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

dict1={"a":1,"b":2,"c":3}
dict2={"b":10,"d":5}
print(merge_dictionaries(dict1,dict2))

def word_frequency(sentence):
    words=sentence.split()
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency

sentence="apple orange banana apple orange apple"
print(word_frequency(sentence))

company_employees={
    "Engineering":{
        "Alice" :{"age":30,"role":"Software Engineer"},
        "Bob" :{"age":28,"role":"DevOps Engineer"}
        },
        "HR":{
            "Charlie" :{"age":25,"role":"HR Manager"},
    }
}

print(company_employees["Engineering"]["Alice"]["role"])

company_employees["Engineering"]["David"]={"age":27,"role":"Data Scientist"}

def count_employees(company_dict):
    total=0
    for department in company_dict:
        total+=len(company_dict[department])
        return total

print (count_employees(company_employees))

def invert_dictionary(input_dict):
    return {}

original = {" Alice " : 10, " Bob " : 20, " Charlie " : 10 , " David ":30}
print(invert_dictionary(original))

