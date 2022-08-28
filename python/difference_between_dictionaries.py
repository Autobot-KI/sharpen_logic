import json

def main(dict_a:dict, dict_b:dict):
	a, b = set(dict_a.items()), set(dict_b.items())
	return {"dict_a": tuple(a-b), "dict_b": tuple(b-a)}

dict_a = {
	"foo": "111", 
	"bar": "222", 
	"foo_bar": "333"
}
dict_b = {
	"foo": "1", 
	"bar": "222", 
	"foo_bar": "3"
}
print(json.dumps(main(dict_a, dict_b), indent=4))