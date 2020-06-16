import mdl
from display import *
from matrix import *
from draw import *
import ease

"""======== first_pass( commands ) ==========

  Checks the commands array for any animation commands
  (frames, basename, vary)

  Should set num_frames and basename if the frames
  or basename commands are present

  If vary is found, but frames is not, the entire
  program should exit.

  If frames is found, but basename is not, set name
  to some default value, and print out a message
  with the name being used.
  ==================== """
def first_pass( commands ):

    frameCheck = varyCheck = tweenCheck = nameCheck = False
    name = ''
    num_frames = 1

    for command in commands:

        if command['op'] == 'frames':
            num_frames = int(command['args'][0])
            frameCheck = True
        elif command['op'] == 'vary':
            varyCheck = True
        elif command['op'] == 'tween':
            tweenCheck = True
        elif command['op'] == 'basename':
            name = command['args'][0]
            nameCheck = True

    if varyCheck and not frameCheck:
        print('Error: Vary command found without setting number of frames!')
        exit()

    elif tweenCheck and not frameCheck:
        print('Error: Tween command found without setting number of frames!')
        exit()

    elif frameCheck and not nameCheck:
        print('Animation code present but basename was not set. Using "frame" as basename.')
        name = 'frame'

    return (name, num_frames)

"""======== second_pass( commands ) ==========

  In order to set the knobs for animation, we need to keep
  a seaprate value for each knob for each frame. We can do
  this by using an array of dictionaries. Each array index
  will correspond to a frame (eg. knobs[0] would be the first
  frame, knobs[2] would be the 3rd frame and so on).

  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.

  Go through the command array, and when you find vary, go
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropirate value.
  ===================="""
def second_pass( commands, num_frames ):
    knobs = list()

    for command in commands:
        if command['op'] in ['move', 'scale', 'rotate']:
            if command['knob']:
                knobs.append(command['knob'])

    frames = [ {} for i in range(num_frames) ]
    set_values = dict()
    knob_lists = dict()

    for command in commands:
        if command['op'] == 'vary':
            args = command['args']
            knob_name = command['knob']
            start_frame = int(args[0])
            end_frame = int(args[1])
            start_value = float(args[2])
            end_value = float(args[3])

            ease_type = command['ease']
            if ease_type not in ease.EASES:
                print('Invalid ease for knob: ' + knob_name)
                exit()
            if ((start_frame < 0) or
                (end_frame >= num_frames) or
                (end_frame <= start_frame)):
                print('Invalid vary command for knob: ' + knob_name)
                exit()

            values = ease.generate(ease_type, start_value, end_value, (1+end_frame-start_frame))
            for i in range(len(values)):
                frames[i+start_frame][knob_name] = values[i]
        
        elif command['op'] == 'set':
            if command['knob']:
                set_values[command['knob']] = command['args'][0]
            else:
                for knob in knobs:
                    set_values[knob] = command['args'][0]
        
        elif command['op'] == 'save_knobs':
            knob_lists[command['knob_list']] = set_values
            set_values = dict()
        
        elif command['op'] == 'tween':
            args = command['args']
            start_frame = int(args[0])
            end_frame = int(args[1])
            start_knob_list = knob_lists[command['knob_list0']]
            end_knob_list = knob_lists[command['knob_list1']]
            ease_type = command['ease']
            frame_diff = (1+end_frame-start_frame)

            if ease_type not in ease.EASES:
                print(f'Invalid ease for tween with lists: {command["knob_list0"]}, {command["knob_list1"]}')
                exit()   
            if ((start_frame < 0) or
                (end_frame >= num_frames) or
                (end_frame <= start_frame)):
                print(f'Invalid tween command for lists: {command["knob_list0"]}, {command["knob_list1"]}')
                exit()
            # if set(start_knob_list.keys()) != set(end_knob_list.keys()):
            #     print(f'Attempting to tween mismatched knob lists: {command["knob_list0"]}, {command["knob_list1"]}')
            #     exit()
            
            listed_knobs = list(start_knob_list.keys())
            calculated_vals = dict()
            for knob_name in listed_knobs:
                start_value = start_knob_list[knob_name]
                end_value = end_knob_list[knob_name]
                calculated_vals[knob_name] = ease.generate(ease_type, start_value, end_value, frame_diff)

            for i in range(frame_diff):
                for knob_name in listed_knobs:
                    frames[i+start_frame][knob_name] = calculated_vals[knob_name][i]

    return frames


def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print("Parsing failed.")
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    (name, num_frames) = first_pass(commands)
    frames = second_pass(commands, num_frames)

    for f in range(num_frames):
        tmp = new_matrix()
        ident( tmp )

        stack = [ [x[:] for x in tmp] ]
        screen = new_screen()
        zbuffer = new_zbuffer()
        tmp = []
        step_3d = 100
        consts = ''
        coords = []
        coords1 = []


        #Set symbol values for multiple frames
        if num_frames > 1:
            frame = frames[f]
            for knob in frame:
                symbols[knob][1] = frame[knob]
                print('\tknob: ' + knob + '\tvalue: ' + str(frame[knob]))

        for command in commands:
            print(command)
            c = command['op']
            args = command['args']
            knob_value = 1

            if c == 'box':
                if command['constants']:
                    reflect = command['constants']
                add_box(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'sphere':
                if command['constants']:
                    reflect = command['constants']
                add_sphere(tmp,
                           args[0], args[1], args[2], args[3], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'torus':
                if command['constants']:
                    reflect = command['constants']
                add_torus(tmp,
                          args[0], args[1], args[2], args[3], args[4], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'line':
                add_edge(tmp,
                         args[0], args[1], args[2], args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_lines(tmp, screen, zbuffer, color)
                tmp = []
            elif c == 'move':
                if command['knob']:
                    knob_value = symbols[command['knob']][1]
                tmp = make_translate(args[0] * knob_value, args[1] * knob_value, args[2] * knob_value)
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'scale':
                if command['knob']:
                    knob_value = symbols[command['knob']][1]
                tmp = make_scale(args[0] * knob_value, args[1] * knob_value, args[2] * knob_value)
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'rotate':
                if command['knob']:
                    knob_value = symbols[command['knob']][1]
                theta = args[1] * (math.pi/180) * knob_value
                if args[0] == 'x':
                    tmp = make_rotX(theta)
                elif args[0] == 'y':
                    tmp = make_rotY(theta)
                else:
                    tmp = make_rotZ(theta)
                matrix_mult( stack[-1], tmp )
                stack[-1] = [ x[:] for x in tmp]
                tmp = []
            elif c == 'push':
                stack.append([x[:] for x in stack[-1]] )
            elif c == 'pop':
                stack.pop()
            elif c == 'display':
                display(screen)
            elif c == 'save':
                save_extension(screen, args[0]+'.png')
            # end operation loop
        if num_frames > 1:
            fname = 'anim/%s%03d.png'%(name, f)
            print('Saving frame: '  + fname)
            save_extension(screen, fname)
        # end fromes loop
    if num_frames > 1:
        make_animation(name)
