graph = {
    'a': {'b': 1, 'c': 2, 'd': 3},
    'b': {'a': 1, 'c': 5},
    'c': {'a': 2, 'b': 5, 'd': 5, 'e': 5, 'f': 2, 'g': 4},
    'd': {'a': 3, 'c': 5, 'g': 4},
    'e': {'b': 3, 'c': 5, 'f': 3, 'h': 2},
    'f': {'c': 2, 'e': 3, 'g': 4, 'h': 1},
    'g': {'c': 4, 'd': 4, 'f': 4, 'h': 2},
    'h': {'e': 2, 'f': 1, 'g': 2, "i": 5, 'j': 5, 'k': 3},
    'i': {'h': 5, 'k': 4},
    'j': {'h': 5, 'k': 3},
    'k': {'h': 3, 'i': 4, 'j': 3}
}


def djikstra(graph, start, end):
    shortways = {}  # ทางที่สั้นที่สุด
    back = {}  # ทางกลับบ้าน (จุดstart )
    unseenNodes = graph  # จุดที่ยังไม่ได้ดำเนินการ
    inf = 9999999
    path = []  # ทางที่เคยผ่านไปแล้ว

    # สร้างways ให้เป็น infinity เพื่อมาแก้ไขหาค่าน้อยสุเ
    for node in unseenNodes:
        shortways[node] = 9999999
        shortways[start] = 0

    while unseenNodes:
        mindis = None

        # เช็คในทางเดินว่าไปทางไหนง่ายสุด
        for node in unseenNodes:
            if mindis is None:
                mindis = node
            elif shortways[node] < shortways[mindis]:
                mindis = node

        pdict = graph[mindis].items()

        # เช็คว่าผลรวมน้ำหนักของทางที่เดินน้อยกว่าทางที่เดินกลับบ้าน
        for node1, w in pdict:
            if w + shortways[mindis] < shortways[node1]:
                shortways[node1] = w + shortways[mindis]
                back[node1] = mindis

        unseenNodes.pop(mindis)

    now = end
    while now != start:
        path.insert(0, now)
        now = back[now]
        
    path.insert(0, start)
    if shortways[end] != inf:
        print(str(shortways[end]) + " " + (str(path)))


djikstra(graph, 'a', 'k')
