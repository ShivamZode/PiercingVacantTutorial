import QrScanner from './static/qr-scanner.min.js';

const videoElem = document.getElementById('videoElem');
const qrScanner = new QrScanner(videoElem, result => {
    console.log('Decoded QR code:', result);
});

navigator.mediaDevices.enumerateDevices()
    .then(devices => {

        const backCamera = devices.find(device => device.kind === 'videoinput' && device.label.toLowerCase().includes('back'));
        const constraints = {
            video: {
                deviceId: backCamera ? { exact: backCamera.deviceId } : undefined,
                facingMode: backCamera ? undefined : 'environment'
            }
        };

        return navigator.mediaDevices.getUserMedia(constraints);
    })
    .then(stream => {
        videoElem.srcObject = stream;
        videoElem.play();
        qrScanner.start();
    })
    .catch(err => {
        console.error('Error accessing the camera:', err);
    });
