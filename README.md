# M5Stack-Helium-Mapper

## Description of Project

This is a [M5Stack](https://m5stack.com) [UIFlow](https://flow.m5stack.com) used to connect to any available [Helium LoRaWAN gateway](https://helium.com) and send location information to [Helium Cargo Integration](https://cargo.helium.com/).  Using UIFlow, you can also generate the necessary Micro Python code to utilize this capability outside of UIFlow.

## Required Hardware

Please note:  If you are a US resident, [Digikey](https://www.digikey.com/) carries MOST of these devices.  You really should try there first as shipping directly from M5Stack is either expensive or takes a while. 
If you can't find the item on Digiky (their search sucks), try searching for the M5Stack item number from the M5Stack web page. 

* M5Stack [Core](https://m5stack.com/collections/m5-core) ( Black, Gray, Fire or Core2)
* M5Stack [LoRaWAN Module](https://m5stack.com/collections/m5-module/products/lorawan-modulerhf76-052?variant=30331964325978)
* M5Stack [GPS Module](https://m5stack.com/collections/m5-module/products/gps-module)

## Hardware Modifications

Unfortunately, the LoRaWAN module and the GPS module use the same UART pins.  To resolve the conflict you can follow the instructions [here](https://docs.m5stack.com/#/en/module/gps) to change the GPS module to use pins 5 and 13.

## Status of code

CUrrently the code is able to connect to the Helium Network, but when I try to add in the GPS logic, it breaks the UART response from LoRaWAN.  Waiting on response from M5Stack Support.
