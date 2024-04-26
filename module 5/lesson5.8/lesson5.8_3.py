numbers_teams_and_matches = int(input())
uniforms_teams = []

for i in range(numbers_teams_and_matches):
    uniforms_teams.append(list(map(int, input().split())))

counter_match = 0

for i in range(numbers_teams_and_matches - 1):
    for j in range(i + 1, numbers_teams_and_matches):
        if uniforms_teams[i][0] == uniforms_teams[j][1]:
            counter_match += 1
        if uniforms_teams[i][1] == uniforms_teams[j][0]:
            counter_match += 1

print(counter_match)
