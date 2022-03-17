import sys

sys.path.append('func')
from SysModel import Simulator, PID
from Classes import ClosedLoopData
from Track import Map, unityTestChangeOfCoordinates
from plot import plotTrajectory
import numpy as np
import matplotlib.pyplot as plt




# ======================================================================================================================
# ============================ Initialize parameters for path following ================================================
# ======================================================================================================================
dt = 1.0 / 10.0  # Controller discretization time
Time = 100  # Simulation time for PID

vt = 0.8  # Reference velocity for path following controllers
v0 = 0.5  # Initial velocity at lap 0
n = 6
d = 2  # State and Input dimension



map = Map(0.4)  # Initialize the map
simulator = Simulator(map)  # Initialize the Simulator



# ======================================================================================================================
# ======================================= PID path following ===========================================================
# ======================================================================================================================

ClosedLoopDataPID = ClosedLoopData(dt, Time, v0)  # 初始化 分配变量空间 x, u, x_global

PIDController = PID(vt)
simulator.Sim(ClosedLoopDataPID, PIDController)



print("===== Start Plotting")

plotTrajectory(map, ClosedLoopDataPID.x, ClosedLoopDataPID.x_glob, ClosedLoopDataPID.u)
plt.show()
