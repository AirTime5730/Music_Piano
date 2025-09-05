import pygame
import pygame.midi
import fluidsynth
import pyautogui

pyautogui.PAUSE = 0
# Initialize pygame and fluidsynth
pygame.init()
pygame.midi.init()

preset = int(input("Enter the preset number: "))
bank = int(input("Enter the bank number: "))
# Initialize FluidSynth with the provided sound font file
if preset <= 30 and bank == 0:
    SOUND_FONT_PATH = "Music/SF2/SGM_V2_01_part1.sf2"
elif preset > 30 and preset <= 79 and bank == 0:
    SOUND_FONT_PATH = "Music/SF2/SGM_V2_01_part2.sf2"
else:
    SOUND_FONT_PATH = "Music/SF2/SGM_V2_01_part3.sf2"
fs = fluidsynth.Synth()
fs.start(driver="coreaudio")  # Use "coreaudio" for macOS
sfid = fs.sfload(SOUND_FONT_PATH)
fs.program_select(0, sfid, bank, preset)  # Select the loaded sound font for channel 0
# Use 88 for Just died in your arms tonight

natural_key_mapping = {
    pygame.K_z: 48,  # C2
    pygame.K_x: 50,  # D2
    pygame.K_c: 52,  # E2
    pygame.K_v: 53,  # F2
    pygame.K_b: 55,  # G2
    pygame.K_n: 57,  # A2
    pygame.K_m: 59,  # B2
    pygame.K_COMMA: 60,  # C3
    pygame.K_a: 60,  # C3
    pygame.K_s: 62,  # D3
    pygame.K_d: 64,  # E3
    pygame.K_f: 65,  # F3
    pygame.K_g: 67,  # G3
    pygame.K_h: 69,  # A3
    pygame.K_j: 71,  # B3
    pygame.K_k: 72,  # C4
    pygame.K_q: 72,  # C4
    pygame.K_w: 74,  # D4
    pygame.K_e: 76,  # E4
    pygame.K_r: 77,  # F4
    pygame.K_t: 79,  # G4
    pygame.K_y: 81,  # A4
    pygame.K_u: 83,  # B4
    pygame.K_i: 84,  # C5
    pygame.K_1: 84,  # C5
    pygame.K_2: 86,  # D5
    pygame.K_3: 88,  # E5
    pygame.K_4: 89,  # F5
    pygame.K_5: 91,  # G5
    pygame.K_6: 93,  # A5
    pygame.K_7: 95,  # B5
    pygame.K_8: 96,  # C6
}
natural_key_mapping = {key: [value] if not isinstance(value, list) else value for key, value in natural_key_mapping.items()}
#VERY IMPORTANT

def change_key_binding_sharps(mapping, key_input):
    if isinstance(key_input, set):
        for key in key_input:
            if key in mapping:
                # Increment each value in the list
                mapping[key] = [note + 1 for note in mapping[key]]
    else:
        if key_input in mapping:
            # Increment each value in the list
            mapping[key_input] = [note + 1 for note in mapping[key_input]]

def change_key_binding_flats(mapping, key_input):
    if isinstance(key_input, set):
        for key in key_input:
            if key in mapping:
                # Decrement each value in the list
                mapping[key] = [note - 1 for note in mapping[key]]
    else:
        if key_input in mapping:
            # Decrement each value in the list
            mapping[key_input] = [note - 1 for note in mapping[key_input]]


# Map keys to MIDI notes for natural notes
KEY = input("Enter the key: (C for custom mapping)")
if KEY == "C":
    pass
