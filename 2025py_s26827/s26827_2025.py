# ----------------------------------------
# Program: DNA FASTA Sequence Generator
# Student ID: s26827
# Purpose: This program generates a random DNA sequence of specified length,
# inserts user's name into it (not counted in stats), saves the sequence in FASTA format,
# and prints detailed nucleotide statistics.
# This project is part of the coursework to demonstrate basic bioinformatics file handling.
# ----------------------------------------

import random  # Import the random module to generate random choices

# Get and validate sequence length input from user
# ORIGINAL:
# length = int(input("Enter the sequence length: "))
# MODIFIED (added validation to prevent crash on invalid input):
while True:
    try:
        length = int(input("Enter the sequence length: "))  # Prompt user to input length
        if length <= 0:
            print("Length must be a positive integer.")  # Prevent zero or negative numbers
            continue
        break
    except ValueError:
        print("Please enter a valid number.")  # Catch non-integer inputs

# Ask the user for sequence metadata
seq_id = input("Enter the sequence ID: ")  # User provides ID of the sequence
description = input("Provide a description of the sequence: ")  # Short description

# Ask for user's name and sanitize it
# ORIGINAL:
# name = input("Enter your name: ")
# MODIFIED (replaces characters not in ACGT with 'A' to preserve DNA style):
name = input("Enter your name: ")  # Name to be inserted in sequence
name = ''.join([ch if ch in "ACGT" else 'A' for ch in name.upper()])  # Clean name to only use A, C, G, T

# Generate a random DNA sequence using nucleotides
nucleotides = ['A', 'C', 'G', 'T']  # DNA bases
sequence = ''.join(random.choices(nucleotides, k=length))  # Generate random DNA string of given length

# Insert name at a random position in the sequence (does not count toward length)
insert_pos = random.randint(0, len(sequence))  # Choose random position in sequence
sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]  # Insert name into sequence

# Prepare the filename using the ID and save the FASTA file
filename = f"{seq_id}.fasta"  # File name based on sequence ID
with open(filename, 'w') as f:
    f.write(f">{seq_id} {description}\n")  # Write FASTA header with ID and description

    # ORIGINAL:
    # f.write(sequence_with_name + "\n")
    # MODIFIED (adds line breaks every 60 chars for FASTA readability):
    for i in range(0, len(sequence_with_name), 60):
        f.write(sequence_with_name[i:i+60] + "\n")  # Write sequence in lines of 60 characters

# Confirm save
print(f"The sequence was saved to the file {filename}")

# Calculate nucleotide statistics (excluding the inserted name)
a_count = sequence.count('A')  # Count A's in original sequence
c_count = sequence.count('C')  # Count C's
g_count = sequence.count('G')  # Count G's
t_count = sequence.count('T')  # Count T's

total = len(sequence)  # Total length without name

# Calculate percentages
a_percent = (a_count / total) * 100
c_percent = (c_count / total) * 100
g_percent = (g_count / total) * 100
t_percent = (t_count / total) * 100

# CG to AT ratio
cg_ratio = ((c_count + g_count) / total) * 100

# Display results to the user
print("Sequence statistics:")
print(f"A: {a_percent:.1f}%")
print(f"C: {c_percent:.1f}%")
print(f"G: {g_percent:.1f}%")
print(f"T: {t_percent:.1f}%")
print(f"%CG: {cg_ratio:.1f}")
