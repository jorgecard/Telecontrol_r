from SoftOscilloscope2 import SerialPlot
plot = SerialPlot('COM6', 115200)
plot.start()

'''
Takes a generic stream and sets custom parameters
'''
# from SoftOscilloscope import GenericPlot
# plot = GenericPlot(
# 	myStream, 
# 	xlim=(-100,100),
# 	ylim=(-50, 50),
# 	interval=1, 
# 	autoscale=False,
# 	read_size=1)
# plot.start()