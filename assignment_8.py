import sys
import os
import pygame
import tkinter as tk
from tkinter import filedialog

SPRITESHEET_FILE = "spritesheet.png"
FRAME_WIDTH = 64
FRAME_HEIGHT = 64
ANIM_FPS = 12
SCALE = 2 

def load_frames(sheet, frame_w, frame_h):
    frames = []
    sheet_w, sheet_h = sheet.get_size()
    for y in range(0, sheet_h, frame_h):
        for x in range(0, sheet_w, frame_w):
            rect = pygame.Rect(x, y, frame_w, frame_h)
            frame = sheet.subsurface(rect).copy()
            frames.append(frame)
    return frames

def ask_for_file(initial_dir):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        initialdir=initial_dir,
        title="Select spritesheet image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All files", "*.*")]
    )
    root.destroy()
    return path or None

def find_spritesheet(base_dir, filename):
    candidate = os.path.join(base_dir, filename)
    if os.path.exists(candidate):
        return candidate
    cwd_candidate = os.path.join(os.getcwd(), filename)
    if os.path.exists(cwd_candidate):
        return cwd_candidate
    exts = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    for f in os.listdir(base_dir):
        if f.lower().endswith(exts):
            return os.path.join(base_dir, f)
    return ask_for_file(base_dir)

def main():
    base_dir = os.path.dirname(__file__)
    sheet_path = find_spritesheet(base_dir, SPRITESHEET_FILE)
    if not sheet_path or not os.path.exists(sheet_path):
        print(f"Spritesheet not found. Looked in: {base_dir} and current working directory.")
        sys.exit(1)

    print(f"Using spritesheet: {sheet_path}")

    pygame.init()

    pygame.display.init()
    pygame.display.set_mode((1, 1))

    sheet = pygame.image.load(sheet_path).convert_alpha()
    original_frames = load_frames(sheet, FRAME_WIDTH, FRAME_HEIGHT)
    if not original_frames:
        print("No frames extracted. Check FRAME_WIDTH/FRAME_HEIGHT.")
        pygame.quit()
        sys.exit(1)

    print(f"Extracted {len(original_frames)} frames (each {FRAME_WIDTH}x{FRAME_HEIGHT})")

    current_scale = max(1, int(SCALE))
    def rescale_frames(scale):
        w = FRAME_WIDTH * scale
        h = FRAME_HEIGHT * scale
        return [pygame.transform.scale(f, (w, h)) for f in original_frames]

    frames = rescale_frames(current_scale)
    disp_w = FRAME_WIDTH * current_scale
    disp_h = FRAME_HEIGHT * current_scale

    screen = pygame.display.set_mode((disp_w, disp_h), pygame.RESIZABLE)
    pygame.display.set_caption(f"Spritesheet Animation — {os.path.basename(sheet_path)}")

    clock = pygame.time.Clock()
    running = True

    print("Press + to increase size, - to decrease size, ESC to quit.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS):
                    if current_scale < 12:
                        current_scale += 1
                        frames = rescale_frames(current_scale)
                        disp_w = FRAME_WIDTH * current_scale
                        disp_h = FRAME_HEIGHT * current_scale
                        screen = pygame.display.set_mode((disp_w, disp_h), pygame.RESIZABLE)
                elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                    if current_scale > 1:
                        current_scale -= 1
                        frames = rescale_frames(current_scale)
                        disp_w = FRAME_WIDTH * current_scale
                        disp_h = FRAME_HEIGHT * current_scale
                        screen = pygame.display.set_mode((disp_w, disp_h), pygame.RESIZABLE)
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        ms = pygame.time.get_ticks()
        frame_index = int((ms / 1000.0) * ANIM_FPS) % len(frames)

        screen.fill((30, 30, 30))
        sw, sh = screen.get_size()
        fw, fh = frames[frame_index].get_size()
        x = max(0, (sw - fw) // 2)
        y = max(0, (sh - fh) // 2)
        screen.blit(frames[frame_index], (x, y))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()