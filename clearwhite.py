#!/usr/bin/python

from gimpfu import *

def plugin_clearwhite(timg, tdrawable):

    #proceed if topleft corner is white
    topleft=list(pdb.gimp_image_pick_color(timg,tdrawable,0,0,0,1,3)) #assigns RGBA list avg color () within radius 5 px from 0,0
	if ((sum(topleft[0:3])>745) & (topleft[3]>10)) : #sums red green and blue, proceed if this value is "white" enough, checks transparecy
       		pdb.gimp_fuzzy_select(tdrawable,0,0,15,2,1,0,0,0) # fuzzy wand selects from the upper left corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		    pdb.gimp_selection_none(timg) #deselect all


    #proceed if topright corner is white
	topright=list(pdb.gimp_image_pick_color(timg,tdrawable,(tdrawable.width-1),0,0,1,3)) #same at tdrawable.width,0
	if ((sum(topright[0:3])>745) & (topright[3]>10)) : #sums red green and blue, proceed if this value is "white" enough
       		pdb.gimp_fuzzy_select(tdrawable,(tdrawable.width-1),0,15,2,1,0,0,0) # fuzzy wand selects from the upper right corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		    pdb.gimp_selection_none(timg) #deselect all

    #proceed if bottomleft corner is white
	bottomleft=list(pdb.gimp_image_pick_color(timg,tdrawable,0,(tdrawable.height-1),0,1,3)) #same at 0,tdrawable.height
	if ((sum(bottomleft[0:3])>745) & (bottomleft[3]>10)) : #sums red green and blue, proceed if this value is "white" enough
       		pdb.gimp_fuzzy_select(tdrawable,0,(tdrawable.height-1),15,2,1,0,0,0) # fuzzy wand selects from the bottom left corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		    pdb.gimp_selection_none(timg) #deselect all

    #proceed if bottom rightcorner is white
	bottomright=list(pdb.gimp_image_pick_color(timg,tdrawable,(tdrawable.width-1),(tdrawable.height-1),0,1,3)) #same at width,height
	if ((sum(bottomright[0:3])>745) & (bottomright[3]>10)) : #sums red green and blue, proceed if this value is "white" enough
       		pdb.gimp_fuzzy_select(tdrawable,(tdrawable.width-1),(tdrawable.height-1),15,2,1,0,0,0) # wand selects from bottom right corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		    pdb.gimp_selection_none(timg) #deselect all

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
