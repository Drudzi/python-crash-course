import sys, cProfile
from random import randint
from time import sleep

import pygame

from ss_settings import Settings
from ss_spaceship import SpaceShip
from ss_bullet import Bullet
from ss_enemy import Enemy
from ss_gamestats import GameStats
from ss_button import Button
from ss_scoreboard import ScoreBoard

class SidewaysShooter:
    """The overall class to manage the game and it's resources and behaviour."""
    
    def __init__(self):
        """Initialize the game and create its resources."""
        pygame.init()

        self.fps = 120
        self.fps_clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Sideways Shooter")

        self.stats = GameStats(self)
        self.scoreboard = ScoreBoard(self)

        self.spaceship = SpaceShip(self)

        self.bullets = pygame.sprite.Group()
        
        self.pre_enemies = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.play_button = Button(self, 'Play', 'play', (0, 150, 0), 48)
        self.easy_button = Button(self, 'Easy', 'easy', (180, 180, 0), 32)
        self.medium_button = Button(self, 'Medium', 'medium', (200, 140, 0), 32)
        self.hard_button = Button(self, 'Hard', 'hard', (150, 0, 0), 32)

        self._create_fleet()

    def run_game(self):
        """Method including the main game loop. Runs the game."""
        
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.spaceship.update()
                self._update_bullets()
                self._update_enemies()
            
            self._update_screen()

    def _check_events(self):
        """Respond to user inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_score()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_buttons(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Resond to the play-button being clicked."""
        click = self.play_button.rect.collidepoint(mouse_pos)
        if click and not self.stats.game_active:
            
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            self.scoreboard.prep_score()
            
            self.enemies.empty()
            self.bullets.empty()
            
            self._create_fleet()
            
            self.spaceship.center_spaceship()

            pygame.mouse.set_visible(False)
    
    def _check_difficulty_buttons(self, mouse_pos):
        """Resond to clicks on diff-buttons."""
        easy_click = self.easy_button.rect.collidepoint(mouse_pos)
        medium_click = self.medium_button.rect.collidepoint(mouse_pos)
        hard_click = self.hard_button.rect.collidepoint(mouse_pos)

        if easy_click and not self.stats.game_active:
            self.settings.difficulty = 'easy'
            self.settings.speedup_scale = 1.1
        
        elif medium_click and not self.stats.game_active:
            self.settings.difficulty = 'medium'
            self.settings.speedup_scale = 1.2
        
        elif hard_click and not self.stats.game_active:
            self.settings.difficulty = 'hard'
            self.settings.speedup_scale = 1.3
    
    def _active_difficulty_text_color(self):
        """Set the appropriate text color on the diff-buttons."""
        if self.settings.difficulty == 'easy':
            self.easy_button.text_color = self.settings.active_diff_text_color
            self.easy_button._prep_msg('Easy')
        else:
            self.easy_button.text_color = (255, 255, 255)
            self.easy_button._prep_msg('Easy')
        
        if self.settings.difficulty == 'medium':
            self.medium_button.text_color = self.settings.active_diff_text_color
            self.medium_button._prep_msg('Medium')
        else:
            self.medium_button.text_color = (255, 255, 255)
            self.medium_button._prep_msg('Medium')
        
        if self.settings.difficulty == 'hard':
            self.hard_button.text_color = self.settings.active_diff_text_color
            self.hard_button._prep_msg('Hard')
        else:
            self.hard_button.text_color = (255, 255, 255)
            self.hard_button._prep_msg('Hard')

    def _check_keydown_events(self, event):
        """Check if a key has been pressed."""
        if event.key == pygame.K_UP:
            self.spaceship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.spaceship.moving_down = True
        if event.key == pygame.K_q:
            self.stats.save_high_score()
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Check if key has been released."""
        if event.key == pygame.K_UP:
            self.spaceship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.spaceship.moving_down = False

    def _fire_bullet(self):
        """Add new bullet to bullets group."""
        if len(self.bullets) < self.settings.amount_bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the bullets position and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        
        self._check_bullet_enemy_collision()
    
    def _check_bullet_enemy_collision(self):
        """Respond to bullet-enemy collissions."""
        #Check whether a bullet has hit an enemy, kill it and remove the bullet:
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.kill_score * len(enemies)
            
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.enemies:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()
        
    def _update_enemies(self):
        """Update the positions of the enemies in the fleet."""
        self.enemies.update()

        if pygame.sprite.spritecollideany(self.spaceship, self.enemies):
            self._ship_hit()
        
        self._check_enemies_leftEdge()
    
    def _create_fleet(self):
        """Create an enemy fleet."""
    
        while len(self.enemies.sprites()) <= (self.settings.amount_enemies_fleet - 1):
            self._create_enemy()
               
    def _create_enemy(self):
        """Create an enemy and set its position."""
        enemy = Enemy(self)

        self.pre_enemies.add(enemy)
        
        collisions = pygame.sprite.groupcollide(
        self.pre_enemies, self.enemies, True, False, pygame.sprite.collide_rect_ratio(1.2))
        
        if not collisions: #If there was no collision...
            self.enemies.add(enemy)
        
        self.pre_enemies.empty()
        collisions.clear()
    
    def _ship_hit(self):
        """Respond to the spaceship getting hit by an enemy."""
        if self.stats.spaceships_used < self.settings.spaceship_limit:
            self.stats.spaceships_used += 1

            self.enemies.empty()
            self.bullets.empty()

            self._create_fleet()
            self.spaceship.center_spaceship()

            sleep(0.5)
        
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_enemies_leftEdge(self):
        """Respond to an enemy reaching the left edge of the screen."""
        for enemy in self.enemies.sprites():
            if enemy.rect.left <= 0:
                self._ship_hit()
                break
            
    def _update_screen(self):
        """Update the surfaces on the screen and flip the new one."""
        #self.screen.blit(self.settings.background_image, (0, 0))
        self.screen.fill((self.settings.background_color))
        self.spaceship.blit_spaceship()
        
        for bullet in self.bullets.sprites():
            bullet.blit_bullet()
        
        self.enemies.draw(self.screen)

        self.scoreboard.draw_score()
        
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
            self._active_difficulty_text_color()

        pygame.display.flip()


if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()