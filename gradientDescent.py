import math
from random import randint

class Function:
    def __init__(self):
        print("Function : ", end = '')
        self.gradient = [0,0]

class Ackley(Function):
    def __init__(self):
        super().__init__()
        self.fun = "-20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2*pi*x) + cos(2*pi*y))) + e + 20"
        print("Ackley")
        
    def getValue(self, X):
        return -20 * math.exp(-0.2 * math.sqrt(0.5 * (X[0]**2 + X[1]**2))) - math.exp(0.5 * (math.cos(2*math.pi*X[0]) + math.cos(2*math.pi*X[1]))) + math.e + 20
        
    def getGradient(self, X):
        self.gradient[0] = math.pi * math.exp((math.cos(2*math.pi*X[0]) + math.cos(2*math.pi*X[1]))/2) * math.sin(2*math.pi*X[0]) + (2**(3/2) * X[0] * math.exp(-math.sqrt(X[0]**2 + X[1]**2)/(5*math.sqrt(2))))/(math.sqrt(X[0]**2 + X[1]**2))
        self.gradient[1] = math.pi * math.exp((math.cos(2*math.pi*X[0]) + math.cos(2*math.pi*X[1]))/2) * math.sin(2*math.pi*X[1]) + (2**(3/2) * X[1] * math.exp(-math.sqrt(X[0]**2 + X[1]**2)/(5*math.sqrt(2))))/(math.sqrt(X[0]**2 + X[1]**2))
        return self.gradient

class Sphere(Function):
    def __init__(self):
        super().__init__()
        self.fun = "x^2 + y^2"
        print("Sphere")
        
    def getValue(self, X):
        return X[0]**2 + X[1]**2
        
    def getGradient(self, X):
        self.gradient[0] = 2*X[0]
        self.gradient[1] = 2*X[1]
        return self.gradient
   
class Rosenbrock(Function):
    def __init__(self):
        super().__init__()
        self.fun = "(1 - x)^2 + 100(y - x^2)^2"
        print("Rosenbrock")
        
    def getValue(self, X):
        return (1 - X[0])**2 + 100*(X[1] - X[0])**2
        
    def getGradient(self, X):
        self.gradient[0] = - 2*(1 - X[0]) - 200*(X[1] - X[0]) 
        self.gradient[1] = 200*(X[1] - X[0])
        return self.gradient
        
class Updater:
    def __init__(self):
        self.moment = [0, 0]
        self.learningRate = 0.001
        self.fraction = 0.9
        
    def getLearningRate(self):
        return self.learningRate
    
    def setLearningRate(self, learningRate):
        self.learningRate = learningRate
        
    def getFraction(self, fraction):
        return self.fraction
       
    def setFraction(self, fraction):
        self.fraction = fraction   
        
    def update(self, x, g):
        x[0] = x[0] - self.learningRate * g[0]
        x[1] = x[1] - self.learningRate * g[1]
        return x
    
    def updateWithMomentum(self, x, g):
        self.moment[0] = self.fraction * self.moment[0] + self.learningRate * g[0]
        self.moment[1] = self.fraction * self.moment[1] + self.learningRate * g[1]
        
        x[0] = x[0] - self.moment[0]
        x[1] = x[1] - self.moment[1]
        #print("Moment:", self.moment)
        return x

class Stopper:
    def __init__(self):
        self.numOfIterations = 0
        self.maxNumOfIterations = 5000
        
    def getNumOfIterations(self):
        return self.numOfIterations
    
    def getMaxNumOfIterations(self):
        return self.maxNumOfIterations
    
    def setMaxNumOfIterations(self, maxNumOfIterations):
        self.maxNumOfIterations = maxNumOfIterations
    
    def shouldStop(self, x, v, g):
        if (self.numOfIterations >= self.maxNumOfIterations or v < math.e**-5):
            return 1
        self.numOfIterations += 1
        return 0
    
    
function = Rosenbrock() # Ackley() or Sphere() or Rosenbrock()

X = [randint(0,10), randint(0,10)]
#X = [5,5]

print("Starting point:", X, "\n")
v = function.getValue(X)
g = function.getGradient(X)

stopper = Stopper()
updater = Updater()

while not (stopper.shouldStop(X, v, g)):
    #print("Gradient :", g)
    #print("Point :", X)
    #print(v, "->", end=" ")
    
    g = function.getGradient(X)
    
    X = updater.update(X, g)
    #X = updater.updateWithMomentum(X, g)
    
    v = function.getValue(X)
    
    
print("\nEnding point:", X)
print("Ending value:", function.getValue(X))
print("number of iterations:", stopper.getNumOfIterations())
