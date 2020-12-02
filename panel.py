import sys, os, glob, shutil
import gerberex
from gerberex import DxfFile, GerberComposition, DrillComposition


# Directory of Gerbers/drills from the original board - exclude the board outline
board = 'board'

# Directory of Gebers/drills from the panelised board - include only the board outline and NPTH drill file
panel = 'panel'

# Directory in which to put the output files
output = 'output'

# X and Y count
x_count = 5
y_count = 4

# X and Y offset
x_offset = 67
y_offset = -58

try:
    os.mkdir(output)
except FileExistsError:
    pass

def putstr(text):
    sys.stdout.write(text)
    sys.stdout.flush()

# Build panels
gerbers = [os.path.basename(x) for x in glob.glob(board + "/*")]

for gerber in gerbers:
    putstr('merging %s: ' % gerber)
    if gerber.endswith('DRL'):
        putstr("Drill\n")
        ctx = DrillComposition()
    else:
        putstr("Gerber\n")
        ctx = GerberComposition()

    for x in range(0, x_count):
        for y in range(0, y_count):
            file = gerberex.read(board + '/' + gerber)
            file.to_metric()
            file.offset(x*x_offset, -y*y_offset)
            ctx.merge(file) 
            putstr('.')

    # Check for file in panel directory, and merge that in as well
    if os.path.isfile(panel + '/' + gerber):
        putstr(' - merging panelized file')
        file = gerberex.read(panel + '/' + gerber)
        file.to_metric()
        ctx.merge(file) 

    ctx.dump(output + '/' + gerber)
    putstr(' end\n')

# Check for any files in panel dir which aren't in output
p_gerbers = [os.path.basename(x) for x in glob.glob(panel + '/*')]
for gerber in p_gerbers:
    if gerber not in gerbers:
        putstr('Copying ' + gerber + '\n')
        shutil.copyfile(panel + "/" + gerber, output + '/' + gerber)

putstr('. end\n')