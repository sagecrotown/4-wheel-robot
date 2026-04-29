# 4-wheel-robot

### Prototype of four wheeled robot. Changing and learning.

4/29/26: Added rotational input so left joystick controls robot translation and right joystick controls pose. Implemented mecanum equations. Robot still can't spin and move at the same time without logical input priority issues (fixable) or power issues (also fixable but tougher). Becuase I'm working with 3.7V batteries and cheap motors, it's hard to send torques with the finesse I need. They stall out if I use anything less than about half power. TODO: solder connectors onto bigger batteries, buy better motors, look into feedback control (requires encoders).

4/28/26: Already had bluetooth connectivity but refined it so controller inputs actually matched wheel actions. Changed simple drive functions so robot can drive forwards/backwards and spin in place (though not at the same time yet). TODO: implement more complex and better drive functions based on mecanum equations that can handle multidirectional inputs. 
