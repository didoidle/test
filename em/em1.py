import numpy as np

def EM_step(B, C, D, h, mu, Maximization_step):

    #A = (0.5 * h)/(0.5 + mu)
    B = (mu*h)/(0.5 + mu)
    mu = (B + C) / ( 6 * (B + C + D))

    Maximization_step = np.vstack([mu])
    np.array(Maximization_step)
    Maximization_step = np.sort(Maximization_step, axis = 0)[::-1]
    mu = Maximization_step[0][0]
    return B, mu, Maximization_step

Maximization_step = np.zeros((0,1))
#A = 0.5
B = 0
mu = 0
for i in range(15):
    B, mu, Maximization_step = EM_step(B, mu, Maximization_step)
    print(round(B,5), round(mu,5))
    
    
