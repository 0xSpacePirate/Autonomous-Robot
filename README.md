## Self-balancing-Robot

This project focuses on building an autonomous single-wheeled self-balancing
humanoid robot made from scratch. This report presents the techniques used to
design the robot and using reinforcement learning (RL) and a PID Controller make it
self-balancing. In the project was also included a 3D Simulation.

One of the goals of the project was to make a brand new robot design and not copy
from the already created ones on the internet. The design was supposed to represent
the Robert Gordon University robot (see image below):

<img src="https://github.com/SpacePirato/Autonomous-Robot/blob/master/Library/7.PNG" width="40%">

## Please refer to the pdf document for more detailed information! 
# The pdf document can be found at: [Honours Project Report](https://github.com/SpacePirato/Autonomous-Robot/blob/master/Library/Honours%20Report%20-%20PETAR%20BONCHEV%20(1607262).pdf)

More info on the motivation & literature review can be found in the PDF document - chapters: 1-2;

-----------------------------------------------------------------------------------

The hardware that was used to control the robot:
1. Raspberry Pi 4 Model B
2. Gyroscope MPU-6050
3. Servo DXW90 (plastic) & Servo MG90S (metal) - both modified in 
                      order to be able to rotate with 360 degrees
4. Jumper cables
5. 6 AA 2900mAh batteries
6. Battery holder
7. UBEC 5V switch regulator

The first prototype can be seen below:

<img src="https://github.com/SpacePirato/Autonomous-Robot/blob/master/Library/6.PNG" width="30%" height="20%">

More info on the setup can be found in the PDF document - chapter: 3;

-----------------------------------------------------------------------------------

The design of the second prototype is more sophisticated and showed better results, 
however the legs had to be extended due to the reason that the robot was falling to quickly.

<img src="https://github.com/SpacePirato/Autonomous-Robot/blob/master/Library/1.PNG" width="30%" height="20%">

The project was not finished. Partially working self balacing robot using only a PID controller.
Examples can be seen below which represent the results from the first prototype:

[Prototype video one](https://youtu.be/z1m1uqZzNYo)
[Prototype video two](https://youtu.be/aM4gjytkHWw)

Final version of prototype 2:

<img src="https://github.com/SpacePirato/Autonomous-Robot/blob/master/Library/robot.jpg" width="30%" height="20%">






-----------------------------------------------------------------------------------

The results from the two prototypes show that with the many improvements implemented, 
the robot manages to self balance itself better and better but not fully.

<img src="https://github.com/SpacePirato/Autonomous-Robot/blob/master/Library/8.PNG" width="50%">

More detailed info on the results can be found in the PDF document - chapter 8;



