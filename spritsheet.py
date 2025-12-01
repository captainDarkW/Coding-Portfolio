import os
import pygame

FRAME_W = 64
FRAME_H = 64
FRAMES = 8
OUT_NAME = "spritesheet.png"

def make_frame(i):
    surf = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
    surf.fill((30, 30, 30, 255))
    cx = int(8 + (FRAME_W - 16) * (i / (FRAMES - 1)))
    cy = FRAME_H // 2
    r = 14
    color = (255, max(0, 200 - i*20), min(255, 80 + i*20), 255)
    pygame.draw.ellipse(surf, color, (cx - r, cy - r, r*2, r*2))
    accent = (min(255, 20 * (i+1)), 50, max(0, 255 - 20*i))
    pygame.draw.rect(surf, accent, (4, 4, 8, 8))
    return surf

def generate():
    pygame.init()
    sheet_w = FRAME_W * FRAMES
    sheet_h = FRAME_H
    sheet = pygame.Surface((sheet_w, sheet_h), pygame.SRCALPHA)
    for i in range(FRAMES):
        frame = make_frame(i)
        sheet.blit(frame, (i * FRAME_W, 0))
    out_path = os.path.join(os.path.dirname(__file__), OUT_NAME)
    pygame.image.save(sheet, out_path)
    print(f"Saved spritesheet: {out_path}")

if __name__ == "__main__":
    generate()