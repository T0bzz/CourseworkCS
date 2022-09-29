import pygame
from math import sin, tan, cos

def move(pos, eq, width, height):
    """Eval() the equation to return a new position"""
    x = pos[0] + 1
    if x >= width:
        x = 0  # reset X position
    try:
        y = eval(eq[3:])  # skip "y ="
        if type(y) not in (int, float):
            raise Exception("Unexpected eval() return")
    except:
        x, y = pos  # don't move if equation is invalid
    if abs(y) > (height // 2):  # reset position when off the screen
        return 0, 0
    return x, y


pygame.init()
# grab the first installed font
sys_font = pygame.font.SysFont(None, 37)
clock = pygame.time.Clock()
width, height = 320, 240
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movement Equation")
x, y = 0, 0
eq = "y = x"  # initial equation
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.TEXTINPUT:
            # very limited input filtering
            if event.text in "0123456789 +-/*x().sintaco":
                eq += event.text
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                eq = eq[:-1]
            elif event.key == pygame.K_ESCAPE:
                x, y = 0, 0  # reset position
    # move the ball position
    x, y = move((x, y), eq, width, height)
    # Update text
    text = sys_font.render(eq, True, pygame.Color("turquoise"))
    # Graphics
    screen.fill(pygame.Color("black"))
    # Draw Text in the center
    screen.blit(text, text.get_rect(center=screen.get_rect().center))
    # Draw the ball (shift y axis so zero is in the center)
    pygame.draw.circle(screen, "red", (x, height // 2 - y), 10)
    # Update Screen
    pygame.display.update()
    clock.tick(30)
pygame.quit()