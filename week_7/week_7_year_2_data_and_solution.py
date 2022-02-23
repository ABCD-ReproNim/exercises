import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

### Option 1: Read + parse ABCD data
### If you have access to the ABCD dataset, you can read in and parce the data using the following code.
### If you are not downloading this data, skip to the next section (option 2) where code is provided to simulate or import data from github.

# import full data (note you must have already downloaded abcd_smrip201.txt -- update the below path to your local version)
smrip201_file = '/home/jovyan/ABCD3/abcd_smrip201.txt'
smrip201 = pd.read_csv(smrip201_file, sep='\t',skiprows=[1],header=[0])

# subset to only include columns of interest
columns = ['subjectkey','sex','smri_vol_scs_hpuslh','smri_vol_scs_hpusrh']
hippo = smrip201.loc[:,columns]
# sum left and right hippocampi
hippo['both'] = hippo['smri_vol_scs_hpuslh'] + hippo['smri_vol_scs_hpusrh']
# make names easier to read
hippo.rename(columns={'smri_vol_scs_hpuslh':'left','smri_vol_scs_hpusrh':'right'},inplace=True)
hippo.head()


### Option 2: Simulate data
### If you choose to instead download this same simulated data from our GitHub skip to the next section (option 3) 
### The below code simulates structural MRI data across 10000 individuals based on the ABCD data element abcd_smrip201
### "hippocampi" column represents the simulated sum total volume in mm^3 of two ROIs located in the left and right hippocampus.

# male
m_mean = 8407
m_std = 813
m_vol = np.random.normal(m_mean, m_std, 5000)
m_dat = pd.DataFrame(m_vol, columns=['hippocampi'])
m_dat['sex'] = 'M'
m_dat.head()

# female
f_mean = 7892
f_std = 775
f_vol = np.random.normal(f_mean, f_std, 5000)
f_dat = pd.DataFrame(f_vol, columns=['hippocampi'])
f_dat['sex'] = 'F'
f_dat.head()

# concatenate
hippo = pd.concat([m_dat, f_dat])


### Option 3: Importing the simulated data from Github
import requests
import io
    
# Download the csv file from GitHub
url = "https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_7/simulated_data.tsv" 
# Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
# Read in the downloaded content and turn it into a pandas dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')), sep='\t')


### Examine relationship between effect size and sample size 

# Function to calculate effect size for a given sample size
def eff_size_cal(df, niter, n_size):
    raw_eff = []
    cohen = []
    z = []
    for i in range(niter):
        male = df[df['sex']=='M'].sample(n_size)
        female = df[df['sex']=='F'].sample(n_size)
        m_mu = male['hippocampi'].mean()
        f_mu = female['hippocampi'].mean()
        #pooled standard deviation for males and females
        # here: same number of male and female, hence just averaging the two variance
        # if not same sample size, do a proportional weighting
        pooled_var = ((male['hippocampi'].std())**2 + (female['hippocampi'].std())**2)/2
        sigma = math.sqrt(pooled_var)
        raw_eff.append(m_mu - f_mu)
        cohen.append((m_mu - f_mu)/sigma)
        # to be exact, variance of the difference of the means : v(m - f) = v(m) + v(f) - 2cov(f,m) 
        # we assume data are independant between m and f
        # hence v(m-f) = 2*sigma**2 / n_size 
        z.append( ((m_mu - f_mu)/(math.sqrt(2)*sigma)) / math.sqrt(n_size))
        
    results = pd.DataFrame(list(zip(raw_eff,cohen,z)), columns=['raw_eff','cohen','z'])
    results['n'] = n_size
    
    return results


# set the sample sizes and iterations
start_n = 10
stop_n = 1000
step_n = 20
ns = range(start_n,stop_n,step_n)
iter = 1000

# do the calculations
fin = []
for n in ns:
    print(n)
    temp = eff_size_cal(hippo, iter, n)
    fin.append(temp)
    
fin = pd.concat(fin)


### Plot it!

# force it to display the figures
%matplotlib inline 

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
