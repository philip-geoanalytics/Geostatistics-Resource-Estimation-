# IMPORT DRILLHOLE ASSAY DATA
import pandas as pd

data = pd.read_csv("drillholes.csv")
print(data.head())

# EXPLORATORY DATA ANALYSIS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14, 8))

ax1 = fig.add_subplot(2,2,1)
ax1.hist(data["Au"], bins=10, edgecolor="black")
ax1.set_xlabel("Gold Grade (g/t)")
ax1.set_ylabel("Frequency")
ax1.set_title("Grade Distribution")


# SPATIAL DISTRIBUTION OF GRADES
ax2 = fig.add_subplot(2,2,2, projection ='3d')

scatter = ax2.scatter(
    data["X"],
    data["Y"],
    data["Z"],
    c=data["Au"],
    cmap="viridis"
)

plt.colorbar(scatter, label="Au Grade (g/t)")


# CALCULATE AND MODEL EXPERIMENTAL VARIOGRAMS
from skgstat import Variogram

v = Variogram(
    data[['X','Y','Z']].values,
    data['Au'].values,
    model='spherical'
)

ax3 = fig.add_subplot(2,2,3)
v.plot(axes=ax3)


# VARIOGRAM PARAMETERS
print("Range:", v.parameters[0])
print("Sill:", v.parameters[1])
print("Nugget:", v.parameters[2])


# CREATE BLOCK MODEL
import numpy as np

x = np.arange(100,300,10)
y = np.arange(100,250,10)

xx, yy = np.meshgrid(x,y)

gridx = xx.flatten()
gridy = yy.flatten()

x = x.astype(float)
y = y.astype(float)
 

# ESTIMATE GRADES USING ORDINARY KRIGING
from pykrige.ok import OrdinaryKriging

OK = OrdinaryKriging(
    data['X'],
    data['Y'],
    data['Au'],
    variogram_model="spherical"
)

z_est, ss = OK.execute('grid', x, y)


# GRADE ESTIMATION MAP BASED ON KRIGING INTERPOLATION
ax4 = fig.add_subplot(2,2,4)
img = ax4.contourf(x, y, z_est, cmap='viridis')

plt.colorbar(img, ax=ax4, label='Estimated Grade (g/t)')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_title("Ordinary Kriging Grade Estimate")
plt.tight_layout()
plt.show()


# RESOURCE CALCULATION
block_volume = 10*10*10
density = 2.75
block_tonnage = block_volume*density
total_tonnage = block_tonnage * z_est.size
average_grade = np.mean(z_est)

contained_gold = ( total_tonnage * average_grade)/31.105

print("Total Tonnage: ", total_tonnage)
print("Average Grade: ", average_grade)
print("Contained Gold (oz): ", contained_gold)


# RESOURCE CLASSIFICATION
results = []

for variance in ss.flatten():
    if variance < 0.2:
        results.append("Measured")
    elif variance < 0.5:
        results.append("Indicated")
    else:
        results.append("Inferred")

classified = pd.DataFrame(results, columns=["Classification"])

print(classified)

