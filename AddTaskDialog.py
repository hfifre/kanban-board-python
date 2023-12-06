from Utils import Utils
import pygame

class AddTaskDialog:

    def __init__(self, images):
        self.black_back_back = images["BlackBackBackAddTask"]
        self.black_back = images["BlackBackAddTask"]
        self.input = images["InputAddTask"]

        self.cancel_btn = images["CancelBtn"]
        self.cancel_text = Utils.getTextWithColor("Annuler", 25, pygame.Color("#1C1C1C"))
        self.confirm_btn = images["ConfirmBtn"]
        self.confirm_text = Utils.getTextWithColor("Ajouter", 25, pygame.Color("#1C1C1C"))


        self.add_task_text = Utils.getText("Ajout tâche", 36)
        self.title_label = Utils.getText("Titre", 25)
        self.description_label = Utils.getText("Description", 25)

        temp_cancel_btn_rect = self.cancel_btn.get_rect()
        self.cancel_btn_rect = pygame.Rect(625, 435,temp_cancel_btn_rect.width, temp_cancel_btn_rect.height)

        temp_confirm_btn_rect = self.confirm_btn.get_rect()
        self.confirm_btn_rect = pygame.Rect(790, 435,temp_confirm_btn_rect.width, temp_confirm_btn_rect.height)


    def display(self, screen):
        screen.blit(self.black_back_back, (0,0))
        screen.blit(self.black_back, (402,153))

        screen.blit(self.add_task_text, (402 + 32, 153 + 10))

        screen.blit(self.title_label, (402 + 32,153 + 80))
        screen.blit(self.input, (402 + 32, 153 + 118))

        
        screen.blit(self.description_label, (402 + 32, 153 + 170))
        screen.blit(self.input, (402 + 32, 153 + 208))

        screen.blit(self.cancel_btn, self.cancel_btn_rect)
        screen.blit(self.cancel_text, (625 + 30, 435 + 5))
        screen.blit(self.confirm_btn, self.confirm_btn_rect)
        screen.blit(self.confirm_text, (790 + 30, 435 + 5))


    def check_interaction(self, mouse_pos):
        i = 15



