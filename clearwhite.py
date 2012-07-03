#!/usr/bin/python

from gimpfu import *

def plugin_clearwhite(timg, tdrawable):


#if corner is white proceed
    topleft=list(pdb.gimp_image_pick_color(timg,tdrawable,0,0,0,1,5)) #assigns rgba list avg color () within radius 5 px from 0,0
    if (sum(topleft[0:3])>720) : #sums red green and blue, proceed if this value is "white" enough

        pdb.gimp_fuzzy_select(tdrawable,0,0,100,2,1,0,0,0) # fuzzy wand selects from the upper left corner
        pdb.gimp_layer_add_alpha(timg.active_layer) #adds an alpha layer (if necessary)
        pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent


    pdb.plug_in_autocrop(timg,tdrawable) #crops out the extra stuff

#savesas png in new folder
    pdb.file_png_save2(timg, tdrawable, "/home/ty/newlogos/"+timg.name+".png", timg.name+".png", 0, 0, 0, 0, 0, 0, 0, 0, 1)

register(
        "python_fu_clearwhitespace",
        "Saves the image at a maximum width and height",
        "Saves the image at a maximum width and height",
        "Ty Demarest",
        "Ty Demarest",
        "2012",
        "<Image>/Image/Clear White Space...",
        "RGB*, GRAY*",
        [],
        [],
        plugin_clearwhite)

main()


#tutorial at http://www.ibm.com/developerworks/opensource/library/os-autogimp/
