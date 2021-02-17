from manimlib.constants import *
from manimlib.mobject.geometry import Rectangle

def rect_section(obj,x1=-100,x2=100,y1=-100,y2=100,z1=-100,z2=100,color=YELLOW):
    points=obj.get_points()
    for point in points:
        if point[0]<x1:
            point[0]=x1
        if point[0]>x2:
            point[0]=x2
        if point[1]<y1:
            point[1]=y1
        if point[1]>y2:
            point[1]=y2
        if point[2]<y1:
            point[2]=y1
        if point[2]>y2:
            point[2]=y2
    output=Rectangle(color=color)
    output.set_points(points)
    return output
