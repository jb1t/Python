**Motion Detect**
-

This small script is being used to augment a security system. Most home security systems provide capabilities to sense
motion, however, they typically implement this based on movement within the images on the viewable screen. This can
 cause a number of false alarms if there is a tree moving in the wind in the background or even its shadow. 
 
 This python script is being used on a RPi and hooked up to a Passive Infrared Motion (PIR) sensor. In short, it will 
 detect movement of a significant heat signature. Here are more details: 
 https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work
 
 These PIRs are just like your normal home security system motion detectors.
 ![PIR sensor](http://thefullstacknerd.com/wp-content/uploads/2017/12/PIR.jpg)
 
 What is the scripts purpose? Well when motion is detected it will raise an event. Then we can act on that event in any 
 number of ways. It could send a text message to let someone know there is movement OR it could even trigger an event on[IFTTT](https://ifttt.com/) and do ANY number of things!
 
 In the interrupt_smtp.py script, it will require a password from the user from their email. Once that is supplied, it 
 will send them a text and trigger a IFTTT event immediately to let them know it is working. Then whenever the PIR 
 sensor detects a motion it will trigger both of those events again. However, now it will wait a period of N minutes 
 before sending out another event if motion is detected (that way you don't get annoyed).
