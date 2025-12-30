"""
GUI String Manipulator
----------------------
A graphical user interface application for string manipulation and analysis.
Features: Title-case conversion, character counting, word counting.

Author: Lakulish Saini

Requirements: graphics.py and button.py must be in the same directory.
"""

from graphics import *
from button import *


def main():
    # Create the main window
    window = GraphWin("String Manipulator", 500, 350)
    window.setBackground("white")
    
    # Title
    title = Text(Point(250, 25), "String Manipulator")
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor("purple")
    title.draw(window)
    
    # Input label
    label = Text(Point(100, 60), "Enter a string:")
    label.setSize(15)
    label.setStyle("bold")
    label.draw(window)
    
    # Input box
    input_box = Entry(Point(290, 60), 20)
    input_box.setSize(15)
    input_box.setFill("white")
    input_box.draw(window)
    
    # Display area
    display = Rectangle(Point(30, 90), Point(400, 315))
    display.setOutline("gray")
    display.draw(window)
    
    # Buttons
    analyze_btn = Button(window, Point(450, 60), 60, 30, "Analyze")
    analyze_btn.activate()
    
    quit_btn = Button(window, Point(450, 300), 60, 30, "Exit")
    quit_btn.activate()
    
    # Result text objects
    result1 = Text(Point(200, 130), "")
    result1.setSize(15)
    result1.draw(window)
    
    result2 = Text(Point(200, 160), "")
    result2.setSize(15)
    result2.draw(window)
    
    result3 = Text(Point(200, 190), "")
    result3.setSize(15)
    result3.draw(window)
    
    result4 = Text(Point(200, 220), "")
    result4.setSize(15)
    result4.draw(window)
    
    # Main event loop
    while True:
        click_point = window.getMouse()
        
        if analyze_btn.clicked(click_point):
            # Get and analyze the string
            text = input_box.getText()
            
            if text:  # Only process if there's input
                # Title-case version
                title_case = text.title()
                
                # Count specific characters
                count_r = text.lower().count("r")
                
                # Word count
                word_count = len(text.split())
                
                # Character count (excluding spaces)
                char_count = len(text.replace(" ", ""))
                
                # Display results
                result1.setText(f"Title Case: {title_case}")
                result2.setText(f"Number of 'r's: {count_r}")
                result3.setText(f"Number of words: {word_count}")
                result4.setText(f"Characters (no spaces): {char_count}")
                
                # Clear input for next entry
                input_box.setText("")
        
        elif quit_btn.clicked(click_point):
            window.close()
            return


if __name__ == "__main__":
    main()

