import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    #d = 2*5.2 + 4 * 6.7 + 6 * 9.1 + 8 * 10.9
    #print(d)
    #e = 2*5.2 + 2*6.7 +2*9.1 + 2*10.9
    #print(e)
    x = np.ndarray((4,1))
    y = np.ndarray((4,1))
    x[0,0] = 1
    x[1,0] = 2
    x[2,0] = 3
    x[3,0] = 4
    y[0,0] = 5.2
    y[1,0] = 6.7
    y[2,0] = 9.1
    y[3,0] = 10.9
    A = np.ndarray((2,2))
    A[0,0] = 60
    A[0,1] = 20
    A[1,0] = 20
    A[1,1] = 8
    ainv = np.linalg.inv(A)
    z = np.ndarray((2,1))
    z[0,0] = 179
    z[1,0] = 63.8
    res = np.dot(ainv,z) # a = res[0,0] and b=[1,0]
    print(res)

    # do a scatter plot of the data
    area = 10
    colors =['black']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    plt.title('Linear Least Squares Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    #plot the fitted line
    yfitted = x*res[0,0] + res[1,0]
    line,=plt.plot(x, yfitted, '--', linewidth=2) #line plot
    line.set_color('red')
    plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
