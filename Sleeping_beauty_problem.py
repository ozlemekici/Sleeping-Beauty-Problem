# %%
import numpy as np

# %%
N = 100000 #days

# %%
A = np.random.randint(0,2,(N,3))
# 0 : Tails
# 1 : Heads
# 0th col : H or T 
# 1st col : Woken next day:1 or sleeping:0
# 2nd col : put the sleep and woken next day:1 or not:0


# %%
A[A[:,0]==1,0:3] = 1 # if it is T(=0) woken next day 
#if it is H (=1) woken next day then put the sleep and woken next day


# %%
# Since it is asked while awake, 
# we filter the awake:1 in the 2nd and 3rd columns
filt_tot = np.sum(A[:,1]==1) + np.sum(A[:,2]==1)


# %%
# we can find the ratio of the sum of the number of awake states  
# to the sum of the number of column 0ths with Tail
tails_tot = np.sum(A[:,0] == 0)


# %%
prob = tails_tot/filt_tot
print("Probability: ",prob)
