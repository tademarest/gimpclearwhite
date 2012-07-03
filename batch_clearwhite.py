#!/usr/bin/python

from gimpfu import *
import glob

#iterates over files in the directory
for filename in glob.glob("/home/ty/testimages/*.*"):

	# print name for debugging
	print filename

	# load image
	timg = pdb.gimp_file_load(filename,filename)

	# get layer
	tdrawable = pdb.gimp_image_get_active_layer(timg)

	#adds an alpha layer (if necessary)
        pdb.gimp_layer_add_alpha(timg.active_layer) 

    	#proceed if topleft corner is white
	topleft=list(pdb.gimp_image_pick_color(timg,tdrawable,0,0,0,1,3)) #assigns RGBA list avg color () within radius 5 px from 0,0
	if ((sum(topleft[0:3])>745) & (topleft[3]>10)) : #sums red green and blue, proceed if this value is "white" enough, checks transparecy
       		pdb.gimp_fuzzy_select(tdrawable,0,0,15,2,1,0,0,0) # fuzzy wand selects from the upper left corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		pdb.gimp_selection_none(timg) #deselect all
		#print((sum(topleft[0:3])>745))

	
    	#proceed if topright corner is white
	topright=list(pdb.gimp_image_pick_color(timg,tdrawable,(tdrawable.width-1),0,0,1,3)) #same at tdrawable.width,0
	if ((sum(topright[0:3])>745) & (topright[3]>10)) : #sums red green and blue, proceed if this value is "white" enough
       		pdb.gimp_fuzzy_select(tdrawable,(tdrawable.width-1),0,15,2,1,0,0,0) # fuzzy wand selects from the upper right corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		pdb.gimp_selection_none(timg) #deselect all
		#print((sum(topright[0:3])>745) & (topright[3]>10))

    	#proceed if bottomleft corner is white
	bottomleft=list(pdb.gimp_image_pick_color(timg,tdrawable,0,(tdrawable.height-1),0,1,3)) #same at 0,tdrawable.height
	if ((sum(bottomleft[0:3])>745) & (bottomleft[3]>10)) : #sums red green and blue, proceed if this value is "white" enough
       		pdb.gimp_fuzzy_select(tdrawable,0,(tdrawable.height-1),15,2,1,0,0,0) # fuzzy wand selects from the bottom left corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		pdb.gimp_selection_none(timg) #deselect all
		#print((sum(bottomleft[0:3])>745) & (bottomleft[3]>10))

    	#proceed if bottom rightcorner is white
	bottomright=list(pdb.gimp_image_pick_color(timg,tdrawable,(tdrawable.width-1),(tdrawable.height-1),0,1,3)) #same at width,height
	if ((sum(bottomright[0:3])>745) & (bottomright[3]>10)) : #sums red green and blue, proceed if this value is "white" enough
       		pdb.gimp_fuzzy_select(tdrawable,(tdrawable.width-1),(tdrawable.height-1),15,2,1,0,0,0) # wand selects from bottom right corner
        	pdb.gimp_edit_clear(tdrawable) #clears the selected, ie makes selected transparent
		pdb.gimp_selection_none(timg) #deselect all
		#print((sum(bottomright[0:3])>745) & (bottomright[3]>10))

	#crops out the extra stuff whether or not there was a white border
	pdb.plug_in_autocrop(timg,tdrawable) 

	#savesas png in new folder, truncate file extention concatenate .png
    	pdb.file_png_save2(timg, tdrawable, "/home/ty/newlogos/"+str(timg.name)[0:(len(timg.name)-4)]+".png", timg.name+".png", 0, 0, 0, 0, 0, 		0, 0, 0, 1)

# quit gimp
pdb.gimp_quit(0)


#shell command as follows> gimp --verbose -i --batch-interpreter python-fu-eval --batch - < batch_clearwhite.py


#tutorial at http://www.ibm.com/developerworks/opensource/library/os-autogimp/
#batch info at http://blenderartists.org/forum/showthread.php?84073-Gimp-Python-batch-how-to
#and at http://registry.gimp.org/node/15187
