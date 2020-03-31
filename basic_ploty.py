import matplotlib.pyplot as plt
import pandas


provision = ['Ontario','Alberta','British Columbia','Manitoba','Saskatchewan',"Nunavut",'Northwest Territories','Quebec','Nova Scotia','New Brunswick','Prince Edward Island','Yukon','Newfoundland and Labrador']
populations = [14446515,4345737,5020302,1360396,1168423,38787,44598,8433301,965382,772094,154748,40369,523790]
cases = [1706,690,960,96,175,0,1,3430,127,68,18,5,148]
fig,axs = plt.subplots(2)
# fig.suptitle("")
axs[0].plot(provision,populations,'r--',label = "Population")
axs[1].plot(provision,cases,'g^',label = "Cases")
axs[0].legend()
axs[1].legend()
plt.xlabel("Provisions")


plt.title("Populations vs Cases")

plt.show()