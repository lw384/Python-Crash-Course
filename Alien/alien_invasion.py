import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from star import Star
from bullets import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scroeboard import Scoreboard


class AlienInvasion:
    """class to manage game assets and behavior"""
    def __init__(self):
        """init game"""
        pygame.init()
        # 设置刷新率
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.star = Star(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.game_active = False
        self.play_button = Button(self,'play')

        self.create_fleet()
        

    def check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        
    
    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    

    def fire_bullet(self):
        """create new bullets and add them to group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullet(self):
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
        if not self.aliens:
            self.bullets.empty()
            self.creat_fleet()


    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x , curretn_y = alien_width,alien_height
        while curretn_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self.create_alien(current_x,curretn_y)
                current_x += 2 * alien_width
            
            current_x = alien_width
            curretn_y += 2 * alien_height

    def create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def update_alien(self):
        self.check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()
        
        self.check_aliens_bottom()
    
    def ship_hit(self):
        if self.stats.ship_left > 0:
          self.stats.ship_left -=1
          
          self.bullets.empty()
          self.aliens.empty()
          self.create_fleet()
          self.ship.center_ship()
          sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(False)
    
    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed;
        self.settings.fleet_direction *=-1
    

    def check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self.ship_hit()
                break
    def check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.sb.prep_score()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()
            self.create_fleet()
            self.ship.center_ship()
            

            pygame.mouse.set_visible(False)


    def update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color) 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.star.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def run_game(self):
        while True:
             self.check_events()

             if self.game_active:
              self.ship.update()  
              self.update_bullet()
              self.update_alien()
            
           

             self.update_screen()
             self.clock.tick(60)
            
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

