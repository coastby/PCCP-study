# [programmers] Lever.3 베스트 앨범

"""
6:6
1. `"genre" : [(재생횟수, 고유번호)]` 형태로 genres와 plays를 loop를 돌며 딕셔너리를 채운다.
2. 만들어진 딕셔너리를 돌며 장르 당 총 재생횟수를 저장하기 위해 `(총 재생횟수, 장르)` 형태로 리스트를 만든다.
3. 이 리스트를 내림차순으로 정렬한다.
4. 리스트를 순회하며 딕셔너리에서 장르의 `(재생횟수, 고유번호)` 리스트를 가져온다.
5. 장르 당 노래 리스트를 내림차순으로 정렬한다.
    1. 첫 번째, 두번째 원소를 가져온다.
        1. 두번째 원소가 없으면 첫번째 원소만 answer에 등록한다.
    2. 첫 번째 원소와 두 번째 원소의 재생횟수가 같으면 고유번호가 낮은 두번째 원소를 먼저 등록하고 첫번째를 등록한다.
    3. 같지 않으면 순서대로 등록한다.
"""

def solution(genres, plays):
    g_list = {}     #"genre" : [(재생횟수, 고유번호)]

    for i in range(len(genres)):
        if genres[i] not in g_list:
            g_list[genres[i]] = []
        g_list[genres[i]].append((plays[i], i))


    g_play = [] #(총재생횟수, 장르)
    for g in g_list:
        g_num = 0
        for s_play in g_list[g]:
            g_num += s_play[0]
        g_play.append((g_num, g))

    g_play.sort(reverse = True)


    answer = []

    for i in range(len(g_play)):
        g = sorted(g_list[g_play[i][1]], key=lambda m: (-m[0], m[1]))
        answer.append(g[0][1])
        try:
            answer.append(g[1][1])
        except:
            pass

    return answer