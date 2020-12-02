import pygame
from pygame.locals import *
from queue import Queue
import random


class Cards:
    spades_2 = pygame.image.load('pictures/spades/2.png')
    spades_3 = pygame.image.load('pictures/spades/3.png')
    spades_4 = pygame.image.load('pictures/spades/4.png')
    spades_5 = pygame.image.load('pictures/spades/5.png')
    spades_6 = pygame.image.load('pictures/spades/6.png')
    spades_7 = pygame.image.load('pictures/spades/7.png')
    spades_8 = pygame.image.load('pictures/spades/8.png')
    spades_9 = pygame.image.load('pictures/spades/9.png')
    spades_10 = pygame.image.load('pictures/spades/10.png')
    spades_J = pygame.image.load('pictures/spades/J.png')
    spades_Q = pygame.image.load('pictures/spades/Q.png')
    spades_K = pygame.image.load('pictures/spades/K.png')
    spades_A = pygame.image.load('pictures/spades/A.png')

    hearts_2 = pygame.image.load('pictures/hearts/2.png')
    hearts_3 = pygame.image.load('pictures/hearts/3.png')
    hearts_4 = pygame.image.load('pictures/hearts/4.png')
    hearts_5 = pygame.image.load('pictures/hearts/5.png')
    hearts_6 = pygame.image.load('pictures/hearts/6.png')
    hearts_7 = pygame.image.load('pictures/hearts/7.png')
    hearts_8 = pygame.image.load('pictures/hearts/8.png')
    hearts_9 = pygame.image.load('pictures/hearts/9.png')
    hearts_10 = pygame.image.load('pictures/hearts/10.png')
    hearts_J = pygame.image.load('pictures/hearts/J.png')
    hearts_Q = pygame.image.load('pictures/hearts/Q.png')
    hearts_K = pygame.image.load('pictures/hearts/K.png')
    hearts_A = pygame.image.load('pictures/hearts/A.png')

    diamonds_2 = pygame.image.load('pictures/diamonds/2.png')
    diamonds_3 = pygame.image.load('pictures/diamonds/3.png')
    diamonds_4 = pygame.image.load('pictures/diamonds/4.png')
    diamonds_5 = pygame.image.load('pictures/diamonds/5.png')
    diamonds_6 = pygame.image.load('pictures/diamonds/6.png')
    diamonds_7 = pygame.image.load('pictures/diamonds/7.png')
    diamonds_8 = pygame.image.load('pictures/diamonds/8.png')
    diamonds_9 = pygame.image.load('pictures/diamonds/9.png')
    diamonds_10 = pygame.image.load('pictures/diamonds/10.png')
    diamonds_J = pygame.image.load('pictures/diamonds/J.png')
    diamonds_Q = pygame.image.load('pictures/diamonds/Q.png')
    diamonds_K = pygame.image.load('pictures/diamonds/K.png')
    diamonds_A = pygame.image.load('pictures/diamonds/A.png')

    clubs_2 = pygame.image.load('pictures/clubs/2.png')
    clubs_3 = pygame.image.load('pictures/clubs/3.png')
    clubs_4 = pygame.image.load('pictures/clubs/4.png')
    clubs_5 = pygame.image.load('pictures/clubs/5.png')
    clubs_6 = pygame.image.load('pictures/clubs/6.png')
    clubs_7 = pygame.image.load('pictures/clubs/7.png')
    clubs_8 = pygame.image.load('pictures/clubs/8.png')
    clubs_9 = pygame.image.load('pictures/clubs/9.png')
    clubs_10 = pygame.image.load('pictures/clubs/10.png')
    clubs_J = pygame.image.load('pictures/clubs/J.png')
    clubs_Q = pygame.image.load('pictures/clubs/Q.png')
    clubs_K = pygame.image.load('pictures/clubs/K.png')
    clubs_A = pygame.image.load('pictures/clubs/A.png')


pygame.init()
screen = pygame.display.set_mode((1280, 720))

deck = [card for card in dir(Cards) if not card.startswith("__")]
random.shuffle(deck)
deck_pc = Queue(26)
deck_player = Queue(26)

for d in deck:
    if deck_pc.full():
        deck_player.put(d)
    else:
        deck_pc.put(d)


def game():
    icon = pygame.image.load('pictures/icon.png')
    # bg = pygame.image.load('pictures/bg.jpg')

    back_blue = pygame.image.load('pictures/back_blue.png')
    # back_red = pygame.image.load('pictures/back_red.png')

    card_width = int(screen.get_width()/9)
    card_height = int(card_width * 1.25)
    # print(card_width, card_height)

    deck_pc_width = screen.get_width()/2-(card_width/2)
    deck_pc_height = screen.get_height()*0.02
    deck_player_width = screen.get_width()/2-(card_width/2)
    deck_player_height = screen.get_height()*0.98-card_height

    pc_width = screen.get_width()*0.5-(card_width+card_width*0.2)
    pc_height = screen.get_height()/2-(card_height/2)
    player_width = screen.get_width()*0.5+card_width*0.2
    player_height = screen.get_height()/2-(card_height/2)

    pygame.display.set_caption("War")
    pygame.display.set_icon(icon)

    screen.fill((0, 166, 43))
    # screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))

    if not deck_pc.empty():
        screen.blit(pygame.transform.scale(back_blue, (card_width, card_height)), (deck_pc_width, deck_pc_height))
    if not deck_player.empty():
        screen.blit(pygame.transform.scale(back_blue, (card_width, card_height)), (deck_player_width, deck_player_height))
    pygame.display.update()

    pygame.time.wait(500)

    card = deck_pc.get()
    screen.blit(pygame.transform.scale(getattr(Cards, card), (card_width, card_height)), (pc_width, pc_height))

    # if not first:
    card = deck_player.get()
    screen.blit(pygame.transform.scale(getattr(Cards, card), (card_width, card_height)), (player_width, player_height))
    pygame.display.update()


running = True
game()

while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        game()

    # elif event.type == VIDEORESIZE:
    #     card_width = int(screen.get_width() / 9)
    #     card_height = int(card_width * 1.25)
    #     print(card_width, card_height)
    #
    #     pc_width = screen.get_width() / 2 - (card_width / 2)
    #     pc_height = screen.get_height() * 0.02
    #     player_width = screen.get_width() / 2 - (card_width / 2)
    #     player_height = screen.get_height() * 0.98 - card_height
    #
    #     screen.fill((0, 166, 43))
    #     screen.blit(pygame.transform.scale(back_blue, (card_width, card_height)), (pc_width, pc_height))
    #     screen.blit(pygame.transform.scale(back_blue, (card_width, card_height)), (player_width, player_height))
    #     # screen.blit(pygame.transform.scale(bg, event.dict['size']), (0, 0))
    #
    #     pygame.display.update()
    # elif event.type == VIDEOEXPOSE:  # handles window minimising/maximising
    #     # screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
    #
    #     pygame.display.update()
