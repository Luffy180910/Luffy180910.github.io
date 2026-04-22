from matplotlib import pyplot as plt
import numpy as np

class Boids:
    def __init__(self, Na, home=[0,0], initial_bound=1):
        self.Na = Na  # agent
        self.d = len(home)
        self.home = np.array(home)
        self.agents = (np.random.random((Na, self.d*2))-0.5)*initial_bound*2
        self.radius_repulsion = 1
        self.radius_alignment = 0.1
        self.radius_repulsion_predator = 10
        self.predators = None
        
    def _pairwise_distances(self, X, Y):
        D = -2 * X @ Y.T + np.sum(Y ** 2, axis=1) + np.sum(X ** 2, axis=1)[:, np.newaxis]
        D[D < 0] = 0
        return D
    
    def set_predators(self, locations):
        self.predators = locations
        
    def _force(self):
        Daa = self._pairwise_distances(self.agents[:,:self.d], self.agents[:,:self.d])
        Neibors_repulsion = (Daa < self.radius_repulsion).astype(int)
        Neibors_alignment = (Daa < self.radius_alignment).astype(int)
        
        Dr = (1/(Daa+np.eye(self.Na))) * Neibors_repulsion
        Fr = np.diag(np.sum(Dr, axis=1))@ self.agents[:,:self.d] - Dr @ self.agents[:,:self.d]
        
        if self.predators is not None:
            Dap = self._pairwise_distances(self.agents[:,:self.d], self.predators[:,:self.d])
            Predator_repulsion = (Dap < self.radius_repulsion_predator).astype(int)      
            Dp = (1/Dap) * Predator_repulsion
            Fp = np.diag(np.sum(Dp, axis=1))@ self.agents[:,:self.d] - Dp @ self.predators[:,:self.d]
        else:
            Fp = 0
        
        Fh = self.home - self.agents[:,:self.d]
    
        Fa = Neibors_alignment @ self.agents[:,self.d:] - 2*self.agents[:,self.d:]
        
        s = 5
        Ff = -np.diag(np.sqrt(np.sum(np.square(self.agents[:,self.d:]), axis=1))- s)/s @ self.agents[:,self.d:]
        
        F_total = 0.5*Fr + 10*Fh + Ff + Fa + 10*Fp
        return 200 * np.tanh(0.1*F_total)
        
    def evolve(self, dt = 0.01):
        self.agents[:,self.d:] += dt*self._force()
        self.agents[:,:self.d] += dt*self.agents[:,self.d:]
        
Na = 30
d = 2
n_history = 10
film = np.zeros((Na, d*n_history))
predator = 0.5*np.array([[np.sin(0.1*t),np.cos(0.1*t)] for t in range(100)])
boids = Boids(Na)    
for t in range(100):
    boids.set_predators(predator[t:t+1])
    boids.evolve()
    film = np.hstack([boids.agents[:,:d], film[:,:-d]])
    if t > n_history:
        plt.figure()
        plt.plot(predator[t,0], predator[t,1],'ro')
        plt.plot(predator[t-n_history:t,0], predator[t-n_history:t,1],'r-',alpha=0.5)
        for i in range(Na):
            plt.plot(film[i,0],film[i,1], 'ko')
            plt.plot(film[i,::2],film[i,1::2], 'k-',alpha=0.5)
        bound = 3
        plt.xlim([-bound,bound])
        plt.ylim([-bound,bound])
        plt.title('t={}'.format(t))
        #plt.savefig('../fig/{}.jpg'.format(t))
        plt.show()
