import numpy as np


def rot(theta):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    rot_mat = np.array([
        [cos_theta, sin_theta],
        [-sin_theta, cos_theta]
    ])
    return rot_mat


class Model:

    def __init__(self, rot_size, rot_mass, cart_size, cart_mass):
        assert type(rot_size) is tuple and len(rot_size) == 2
        assert type(cart_size) is tuple and len(cart_size) == 2
        cart_size = np.array(cart_size)
        rot_size = np.array(rot_size)
        self.rot_size = rot_size
        self.rot_mass = rot_mass
        self.cart_size = cart_size
        self.cart_mass = cart_mass
        self.q = np.array([0.5, 0])
        self.qdot = np.zeros(2)
        self.M = None
        self.C = None
        self.set_q_and_qdot(self.q, self.qdot)

    def set_q_and_qdot(self, q, qdot):
        assert type(q) is np.ndarray and np.shape(q) == (2,), f"{np.shape(q)}"
        assert type(qdot) is np.ndarray and np.shape(
            qdot) == (2,), f"{np.shape(qdot) == 2}"
        self.q = q
        self.qdot = qdot

        self.cart_pos = (self.q[0], 0.1)
        self.cart_theta = 0
        self.rot_theta = self.q[1]
        self.rot_pos = self.cart_pos + \
            np.matmul(rot(self.rot_theta), np.array([0, self.rot_size[0] / 2]))
        # print(f"cart pos{self.cart_pos}, cart theta {self.cart_theta}")
        # print(f"rot pos{self.rot_pos}, rot theta {self.rot_theta}")
        # # print(f"rot {rot(self.cart_theta)}")
        # print(f"res {np.matmul(rot(self.rot_theta), np.array([0, self.rot_size[0] / 2]))}")
        # exit(0)
    def get_cart_pos_theta(self):
        return self.cart_pos, self.cart_theta

    def get_rot_pos_theta(self):
        return self.rot_pos, self.rot_theta
