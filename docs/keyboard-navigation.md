# ⌨️ Keyboard Navigation

The current program is driven through standard input and a numbered menu. It has no pointer-driven interface, tab order, keyboard shortcuts, or graphical focus model.

Manual review should confirm:
- The menu can be operated with a keyboard.
- Each prompt follows the selected menu action.
- The user can understand how to return to the menu.
- Non-numeric input does not trap the process in an unexplained loop.
- Screen-reader users can follow the sequential prompts.

The final item is an observed weakness: cin fail state is not explicitly cleared for non-numeric menu input.
