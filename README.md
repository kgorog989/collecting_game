# Egg Hunt! 

Game implemented in Python using the pygame module. Map created in Tiled. 

<p align="center" width="100%">
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/a1881eaf-6568-47f6-9d3d-89300437aad3">

## Game Objective

Collect as many eggs as possible while avoiding cows.

If you collide with a cow, you lose a life. The game ends when all lives are lost.

## Controls

- **Arrow Keys** – Move the player

- **Spacebar** – Show current high score

## Features

#### Player

- Animated character

- Camera follows the player

- 3 lives total

- 3 seconds of invincibility after taking damage (displayed at the bottom left corner)

- Teleports back to the starting position after losing a life

#### Enemies & NPCs

- Cows and chickens move randomly

- Each has its own animation

- Movement direction and speed are randomized after a set time

#### Eggs & Scoring

- Chickens spawn eggs at random time intervals

- Eggs are destroyed if a cow collides with them

- Collecting an egg increases the score by 1

- Score and remaining lives are shown at the top of the screen with icons

#### Game Over & Saving

- Colliding with a cow costs one life

- When all lives are lost, the game closes

- High score is saved to a file when the game ends

#### Audio

- Background music

- Sound effects for:

   - Collecting eggs

   - Colliding with cows

## Technologies Used 

- Python

- Pygame

- Tiled Map Editor

## Game Screenshots

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

## Graphics, font, and audio sources

Sprout Lands Asset Pack (Basic Pack) by CUP NOOBLE:  
https://cupnooble.itch.io/sprout-lands-asset-pack

16x16 heart by simodias (cc4):  
https://simodias.itch.io/heart

Masaaki Font by Philippe Moesch:  
https://www.1001freefonts.com/masaaki.font

Take Item Sound Effect by zennnsounds from pixabay.com:  
https://pixabay.com/sound-effects/take-item-sound-effect-163073/

Relaxing Chiptune Music by Migfus20 from Freesound (cc4):  
https://freesound.org/people/Migfus20/sounds/679054/

Moo1 - Moo Moo the Cow by manofham from Freesound (cc0):  
https://freesound.org/people/manofham/sounds/700378/

Licenses: 

  https://creativecommons.org/licenses/by/4.0/
  
  https://creativecommons.org/publicdomain/zero/1.0/
