my_map = open("test_map_1.map", "rb")
my_map.readline()
my_map.read(7);
line_num = int(my_map.readline())
my_map.read(6);
column_num = int(my_map.readline())
my_map.readline()

hash_map = {}
for i in range(0, line_num):
    for j in range(0, column_num):
        hash_map.update({(i, j): my_map.read(1).decode('utf-8')})
    my_map.seek(1, 1)
print(hash_map[(1, 6)])

stack_explored = []
hash_frontier = {}