
import random
from PIL import Image
from snake import Snake
import pygame
from app_obj import Apple, PowUp
import constants
pygame.init()


def create_window():
    height=720
    width = 720
    size = (width, height)
    green = (0, 255, 0)
    window = pygame.display.set_mode(size)
    window.fill(green)
    return window


def music():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)


def check_collision(rect1_x, rect1_y, rect1_w, rect1_h, rect2_x, rect2_y, rect2_w, rect2_h):
    return (rect1_x < rect2_x + rect2_w and
            rect1_x + rect1_w > rect2_x and
            rect1_y < rect2_y + rect2_h and
            rect1_y + rect1_h > rect2_y)


def main():
    gif = Image.open("Sad Spider Man GIF.gif")
    frames = []
    try:
        while True:
            frame = gif.copy().convert("RGBA")
            py_frame = pygame.image.fromstring(frame.tobytes(), frame.size,"RGBA" )
            frames.append(py_frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass

    show_gif = False
    frame_index = 0

    a1 = Apple()
    p = PowUp()
    win = create_window()
    s = Snake()

    points = 0
    font = pygame.font.SysFont("Arial", 36)
    text_pos = (0, 0)
    green = (0, 200, 0)
    finish = False

    snake_segments = [[s.get_x_s(), s.get_y_s()]]
    SEGMENT_SIZE = 15

    is_play = True
    direction = "UP"
    is_double = False
    lose = False
    power = "-"

    music()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    tup = ['double', 'speed']

    body_vertical_img = pygame.image.load('body_vertical.png')
    body_horizontal_img = pygame.image.load('body_horizontal.png')

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif pygame.KEYDOWN == event.type:
                if event.key == pygame.K_p:
                    if is_play:
                        is_play = False
                        pygame.mixer.music.pause()
                    else:
                        is_play = True
                        pygame.mixer.music.unpause()

                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        if not lose:
            head_x, head_y = snake_segments [0]

            if direction == "UP":
                s.set_image(pygame.image.load('head_up.png'))
            elif direction == "DOWN":
                s.set_image(pygame.image.load('head_down.png'))
            elif direction == "LEFT":
                s.set_image(pygame.image.load('head_left.png'))
            elif direction == "RIGHT":
                s.set_image(pygame.image.load('head_right.png'))

            new_head_x, new_head_y = head_x, head_y
            if direction == "UP":
                new_head_y -= SEGMENT_SIZE
            elif direction == "DOWN":
                new_head_y += SEGMENT_SIZE
            elif direction == "LEFT":
                new_head_x -= SEGMENT_SIZE
            elif direction == "RIGHT":
                new_head_x += SEGMENT_SIZE

            new_head = [new_head_x, new_head_y]
            snake_segments.insert(0, new_head)

            if (new_head[0] < 0 or new_head[0] >= 720 or
                    new_head[1] < 0 or new_head[1] >= 720):
                lose = True

            if new_head in snake_segments[1:]:
                lose = True

            apple_eaten = False
            if check_collision(new_head[0], new_head[1], SEGMENT_SIZE, SEGMENT_SIZE,
                               a1.get_x(), a1.get_y(), a1.get_img_width(), a1.get_img_height()):
                points += a1.get_score()
                apple_eaten = True
                a1.change_coo()

            if not apple_eaten:
                snake_segments.pop()

            if not p.get_is_on():
                if check_collision(new_head[0], new_head[1], SEGMENT_SIZE, SEGMENT_SIZE,
                                   p.get_x(), p.get_y(), p.get_img_width(), p.get_img_height()):
                    p.timer()
                    power_type = tup[random.randint(0, len(tup) -1)]

                    if power_type == 'speed':
                        power = 'speed'
                    else:
                        power = 'double'
                        is_double = True
                        a1.set_score(2)
                    p.disappear()
            else:
                p.time_over()
                if not p.get_is_on():
                    power = '-'
                    if is_double:
                        is_double = False
                        a1.set_score(1)
                    p.change_coo()

        win.fill(green)

        apple_x = max(0, min(a1.get_x(), 720 - a1.get_img_width()))
        apple_y = max(0, min(a1.get_y(), 720 - a1.get_img_height()))
        win.blit(a1.get_img(), (apple_x, apple_y))

        if not p.get_is_on():
            pow_x = max(0, min(p.get_x(), 720 - p.get_img_width()))
            pow_y = max(0, min(p.get_y(), 720 - p.get_img_height()))
            win.blit(p.get_img(), (pow_x, pow_y))

        for i in range(len(snake_segments) - 1, 0, -1):
            segment = snake_segments[i]
            prev_segment = snake_segments[i - 1]

            if segment[0] == prev_segment[0]:
                win.blit(body_vertical_img, (segment[0], segment[1]))
            elif segment[1] == prev_segment[1]:
                win.blit(body_horizontal_img, (segment[0], segment[1]))


        if snake_segments:
            head_segment = snake_segments[0]
            win.blit(s.get_image(), (head_segment[0], head_segment[1]))



        text = font.render(f"Score: {points} | Length: {len(snake_segments)}", True, (0, 0, 0))
        win.blit(text, text_pos)

        show_pow = font.render(f"Power: {power}", True, (0, 0, 0))
        win.blit(show_pow, (400, 0))

        if lose:
            show_gif = True

        if show_gif and frames:
            clock.tick(10)
            lost = font.render("you lost :(", True, (0, 0, 0))
            win.blit(lost, (300, 400))
            win.blit(frames[frame_index], (100, 100))
            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0

        pygame.display.flip()

        current_fps = 18
        if power == 'speed':
            current_fps = 30
        clock.tick(current_fps)

    pygame.quit()


if __name__ == '__main__':
    main()