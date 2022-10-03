from os import listdir, path

TITLE = 'PyChinko'
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
FPS = 40
FILL_COLOR = 'black'

TILE_WIDTH = 24
TILE_HEIGHT = 24
GRID_WIDTH = SCREEN_WIDTH//TILE_WIDTH
GRID_HEIGHT = SCREEN_HEIGHT//TILE_HEIGHT
X_OFFSET = 9*TILE_WIDTH
Y_OFFSET = 4*TILE_WIDTH

ids = ['-2', '-1', '1', '2', '3', '4', '5', '6']

image_dict = {'-2':'pychinko/gfx/entities/circuit_bkgrd_1.png',
        '-1':'pychinko/gfx/entities/circuit_bkgrd.png',
        '1':'pychinko/gfx/entities/basic_orb.png',
        '2':'pychinko/gfx/entities/arrow_ui.png',
        '3':'pychinko/gfx/entities/wire_wall.png',
        '4':'pychinko/gfx/entities/block_wall.png',
        '5':'pychinko/gfx/entities/basic_peg.png',
        '6':'pychinko/gfx/entities/refresh_peg.png'
}

id_dict = {'BACKGROUND':'-1',
        'ORB':'1',
        'ARROW':'2',
        'WALL':'3',
        'CEILING':'4',
        'PEG':'5'
}

sfx_dict = {'GAME_OVER':'sfx/game_over.wav',
'HIT_DMG':'pychinko/sfx/hit_damage.wav',
'HIT_OPP':'pychinko/sfx/hit_opponent.wav',
'HIT_OPP_WEAK':'pychinko/sfx/hit_opponent1.wav',
'HIT_WALL':'pychinko/sfx/wall_hit.wav',
'ORB':'pychinko/sfx/orb_fire.wav',
'PEG_0':'pychinko/sfx/peg_hit.wav',
'PEG_1':'pychinko/sfx/peg_hit1.wav',
'PEG_2':'pychinko/sfx/peg_hit2.wav',
'PEG_3':'pychinko/sfx/peg_hit3.wav',
'REFRESH':'pychinko/sfx/refresh_hit.wav',
'SELECT':'pychinko/sfx/select.wav',
'VICTORY':'pychinko/sfx/level_complete.wav'
}

LEVELS = ['00']

def load_files(dir, sub):
    '''
    Given the name of a directory, returns a list of all files within
    containing a substring
    '''
    files = []
    for file in listdir(dir):
        f = path.join(dir, file)
        if path.isfile(f):
            if sub in f:
                files.append(f)
    return files

if __name__ == '__main__':
    files = load_files('pychinko/gfx/entities', 'orb')
    print(files)