elif KEY == "G":
    keys_to_increment = {
        pygame.K_v,
        pygame.K_f,
        pygame.K_r,
        pygame.K_4
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "D":
    keys_to_increment = {
        pygame.K_v,
        pygame.K_f,
        pygame.K_r,
        pygame.K_4,
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "A":
    keys_to_increment = {
        pygame.K_v,
        pygame.K_f,
        pygame.K_r,
        pygame.K_4,
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8,
        pygame.K_b,
        pygame.K_g,
        pygame.K_t,
        pygame.K_5
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "E":
    keys_to_increment = {
        pygame.K_v,
        pygame.K_f,
        pygame.K_r,
        pygame.K_4,
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8,
        pygame.K_b,
        pygame.K_g,
        pygame.K_t,
        pygame.K_5,
        pygame.K_x,
        pygame.K_s,
        pygame.K_w,
        pygame.K_2
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "B":
    keys_to_increment = {
        pygame.K_v,
        pygame.K_f,
        pygame.K_r,
        pygame.K_4,
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8,
        pygame.K_b,
        pygame.K_g,
        pygame.K_t,
        pygame.K_5,
        pygame.K_x,
        pygame.K_s,
        pygame.K_w,
        pygame.K_2,
        pygame.K_n,
        pygame.K_h,
        pygame.K_y,
        pygame.K_6
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "F#":
    keys_to_increment = {
        pygame.K_v,
        pygame.K_f,
        pygame.K_r,
        pygame.K_4,
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8,
        pygame.K_b,
        pygame.K_g,
        pygame.K_t,
        pygame.K_5,
        pygame.K_x,
        pygame.K_s,
        pygame.K_w,
        pygame.K_2,
        pygame.K_n,
        pygame.K_h,
        pygame.K_y,
        pygame.K_6,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_3
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "F":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)
elif KEY == "TF":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)
    keys_to_increment = {
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8
    }
    change_key_binding_sharps(natural_key_mapping, keys_to_increment)
elif KEY == "Bb":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_3
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)
elif KEY == "Eb":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_3,
        pygame.K_n,
        pygame.K_h,
        pygame.K_y,
        pygame.K_6
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)
elif KEY == "Ab":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_3,
        pygame.K_n,
        pygame.K_h,
        pygame.K_y,
        pygame.K_6,
        pygame.K_x,
        pygame.K_s,
        pygame.K_w,
        pygame.K_2
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)
elif KEY == "Db":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_3,
        pygame.K_n,
        pygame.K_h,
        pygame.K_y,
        pygame.K_6,
        pygame.K_x,
        pygame.K_s,
        pygame.K_w,
        pygame.K_2,
        pygame.K_b,
        pygame.K_g,
        pygame.K_t,
        pygame.K_5
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)
elif KEY == "Gb":
    keys_to_increment = {
        pygame.K_m,
        pygame.K_j,
        pygame.K_u,
        pygame.K_7,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_3,
        pygame.K_n,
        pygame.K_h,
        pygame.K_y,
        pygame.K_6,
        pygame.K_x,
        pygame.K_s,
        pygame.K_w,
        pygame.K_2,
        pygame.K_b,
        pygame.K_g,
        pygame.K_t,
        pygame.K_5,
        pygame.K_z,
        pygame.K_COMMA,
        pygame.K_a,
        pygame.K_k,
        pygame.K_q,
        pygame.K_i,
        pygame.K_1,
        pygame.K_8
    }
    change_key_binding_flats(natural_key_mapping, keys_to_increment)

# Offset for sharps
sharp_offsets = {note: note + 1 for note in range(24, 108)}
flat_offsets = {note: note - 1 for note in range(24, 108)}

custom_mapping = int(input("Enter the custom mapping: "))
if custom_mapping == 1:
    natural_key_mapping = {
        pygame.K_q: [71, 74, 78],
        pygame.K_w: [71, 76, 81],
        pygame.K_e: [71, 76, 79],
        pygame.K_a: [71, 76, 78],
        pygame.K_s: [69, 71, 76],
        pygame.K_z: [69, 73, 76],
        pygame.K_x: [69, 73, 78],
        pygame.K_c: [45],
        pygame.K_v: [47],
        pygame.K_b: [49],
        pygame.K_n: [50],
        pygame.K_m: [52],
        }

# Map MIDI notes to key names
midi_note_to_key = {
    24: "C1", 25: "C#1", 26: "D1", 27: "D#1", 28: "E1", 29: "F1", 30: "F#1", 31: "G1", 32: "G#1", 33: "A1", 34: "A#1", 35: "B1",
    36: "C2", 37: "C#2", 38: "D2", 39: "D#2", 40: "E2", 41: "F2", 42: "F#2", 43: "G2", 44: "G#2", 45: "A2", 46: "A#2", 47: "B2",
    48: "C3", 49: "C#3", 50: "D3", 51: "D#3", 52: "E3", 53: "F3", 54: "F#3", 55: "G3", 56: "G#3", 57: "A3", 58: "A#3", 59: "B3",
    60: "C4", 61: "C#4", 62: "D4", 63: "D#4", 64: "E4", 65: "F4", 66: "F#4", 67: "G4", 68: "G#4", 69: "A4", 70: "A#4", 71: "B4",
    72: "C5", 73: "C#5", 74: "D5", 75: "D#5", 76: "E5", 77: "F5", 78: "F#5", 79: "G5", 80: "G#5", 81: "A5", 82: "A#5", 83: "B5",
    84: "C6", 85: "C#6", 86: "D6", 87: "D#6", 88: "E6", 89: "F6", 90: "F#6", 91: "G6", 92: "G#6", 93: "A6", 94: "A#6", 95: "B6",
    96: "C7", 97: "C#7", 98: "D7", 99: "D#7", 100: "E7", 101: "F7", 102: "F#7", 103: "G7", 104: "G#7", 105: "A7", 106: "A#7", 107: "B7",
    108: "C8"
}

