import json

# print(dir(json))


with open('test1.json','r') as file,open('test1.json','a') as file2:
    data = file.read()
    print(type(data))

    mod = json.loads(data)
    print(type(mod))


    mod['Country P'] = 'ABC'
    for k,v  in mod.items():
        print(k,v)

    dumps_mod = json.dumps(mod)
    print(type(dumps_mod))

    file2.write(dumps_mod)




