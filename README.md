# CSE379

In order to re-create this project you will need a few things:

1. Download the minecraft client from the official minecraft site.
2. download minecraft forge, you will need this to modify both the server and the client. I did my best to give a working server,
with most to all things preinstalled hence why the file is so big.
3. the coroutil package, you can find a copy of these mods in the mods folder inside the CSE379 server folder. You will need to
add those to the mods folder on the client side. 
Note: this is a hidden file. On windows you can find it by typing in %appdata% and go to the .minecraft file, in there add to the mods
folder. If you do not have that folder, create it then add to it. Mac Users... good luck finding the .minecraft folder I know you can
do it!
4. the datastreaming files
5. mineflayer files

Now that you have the initial setup requirements, there are a few way to reproduce a similiar effect (will never be exactly the same
since it is realtime streaming) to the video @ https://youtu.be/2Fz7VabubR0
1. start up the forge server. Inside the CSE379 Server file, there is a jar file that says forge and a bunch of numbers and stuff after
it, you will want to run that server, not the one that says minecraft 1.12.2 server (that one is an unmodded one).
2. run the datastreaming. You can save the output to a file or attempt to pipe it to stdin while the mineflayer is running.
For fun to mess with people and also testing purposes, I have left STDIN open while the mineflayer file is running so that way you 
can also manually type commands as well as chat as the bot.
3. start up mineflayer. There are a ton of files in there (the entire mineflayer library and stuff). To find the file we made follow
the path: CSE379_mineflayer\node_modules\minecraft-protocol-forge\examples\client_forge in this folder you will see a file called 
CSE_bot, that is the file you will want to run. You will also see some example txt files similiar to which we used for making the 
video. To run this: type node CSE379_bot.js <host> <port> where host is the current IP address of the server and port is the current port.
These may change depending on where you are. Default port is 25565. you can also check the server IP inside the .properties file in the 
minecraft server folder.

Note: the first time you run the bot you may need to give it admin. 
Note: You cannot type commands unless you are an admin of the server!!!
To do this, go to the server console and type /OP <name>.
EX: /OP WeatherBot
