from taipy.gui import Gui

page = """
<|layout|columns = 4 5 4|

<||>

<||>

<||>

 |>

"""

gui = Gui(page = page)
gui.run(dark_mode = False)