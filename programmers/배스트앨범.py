genres = ["classic", "pop", "classic", "classic", "pop","sexy"]
plays = [500, 600, 150, 800, 2500, 1700]

def solution(genres, plays):
    answer = []
    genre_play_dict = {}

    zipped = list(zip(genres,plays))
    zipped.sort(reverse=True)
    print(zipped)

    for genre, play in zipped:
        if genre not in genre_play_dict:
            genre_play_dict[genre] = 0
        genre_play_dict[genre] += play
    genres_rank = sorted(genre_play_dict, key=genre_play_dict.get,reverse=True)
    zipped.sort(key=lambda x: genres_rank.index(x[0]))

    print(genre_play_dict)
    print(genres_rank)
    print(zipped)
    



    
    # for i in genres:
    #     album[i] = 0
    # print(album)

    # for i in range(len(genres)):
    #     album[genres[i]] += plays[i]
    # print(album)

    # n_album = sorted(album.keys(), key=(lambda x: album[x]), reverse=True)
    # print("앨범:", n_album)

    
    # for i in n_album:
    #     q = []
    #     for j in range(len(genres)):
    #         if i==genres[j]:
    #             q.append(plays[j])
    #     print(q)
    #     answer.append(plays.index(max(q)))
    #     q.remove((max(q)))
    #     answer.append(plays.index(max(q)))
    #     print(answer)
        
    return answer


solution(genres,plays)