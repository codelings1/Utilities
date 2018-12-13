import pyautogui

# Open Chromium Browser
pyautogui.click(x=22, y=177, clicks=1, button='left')
pyautogui.hotkey('ctrl','t')

# Open internet page
pyautogui.typewrite('10')
pyautogui.press('right')
pyautogui.hotkey('enter')

pyautogui.typewrite("H", interval=2)

pyautogui.click(x=454, y=502, clicks=1, button='left')
pyautogui.click(x=473, y=657, clicks=1, button='left')

# Fill ESS form
pyautogui.click(x=777, y=363, clicks=1, button='left')
pyautogui.typewrite('')
pyautogui.hotkey('enter')

pyautogui.click(x=1119, y=482, clicks=1, button='left')
