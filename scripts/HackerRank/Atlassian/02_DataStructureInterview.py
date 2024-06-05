


class TeamScore:
    name = ""
    score = 0
    
    def __init__(self, name, score=0) -> None:
        self.name = name
        self.score = score
        

def getResults(ballots):
    res_dict = {}
    eps = 0.000001
    cur_eps = 0
    
    # work out the number of team
    team_set = set()
    for ballot in ballots:
        for t_name in ballot:
            if t_name not in team_set:
                team_set.add(t_name)
    n_team = len(team_set)
    
    # process the result
    for ballot in ballots:
        # cur_eps += eps
        # cur_eps = eps * len(ballot)
        cur_eps = eps
        cur_score = n_team
        for t_name in ballot:
            if t_name not in res_dict:
                res_dict[t_name] = TeamScore(t_name, cur_score - cur_eps)
            else:
                res_dict[t_name].score += cur_score - cur_eps
            
            # reduce score by 1 until it reached 0 (i.e. 3, 2, 1, 0, 0, 0 ...)
            if cur_score > 0:
                cur_score -= 1
    
    # sort the result from largest to smallest
    res_list = list(res_dict.values())
    res_list.sort(key = lambda x: x. score, reverse=True)
    
            
    # return result
    return [x.name for x in res_list]


# O(m * n)
# m: number of ballots
# n: number of team

ballots = []
# ballots.append(['A'])
# ballots.append(['B'])
# print(getResults(ballots))

ballots.append(['A']) -> 3 - eps
ballots.append(['C', 'B']) -> 2 - eps
ballots.append(['D', 'E', 'B']) -> 1 - eps

A: 3 - eps
B: 3 - 2*eps
print(getResults(ballots))

# ballots.append(['A', 'C', 'D'])
# ballots.append(['B'])
# print(getResults(ballots))

# per_1 = ['A']
# per_2 = ['B']
# --> ['A', 'B']


# per_1 = ['A', 'C', 'D', 'B', 'F']
# per_1 = ['A', 'C', 'D']
# per_2 = ['B']
# ==> ['A', 'C', 'B']