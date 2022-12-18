import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# example np
tab = [[1,2,3],[9,8,7]]
npArray = np.array(tab)
print(npArray.shape)
print(npArray[0])
print(npArray[:,1])

# example plp
plt.plot([1,2,3],[4,6,8]);
plt.title("test",fontsize=20)
plt.xlabel("x axis", fontsize=20)
plt.ylabel("y axis", fontsize=20)
plt.savefig("examplePlp1.png")

# example pd
data = {
  'car':[5,4,1,7],
  'boats':[2,6,0,2]
}

vehicles = pd.DataFrame(data, index=['peter', "sara", 'ali', 'john']);

print(vehicles.info())
print(vehicles.loc['ali'])
