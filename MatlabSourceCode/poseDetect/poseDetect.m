I = imread('left1.jpg');

data = load("stereoParams.mat");
intrinsics = data.stereoParams.CameraParameters1.Intrinsics; 
tagSize = 0.1;
I = undistortImage(I,intrinsics,"OutputView","same");
[id,loc,pose] = readAprilTag(I,"tag36h11",intrinsics,tagSize);
worldPoints = [0 0 0; tagSize/2 0 0; 0 tagSize/2 0; 0 0 tagSize/2];
for i = 1:length(pose)
    % Get image coordinates for axes.
    imagePoints = worldToImage(intrinsics,pose(i).Rotation,pose(i).Translation,worldPoints);

    % Draw colored axes.
    I = insertShape(I,"Line",[imagePoints(1,:) imagePoints(2,:); ...
        imagePoints(1,:) imagePoints(3,:); imagePoints(1,:) imagePoints(4,:)], ...
        "Color",["red","green","blue"],"LineWidth",7);

    I = insertText(I,loc(1,:,i),id(i),"BoxOpacity",1,"FontSize",25);
end
imshow(I)

%eulZYX = rotm2eul(pose.Rotation) * 180/pi
%Translation = pose.Translation * 100
%[x,y,z] = transformPointsInverse(pose,.03,.05,.33) 

cameraCoordinates = [.03 .05 .33]; 
cameraCoordinatesTransformed = cameraCoordinates - pose.Translation;
worldCoordinates = cameraCoordinatesTransformed * pose.Rotation'