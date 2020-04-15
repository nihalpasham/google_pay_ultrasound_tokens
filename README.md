# Reverse engineering Google pay's -Tez mode

Context: 
Google pay (Tez-mode) uses ultrasound to discover and pair parties in a cash transaction. In other words, if you want to transfer some money to a friend/foe, this feature lets you transfer money without having to give out your phone-number or bank-details, assuming both of you are in 'relative close proximity'. 

Tez mode' does not rely on RF-based technologies like (Bluetooth, Wi-Fi, NFC etc.) for data transfer and leverages 'sound' instead, which has certain advantages (such as it doesn't pass through walls). In G-pay's case, this is used to establish physical co-presence by transmitting a short 8 digit token as inaudible sound. 

I have reverse engineered the ultrasound signal and data-transfer protocol. This repo contains code for an ultrasound receiver, capable of sniffing out 'google-pay generated' 8-digit tokens.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uf85JEeVDTo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Layout of this repo:**

This repo contains 4 folders
1. **Code**: contains the code (i.e. python scripts) you'll need for signal processing and visualization. Note- All of the code was developed in a jupyter notebook, so code in this folder may not work out of the box. You may have to make a few edits. 
2. **Jupyter Notebooks**: This is where you should start. Just download the notebook and samples from the repo. The notebook has instructions for each step. Additionally, you can refer to my [medium post](https://link.medium.com/e0YFNXXrC5) for a more in-depth look at the reverse engineering process.   
3. **Gnu-Radio Flowgraphs**: This folder contains a gnu-radio flowgraph. You'll need this to properly filter the raw signal. 
4. **Recorded G-pay ultrasound samples**: Contains multiple recordings of the near-ultrasound signal. It has 2 for Android and 2 for iOS. I've included the actual 8-digit tokens for each of them in their file names (makes it easy to verifiy).

**Usage:**
1. Just download the Jupyter Notebook and follow along OR
2. For a more in-depth look at the reverse engineering process
   * Part1 - [A noob’s attempt at reverse engineering Google pay’s Cash or Tez mode — part 1](https://link.medium.com/WcttcAFxz5)
   * Part2 - [A noob’s attempt at reverse engineering Google pay’s Cash or Tez mode — part 2](https://link.medium.com/e0YFNXXrC5)
   * Part3 - Coming Soon! (still under lockdown ...need to get some groceries. So, that takes precedence).

**Notes:**
1. Google just confirmed that they've made a change to the Android version of the G-pay app. They've disabled Tez-mode in their latest version of the app. **As far as I know, it has nothing to do with this work.**
2. This technology i.e. cash-mode is used in a number of other google products (chromecast guest-mode, google nearby, google-play etc). I have not tested them.
3. *There is **no vulnerability** here - g-pay only uses the ultrasound channel for discovery and pairing. For actual payments, it still relies on an internet connection* 
4. Lastly, although paring tokens are replayable, they're short-lived. So, not much to worry about there.
5. However, there is still a lot of stuff I havent looked at. So more to come!
