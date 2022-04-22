images = imageDatastore("left\");
imageFileNames = images.Files;

I = images.readimage(1);


figure
imshow(I)

J1 = undistortImage(I,cameraParams);

figure; 
imshow(J1);