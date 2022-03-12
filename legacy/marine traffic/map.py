#Lib import
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib
import json
from shapely.geometry import Polygon, Point

ship_type = {
	'cargo':['Cement Carrier', 'Livestock Carrier', 'Reefer', 'Heavy Load Carrier', 'Timber Carrier', 'Cargo/Containership', 'Self Discharging Bulk Carrier', 'Vehicles Carrier', 'Ro-Ro Cargo', 'Bulk Carrier', 'General Cargo', 'Container Ship'],
	'tankers':['Oil/Chemical Tanker', 'Chemical Tanker', 'Crude Oil Tanker', 'Shuttle Tanker', 'LNG Tanker', 'Oil Products Tanker', ],
	'passenger':['Ro-Ro/Passenger Ship', 'Accommodation Vessel', 'Passenger Ship', ],
	'high speed':['High Speed Craft', ],
	'tug and special':['Drilling Rig', 'Buoy-Laying Vessel', 'Pipe Layer Platform', 'Platform', 'Suction Dredger', 'Crane Ship', 'Pipe Burying Vessel', 'Multi Purpose Offshore Vessel', 'Research/Survey Vessel', 'Construction Support Vessel', 'Offshore Supply Ship', 'Tug', 'Floating Storage/Production', 'Drill Ship', 'Well Stimulation Vessel', 'Pipe Layer', 'Supply Vessel', 'Pipelay Crane Vessel', ],
	'fishing':[],
	'pleasure':['Yacht'],
	'other':[]
}


data=json.loads(open('data.json', 'r').read())
data = [i for i in data if 'OF THE SEAS' in i['name']]
color = []

longi = [float(i['longitude']) for i in data]
lat = [float(i['latitude']) for i in data]
description = [i['description'] for i in data]

for i in description:
	if i in ship_type['cargo']:
		color.append('#00FF7F')
	elif i in ship_type['tankers']:
		color.append('#FF0000')
	elif i in ship_type['passenger']:
		color.append('#0000FF')
	elif i in ship_type['high speed']:
		color.append('#FFFF00')
	elif i in ship_type['tug and special']:
		color.append('#00FFFF')
	elif i in ship_type['fishing']:
		color.append('#FFB6C1')
	elif i in ship_type['pleasure']:
		color.append('#FFC0CB')
	else:
		color.append('#DDDDDD')

world_map = gpd.read_file('ne_10m_admin_0_countries.shp')

fig, ax = plt.subplots(figsize=(20, 20))
ax.set_facecolor("#87CEEB")
world_map.plot(ax=ax, color='black')
gpd.read_file('ne_10m_admin_1_states_provinces.shp').plot(ax=ax, color='white')
sc = ax.scatter(longi, lat, c=color)

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
	try:
	    pos = sc.get_offsets()[ind["ind"][0]]
	    annot.xy = pos
	    text = "{}\n{}".format(data[int(" ".join(list(map(str,ind["ind"]))))]['name'], data[int(" ".join(list(map(str,ind["ind"]))))]['description'])
	    annot.set_text(text)
	    annot.get_bbox_patch().set_alpha(0.4)
	except:
		pass


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()