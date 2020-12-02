# easyeda-panel

Panelizing boards for production in EasyEDA is, frankly, a PITA - at least, it is when using JLCPCB's PCBA capabilities.  Especially so when the board has copper pours on it.

This is an attempt to make life easier.  It'll panelize boards in a rectangular array with mousebites for separating them, as required for JLCPCB's PCBA service.

To use, you'll need to start off by exporting two sets of Gerbers from EasyEDA - one of the unpanelized board, and one after adding the outlines for panelization and the mousebites using 'Tools->Panelize' in EasyEDA.  Export a CPL (pick and place) file from the panelized version as well, making sure to tick the 'Include panelized components' co-ordinates' checkbox.

Expand the zip for the unpanelized board in one directory (suggest calling it 'board'), removing anything that's not a Gerber or Excellon file.  Also remove the board outline file.

Expand the zip for the panelized board in another directory (maybe 'panel').  Remove everything *except* the outline and NPTH drill file.

What we've done now is to put everything which needs to be replicated for the panelization in one directory, and the bits we just need one copy of (the board outline and the NPTH file which contains the mousebites) in another.

Update panel.py to reflect the names of your directories, the number of repeats of the board that you want in X and Y directions and the step distance for each.  This will be the size of your board plus the column/row spacing that you specified when panelizing in EasyEDA.

Run it from the parent directory of the two directries with the Gerbers in.  It'll create a third directory, 'output' (you can change this as well s'il vous fait plaisir), and will create the required Gerber and Excellon files in it.  They'll have the same names as the originals, making it easy enough to sort out which is which.

Zip the whole output directory, and you've your Gerber/drill files ready to upload.

