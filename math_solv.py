from input_a import input_a
from input_dis import input_d
from input_t import input_t
from input_u import input_u
from input_vd import input_vd

def m_solv():
    v = float(input_vd())
    u = float(input_u())
    a = float(input_a())
    dis = float(input_d())
    t = float(input_t())
    s1 = v*t
    s2 = (u*t)+(0.5*a*t*t)

    if s2 >= (s1+dis):
        return True
    else:
        return False
