# What does it take to succeed?

There is no clear answer to this question. Some studies suggest that intelligence is a factor in success, but it is not the only one. According to a BBC article, multiple psychological factors contribute to feats of creativity and insight.  On the other hand, a Scientific American article suggests that luck and opportunity may play a far greater role than we ever realized, across a number of fields, including financial trading, business, sports, art, music, literature, and science.

While it is difficult to run a social experiment on it, we can run a simulation to find out more. We implement a simple python program to test. We start with the following:

* A population of 1000 sims, with IQ between 0 and 1 in normal distribution.

* Each sim has 100 to start with

We run 40 rounds of "life events". In each turn, just like monopoly, a sim would get 100 in the first 20 rounds.   In each turn, a sim could be lucky, unlucky or so-so. A lucky event is one in which the sim gets an amount of 100 x IQ.  That is the smarter you are, the more you get. A sim might be unlucky in which the sim loss 50% of the amount it owns. A so-so events is like normal daily life, nothing happens.

We plot the results of the wealth distribution as a histogram. Very few sims get to the wealth level of 2000+. Wealth of most sims skews to the left, which is similar to real life.
![wealth histogram](https://github.com/siufai6/life-simulated/blob/main/wealth_hist.png)
We plot these two against wealth levels. Clearly, higher IQ does not always guarantee more wealth/success. Even some of the  slightly lower IQ sims are doing OK.
![IQ vs Wealth](https://github.com/siufai6/life-simulated/blob/main/iq_wealth.png)
Next we try to see what role does luck holds? It is a bit more clear and the trend could be easily spotted. The luckier the sim, the more wealth the sim got, in general
![luck vs wealth](https://github.com/siufai6/life-simulated/blob/main/luck_wealth.png)
If we zoom in to the last 5 rounds, the effect is even more prominent. It became very obvious that luck plays an important role. 
![last 5 rounds](https://github.com/siufai6/life-simulated/blob/main/last5.png)
In addition, another factor is the sequence of events. If a sim has a series of unlucky events happening to it, this hugely impact its wealth level. 

## So, what is the take away?

* Don't do stupid things.  
* Try to maximize your luck. How?
  - meet new people, goto new places.
  - Be curious about life, explore, learn.
  - Be optimistic, avoid people who would drag you down.
* preliminary results shows a basic income for all the sims could help some of the unfortunate ones, more work needed on this later.
