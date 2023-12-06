from Utils import Utils
from Cursor import Cursor
import pygame
from AppState import AppState

class Task:

    back_task_img = None
    back_task_hovered_img = None

    def __init__(self, title, description):
        self.title = title
        self.description = description

        self.title_text = Utils.getText(title, 20)
        self.description_text = Utils.getText(description, 10)

        self.is_hovered = False

        temp_back_task_rect = Task.back_task_img.get_rect()
        self.back_task_rect = pygame.Rect(0,0, temp_back_task_rect.width, temp_back_task_rect.height)


    def draw(self, screen, i, delta_section_pos):
        
        delta_back_pos = (delta_section_pos[0] + 16, delta_section_pos[1] + 16 + 16 * i + 63 * i)
        self.back_task_rect.update(delta_back_pos[0], delta_back_pos[1], self.back_task_rect.width, self.back_task_rect.height)

        if self.is_hovered:
            screen.blit(Task.back_task_hovered_img, self.back_task_rect)
        else:
            screen.blit(Task.back_task_img, self.back_task_rect)

        screen.blit(self.title_text, (delta_back_pos[0] + 16 , delta_back_pos[1] + 10))
        screen.blit(self.description_text, (delta_back_pos[0] + 16 , delta_back_pos[1] + 36))

    def check_interaction(self, mouse_pos):
        is_hovered = self.back_task_rect.collidepoint(mouse_pos)


        if AppState.is_clicking and is_hovered:
            print("Click Task ", self.title)
            AppState.selected_task = self

        if self.is_hovered == is_hovered:
            return

        self.is_hovered = is_hovered
        
        Cursor.nb_hovered += (1 if is_hovered else -1)
        Cursor.has_changed = True

        