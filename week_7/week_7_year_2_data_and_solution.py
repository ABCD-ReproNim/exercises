# After simulating or downloading the data: set the sample sizes and iterations
start_n = 10
stop_n = 1000
step_n = 20
ns = range(start_n,stop_n,step_n)
iter = 1000

# do the calculations
fin = []
for n in ns:
    print(n)
    temp = eff_size_cal(hippo, iter, n) #utilizes function provided in instructions
    fin.append(temp)
    
fin = pd.concat(fin)


### Plot it!

fig, ax = plt.subplots(3, figsize=(10, 15))
x = fin['n']

# create scatter plots for effect size distributions
ax[0].scatter(x, y = fin['raw_eff'], s=.5, c='r')
ax[1].scatter(x, y = fin['cohen'], s=.5, c='b')
ax[2].scatter(x, y = fin['z'], s=.5, c='g')

# lable plots
ax[0].set_ylabel("Distribution of Raw Effect Sizes")
ax[1].set_ylabel("Distribution of Choen's d")
ax[2].set_ylabel("Distribution of z-scored Cohen’s d")
ax[0].set_xlabel("Sample Size")
ax[1].set_xlabel("Sample Size")
ax[2].set_xlabel("Sample Size")

# plot regression lines to help visualize epectation value trends:
raw_eff_mean = np.polyfit(x, fin['raw_eff'], 1)
raw_eff_p = np.poly1d(raw_eff_mean)
cohen_mean = np.polyfit(x, fin['cohen'], 1)
cohen_p = np.poly1d(cohen_mean)
z_mean = np.polyfit(x, fin['z'], 1)
z_p = np.poly1d(z_mean)

mean_line = ax[0].plot(x,raw_eff_p(x),"r-", label='Mean', c='black')
mean_line = ax[1].plot(x,cohen_p(x),"r-", label='Mean', c='black')
mean_line = ax[2].plot(x,z_p(x),"r-", label='Mean', c='black')
