# open an url in browser 

import webbrowser as wb 

url = str(input("Enter the url: ") or "https://www.google.com/")
wb.open_new_tab(url)
