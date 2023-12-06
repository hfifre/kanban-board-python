import pygame
import os
from Section import Section
from Task import Task
from Utils import Utils
from Cursor import Cursor
from AddTaskDialog import AddTaskDialog
from AppState import AppState
from AddBtn import AddBtn

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((1360, 800))
    pygame.display.set_caption('Kanban')


    base_path = os.path.dirname(os.path.abspath(__file__))
    Utils.asset_path = os.path.join(base_path, "assets")


    image_base_path = os.path.join(Utils.asset_path, "images")


    titles_to_load = ["A FAIRE", "EN COURS", "EN TEST", "TERMINE"]

    files_to_load = [f for f in os.listdir(image_base_path) if os.path.isfile(os.path.join(image_base_path, f))]
    images = {}

    sections = []


    for imageToLoadName in files_to_load:
        
        img = pygame.image.load(os.path.join(image_base_path, imageToLoadName))
        pygame.Surface.convert_alpha(img)
        name, extension = os.path.splitext(imageToLoadName)

        if name == "BackSection":
            Section.back_section_img = img
        elif name == "BackTask":
            Task.back_task_img = img
        elif name == "BackTaskHovered":
            Task.back_task_hovered_img = img
        elif name == "TitleBackHovered":
            Section.back_title_hovered_img = img
        elif "TitleBack" in name:
            sectionId = len(sections)
            title_back_img = img
            title_back_pos = (50 + 320 * sectionId, 26)
            title_text = Utils.getText(titles_to_load[sectionId], 36)
            title_text_pos = (136 + 320 * sectionId, 34)
            back_task_pos = (50 + 320 * sectionId, 116)
            sections.append(Section(title_back_img, title_back_pos, title_text, title_text_pos, back_task_pos))
        else:
            images[name] = img


    return screen, images, sections
    


def tryUpdateCursor():
    if not Cursor.has_changed:
        return
    
    if Cursor.nb_hovered > 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)


def main():
    screen, images, sections = initialize()

    task = Task("Créer UI", "Toi même tu sais.")
    sections[0].addTask(task)

    task = Task("Integration", "Toi même tu sais.")
    sections[0].addTask(task)

    task = Task("Finaliser Processus", "Toi même tu sais.")
    sections[0].addTask(task)

    add_btn = AddBtn(images)
    add_task_dialog = AddTaskDialog(images)

    running = True

    pygame.mouse.set_cursor(*pygame.cursors.arrow)

    

    while running:
        
        AppState.key_pressed = []
        AppState.is_clicking = False
        Cursor.has_changed = False

        if Cursor.nb_hovered < 0:
            Cursor.nb_hovered = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                AppState.is_clicking = True

            if event.type == pygame.KEYDOWN:
                AppState.key_pressed.append(event.key)


        back_color = pygame.Color("#1C1C1C")
        screen.fill(back_color)

        mouse_pos = pygame.mouse.get_pos()


        for section in sections:

            if not AppState.in_add_mode:
                section.check_interaction(mouse_pos)
                add_btn.check_interaction(mouse_pos)

            section.display(screen)

        add_btn.display(screen)

        if AppState.in_add_mode:
            add_task_dialog.check_interaction(mouse_pos)
            add_task_dialog.display(screen)

        tryUpdateCursor()



  
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    main()
