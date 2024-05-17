function domReady(fn) {
  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    setTimeout(fn, 1000);
  } else {
    document.addEventListener("DOMContentLoaded", fn);
  }
}

domReady(function () {

  // If found your qr code
  function onScanSuccess(decodeText, decodeResult) {
    alert("Your QR is : " + decodeText); // Fixed the alert message
  }

  let htmlscanner = new Html5QrcodeScanner(
    "my-qr-reader",
    { fps: 10, qrbos: 250 }
  );
  htmlscanner.render(onScanSuccess);

  // Start scanning immediately after the scanner is open
  htmlscanner.start();
});
