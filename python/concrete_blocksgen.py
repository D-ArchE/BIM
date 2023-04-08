# Import necessary libraries
import math
import os

# Define a function to calculate the amount of materials needed for a given number of concrete blocks
def calculate_materials(num_blocks, cement_ratio, sand_ratio, gravel_ratio, water_ratio):
    os.system("clear")
    # Calculate the total volume of materials needed in cubic feet
    total_volume = num_blocks * 0.0283168 * 8
    
    # Calculate the volume of cement needed in cubic feet
    cement_volume = total_volume * cement_ratio
    
    # Calculate the weight of cement needed in pounds
    cement_weight = cement_volume * 94
    
    # Calculate the volume of sand needed in cubic feet
    sand_volume = total_volume * sand_ratio
    
    # Calculate the weight of sand needed in pounds
    sand_weight = sand_volume * 100
    
    # Calculate the volume of gravel needed in cubic feet
    gravel_volume = total_volume * gravel_ratio
    
    # Calculate the weight of gravel needed in pounds
    gravel_weight = gravel_volume * 100
    
    # Calculate the volume of water needed in liters
    water_volume = total_volume * water_ratio * 1000
    
    # Return the calculated amounts of materials
    return {
        'cement': cement_weight,
        'sand': sand_weight,
        'gravel': gravel_weight,
        'water': water_volume
    }

# Define pre-defined ratios for making concrete blocks with 1-4 Lego pieces
ratios = {
    1: {'cement': 0.0625, 'sand': 0.125, 'gravel': 0.1875, 'water': 0.03125},
    2: {'cement': 0.125, 'sand': 0.125, 'gravel': 0.1875, 'water': 0.0625},
    3: {'cement': 0.1875, 'sand': 0.125, 'gravel': 0.1875, 'water': 0.09375},
    4: {'cement': 0.25, 'sand': 0.125, 'gravel': 0.1875, 'water': 0.125}
}

# Ask the user for input on the number of concrete blocks to make and the number of Lego pieces in each block
num_blocks = int(input("How many concrete blocks do you want to make? "))
lego_pieces = int(input("How many Lego pieces are in each block (1-4)? "))

# Use the pre-defined ratios to calculate the amount of materials needed
materials = calculate_materials(num_blocks, ratios[lego_pieces]['cement'], ratios[lego_pieces]['sand'], ratios[lego_pieces]['gravel'], ratios[lego_pieces]['water'])

# Print the results
print(f"To make {num_blocks} concrete blocks with {lego_pieces} Lego pieces each, you will need:")
print(f"{materials['cement']} pounds of cement")
print(f"{materials['sand']} pounds of sand")
print(f"{materials['gravel']} pounds of gravel")
print(f"{materials['water']} liters of water")
