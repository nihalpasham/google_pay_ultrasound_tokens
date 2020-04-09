# Reverse engineering Google pay's -Tez mode
Context: Google pay (Tez-mode) uses ultrasound to discover and pair parties. 'Tez mode' allows G-pay to avoid having to rely on RF-based technologies like (Bluetooth, Wi-Fi, NFC etc.) for data transfer and leverage 'sound' instead, which has certain advantages (such as it doesn't pass through walls). In G-pay's case, it tries to establish physical co-presence by transmitting a short 8 digit token as inaudible sound. 

I have reverse engineered the ultrasound signal and data-transfer protocol. This repo contains code that will allow you to build an ultrasound receiver to intercept the 8-digit token generated by Google pay.  
