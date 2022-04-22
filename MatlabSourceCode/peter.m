cam = CentralCamera('focal',.015,'pixel',10e-6,'resolution',[752,480],'centre',[376,240],'name','myCam');
P = [.3 .4 3]';
cam.project(P)
P = mkgrid(3,.2,'pose',SE3(0,0,1));
cam.project(P)
cam.plot(P)

Tcam = SE3(-.8,0,.5) * SE3.Ry(.9);
cam.plot(P,'pose',Tcam);

cube = mkcube(.2,'pose',SE3(0,0,1));
Tcam = SE3(-.7,0,.4) * SE3.Ry(.8);
cam.plot(cube,'pose',Tcam);
cam.project(cube,'pose',Tcam)

[X,Y,Z] = mkcube(.2,'pose',SE3(0,0,1),'edge');
cam.mesh(X,Y,Z);
Tcam = SE3(-.7,0,.4) * SE3.Ry(.8);
cam.mesh(X,Y,Z,'pose',Tcam);