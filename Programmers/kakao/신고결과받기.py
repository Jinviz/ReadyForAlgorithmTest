import copy

def solution(id_list, report, k):
    mail = {id: 0 for id in id_list}
    receive_ben = {id: set() for id in id_list}
    
    for ben in report:
        poster, receiver = ben.split()
        receive_ben[receiver].add(poster)
    
    for key,values in receive_ben.items():
        if len(values) >= k:
            for poster in values:
                mail[poster] += 1
    
    return list(mail.values())