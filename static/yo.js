const videoElement = document.getElementById('video');
videoElement.setAttribute('autoplay', true);
//document.body.append(videoElement);

// const extractedFacesContainer = document.createElement('div');
// document.body.append(extractedFacesContainer);

// dont put
// const nameInput = document.createElement('input');
// nameInput.setAttribute('type', 'text');
// nameInput.setAttribute('placeholder', 'Enter your name');
// document.body.append(nameInput);

// const submitButton = document.createElement('button');
// submitButton.textContent = 'Submit';
// document.body.append(submitButton);

//put
let isFaceDetected = false;
let resizedDetections; 

Promise.all([
  faceapi.nets.faceRecognitionNet.loadFromUri('static/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('static/models'),
  faceapi.nets.ssdMobilenetv1.loadFromUri('static/models')
]).then(startVideo);

async function startVideo() {
  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  videoElement.srcObject = stream;
  const messageElement = document.getElementById('scanningMessage'); // Moved here

  videoElement.addEventListener('play', async () => {
    const canvas = faceapi.createCanvasFromMedia(videoElement);
    document.body.append(canvas);
    const displaySize = { width: videoElement.width, height: videoElement.height };
    faceapi.matchDimensions(canvas, displaySize);

    const interval = setInterval(async () => {
      if (!isFaceDetected) {
        const detections = await faceapi.detectAllFaces(videoElement).withFaceDescriptors();
        const resizedDetections = faceapi.resizeResults(detections, displaySize);

        if (resizedDetections.length > 0) {
          isFaceDetected = true;
          // const faceCanvas = document.createElement('canvas');
          const face = resizedDetections[0];
          const { x, y, width, height } = face.detection.box;

          // Fill face descriptor
          const faceDescriptorTextarea = document.getElementById('faceDescriptor');
          faceDescriptorTextarea.value = JSON.stringify(face.descriptor);

          // Stop extracting face
          clearInterval(interval);

          // Show message on HTML page
          messageElement.innerText = "Face scanning completed.";
          messageElement.style.display = "block"; // Show the message element
        }
      }

      // Clear canvas
      canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);

    }, 100);
  });
}
