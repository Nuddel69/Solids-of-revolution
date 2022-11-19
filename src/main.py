import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
from pathlib import Path
from contextlib import suppress
import argparse

import core
from gui import Gui
from model import Model
from generators import Generators


def main(path: str, model: Model, isFunc, args) -> None:
    if (args.demo):
        gui = Gui(Path(path, '../assets'), True);
    else:
        gui = Gui(Path(path, '../assets'));


    if (isFunc):
        gui.render_function();

    while not gui.terminated:
        rotation = gui.get_rotation()

        if rotation is None:
            continue

        if rotation != [0, 0, 0]:
            old_vertices = model.get_vertices()
            rotation_matrix = core.create_matrix(rotation)
            
            new_vertices = core.rotate_vertices(old_vertices, rotation_matrix)
            model.set_vertices(new_vertices)
        
        gui.render_model(model)

        if (args.demo == 0):
            gui.render_info()
        
        gui.update_display()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'main.py')

    parser.add_argument("-d", "--demo", dest="demo", action="store_true", help="run program demo");

    args = parser.parse_args();
    
    abs_path = Path(__file__).resolve().parent

    isFunc = False;
    model = None
    while model is None:
        with suppress(IndexError, ValueError):
            if sys.platform == 'win32':
                os.system('cls')
            else:
                os.system('clear')

            print('Available Models:')
            for index, model_name in enumerate(Generators.__all__):
                print(f'{index+1:<{2}} : {model_name}')

            choice = int(input('\n> '))

            if (Generators.__all__[choice-1] == 'function') : isFunc = True;
            
            model = Model(*getattr(Generators, Generators.__all__[choice-1])())
            break
    
    main(abs_path, model, isFunc, args);
