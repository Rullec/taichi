import numpy as np
def draw_box(pos, length, kuan, theta, gui):
    x_max, x_min = kuan/2, -kuan/2
    y_max, y_min = length/2, -length/2
    # place a box in the origin point
    p_lst = [[x_max, y_max],
             [x_max, y_min],
             [x_min, y_min],
             [x_min, y_max]]

    # rotate
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    rot_mat = np.array([
        [cos_theta, sin_theta],
        [-sin_theta, cos_theta]
    ])

    # translate
    p_lst = [(np.matmul(rot_mat, np.array(i))).tolist()
             for i in p_lst]
    p_lst = [[i[0] + pos[0], i[1] + pos[1]] for i in p_lst]

    # draw
    gui.line(p_lst[0], p_lst[1])
    gui.line(p_lst[1], p_lst[2])
    gui.line(p_lst[2], p_lst[3])
    gui.line(p_lst[3], p_lst[0])
