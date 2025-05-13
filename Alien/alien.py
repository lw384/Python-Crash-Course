import pygame
from cairosvg import svg2png
from io import BytesIO
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """管理alien的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

  
        self.image = self.load_svg('Alien/images/alien.svg', size=(50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position
        self.x = float(self.rect.x)
       

    def load_svg(self, svg_path, size=(64, 64)):
        """加载SVG文件并转换为Pygame可用的surface
        
        Args:
            svg_path: SVG文件的路径
            size: 期望的输出尺寸,默认为64x64
        """
        # 将SVG转换为PNG
        png_data = svg2png(url=svg_path, output_width=size[0], output_height=size[1])
        
        # 将PNG数据转换为Pygame surface
        png_io = BytesIO(png_data)
        return pygame.image.load(png_io)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
        
        
        
        