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


values = {
    "spades_2": 2,
    "spades_3": 3,
    "spades_4": 4,
    "spades_5": 5,
    "spades_6": 6,
    "spades_7": 7,
    "spades_8": 8,
    "spades_9": 9,
    "spades_10": 10,
    "spades_J": 12,
    "spades_Q": 13,
    "spades_K": 14,
    "spades_A": 15,

    "hearts_2": 2,
    "hearts_3": 3,
    "hearts_4": 4,
    "hearts_5": 5,
    "hearts_6": 6,
    "hearts_7": 7,
    "hearts_8": 8,
    "hearts_9": 9,
    "hearts_10": 10,
    "hearts_J": 12,
    "hearts_Q": 13,
    "hearts_K": 14,
    "hearts_A": 15,

    "diamonds_2": 2,
    "diamonds_3": 3,
    "diamonds_4": 4,
    "diamonds_5": 5,
    "diamonds_6": 6,
    "diamonds_7": 7,
    "diamonds_8": 8,
    "diamonds_9": 9,
    "diamonds_10": 10,
    "diamonds_J": 12,
    "diamonds_Q": 13,
    "diamonds_K": 14,
    "diamonds_A": 15,

    "clubs_2": 2,
    "clubs_3": 3,
    "clubs_4": 4,
    "clubs_5": 5,
    "clubs_6": 6,
    "clubs_7": 7,
    "clubs_8": 8,
    "clubs_9": 9,
    "clubs_10": 10,
    "clubs_J": 12,
    "clubs_Q": 13,
    "clubs_K": 14,
    "clubs_A": 15
}


pygame.init()
font = pygame.font.SysFont("monospace", 16, True)
font_score = pygame.font.SysFont("monospace", 24, True)
font_middle = pygame.font.SysFont("monospace", 35, True)
font_war = pygame.font.SysFont("monospace", 50, True)
font_title = pygame.font.SysFont("monospace", 100, True)
screen = pygame.display.set_mode((800, 800))

deck = [card for card in dir(Cards) if not card.startswith("__")]
deck_pc = Queue(52)
deck_player = Queue(52)
deck_war = Queue(52)

icon = pygame.image.load('pictures/icon.png')
bg = pygame.image.load('pictures/bg.png')


def init_decks():
    random.shuffle(deck)
    global deck_pc, deck_player, deck_war

    while not deck_pc.empty():
        deck_pc.get()
    while not deck_player.empty():
        deck_player.get()
    while not deck_war.empty():
        deck_war.get()

    i = 1
    for d in deck:
        if i % 2:
            deck_player.put(d)
        else:
            deck_pc.put(d)
        i += 1


def game():
    global war, war_size, first, war_winner

    back_blue = pygame.image.load('pictures/back_blue.png')
    # back_red = pygame.image.load('pictures/back_red.png')

    card_width = int(140)
    card_height = int(card_width * 1.25)

    deck_pc_width = screen.get_width()/2-(card_width/2)
    deck_pc_height = screen.get_height()*0.03
    deck_player_width = screen.get_width()/2-(card_width/2)
    deck_player_height = screen.get_height()*0.97-card_height

    pc_width = screen.get_width()*0.5-(card_width+card_width*0.8)
    pc_height = screen.get_height()/2-(card_height/2)
    player_width = screen.get_width()*0.5+card_width*0.8
    player_height = screen.get_height()/2-(card_height/2)

    pygame.display.set_caption("War")
    pygame.display.set_icon(icon)

    screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))

    if not first:
        card_pc = deck_pc.get()
        screen.blit(pygame.transform.scale(getattr(Cards, card_pc), (card_width, card_height)), (pc_width, pc_height))

        card_player = deck_player.get()
        screen.blit(pygame.transform.scale(getattr(Cards, card_player), (card_width, card_height)), (player_width, player_height))

        # draw PC name
        pc_name = font.render("PC", True, (255, 255, 255))
        pygame.draw.rect(screen, (62, 161, 87), (pc_width + card_width / 2 - 10, pc_height + card_height + 3, 20, 15))
        screen.blit(pc_name, (pc_width + card_width / 2 - 10, pc_height + card_height + 2))

        # draw PLAYER name
        player_name = font.render("PLAYER", True, (255, 255, 255))
        pygame.draw.rect(screen, (62, 161, 87), (player_width + card_width / 2 - 30, pc_height + card_height + 3, 60, 15))
        screen.blit(player_name, (player_width + card_width / 2 - 30, pc_height + card_height + 2))

        pygame.display.update()

    # draw PC name
    pc_name = font.render("PC", True, (255, 255, 255))
    pygame.draw.rect(screen, (62, 161, 87), (deck_pc_width + card_width/2 - 10, 3, 20, 15))
    screen.blit(pc_name, (deck_pc_width + card_width/2 - 10, 1))

    if not deck_pc.empty():
        screen.blit(pygame.transform.scale(back_blue, (card_width, card_height)), (deck_pc_width, deck_pc_height))

    deck_pc_size = font.render("Cards in deck: "+str(deck_pc.qsize()), True, (255, 255, 255))
    pygame.draw.rect(screen, (62, 161, 87), (deck_pc_width-15, deck_pc_height + card_height + 7, card_width+30, 20))
    screen.blit(deck_pc_size, (deck_pc_width-15, deck_pc_height + card_height + 7))

    # draw PLAYER name
    player_name = font.render("PLAYER", True, (255, 255, 255))
    pygame.draw.rect(screen, (62, 161, 87), (deck_player_width + card_width / 2 - 30, screen.get_height() - 18, 60, 15))
    screen.blit(player_name, (deck_player_width + card_width / 2 - 30, screen.get_height() - 19))

    if not deck_player.empty():
        screen.blit(pygame.transform.scale(back_blue, (card_width, card_height)), (deck_player_width, deck_player_height))

    deck_player_size = font.render("Cards in deck: " + str(deck_player.qsize()), True, (255, 255, 255))
    pygame.draw.rect(screen, (62, 161, 87), (deck_player_width - 15, deck_player_height - 27, card_width + 30, 20))
    screen.blit(deck_player_size, (deck_player_width - 15, deck_player_height - 27))

    pygame.display.update()

    if not first:
        if values[card_pc] > values[card_player]:
            if war == 0:
                deck_pc.put(card_player)
                deck_pc.put(card_pc)
            elif war == 1:
                if deck_war.qsize()/2 < war_size:
                    deck_war.put(card_player)
                    deck_war.put(card_pc)
                else:
                    war = 0
                    war_size = 0
                    war_winner = "PC"
                    deck_war.put(card_player)
                    deck_war.put(card_pc)
                    while not deck_war.empty():
                        deck_pc.put(deck_war.get())

        if values[card_player] > values[card_pc]:
            if war == 0:
                deck_player.put(card_player)
                deck_player.put(card_pc)
            elif war == 1:
                if deck_war.qsize()/2 < war_size:
                    deck_war.put(card_player)
                    deck_war.put(card_pc)
                else:
                    war = 0
                    war_size = 0
                    war_winner = "PLAYER"
                    deck_war.put(card_player)
                    deck_war.put(card_pc)
                    while not deck_war.empty():
                        deck_player.put(deck_war.get())

        # WAR
        if values[card_player] == values[card_pc]:
            if war == 0:
                war = 1
                if card_pc == "clubs_A" or card_pc == "diamonds_A" or card_pc == "hearts_A" or card_pc == "spades_A":
                    war_size = 11
                else:
                    war_size = values[card_player]
                deck_war.put(card_player)
                deck_war.put(card_pc)
            elif war == 1:
                if deck_war.qsize() / 2 < war_size:
                    deck_war.put(card_player)
                    deck_war.put(card_pc)
                else:
                    war_size += values[card_player]
                    print("war after war", war_size)
                    deck_war.put(card_player)
                    deck_war.put(card_pc)

    pygame.display.update()


