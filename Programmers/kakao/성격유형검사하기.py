def solution(survey, choices):
    answer = ''
    types = ['R','T','C','F','J','M','A','N']
    type_score = {type: 0 for type in types}
    I_DONT_KNOW = 4
    
    for idx, choice in enumerate(choices):
        left, right = survey[idx][0], survey[idx][1]
        if choice < I_DONT_KNOW:
            type_score[left] += I_DONT_KNOW-choice
        elif choice > I_DONT_KNOW:
            type_score[right] += choice-I_DONT_KNOW
    
    for n in range(4):
        type1, type2 = types[n*2], types[n*2+1]
        type_score[type1]
        if type_score[type1] > type_score[type2]:
            answer += type1
        elif type_score[type1] < type_score[type2]:
            answer += type2
        elif type_score[type1] == type_score[type2]:
            answer += type1
    
    return answer