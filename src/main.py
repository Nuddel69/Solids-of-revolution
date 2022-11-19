import os
import sys
from pathlib import Path
from contextlib import suppress

import core
from gui import Gui
from model import Model
from generators import Generators
from solid_of_revolution import Revolution_function


def main(path: str, model: Model, isFunc) -> None:
    gui = Gui(Path(path, '../assets'))

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

        if (isFunc):
            gui.render_function();

        gui.render_info()
        
        gui.update_display()

if __name__ == '__main__':
    abs_path = Path(__file__).resolve().parent

    func = Revolution_function();
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
            if (Generators.__all__[choice-1] == 'function'):
                model = Model(*getattr(Generators, Generators.__all__[choice-1])(func.f_main, func._a, func._b))
                isFunc = True;
            else:
                model = Model(*getattr(Generators, Generators.__all__[choice-1])())
                isFunc = False;
            break
    
    main(abs_path, model, isFunc);
