from chessboard import calibrate_chessboard
from utils import load_coefficients, save_coefficients

# Parameters
IMAGES_DIR = 'chess'
IMAGES_FORMAT = '.JPG'
SQUARE_SIZE = 2.0
WIDTH = 8
HEIGHT = 6

# Calibrate
ret, mtx, dist, rvecs, tvecs = calibrate_chessboard(
    IMAGES_DIR,
    IMAGES_FORMAT,
    SQUARE_SIZE,
    WIDTH,
    HEIGHT
)
# Save coefficients into a file
save_coefficients(mtx, dist, "calibration_chessboard.yml")