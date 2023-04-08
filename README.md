# Grand-Master-Robot
Grand-Master-Robot is a fully autonomous robot has the ability to play full chess round against people.

# Vision:
The Grand-Master Robot uses computer vision to recognize where the chess pieces are on the board before deciding what move to make. The Robot sees through a Raspberry Pi camera module which attached directly to the raspberry pi, where the both are located in a box above the chess board. I used python3.7 and OpenCV 3 to drive the camera, after capturing the image there are many Image processing stages before we decide what is the actual state of the board:
1-	Change the perspective of the taken image by applying a perspective warp matrix. (the output would be just the board).
2-	Apply color filter to change all the board color to white.
3-	Slice the image to 64 small images (one for each board square).
4-	Apply Support Vector Machine (SVM) on each board square to determine either the square empty or occupied, and if it is occupied what is the color of the stone which placed on it.
5-	Use convolutional neural networks (CNN), to determine what type of piece the player promoted their pawn to.
Note: In chess, promotion is the replacement of a pawn with a new piece when the pawn is moved to its last rank. The player replaces the pawn immediately with a queen, rook, bishop, or knight of the same color
After applying these steps, we can know the real state of the board, and the we can determine the occurred changes by tracking the difference between the images.
# The Arm:
The Robot uses a three-dimensional robotic arm made by plexiglass, the whole design done with CorelDraw program, and cut using CNC machine, except the gripper designed with Soled-Works program, and build by 3D-printer. I used stepper motor Nema 17 to control the elbow and the shoulder, Nema 23 to move the whole arm up and down and servo motor to control the gripper. I used TB 6600 driver to drive each stepper motor.
# The stone:
I paint the stones with green and orange color, to make the detection process easier.
Chess Engine:
In order to help to robot to make a decision of the best move on his turn I used Stock Fish engine, which is a free and open-source chess engine, commonly used to calculate the optimal move in various chess scenarios needed for a checkmate. The Stock Fish has its own API, so all wat I wanted to do is to make an API call contains the actual stat of the board, and he will respond with the best move.
The speaker:
The Robot has the ability to speak, using an external speaker and python. The main of adding this ability to warn the opponent in some special cases like: illegal move, check or check mate.
# Summary:
I delivered a full autonomous manipulator arm that has the ability to play with a mind that can beat chess world-champions with less-than-a-minute for each move, using computational power as minimum as a Raspberry Pi 3 controller.
