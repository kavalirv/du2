
def qd_tree_complete(points):
    if len(points) <= 1:
        print(points)
        return points
    left = 0
    right = len(points)
    mid = int((left+right-1)//2)  # -1 řeší dělění lichých čísel

    #  sort podle x
    points.sort(key=lambda p: p[0])
    lefty_x = points[:mid]
    righty_x = points[mid:]
    middle_x = lefty_x[-1]
    print("Middle point: {}, body před: {}, body za: {}".format(middle_x, lefty_x, righty_x))

    #  sort podle y
    points.sort(key=lambda p: p[1])
    lefty_y = points[:mid]
    righty_y = points[mid:]
    middle_y = lefty_y[-1]
    print("Middle point: {}, body před: {}, body za: {}".format(middle_y, lefty_y, righty_y))

qd_tree_complete([(0.2721733396134992, 0.16110421582040624), (0.5828583727174798, 0.14221065549839018), (0.7408569558116688, 0.836419046573464), (0.3299483355463435, 0.12215068526416473), (0.5610962373889725, 0.3706195830443474)])