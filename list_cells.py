import json
with open('notebooks/07_playground.ipynb', encoding='utf-8') as f:
    nb = json.load(f)
cells = nb['cells']
for i, c in enumerate(cells):
    cid = c.get('id','')
    ct = c['cell_type']
    src = ''.join(c['source'])[:80].replace('\n',' ')
    print(f"Cell {i} id={cid!r} [{ct}]: {src[:70].encode('ascii','replace').decode()}")
