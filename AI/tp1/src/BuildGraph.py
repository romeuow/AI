import importlib

BuildMap = importlib.import_module('BuildMap')

hash_map = BuildMap.build_map()
print(len(hash_map))