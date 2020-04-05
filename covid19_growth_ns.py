import matplotlib.pyplot as plt
import numpy as np

date, day, neg, pos, dt = np.loadtxt('covid19_growth_ns_data.csv',
                                     unpack=True,
                                     delimiter=',',
                                     skiprows=1)


plt.subplot(2, 1, 1)
plt.plot(day, neg)
plt.title('Covid19 growth in Nova Scotia')
plt.ylabel('Negatives')
plt.xticks(np.arange(min(day), max(day) + 1, 1.0))

plt.subplot(2, 1, 2)
plt.plot(day, pos)
plt.ylabel('Positives')
plt.xticks(np.arange(min(day), max(day) + 1, 1.0))
plt.xlabel('Days')

# plt.subplot(3, 1, 3)
# plt.plot(d, c)
# plt.ylabel('Con')
# plt.xticks(np.arange(min(d), max(d)+1, 1.0))

# plt.subplot(3, 1, 4)
# plt.plot(d, dt)
# plt.ylabel('Deaths')
# plt.xlabel('Days')
# plt.xticks(np.arange(min(d), max(d)+1, 1.0))

plt.show()
