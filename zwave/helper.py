import math

import pygame


def velocity_by_keys(speed, keys):

    ## speed to axes in diagonal movement ##
    if (keys[pygame.K_a] or keys[pygame.K_d]) and (keys[pygame.K_w] or keys[pygame.K_s]):
        return (speed * 0.7)

    ## speed to axes in horizontal and vertical movements ##
    else:
        return speed

def velocity_by_angle(speed, angle):

    ## algorithm to set velocity for 'x' and 'y' based on the angle of sprite ##
    velocity = {}
    velocity["x"] = math.cos(math.radians(angle)) * speed
    velocity["y"] = (math.sin(math.radians(angle)) * -1) * speed

    return velocity

def angle_by_two_points(point1, point2):

    rads = math.atan2((point2["y"] - point1["y"]) * -1, point2["x"] - point1["x"])
    rads %= 2 * math.pi
    return math.degrees(rads)

def pygame_image(image, width, height = False, alpha = True):

    ## if the height was not informed, it will be equal to the width ##
    if not height:
        height = width

    ## load image ##
    image = pygame.image.load(image)

    ## convet with alpha or not ##
    image = image.convert_alpha() if alpha else image.convert()

    ## scale image ##
    image = pygame.transform.scale(image, (width, height))

    return image

def pygame_sprite_by_image(image):

    ## make a generic sprite and set image  ##
    sprite = pygame.sprite.Sprite()
    sprite.image = image

    ## make sprite rect ##
    sprite.rect = sprite.image.get_rect()

    return sprite

def pygame_rotate(image, angle):

    ## new rect from original image rect ##
    area = image.get_rect()

    ## make new image already rotated ##
    new = pygame.transform.rotozoom(image, angle, 1)

    ## center new rect with new rotated image ##
    area.center = new.get_rect().center

    ## return a copy of the new rotated image, centralized in the correct position ##
    return new.subsurface(area).copy()

def pygame_button(text, font, x, y, color = (0, 0, 0), alignment = None):

    ## text button ##
    text = font.render(text, 1, (255,255,255))

    ## surface that contain text ##
    surface = pygame.Surface((text.get_rect().width + 50, text.get_rect().height + 20))

    ## background color #
    surface.fill(color)

    ## insert text inside surface ##
    x1, y1 = ((text.get_rect().width + 50) / 2) - (text.get_rect().width / 2), 15
    surface.blit(text, pygame.Rect(x1, y1, text.get_rect().width, text.get_rect().height))

    ## set button transparency ##
    surface.set_alpha(200)

    ## transform burron surface in a sprite ##
    button = pygame_sprite_by_image(surface)

    ## set sprite position ##
    x2, y2 = x, y
    if alignment == "center":
        x2 = x - (surface.get_rect().width / 2)
    elif alignment == "left":
        x2 = x - surface.get_rect().width

    button.rect.x, button.rect.y = x2, y2

    ## return new button already in a sprite group ##
    return pygame.sprite.GroupSingle(button)
