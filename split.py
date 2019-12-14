from quadtree import qd_tree_complete
import json
with open("export.geojson", "r",encoding='utf-8') as f:
    data = json.load(f)

# vytiskne data a vytvoří seznam pro souřadnice, který vstoupí do qd_tree
print(data)
coord = []

# vytáhne souřadnice z dat a vytiskne je
for feat in data['features']:
    u = feat['geometry']['coordinates']
    coord.append(u)


print(coord)

# aplikuje soubor a souřadnice do qd_tree

qd_tree_complete(coord)
