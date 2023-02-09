import os 
import yaml
import sys

# join the path in Unix style
def pjoin(*path_list):
    return "/".join(path_list)

# recursively list the file and generate mkdocs.yml
# you can set the order when order = 1
def dfs_find(fa, fa_list, pre, order, argv_list):

    pa = pjoin(pre, fa)

    print ("Get into ", pa)

    for _, dirs, fs in os.walk(pa):
        break
    fs = list(filter(lambda t: t != ".order", fs))
    print("files: ", fs)

    all_list = []
    all_list = all_list + dirs
    all_list = all_list + fs
    
    print ("all_list is: ", all_list)
    
    order_list = []
    if (os.path.exists(pjoin(pa, ".order"))):
        with open(pjoin(pa, ".order"), "r") as order_file:
            order_list = order_file.read().split()
    print("order_list is: ",order_list)
    
    notin_list = list(filter(lambda t: t not in order_list, all_list))
    notin_list = sorted(notin_list, key = lambda t: os.stat(pjoin(pa, t)).st_ctime)

    order_list = order_list + notin_list
    lenth = len(order_list)
    print("#files: ", lenth)

    if (order and ((fa in argv_list) or (not argv_list))):
        while 1:
            os.system("cls")
            new_order_list = [i for i in range(0, lenth)]
            print("The current order of files in ", pa)
            for node, cnt in enumerate(order_list):
                print (node, cnt)
            command = input("Change the order:\n \
1. sw a b ---- swap ath and bth\n \
2. up a   ---- up ath\n \
3. dn a   ---- down ath\n \
4. input a whole new order (should be a permutation), say a, b, c, then ath file would be in the first place then\n \
5. e      ---- exit\n \
6. ea     ---- exit for all\n")
            commands = command.split()
            print(commands)
            if (commands[0] == "e"):
                print ("exit")
                break
            
            elif (commands[0] == "ea"):
                print ("exit")
                order = False
                break

            elif (commands[0] == "sw"):
                if (commands[1].isdigit() and commands[2].isdigit()):
                    a, b = int(commands[1]), int(commands[2])
                    if (a >= 0 and a < lenth and b >= 0 and b < lenth):
                        order_list[a], order_list[b] = order_list[b], order_list[a]
                    
            elif (commands[0] == "up"):
                if (commands[1].isdigit()):
                    a = int(commands[1])
                    if (a >= 1 and a < lenth):
                        order_list[a], order_list[a - 1] = order_list[a - 1], order_list[a]

            elif (commands[0] == "dn"):
                if (commands[1].isdigit()):
                    a = int(commands[1])
                    if (a >= 0 and a < lenth - 1):
                        order_list[a], order_list[a + 1] = order_list[a + 1], order_list[a]
            
            else:
                if (all(t.isdigit() for t in commands)):
                    num_list = [int(t) for t in commands]
                    counter = [t in num_list for t in range(0, lenth)]
                    if (len(num_list) == lenth and all(t == True for t in counter)):
                        for i, cnt in enumerate(num_list):
                            new_order_list[cnt] = order_list[num_list[i]]
                        order_list = new_order_list

    for node in order_list:
        if (os.path.isdir(pjoin(pa, node))):
            dir_list = []
            dfs_find(node, dir_list, pa, order, argv_list)
            dir_dict = {node: dir_list}
            fa_list.append(dir_dict)
        if (os.path.isfile(pjoin(pa, node))):
            file_dict = {os.path.splitext(node)[0] \
                if os.path.splitext(node)[0] != "index"\
                else fa: pjoin(pa, node)[7:]}
            if (node == "index.md"):
                fa_list.insert(0, file_dict)
            else:
                fa_list.append(file_dict)
    with open(pjoin(pa, ".order"), "w+") as order_file:
        for node in order_list:
            order_file.write(node + " ")


# 打开yml文件，读取文件数据流
f = open("mkdocs.yml","r", encoding="utf-8")
ayml=yaml.load(f.read(), Loader=yaml.Loader)
f.close()

default = {'RABBIT': [{'ME': 'index.md'}]}
ayml["nav"] = [default]

argv_list = sys.argv[2:]

dfs_find("posts", ayml["nav"], "./docs", len(sys.argv) > 1 and sys.argv[1] == "order", argv_list)

for rt, dirs, files in os.walk('./docs/posts'):
    break 

print (ayml["nav"])


f = open("mkdocs.yml","w", encoding="utf-8")
yaml.dump(ayml, f)
f.close()