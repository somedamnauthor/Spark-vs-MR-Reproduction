#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plotdata = pd.DataFrame({

    "3 worker nodes":[10.6608719826,1.70867705345,1.82269310951,1.86218595505,2.20356583595,2.27514505386,2.21374487877,2.65446901321,3.20512604713,3.69746589661],

    "2 worker nodes":[10.6684150696,1.66746115685,1.72490096092,2.055164814,2.16245102882,2.26351499557,2.40443396568,2.70439696312,2.78744697571,4.06963205338]},

    index=["1", "2", "3", "4", "5", "6","7", "8", "9", "10"])


plotdata.plot(kind="bar",figsize=(16, 9))

plt.title("Iteration Times for PageRank")

plt.xlabel("Iteration")

plt.ylabel("Iteration Time(s)")

plt.savefig("PrIter.png")


# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plotdata = pd.DataFrame({

    "Match and Count":[0.750017007192,0.813282966614,0.917782306671,],
    "Substring Match and Count":[0.79069964091,0.911213318507,0.99557463328],
    "Average on 2 columns":[0.846508979797,0.924602588018,0.987661759059,]},
    index=["1.8", "3.6", "5.4"])


plotdata.plot(kind="bar",figsize=(16, 9))

plt.title("Interactive Querying with 2 Workers")

plt.xlabel("Dataset Volume(GB)")

plt.ylabel("Iteration Time(s)")

plt.savefig("iQ2w.png")


# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plotdata = pd.DataFrame({

    "Match Count":[0.743803739548,0.77001007398,0.887545982997],
    "Sub Match Count":[0.815554300944,0.796601613363,0.918606042862],
    "Average":[0.79437661171,0.788803339005,0.941289027532]},
    index=["1.8", "3.6", "5.4"])


plotdata.plot(kind="bar",figsize=(16, 9))

plt.title("Interactive Querying with 3 Workers")

plt.xlabel("Dataset Volume(GB)")

plt.ylabel("Iteration Time(s)")

plt.savefig("iQ3w.png")


# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plotdata = pd.DataFrame({

    "Match Count":[0.798535346985,0.761678298314,0.911639372508],
    "Sub Match Count":[0.476238409678,0.637361288071,0.924573024114],
    "Average":[0.515535354614,0.636542638143,0.829077641169]},
    index=["1.8 GB", "3.6 GB", "5.4 GB"])


plotdata.plot(kind="bar",figsize=(16, 9))

plt.title("Interactive Querying with 3 Workers with Successive Execution of Queries")

plt.xlabel("Dataset Volume(GB)")

plt.ylabel("Iteration Time(s)")

plt.savefig("iQ3ws.png")


# In[ ]:




