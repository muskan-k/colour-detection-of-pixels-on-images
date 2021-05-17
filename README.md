# Colour detection of the pixels in an image

## Imports: Pandas, OpenCV, copy, Numpy

#### This is more of a program that uses OpenCV to process on images. Following are the features:
  1. Read the image file 
  2. Callback event on mouse click
  3. Shows the color name and RGB values of the pixel that was clicked on
  4. A function call on mouse click that recieves the rgb value of the pixel at (x,y) position in the image (where it was clicked)
  5. A function to calculate the min value of the difference between that pixel's RGB value and the colours present in the csv dataset.
  6. Displaying a rectangle near the clicked pixel with that colour filled, along with a text that displays the colour name and R G B values from the csv.
  7. Exit the window on pressing ESC key.

#### What did I learn?
  1. Reading and displaying an image using ``cv.imread()`` and ``cv.imshow()``
  2. Using an event for mouse click. Here ``cv.EVENT_LBUTTONDOWN`` was used which is for single click.
  3. Obtaining RGB value of the pixel 
  4. Adding rectangle and text on the image using ``cv.rectangle(source,point1,point2,colour,thickness)`` and ``cv.putText(source,text,point,font,fontScale,colour,thickness,linetype)``
  5. On each click, the image was reset using the copy.deepcopy() method to erase the previous rectangle display

#### Will this repository be improved?
  Yes, the project will be updated with added features that allows you to capture your own image using the webcam to obtain the colours of an image from real-time.

## OUTPUT
<img width="900" alt="O1" src="https://user-images.githubusercontent.com/60001051/118470991-e1353b80-b724-11eb-9832-2d9c4c78a8fa.png">
<img width="800" alt="O2" src="https://user-images.githubusercontent.com/60001051/118471033-ec886700-b724-11eb-81e9-d199a4d9cd52.png">
<img width="800" alt="O3" src="https://user-images.githubusercontent.com/60001051/118471044-f01bee00-b724-11eb-8055-6350cf6a90c1.png">
