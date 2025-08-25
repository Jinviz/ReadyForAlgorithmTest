N = int(input())
paper =[list(map(int, input().split())) for _ in range(N)]
blue_paper = 0
white_paper = 0

def check_paper_color(p):
    global blue_paper, white_paper
    is_blue_paper = False
    is_white_paper = False
    for row in p:
        if 0 in row:
            is_white_paper = True
        if 1 in row:
            is_blue_paper = True

    # 한가지 색종이만 있는 경우 + 색종이가 하나인 경우
    if is_white_paper and not is_blue_paper:
        white_paper += 1
    if is_blue_paper and not is_white_paper:
        blue_paper += 1

    # 두가지 색종이가 있는 경우 -> 색종이 분리(재귀 호출))
    n = len(p[0])
    if is_white_paper and is_blue_paper:
        top_p = p[0:n//2]
        bottom_p = p[n//2:n]

        p1 = [row[0:n//2] for row in top_p]
        p2 = [row[n//2:n] for row in top_p]

        p3 = [row[0:n//2]  for row in bottom_p]
        p4 = [row[n//2:n] for row in bottom_p]

        check_paper_color(p1)
        check_paper_color(p2)
        check_paper_color(p3)
        check_paper_color(p4)

check_paper_color(paper)
print(white_paper)
print(blue_paper)