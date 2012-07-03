Date: 3 Jul 2012
Author: Ty Demarest

The following assumes Gimp 2.6+ is installed on the local machine.

The two python scripts in this repository, batch_clearwhite.py and clearwhite.py, use gimp's
built in python/script-fu api to make surrounding whitespace transparent in images of any format
gimp can use.  The two files are similar but are to be used independently for different situations.  
In order to make use of gimp's api, each of these files needs to be in gimp's plug-ins folder, namely
/.../.gimp-2.6/plug-ins  .  


***********Batch Mode****************

As its name implies, batch_clearwhite.py should be used to perform the task on a batch of files
whose folder need be specified in line 6, in the for loop header.  Additionally, he destination folder 
should be specified on line 57, in the saveas png call.  Once this is complete, make the file
executable, ensure it is in your working directory (which should be /.../.gimp-2.6/plug-ins),
and call the following in a bash:

    gimp -i --batch-interpreter python-fu-eval --batch - < batch_clearwhite.py

Note, the -i is for non-interactive mode.  (gimp --verbose -i ... can be called to turn on verbose
output).  


***********Plug-in Mode****************

Open gimp.  If you open it from a terminal window, gimp will send output to the console which can 
be useful if you're debugging a tweak (you can do this by simply calling "gimp" from a bash).  Open
a file whose white background you want to be transparent.  Click the <Image> menu in the menu bar, 
when the menu drops down, choose "Clear White Space...".  This should be at or near the bottom.

Enjoy.

