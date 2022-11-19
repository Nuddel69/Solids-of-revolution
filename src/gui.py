import json
from pathlib import Path
from typing import Tuple

import pygame

from model import Model
from core import Rotation


class Gui:
    def __init__(self, assets_dir: Path, demo: bool = False) -> None:
        pygame.init()

        with open(Path(assets_dir, 'config.json'), 'r') as _file:
            config = json.load(_file)
        
        font_file = Path(assets_dir, config['font_file'])
        self._font = pygame.font.Font(font_file, config['font_size'])

        self._display = pygame.display.set_mode(config['resolution'])
        pygame.display.set_caption(config['title'])

        self._clock = pygame.time.Clock()

        self._center = [int(config['resolution'][i] / 2) for i in range(2)]
        self._upscale = round(self._center[0] / 8)

        self._vertex_size = config['vertex_size']
        self._vertex_offset = int(self._vertex_size / 2)

        self._model_color = config['vertex_colors']
        self._bg_color = config['bg_color']
        self._framerate = config['fps']

        self._scrolling_sens = config['scrolling_sensitivity']
        self._rotation_speed = config['rotation_speed']

        self._terminated = False

        self._render_function = False;

        self._demo = demo;


    @property
    def terminated(self) -> bool:
        return self._terminated
    

    def _render_text(self, text: str, position: Tuple[int, int]) -> None:
        text_surface = self._font.render(text, True, (255, 255, 255))
        text_rectangle = text_surface.get_rect()
        
        text_rectangle.x, text_rectangle.y = position
        self._display.blit(text_surface, text_rectangle)


    def _position_2d_vertex(self, x: int, y: int) -> Tuple[int, int]:
        x = ((x*2) * self._upscale) + self._center[0]
        y = ((y*2) * self._upscale) + self._center[1]
        return x, y


    def render_model(self, model: Model) -> None:
        vertices, edges = model.get_shape()
        if vertices:
            for vertex in vertices:
                x = ((vertex[0]*2) * self._upscale) + self._center[0] + self._vertex_offset
                y = ((vertex[1]*2) * self._upscale) + self._center[1] + self._vertex_offset
                pygame.draw.circle(self._display, self._model_color, (x, y), self._vertex_size)
    
        if edges:
            for link in edges:
                vertex_1 = self._position_2d_vertex(*vertices[link[0]][:2])
                vertex_2 = self._position_2d_vertex(*vertices[link[1]][:2])

                pygame.draw.aaline(self._display, self._model_color, vertex_1, vertex_2, True)
    

    def render_function(self) -> None:
        abs_path = Path(__file__).resolve().parent
        with open(Path(abs_path, '../assets', 'FunctionConfig.json'), 'r') as _file:
            _config = json.load(_file)

        self._func = _config['Function'];
        self._lima = _config['a'];
        self._limb = _config['b'];
        self._render_function = True;
        pass

    def render_info(self) -> None:
        if (self._render_function):
            info = [
                    f'FPS: {self._clock.get_fps():.2f}',
                'X rotation: U/J',
                'Y rotation: I/K',
                'Z rotation: O/L',
                '',
                f'Function: f(x) = {self._func}',
                f'Interval: [{self._lima}, {self._limb}]',
            ]
        else:
            info = [
                f'FPS - {self._clock.get_fps():.2f}',
                'X rotation - U/J',
                'Y rotation - I/K',
                'Z rotation - O/L',
            ]

        for index, text in enumerate(info):
            self._render_text(text, (8, (index*25) + 5))


    def update_display(self) -> None:
        pygame.display.update()
        self._display.fill(self._bg_color)
        self._clock.tick(self._framerate)


    def get_rotation(self) -> Rotation:
        rotation = [0, 0, 0]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self._terminated = True
                return
            
            if event.type == pygame.MOUSEWHEEL:
                self._upscale += (event.y * self._scrolling_sens)

        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_u] or self._demo): rotation[0] += self._rotation_speed
        if (keys[pygame.K_i] or self._demo): rotation[1] += self._rotation_speed
        if keys[pygame.K_o]: rotation[2] += self._rotation_speed
        if keys[pygame.K_j]: rotation[0] -= self._rotation_speed
        if keys[pygame.K_k]: rotation[1] -= self._rotation_speed
        if (keys[pygame.K_l] or self._demo): rotation[2] -= self._rotation_speed

        return rotation
