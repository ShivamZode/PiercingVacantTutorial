const video = document.getElementById('video');
const img = document.getElementById('img');
const outputImage = document.getElementById('outputImage');

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/static/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/static/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/static/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/static/models')
]).then(startVideo);

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  );
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video);
  document.body.append(canvas);
  const displaySize = { width: video.width, height: video.height };
  faceapi.matchDimensions(canvas, displaySize);
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks();

    // Loop through each detected face
    detections.forEach(detection => {
      extractFaceFromBox(video, detection.detection.box);
    });

    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
    faceapi.draw.drawDetections(canvas, resizedDetections);
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
  }, 10);
});

// This function extract a face from video frame with giving bounding box and display result into outputimage
async function extractFaceFromBox(inputImage, box){ 
  const regionsToExtract = [
    new faceapi.Rect(box.x, box.y, box.width, box.height)
  ];

  const faceImages = await faceapi.extractFaces(inputImage, regionsToExtract);

  if (faceImages.length === 0) {
    console.log('Face not found');
  } else {
    faceImages.forEach(cnv => {      
      outputImage.src = cnv.toDataURL();
    });
  }   
}