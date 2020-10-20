import taichi as ti
from render_util import *
from dyna import Model
# configuration
rot_length, rot_kuan = 0.4, 0.1
rot_mass = 1
cart_length, cart_kuan = 0.1, 0.2
cart_mass = 2
frame_id = 0
model = Model((rot_length, rot_kuan), rot_mass,
              (cart_length, cart_kuan), cart_mass)
gui = ti.GUI("id", res=(400, 400))


def update_sim():
    # update robot model
    pass


def render(gui):
    # rot_pos, rot_theta = (0.5, 0.3), frame_id / 100
    # cart_pos = (0.5, 0.5)
    rot_pos, rot_theta = model.get_rot_pos_theta()
    cart_pos, cart_theta = model.get_cart_pos_theta()

    print(f"rot {rot_pos}, {rot_length}, {rot_kuan},  {rot_theta},")
    print(f"cart {cart_pos}, {cart_length}, {cart_kuan},  {cart_theta},")
    # exit()
    draw_box(tuple(rot_pos), rot_length, rot_kuan,  rot_theta, gui)
    draw_box(tuple(cart_pos), cart_length, cart_kuan, 0, gui)
    model.set_q_and_qdot(np.array([0.5 + (frame_id)/1000, frame_id / 100]), np.zeros(2))

while gui.running:

    # 1. update simulation
    update_sim()
    # 2. rendering
    render(gui)
    # 3. post process
    gui.show()
    frame_id += 1
