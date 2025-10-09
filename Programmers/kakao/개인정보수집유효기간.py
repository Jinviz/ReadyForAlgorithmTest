def solution(today, terms, privacies):
    answer = []
    term_list = {}
    MAX_MONTH, MAX_DAY = 12, 28
    t_year, t_month, t_day = map(int, today.split('.'))
    
    for term in terms:
        name, period = term.split()
        term_list[name] = int(period)
        
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        # 유효기간계산
        period = term_list[term]
        year2 = year
        month2 = month + period
        day2 = day - 1
        if day2 == 0:
            day2 = MAX_DAY
            month2 -= 1
        if month2 > MAX_MONTH:
            add_year, month2 = divmod(month2, MAX_MONTH)
            year2 += add_year
        if month2 == 0:
            month2 = MAX_MONTH
            year2 -= 1
        
        # 유효기간검사
        if t_year > year2 or (t_year == year2 and t_month > month2) or (t_year == year2 and t_month == month2 and t_day > day2):
            answer.append(idx+1)
    
    return answer