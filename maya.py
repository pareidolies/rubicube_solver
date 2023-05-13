import pymel.core as pm

#ROTATIONS
def rotate_row(cubes, row, angle):
    group = pm.group(em=True, name='row_{}'.format(row))
    for x in range(3):
        for z in range(3):
            cube = cubes[(x, row, z)]
            pm.parent(cube, group)
    pm.rotate(group, (0, angle, 0), relative=True, centerPivot=True)
    pm.parent(group, world=True)
    for x in range(3):
        for z in range(3):
            cube = cubes[(x, row, z)]
            pm.parent(cube, world=True)
    cmds.delete('row_{}'.format(row))

def rotate_side(cubes, side, angle):
    group = pm.group(em=True, name='side_{}'.format(side))
    for x in range(3):
        for y in range(3):
            cube = cubes[(x, y, side)]
            pm.parent(cube, group)
    pm.rotate(group, (0, 0, angle), relative=True, centerPivot=True)
    pm.parent(group, world=True)
    for x in range(3):
        for y in range(3):
            cube = cubes[(x, y, side)]
            pm.parent(cube, world=True)
    cmds.delete('side_{}'.format(side))

def rotate_column(cubes, column, angle):
    group = pm.group(em=True, name='column_{}'.format(column))
    for y in range(3):
        for z in range(3):
            cube = cubes[(column, y, z)]
            pm.parent(cube, group)
    pm.rotate(group, (angle, 0, 0), relative=True, centerPivot=True)
    pm.parent(group, world=True)
    for y in range(3):
        for z in range(3):
            cube = cubes[(column, y, z)]
            pm.parent(cube, world=True)
    cmds.delete('column_{}'.format(column))

#ANIMATIONS

def anim_rotate_row(cubes, row, angle):
    start_frame = pm.currentTime(query=True)
    end_frame = start_frame + 25
    step_angle = angle / (end_frame - start_frame)
    for frame in range(int(start_frame), int(end_frame)):
        pm.currentTime(frame)
        rotate_row(cubes, row, step_angle)

def anim_rotate_column(cubes, column, angle):
    start_frame = pm.currentTime(query=True)
    end_frame = start_frame + 25
    step_angle = angle / (end_frame - start_frame)
    for frame in range(int(start_frame), int(end_frame)):
        pm.currentTime(frame)
        rotate_column(cubes, column, step_angle)

def anim_rotate_side(cubes, side, angle):
    start_frame = pm.currentTime(query=True)
    end_frame = start_frame + 25
    step_angle = angle / (end_frame - start_frame)
    for frame in range(int(start_frame), int(end_frame)):
        pm.currentTime(frame)
        rotate_side(cubes, side, step_angle)

cmds.select(all=True)
cmds.delete()

cube_size = 1
cubes = {}

#COLORS
whiteBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(whiteBlinn + '.color', 1, 1, 1) 

yellowBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(yellowBlinn + '.color', 1, 1, 0)

blueBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(blueBlinn + '.color', 0, 0, 1) 

redBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(redBlinn + '.color', 1, 0, 0)

greenBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(greenBlinn + '.color', 0, 1, 0)

orangeBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(orangeBlinn + '.color', 1, 0.25, 0)

for x in range(3):
    for y in range(3):
        for z in range(3):
            cube = pm.polyCube(
                name='cube_{}_{}_{}'.format(x, y, z),
                width=cube_size, height=cube_size, depth=cube_size,
            sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
            cmds.polyBevel('cube_{}_{}_{}'.format(x, y, z), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
                worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
                mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
            cubeBaseColorBlinn = cmds.shadingNode("blinn", asShader=True)
            cmds.setAttr(cubeBaseColorBlinn + '.color', 0, 0, 0) # Black
            cmds.select('cube_{}_{}_{}'.format(x, y, z))
            cmds.hyperShade(assign=cubeBaseColorBlinn)
            
            if (z == 2):
                cmds.select('cube_{}_{}_{}.f[1]'.format(x, y, z))
                cmds.hyperShade(assign=yellowBlinn)
                
            if (x == 2):
                cmds.select('cube_{}_{}_{}.f[3]'.format(x, y, z))
                cmds.hyperShade(assign=blueBlinn)
            
            if (y == 2):
                cmds.select('cube_{}_{}_{}.f[4]'.format(x, y, z))
                cmds.hyperShade(assign=redBlinn)
            
            if (y == 0):
                cmds.select('cube_{}_{}_{}.f[0]'.format(x, y, z))
                cmds.hyperShade(assign=orangeBlinn)
            
            if (z == 0):
                cmds.select('cube_{}_{}_{}.f[5]'.format(x, y, z))
                cmds.hyperShade(assign=whiteBlinn)
            
            if (x == 0):
                cmds.select('cube_{}_{}_{}.f[2]'.format(x, y, z))
                cmds.hyperShade(assign=greenBlinn)
            
            cube.translate.set(x*cube_size, y*cube_size, z*cube_size)
            cubes[(x, y, z)] = cube


rotate_row(cubes, 1, 90)

update_cubes = {}
for x in range(3):
    for y in range(3):
        for z in range(3):
            tmp = cubes[(x, y, z)]
            update_cubes[(x, y, z)] = cubes[(int(cmds.getAttr(tmp+'.translateX')), int(cmds.getAttr(tmp+'.translateY')), int(cmds.getAttr(tmp+'.translateZ')))]
cubes = update_cubes

cmds.select(cubes[(1,0,1)])

anim_rotate_side(cubes, 1, 90)
rotate_column(cubes, 1, 90)


