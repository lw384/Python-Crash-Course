import pygame
from cairosvg import svg2png
from io import BytesIO

class Star:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        # 使用load_svg加载SVG文件，设置大小为100x100像素
        self.image = self.load_svg('Alien/images/star.svg', size=(60, 60))
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.center = self.screen_rect.center

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
        
        
        
        
        