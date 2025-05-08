import operator
import sys
import typing

BLACK = 0
WHITE = 1


class Point(typing.NamedTuple):
    x: int
    y: int
    i: int

        
class Paper:
    def __init__(self, x0, x1, y0, y1, color):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.color = color
        
    def area(self) -> int:
        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def remove_point(self, point):
        del self.points_in_x_order[point]
        del self.points_in_y_order[point]
        del self.points_in_i_order[point]

    def init_points(self, points):
        points.sort(key=operator.attrgetter('x'))
        self.points_in_x_order = {p: None for p in points}
        points.sort(key=operator.attrgetter('y'))
        self.points_in_y_order = {p: None for p in points}
        points.sort(key=operator.attrgetter('i'))
        self.points_in_i_order = {p: None for p in points}


def split(paper):
    new_color = BLACK if paper.color == WHITE else WHITE
    new_paper = Paper(paper.x0, paper.x1, paper.y0, paper.y1, new_color)

    point_for_split = next(iter(paper.points_in_i_order))
    small = []
    large = []
    if paper.color == WHITE:
        for p1, p2 in zip(paper.points_in_y_order,
                          reversed(paper.points_in_y_order)):
            if p1 == point_for_split:
                points_to_move = small
                paper.y0 = new_paper.y1 = p1.y
                break
            if p2 == point_for_split:
                points_to_move = large
                paper.y1 = new_paper.y0 = p2.y
                break
            small.append(p1)
            large.append(p2)
    else:
        for p1, p2 in zip(paper.points_in_x_order,
                          reversed(paper.points_in_x_order)):
            if p1 == point_for_split:
                points_to_move = small
                paper.x0 = new_paper.x1 = p1.x
                break
            if p2 == point_for_split:
                points_to_move = large
                paper.x1 = new_paper.x0 = p2.x
                break
            small.append(p1)
            large.append(p2)

    for point in points_to_move:
        paper.remove_point(point)
    paper.remove_point(point_for_split)
    paper.color = new_color

    new_paper.init_points(points_to_move)
    return new_paper


w, h = [int(x) for x in sys.stdin.readline().split()]
N = int(sys.stdin.readline())
all_points = []
for i in range(N):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    all_points.append(Point(x, y, i))

min_area, max_area = w * h, 0
paper = Paper(0, w, 0, h, WHITE)
paper.init_points(all_points)
stack = [paper]
while stack:
    paper = stack[-1]
    if not paper.points_in_i_order:
        stack.pop()
        area = paper.area()
        min_area, max_area = min(min_area, area),  max(max_area, area)
        continue
    new_paper = split(paper)
    stack.append(new_paper)

print(max_area, min_area)