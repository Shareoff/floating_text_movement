# Floating Text Movement Script

Written by **Shareoff#2107**. Thank **tepid#1618** for asking me to do this.  
This script creates a *text* file with generated events for floating text which appear to have movement. This movement is **fully configurable** with easings for x values, y values, angles, color and outline.  
These generated events may then be surgeried into your .rdlevel file!  
*Use at your own caution*, this is obviously useful in very niche situations.  
Feel free to ping/dm me any questions, problems, suggestions etc.

## Installation Instructions
1. Install python (https://www.python.org/downloads/). make sure to add python to PATH in the installation process
2. Download `floating_text_movement.py` (from this repository) to any folder on your PC.
3. Open a terminal in the folder where you downloaded the file (you can do this by navigating there and then writing cmd in the file explorer address line if you're on windows)
3. Run `python -m ensurepip --upgrade`
4. Run `pip install click`
5. Now you're ready to run the script! run `python ./floating_text_movement.py` and hopefully the script will instruct you through the rest.

## Why would I use this over room movement / making a CC with my text?
You may not have enough rooms, or enough CCs, because you're using them for other things.  
In addition this has the advantage over room movements of having easings for color and outline (which you simply cannot do only using rooms)  
But to clarify, this is incredibly niche. If you aren't sure you need this, you probably don't and there may be a better way to do what you want.

## Advanced Usage Instructions
By running the script like `python ./floating_text_movement.py` the script will ask you to input the parameters everytime.  
There are a couple of disadvantages to this, because you may want to run it multiple times with very similar parameters and just make small changes,
and also there are some parameters that I thought were niche enough that I decided they could only be configured from the command line.  
So you may send any number of parameters through the command line options instead of getting prompted by the script,
run `python ./floating_text_movement.py --help` for more information!  
Some additional flags available are `--room` (may be called repeatedly to place the event in any number of rooms), `--size`, `--starting-id` and more.

## Final Words
This is completely superfluous and extra but hey I find it funny so why not  
Go wild, have fun, and let me know if you used it (because funny!)

## Changelog

### 1.2
Fixed bug where using colors with Back/Elastic easings could cause invalid color values. (oops)
### 1.1
Fixed flickering bug (thanks 9th and kirbycreep!). Lowered default event interval to 0.01 of a beat.
### 1.0
Created this script!
