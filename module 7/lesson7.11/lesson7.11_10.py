def actors_sorted_awards(actors: dict):
    'Функция сортирует словарь по количеству наград и возвращает актеров c максимальным и минимальным количеством наград'

    actors = sorted(actors.items(), key=lambda x: x[1], reverse=True)
    max_awards = actors[0]
    min_awards = actors[-1]

    print(f'{max_awards[0]}, {max_awards[1]}')
    print(f'{min_awards[0]}, {min_awards[1]}')

number_actors = int(input())
actors = [input() for actor in range(number_actors)]
actors_awards = {}

for actor in actors:
    if actor not in actors_awards:
        actors_awards[actor] = 1
    else:
        actors_awards[actor] += 1

actors_sorted_awards(actors_awards)
