# %%
import networkx as nx
import numpy as np

# %%
lst: list[str] = ['スタイル・レイアウト',
                  'ドライバビリティ',
                  '操縦性',
                  '安定性',
                  '振動',
                  '騒音',
                  '乗心地',
                  '居住性',
                  '視認性',
                  '空調性能',
                  '強度',
                  '耐久性',
                  '整備性',
                  '信頼性',
                  '安全性',
                  '排ガス清浄性',
                  '燃料経済性',
                  'ブレーキ性能',
                  '高速安定性',
                  '登坂力',
                  '加速性',
                  'アフターサービス',
                  '室内の広さ',
                  'ボディサイズ',
                  '旋回性能',
                  'トランクサイズ',
                  '無公害性']
ism_val: np.ndarray = \
    np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 20
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
# print(f"A = \n{arr_a}")

arr_A: np.ndarray = ism_val.astype(bool)
arr_I: np.ndarray = np.eye(len(arr_A), dtype=bool)
arr_B: np.ndarray = arr_A + arr_I
arr_B_old: np.ndarray = arr_B

for n in range(2, 100):
    arr_B_new = arr_B_old @ (arr_A + arr_I)
    if np.array_equal(arr_B_old, arr_B_new):
        break
    arr_B_old = arr_B_new

arr_T: np.ndarray = arr_B_new.astype(int)
print(f"(A + I)^{n - 1} = (A + I)^{n} =\n{arr_T}")
# %%
arr_T_buf: np.ndarray = arr_T
dummy_id = list(range(len(arr_A)))
lev: list[int] = [0] * len(arr_A)

# レベルを抽出
for n in range(1, 100):
    ndel: list[int] = []
    nid: list[int] = []
    for i, l in enumerate(arr_T_buf):
        # i+1列目（対角）以外が0かどうかを判断
        if np.all(np.delete(l, [i], axis=0) == 0):
            ndel.append(i)
    if len(ndel) == 0:
        break
    else:
        # レベル登録
        for i in ndel:
            lev[dummy_id[i]] = n

        # レベル登録した行列を除外
        arr_T_buf = np.delete(arr_T_buf, ndel, axis=0)
        arr_T_buf = np.delete(arr_T_buf, ndel, axis=1)
        dummy_id = np.delete(dummy_id, ndel, axis=0)
print(lev)

# %%
G = nx.DiGraph()

for i, s in enumerate(lst):
    G.add_node(s, subset=lev[i])

for i, l1 in enumerate(ism_val):
    for j, l2 in enumerate(l1):
        if ism_val[i, j] != 0:
            G.add_edge(lst[i], lst[j])
pos = nx.multipartite_layout(G,
                             align="vertical",
                             scale=1,
                             )

nx.draw(G, pos,
        node_color='lightblue',
        with_labels=True,
        font_family='Hiragino Sans')
# %%




G.add_node('冷房能力', subset=1)
G.add_node('冷房入力', subset=2)
G.add_node('圧縮機', subset=3)
G.add_node('熱交換器', subset=3)
G.add_node('筐体長さ1', subset=4)
G.add_node('筐体長さ2', subset=4)
G.add_node('筐体長さ3', subset=4)
G.add_node('筐体長さ4', subset=4)

G.add_edge('冷房能力', '冷房入力')
G.add_edge('冷房入力', '冷房能力')
G.add_edge('冷房入力', '圧縮機')
G.add_edge('冷房入力', '熱交換器')
G.add_edge('熱交換器', '筐体長さ1')
G.add_edge('熱交換器', '筐体長さ2')
G.add_edge('熱交換器', '筐体長さ3')
G.add_edge('熱交換器', '筐体長さ1')
G.add_edge('冷房入力', '筐体長さ1')
G.add_edge('冷房入力', '筐体長さ2')
G.add_edge('冷房入力', '筐体長さ3')
G.add_edge('冷房入力', '筐体長さ4')

pos = nx.multipartite_layout(G)

nx.draw(G, pos,
        node_color='lightblue',
        with_labels=True,
        font_family='Hiragino Sans')
# %%
