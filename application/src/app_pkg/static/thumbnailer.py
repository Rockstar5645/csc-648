from PIL import Image
import sys, os

path = 'M2_test_images'
im1 = '/sb1.jpg'
im2 = '/sb2.jpg'
im3 = '/sb3.jpg'
im4 = '/sb4.jpg'
im5 = '/sb5.jpg'

f = Image.open(path+im1)
f.thumbnail((200,200))
f.save('thumbnails/sb1_t.jpg') 

f = Image.open(path+im2)
f.thumbnail((200,200))
f.save('thumbnails/sb2_t.jpg') 


f = Image.open(path+im3)
f.thumbnail((200,200))
f.save('thumbnails/sb3_t.jpg') 

f = Image.open(path+im4)
f.thumbnail((200,200))
f.save('thumbnails/sb4_t.jpg') 


f = Image.open(path+im5)
f.thumbnail((200,200))
f.save('thumbnails/sb5_t.jpg') 



