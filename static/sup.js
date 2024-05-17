// Load models
Promise.all([
    faceapi.nets.tinyFaceDetector.loadFromUri('static/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('static/models'),
    faceapi.nets.faceRecognitionNet.loadFromUri('static/models'),
    faceapi.nets.faceExpressionNet.loadFromUri('static/models')
]).then(startVideo);

let isFaceDetected = false;
let storedDescriptor;


async function startVideo() {
    // Access webcam stream
    const video = document.getElementById('video');
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;

    // Detect faces in real-time
    video.addEventListener('play', () => {
        const canvas = faceapi.createCanvasFromMedia(video);
        document.body.append(canvas);
        const displaySize = { width: video.width, height: video.height };
        faceapi.matchDimensions(canvas, displaySize);

        setInterval(async () => {
            if (!isFaceDetected) {
                const detections = await faceapi.detectSingleFace(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceDescriptor();
                if (detections) {
                    const resizedDetections = faceapi.resizeResults(detections, displaySize);
                    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                    faceapi.draw.drawDetections(canvas, resizedDetections);
                    const descriptor = detections.descriptor;
                    storedDescriptor = descriptor;
                    isFaceDetected = true;
                    Ddata = document.getElementById('HDdata')
                    Ddata.value = JSON.stringify(storedDescriptor);
                    document.getElementById('faceForm').submit();
                    
                    
                }
            }
        }, 200); // Adjust interval as needed
    });
}

