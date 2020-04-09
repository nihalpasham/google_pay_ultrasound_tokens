# Reverse engineering Google pay's -Tez mode
Context: Google pay (Tez-mode) uses ultrasound to discover and pair parties. 'Tez mode' does not rely on RF-based technologies like (Bluetooth, Wi-Fi, NFC etc.) for data transfer and leverages 'sound' instead, which has certain advantages (such as it doesn't pass through walls). In G-pay's case, this is used to establish physical co-presence by transmitting a short 8 digit token as inaudible sound. 

I have reverse engineered the ultrasound signal and data-transfer protocol. This repo contains code for an ultrasound receiver, capable of intercepting 'google-pay generated' 8-digit tokens.
