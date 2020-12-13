# BTS_Li-ion
Remote Battery Health monitoring system 

This work includes joint work between PDPU and BSNL.

The purpose of this work is to monitor health of the back-up battery placed at an BTS tower by consdering various methods. For determining state of health (SOH) of the battery 
we have considered various input parameters where live data feedback (temperature, humidity, current, voltage, SOC) is displayed and further used in the control strategy. 
The actual prototype is in BSNL research office. For SOC calculation, we have used a novel combination of the extended Kalman filter (EKF) algorithm, a three-RC-block equivalent
circuit and the traditional coulomb counting method. SOH is further calculated using neural network where SOC is one of the input parameters.

P.S: for new BTS towers there is a provision of solar rooftop which we have also taken into consideration. If incase any doubt fell free to reach out to me. 
