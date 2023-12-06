from Utils import Utils
import pygame
from AppState import AppState
from enum import Enum
from Cursor import Cursor

class InputAddTask(Enum):
    No = 0,
    Title = 1,
    Description = 2



class AddTaskDialog:

    def __init__(self, images):
        self.black_back_back = images["BlackBackBackAddTask"]
        self.black_back = images["BlackBackAddTask"]
        self.input = images["InputAddTask"]
        self.input_hovered = images["InputAddTaskHovered"]

        self.cancel_btn = images["CancelBtn"]
        self.cancel_text = Utils.getTextWithColor("Annuler", 25, pygame.Color("#1C1C1C"))
        self.confirm_btn = images["ConfirmBtn"]
        self.confirm_text = Utils.getTextWithColor("Ajouter", 25, pygame.Color("#1C1C1C"))


        self.add_task_text = Utils.getText("Ajout tâche", 36)
        self.title_label = Utils.getText("Titre", 25)
        self.description_label = Utils.getText("Description", 25)

        self.title_text = Utils.getText("Entrez le titre...", 20)
        self.description_text = Utils.getText("Entrez la description...", 20)

        temp_cancel_btn_rect = self.cancel_btn.get_rect()
        self.cancel_btn_rect = pygame.Rect(625, 435,temp_cancel_btn_rect.width, temp_cancel_btn_rect.height)

        temp_confirm_btn_rect = self.confirm_btn.get_rect()
        self.confirm_btn_rect = pygame.Rect(790, 435,temp_confirm_btn_rect.width, temp_confirm_btn_rect.height)

        temp_input_title_rect = self.input.get_rect()
        self.input_title_rect = pygame.Rect(402 + 32, 153 + 118,temp_input_title_rect.width, temp_input_title_rect.height)

        temp_input_description_rect = self.input.get_rect()
        self.input_description_rect = pygame.Rect(402 + 32, 153 + 208,temp_input_description_rect.width, temp_input_description_rect.height)

        self.title = ""
        self.description = ""

        self.selected_input = InputAddTask.No
        self.is_cancel_hovered = False
        self.is_confirm_hovered = False
        self.is_input_title_hovered = False
        self.is_input_description_hovered = False

    def display(self, screen):
        screen.blit(self.black_back_back, (0,0))
        screen.blit(self.black_back, (402,153))

        screen.blit(self.add_task_text, (402 + 32, 153 + 10))

        screen.blit(self.title_label, (402 + 32,153 + 80))

        if self.is_input_title_hovered or self.selected_input == InputAddTask.Title:
            screen.blit(self.input_hovered, self.input_title_rect)
        else:
            screen.blit(self.input, self.input_title_rect)

        screen.blit(self.title_text, (402 + 32 + 8, 153 + 118))


        
        screen.blit(self.description_label, (402 + 32, 153 + 170))

        if self.is_input_description_hovered or self.selected_input == InputAddTask.Description:
            screen.blit(self.input_hovered , self.input_description_rect)
        else:
            screen.blit(self.input, self.input_description_rect)
        screen.blit(self.description_text, (402 + 32 + 8, 153 + 208))
        

        screen.blit(self.cancel_btn, self.cancel_btn_rect)
        screen.blit(self.cancel_text, (625 + 30, 435 + 5))
        screen.blit(self.confirm_btn, self.confirm_btn_rect)
        screen.blit(self.confirm_text, (790 + 30, 435 + 5))




    def confirmClick(self):
        AppState.in_add_mode = False
        Cursor.nb_hovered -= 1
        Cursor.has_changed = True
        print("Confirm")

    def cancelClick(self):
        AppState.in_add_mode = False
        self.title = ""
        self.description = ""
        Cursor.nb_hovered -= 1
        Cursor.has_changed = True
        print("Cancel")
        


    def check_interaction_btn(self, mouse_pos):
        is_confirm_btn_hovered = self.confirm_btn_rect.collidepoint(mouse_pos)
        is_cancel_btn_hovered = self.cancel_btn_rect.collidepoint(mouse_pos)

        if is_confirm_btn_hovered and AppState.is_clicking:
            self.confirmClick()

        if is_cancel_btn_hovered and AppState.is_clicking:
            self.cancelClick()


        if is_confirm_btn_hovered != self.is_confirm_hovered:
            self.is_confirm_hovered = is_confirm_btn_hovered
            Cursor.nb_hovered += (1 if is_confirm_btn_hovered else -1)
            Cursor.has_changed = True

        if is_cancel_btn_hovered != self.is_cancel_hovered:
            self.is_cancel_hovered = is_cancel_btn_hovered
            Cursor.nb_hovered += (1 if is_cancel_btn_hovered else -1)
            Cursor.has_changed = True

    def check_interaction_input(self, mouse_pos):

        is_input_title_hovered = self.input_title_rect.collidepoint(mouse_pos)
        is_input_description_hovered = self.input_description_rect.collidepoint(mouse_pos)


        if is_input_title_hovered and AppState.is_clicking:
            self.selected_input = InputAddTask.Title

        if is_input_description_hovered and AppState.is_clicking:
            self.selected_input = InputAddTask.Description


        if self.is_input_title_hovered != is_input_title_hovered:
            self.is_input_title_hovered = is_input_title_hovered
            Cursor.nb_hovered += (1 if is_input_title_hovered else -1)
            Cursor.has_changed = True

        if self.is_input_description_hovered != is_input_description_hovered:
            self.is_input_description_hovered = is_input_description_hovered
            Cursor.nb_hovered += (1 if is_input_description_hovered else -1)
            Cursor.has_changed = True


        if self.selected_input == InputAddTask.No:
            return
        
        do_key_pressed = len(AppState.key_pressed) > 0

        for key in AppState.key_pressed:
            
            if self.selected_input == InputAddTask.Title:
                self.title += pygame.key.name(key)
            else:
                self.description += pygame.key.name(key)


        if do_key_pressed:
            if self.selected_input == InputAddTask.Title:
                self.title_text = Utils.getText(self.title, 20)
            else:
                self.description_text = Utils.getText(self.description, 20)


    def check_interaction(self, mouse_pos):
        
        self.check_interaction_btn(mouse_pos)
        self.check_interaction_input(mouse_pos)
        
        

        

        




