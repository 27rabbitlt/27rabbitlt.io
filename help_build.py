import os 
import yaml

for rt, dirs, _ in os.walk('./docs/posts'):
    break 

# 打开yml文件，读取文件数据流
f = open("mkdocs.yml","r", encoding="utf-8")
ayml=yaml.load(f.read(),Loader=yaml.Loader)
f.close()

print(ayml["nav"])

default = {'RABBIT': [{'ME': 'index.md'}]}
ayml["nav"] = [default]

prefix = 'posts'
dir = 'ALGO'

print (os.path.join(prefix, dir))

for dir in dirs:
    dir_list = []
    dir_dict = {dir: dir_list}
    for _, _, fs in os.walk(os.path.join(rt, dir)):
        break
    for file in fs:
        file_dict = {os.path.splitext(file)[0] \
            if os.path.splitext(file)[0] != "index"\
            else dir: os.path.join("posts", dir, file)}
        dir_list.append(file_dict)
    ayml["nav"].append(dir_dict)

print (ayml["nav"])


f = open("mkdocs.yml","w", encoding="utf-8")
yaml.dump(ayml, f)
f.close()