import pygame
from Cursor import Cursor
from AppState import AppState

class Section:

    back_section_img = None
    back_title_hovered_img = None

    def __init__(self, title_back_img, title_back_pos, title_text, title_text_pos, back_task_pos):
        self.title_back_img = title_back_img
        self.title_text = title_text
        self.title_text_pos = title_text_pos

        temp_back_section_rect = Section.back_section_img.get_rect()
        self.back_section_rect = pygame.Rect(back_task_pos[0],back_task_pos[1],temp_back_section_rect.width, temp_back_section_rect.height)
        
        temp_title_back_rect = title_back_img.get_rect()
        self.title_back_rect = pygame.Rect(title_back_pos[0],title_back_pos[1],temp_title_back_rect.width, temp_title_back_rect.height)

        self.is_title_hovered = False
        self.tasks = []


    def display(self, screen : pygame.Surface):
        screen.blit(Section.back_section_img, self.back_section_rect)

        if not self.is_title_hovered:
            screen.blit(self.title_back_img, self.title_back_rect)
        else:
            screen.blit(Section.back_title_hovered_img, self.title_back_rect)

        screen.blit(self.title_text, self.title_text_pos)
    
        i = 0
        for task in self.tasks:
            task.draw(screen, i, (self.back_section_rect[0],self.back_section_rect[1]))
            i += 1

    def addTask(self, task):
        self.tasks.append(task)

    def check_interaction(self, mouse_pos):


        for task in self.tasks:
            task.check_interaction(mouse_pos)
            
        is_title_hovered = self.title_back_rect.collidepoint(mouse_pos)

        if is_title_hovered and AppState.is_clicking:
            AppState.selected_section = self
            
        if self.is_title_hovered == is_title_hovered:
            return

        self.is_title_hovered = is_title_hovered
        
        Cursor.nb_hovered += (1 if is_title_hovered else -1)
        Cursor.has_changed = True

        