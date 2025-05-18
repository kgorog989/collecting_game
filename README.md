# Egg Hunt! 

Game implemented in Python using the pygame module. Map created in Tiled. 

<p align="center" width="100%">
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/a1881eaf-6568-47f6-9d3d-89300437aad3">

### Game Objective, Features
Collect as many eggs as you can without bumping into cows. 

Move with the **arrow keys**, the current highscore can be displayed with the **spacebar**. 

The player character has its own animation and is followed by the camera. 

Cows and chicken move randomly and have their own animation. The movement state and the speed of movement is randomly generated after a certain time passes. 

Colliding with a cow costs a life. Three lives are available, invincibility is enabled for three seconds after losing one life and the player teleports back to the starting position, if no more lives are left the game closes. After death or closing the game the highscore is saved in a separate save file. 

The eggs are created by chickens after a certain time passes which is random for each. Eggs get destroyed if cows collide with them. Picking up an egg raises the score by one. The score and the lives left are both displayed at the top of the screen with an image next to them. 

Picking up an egg and colliding with a cow makes a sound. The game also has background music. 

### Game Screenshots

<p align="center" width="100%">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/c5e9c916-bb90-42d1-984e-60353ca66053">
</p>

<p align="center" width="100%">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/266655b2-acdd-4e12-b73e-40ee569573e2">
</p>

<p align="center" width="100%">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/d88689c9-1365-49f3-8f0c-d7b6503a2b55">

<p align="center" width="100%">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/5b41f3b9-dd9b-4b59-b5cc-5d20c68c8a3c">
