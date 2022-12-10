#!/usr/bin/python3

import sys


def read_coordinates(filename):
    coords = []
    with open(filename, "r") as file:
        raw = file.read().split("\n")
        
    coord_idx = 0
    for line in raw:
        (x, y) = line.strip().split(",")
        coords.append( ("idx_" + str(coord_idx), int(a.strip()), int(b.strip())))
    return coords


def width(coords):
    # row, col
    widest = 0
    for (idx, r, c) in coords:
        if c > widest:
            widest = c
    return widest


def height(coords):
    # row, col
    highest = 0
    for (idx, r, c) in coords:
        if r > highest:
            highest = r
    return highest


def grid(w, h):
    rows = []
    for r_idx in range(h):
        rows.append([{"home": False, "home_idx": None, "nearest": w * h, "nearest_idx": []} for c_idx in range(w)])
    return rows


def fill_grid(grid, coords, grid_width, grid_height):
    """
    We're doing a simple grid walk with each coordinate, making this roughly O(coords * w * h)
    """
    for (coord_idx, coord_row_idx, coord_col_idx) in coords:
        
        # place it
        grid[coord_row_idx][coord_col_idx]["home"] = True
        grid[coord_row_idx][coord_col_idx]["home_idx"] = coord_idx
        
        # walk the rest of the grid
        for grid_row_idx in range(grid_height):
            for grid_col_idx in range(grid_width):
        
