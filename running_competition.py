def solution(players, callings):
    answer = []
    rank = []
    for i in range(len(players)):
        rank.append(i+1)

    rank_to_player = dict(zip(rank, players))
    player_to_rank = dict(zip(players, rank))

    print(rank_to_player)
    print(player_to_rank)
    for i in range(len(callings)):
        print(i, player_to_rank)
        rank = player_to_rank[callings[i]]
        player_to_rank[rank_to_player[rank-1]] += 1
        player_to_rank[rank_to_player[rank]] -= 1
        tmp = rank_to_player[rank]
        rank_to_player[rank] = rank_to_player[rank-1]
        rank_to_player[rank-1] = tmp
        print(i, player_to_rank)

    arr = dict(sorted(player_to_rank.items(), key=lambda x: x[1])) 
    return list(arr.keys())

solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])