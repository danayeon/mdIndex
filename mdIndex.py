from file import File
from methods import checkSharp, generateList

file = File(input('ファイルのパスを入力'))
arry = file.read().readlines()
arry_size = list(range(len(arry)))

quote = "```"

index = int(input('目次にする見出しレベルを入力'))

result = {}
q = 0
for i in arry_size:
    if arry[i][0:3] == quote:
        q += 1
    if q == 0:
        idx = 0
        while idx <= 6:
            if checkSharp(arry[i], idx):
                idx += 1
            else:
                break
        if idx <= index and idx > 0:
            result[i] = idx
    if q == 2:
        q = 0

list_type = input('目次のタイプを選択')
list = '# 目次\n'
for k in result:
    list += generateList(arry[k], result[k], list_type)
list += '\n'
arry.insert(0, list)

file.write().writelines(arry)
