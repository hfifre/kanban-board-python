from Utils import Utils
import pygame
from AppState import AppState 
from Cursor import Cursor

class AddBtn:

    def __init__(self, images):
        self.btn = images["AddTaskBtn"]
        self.btn_hovered = images["AddTaskBtnHovered"]

        self.plus = Utils.getText("+", 40)

        temp_btn_rect = self.btn.get_rect()
        self.btn_rect = pygame.Rect(8,26,temp_btn_rect.width, temp_btn_rect.height)

        self.is_hovered = False

    def display(self, screen):

        if self.is_hovered:
            screen.blit(self.btn_hovered, self.btn_rect)
        else:
            screen.blit(self.btn, self.btn_rect)

        screen.blit(self.plus, (18, 12))

    def check_interaction(self, mouse_pos):
        is_hovered = self.btn_rect.collidepoint(mouse_pos)

        if is_hovered and AppState.is_clicking:
            Cursor.nb_hovered -= 1
            Cursor.has_changed = True
            AppState.in_add_mode = True

        if self.is_hovered == is_hovered:
            return
        
        self.is_hovered = is_hovered

        Cursor.nb_hovered += (1 if is_hovered else -1)
        Cursor.has_changed = True