# Piano Key Class for Visuals
class PianoKey:
    def __init__(self, x, y, width, height, color, note, is_black=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.default_color = color
        self.note = note
        self.is_black = is_black

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

    def light_up(self, color=(101, 110, 230)):  # #656ee6 in RGB
        self.color = color

    def reset_color(self):
        self.color = self.default_color

# Set the screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 200
WHITE_KEY_WIDTH = SCREEN_WIDTH // 52
WHITE_KEY_HEIGHT = 200
BLACK_KEY_WIDTH = WHITE_KEY_WIDTH // 2
BLACK_KEY_HEIGHT = 120

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Electric Piano Player")

# Create piano keys
white_keys = []
black_keys = []
keys_by_note = {}
white_notes = ["C", "D", "E", "F", "G", "A", "B"] * 7 + ["C"]
black_notes = {1: "C#", 2: "D#", 4: "F#", 5: "G#", 6: "A#"}

# Create white keys
for i, note in enumerate(white_notes):
    x = i * WHITE_KEY_WIDTH
    note_name = note + str(i // 7 + 1)
    key = PianoKey(x, SCREEN_HEIGHT - WHITE_KEY_HEIGHT, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT, (255, 255, 255), note_name)
    white_keys.append(key)
    keys_by_note[note_name] = key

# Create black keys
for i in range(52):
    if i % 7 in black_notes:
        x = i * WHITE_KEY_WIDTH + WHITE_KEY_WIDTH // 2 - WHITE_KEY_WIDTH // 2
        note_name = black_notes[i % 7] + str(i // 7 + 1)
        key = PianoKey(x - BLACK_KEY_WIDTH // 2, SCREEN_HEIGHT - WHITE_KEY_HEIGHT, BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT, (0, 0, 0), note_name, is_black=True)
        black_keys.append(key)
        keys_by_note[note_name] = key

# Play and stop notes
def play_note(note):
    fs.noteon(0, note, 127)
    if note in midi_note_to_key:
        key_name = midi_note_to_key[note]
        if key_name in keys_by_note:
            keys_by_note[key_name].light_up()

def stop_note(note):
    fs.noteoff(0, note)
    if note in midi_note_to_key:
        key_name = midi_note_to_key[note]
        if key_name in keys_by_note:
            keys_by_note[key_name].reset_color()

# Main loop
running = True
def piano_loop():
    pressed_keys = set()
    use_sharp = False  # Track whether the next note should be sharp
    use_flat = False  # Track whether the next note should be flat
    sharps_playing = set()  # Track sharp notes currently playing
    flats_playing = set()  # Track flat notes currently playing
    natural_playing = set()  # Track natural notes currently playing
    octave_shift = 0  # Initial octave shift
    global running
    while running:
        screen.fill((200, 200, 200))

        # Draw the keys
        for key in white_keys + black_keys:
            key.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    octave_shift = 12
                elif event.key in [pygame.K_RSHIFT]:
                    octave_shift = -12
                elif event.key in natural_key_mapping and event.key not in pressed_keys:
                    pressed_keys.add(event.key)
                    notes = natural_key_mapping[event.key]
                    for note in notes:
                        note += octave_shift  # Apply the octave shift if necessary
                        if use_sharp and note in sharp_offsets:
                            note = sharp_offsets[note]
                            sharps_playing.add(note)
                        elif use_flat and note in flat_offsets:
                            note = flat_offsets[note]
                            flats_playing.add(note)
                        else:
                            natural_playing.add(note)
                        play_note(note)
                elif event.key == pygame.K_LSHIFT:
                    use_sharp = True
                    # Stop all natural notes
                    for natural_note in list(natural_playing):
                        stop_note(natural_note)
                    natural_playing.clear()
                elif event.key == pygame.K_SPACE:
                    use_flat = True
                    # Stop all natural notes
                    for natural_note in list(natural_playing):
                        stop_note(natural_note)
                    natural_playing.clear()
                elif event.key in [pygame.K_LCTRL, pygame.K_RCTRL]:
                    octave_shift = -24

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_RETURN, pygame.K_RSHIFT, pygame.K_LCTRL, pygame.K_RCTRL]:
                    octave_shift = 0
                elif event.key == pygame.K_LSHIFT:
                    use_sharp = False
                    # Stop all sharp notes
                    for sharp_note in list(sharps_playing):
                        stop_note(sharp_note)
                    sharps_playing.clear()
                elif event.key == pygame.K_SPACE:
                    use_flat = False
                    # Stop all flat notes
                    for flat_note in list(flats_playing):
                        stop_note(flat_note)
                    flats_playing.clear()
                elif event.key in natural_key_mapping and event.key in pressed_keys:
                    pressed_keys.remove(event.key)
                    notes = natural_key_mapping[event.key]
                    for note in notes:
                        note += octave_shift  # Apply the octave shift if necessary
                        if use_sharp and note in sharp_offsets:
                            modified_note = sharp_offsets[note]
                            if modified_note in sharps_playing:
                                sharps_playing.remove(modified_note)
                                stop_note(modified_note)
                        elif use_flat and note in flat_offsets:
                            modified_note = flat_offsets[note]
                            if modified_note in flats_playing:
                                flats_playing.remove(modified_note)
                                stop_note(modified_note)
                        else:
                            if note in natural_playing:
                                natural_playing.remove(note)
                                stop_note(note)

# Start threads
if __name__ == "__main__":
    running = True

    piano_loop()

    # Clean up
    fs.delete()
    pygame.quit()
