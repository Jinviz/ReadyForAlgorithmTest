N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = {-1:0, 0:0, 1:0}

def cut_paper(paper):
    first = paper[0][0]
    isAllSamePaper = all(cell == first for row in paper for cell in row)
    if isAllSamePaper:
        result[first] += 1 
        return
    n = len(paper)
    paper[0:3]
    top_section = paper[0:n//3]
    mid_section = paper[n//3:n//3*2]
    bot_section = paper[n//3*2:n]

    cut_paper([row[0:n//3] for row in top_section])
    cut_paper([row[n//3:n//3*2] for row in top_section])
    cut_paper([row[n//3*2:n] for row in top_section])
    cut_paper([row[0:n//3] for row in mid_section])
    cut_paper([row[n//3:n//3*2] for row in mid_section])
    cut_paper([row[n//3*2:n] for row in mid_section])
    cut_paper([row[0:n//3] for row in bot_section])
    cut_paper([row[n//3:n//3*2] for row in bot_section])
    cut_paper([row[n//3*2:n] for row in bot_section])
    
cut_paper(paper)
print(result[-1])
print(result[0])
print(result[1])
