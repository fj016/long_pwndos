import requests
import os
import plotext


plotext.title("Response time depending on pwd len.")
plotext.clc


url = 'your_url'

increment = 1000		#Change this to suit your needs

def gen(nb):
	i = 'T'
	k = i * nb
	#This is example POST data, it should be modified.
	return {'username':'test', 'password':k}


def animate():
	x = []
	y = []
	t = 0
	for u in range(1,1000):
		plotext.clt()
		plotext.cld()
		m = 0
		z = 0
		for k in range(1,4):
			a = gen(t)
			r = requests.post(url = url, data = a, allow_redirects=False)
			z += r.elapsed.total_seconds()
		m = z / 3
		x.append(t)
		y.append(m)
		t += increment
		plotext.xlabel('Password len.')
		plotext.ylabel('Response time (s)')
		plotext.canvas_color(color = 'black')
		plotext.axes_color(color = 'black')
		plotext.ticks_color(color = 'cyan') 
		plotext.plot(x, y, marker="fhd", color="green")
		plotext.sleep(0.1)
		plotext.show()
		
		
animate()


