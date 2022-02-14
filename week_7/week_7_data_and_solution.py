import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

### If you have access to the ABCD data, you can read in the data using the following code.
### If not, the code to simulate data or import simulated data from github is included below

# import full data
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


### Simulate data
# male
m_mean = 8407
m_std = 813
m_vol = np.random.normal(m_mean, m_std, 5000)
m_dat = pd.DataFrame(m_vol, columns=['both'])
m_dat['sex'] = 'M'
m_dat.head()


# female
f_mean = 7892
f_std = 775
f_vol = np.random.normal(f_mean, f_std, 5000)
f_dat = pd.DataFrame(f_vol, columns=['both'])
f_dat['sex'] = 'F'
f_dat.head()

# concatenate
hippo = pd.concat([m_dat, f_dat])
# write to tsv
#hippo.to_csv('~/Desktop/ABCD-repronim/exercises/week_7/simulated_data.tsv', sep='\t', index=False)

###importing the data from Github
import requests
import io
    
# Downloading the csv file from your GitHub account

url = "https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_7/simulated_data.tsv" 
# Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')), sep='\t')

### function to calculate effect size for a given sample size
def eff_size_cal(df, niter, n_size):
    raw_eff = []
    cohen = []
    z = []
    for i in range(niter):
        male = df[df['sex']=='M'].sample(n_size)
        female = df[df['sex']=='F'].sample(n_size)
        m_mu = male['both'].mean()
        f_mu = female['both'].mean()
        sigma = (male['both'].std() + female['both'].std())/2
        raw_eff.append(m_mu - f_mu)
        cohen.append((m_mu - f_mu)/sigma)
        z.append((m_mu - f_mu)/(sigma/math.sqrt(n_size*2)))
        
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

### Making simple plots
%matplotlib inline 
#force it to display the figures
plt.scatter(fin['n'], fin['raw_eff'])
plt.scatter(fin['n'], fin['cohen'], color='g')
plt.scatter(fin['n'], fin['z'])
