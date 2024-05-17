{pkgs}: {
  deps = [
    pkgs.cmake
    pkgs.dlib
    pkgs.python311Packages.face-recognition
  ];
}
