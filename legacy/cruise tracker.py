#Lib import
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geopandas as gpd
import matplotlib
import json
from shapely.geometry import Polygon, Point
import numpy as np
from update_annot import hover
import os
import matplotlib.font_manager as font_manager
from cycler import cycler

class cruise_ship:

	def __init__(self):
		self.data = sum([[j for j in json.loads(open('data/'+i, 'r').read()).items()] for i in os.listdir(os.getcwd()+r'\data')], [])
		self.name = [[i[0], i[1]['company']] for i in self.data if i[1]['longlat']]
		self.data = [i[1] for i in self.data if i[1]['longlat']]
		self.color = [(i, '#%02x%02x%02x'%j[:-1]) for i, j in eval(open('color.dat').read().strip())]
		self.color_name_index = [i[0] for i in self.color]
		self.color_index = [i[0][1] if i else self.color[28][1] for i in [[self.color[i] for i in range(len(self.color_name_index)) if self.color_name_index[i] in j[1]] for j in self.name]]
		self.color = dict(self.color)
		self.lat, self.longi = [i['longlat'][0] for i in self.data], [i['longlat'][1] for i in self.data]
		self.fig, self.ax = plt.subplots(figsize=(20, 20))
		self.annot = self.ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points", bbox=dict(boxstyle="round", fc="#EBEB00", alpha=0.5))
		self.ncols = int(np.ceil(len(self.color) / 9.0))
		self.sc = self.ax.scatter(self.longi, self.lat, c=self.color_index, zorder=2)
		self.patchList = [self.ax.plot([],[], marker="o", ms=10, ls="", color=self.color[key], label=key)[0] for key in self.color]
		self.l_font = font_manager.FontProperties(family='Tahoma')
		self.l = plt.legend(handles=self.patchList, ncol=self.ncols, bbox_to_anchor=(0.5, -0.065), loc='upper center', prop=self.l_font)

	def plot_map(self):
		gpd.read_file('map resources/ne_10m_admin_0_countries.shp').plot(ax=self.ax, color='black')
		gpd.read_file('map resources/ne_10m_admin_1_states_provinces.shp').plot(ax=self.ax, color='white')
		gpd.read_file('map resources/ne_10m_rivers_lake_centerlines.shp').plot(ax=self.ax, color='#87CEEB', linewidth=0.5)

	def setup_and_plot(self):
		self.l.get_frame().set_linewidth(0)
		self.ax.set_facecolor("#87CEEB")
		self.annot.set_visible(False)
		self.fig.canvas.mpl_connect("motion_notify_event", lambda event: hover(event, self.sc, self.name, self.annot, self.fig, self.ax, self.color_index))
		plt.get_current_fig_manager().full_screen_toggle()
		plt.gcf().canvas.set_window_title('Cruise Ship Tracker')
		plt.title('Cruise Ship Tracker', fontsize=20, family='Gotham Light', pad=10)
		plt.subplots_adjust(bottom=0.25)
		plt.xlabel('Longitude')
		plt.ylabel('Latitude')
		plt.show()

if __name__ == "__main__":
	CruiseShipTracker = cruise_ship()
	CruiseShipTracker.plot_map()
	CruiseShipTracker.setup_and_plot()