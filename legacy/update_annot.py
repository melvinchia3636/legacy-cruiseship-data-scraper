import matplotlib.pyplot as plt

def update_annot(ind, sc, data, annot, fig, ax, color):
    try:
        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "{}\n{}".format(*data[int(" ".join(list(map(str,ind["ind"]))))])
        annot.set_text(text)
        annot.set_backgroundcolor(color[int(" ".join(list(map(str,ind["ind"]))))])
        return True
    except:
        return False

def hover(event, plotline, data, annot, fig, ax, color):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = plotline.contains(event)
        if cont:
            if update_annot(ind, plotline, data, annot, fig, ax, color):
                annot.set_visible(True)
                fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()