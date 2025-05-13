import pygame
from cairosvg import svg2png
from io import BytesIO

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        # 使用load_svg加载SVG文件，设置大小为100x100像素
        self.image = self.load_svg('Alien/images/ship.svg', size=(100, 100))
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
       

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

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        
        
        