def show_score():
    global score_PLAYER, score_PC
    score = font_score.render("PLAYER " + str(score_PLAYER) + " - " + str(score_PC) + " PC", True, (255, 255, 255))
    pygame.draw.rect(screen, (62, 161, 87), (screen.get_width()*0.68-10, 0, 300, 50))
    screen.blit(score, (screen.get_width()*0.68, 20))
    pygame.display.update()


score_PC = 0
score_PLAYER = 0
war = 0
war_size = 0
war_winner = ""
first = False
winner = ""

screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))

title = font_title.render("W A R", True, (255, 255, 255))
pygame.draw.rect(screen, (62, 161, 87), (screen.get_width() * 0.15, screen.get_height() * 0.25, 580, 100))
screen.blit(title, (screen.get_width() * 0.3, screen.get_height() * 0.25))

title = font_score.render("Click to start", True, (255, 255, 255))
pygame.draw.rect(screen, (62, 161, 87), (screen.get_width() * 0.25, screen.get_height() * 0.75, 400, 100))
screen.blit(title, (screen.get_width() * 0.37, screen.get_height() * 0.8))

pygame.display.update()

while 1:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit(0)

    if score_PC == 0 and score_PLAYER == 0:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                first = True

                init_decks()
                game()
                show_score()

    while not deck_pc.empty() and not deck_player.empty():
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 4 or event.button == 5:  # event.button == 4 and 5 are for testing purposes only
                x, y = pygame.mouse.get_pos()
                if 330 <= x <= 470 and 601 <= y <= 775:
                    first = False
                    game()
                    show_score()

        if deck_pc.empty():
            war = 0
            winner = "Player"
            score_PLAYER += 1
            break
        if deck_player.empty():
            war = 0
            winner = "PC"
            score_PC += 1
            break

    while winner:
        screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))

        title = font_war.render("PLAYER " + str(score_PLAYER) + " - " + str(score_PC) + " PC", True, (255, 255, 255))
        pygame.draw.rect(screen, (62, 161, 87), (screen.get_width() * 0.15, screen.get_height() * 0.25, 580, 100))
        screen.blit(title, (screen.get_width() * 0.2, screen.get_height() * 0.28))

        title = font_middle.render("Play again", True, (255, 255, 255))
        pygame.draw.rect(screen, (62, 161, 87), (screen.get_width() * 0.25, screen.get_height() * 0.5, 400, 100))
        screen.blit(title, (screen.get_width() * 0.37, screen.get_height() * 0.54))

        title = font_score.render("Exit", True, (255, 255, 255))
        pygame.draw.rect(screen, (62, 161, 87), (screen.get_width() * 0.76, screen.get_height() * 0.87, 190, 100))
        screen.blit(title, (screen.get_width() * 0.84, screen.get_height() * 0.92))

        pygame.display.update()

        event = pygame.event.wait()
        if event.type == QUIT:
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if screen.get_width() * 0.76 <= x <= screen.get_width() * 0.76+190 and screen.get_height() * 0.87 <= y <= screen.get_height() * 0.87+100:
                    exit(0)
                if screen.get_width() * 0.25 <= x <= screen.get_width() * 0.25+400 and screen.get_height() * 0.5 <= y <= screen.get_height() * 0.5+100:
                    first = True

                    init_decks()
                    game()
                    show_score()

                    winner = ""
