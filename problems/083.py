def path(box):
    size = len(box)
    table = {}
    unvisited = []
    for i in range(size):
        for j in range(size):
            table[i, j] = [999999, None, False]
    table[0, 0][0] = box[0][0]
    for poly in range(1):
        map(table)
        temp = []
        min=999999
        for node in table:
            if table[node][2]==False:
                if table[node][0]<min:
                    min=table[node][0]
                    index=node
        print(index)


def map(n):
    if type(n)==dict:
        for i in n:
            print(i, n[i])
        print('-------------------------------')
    else:
        for i in n:
            print(i)
        print('-------------------------------')

mat = [[131, 673, 234], [201, 96, 342], [630, 803, 746]]
map(mat)
path(mat)
