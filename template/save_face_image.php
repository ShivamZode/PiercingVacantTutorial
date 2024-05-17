<?php
// Define the base directory where the PHP file is located
$baseDir = dirname(__FILE__);

// Specify the folder where the image will be saved
$uploadsDir = $baseDir . "/media/";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the name and image data from the POST request
    $name = $_POST['name'];
    $imageData = $_FILES['image']['tmp_name'];

    // Create the folder if it doesn't exist
    if (!file_exists($uploadsDir)) {
        mkdir($uploadsDir, 0777, true);
    }

    // Define the path where the image will be saved
    $imagePath = $uploadsDir . $name . ".png";

    // Move the uploaded image to the specified folder
    if (move_uploaded_file($imageData, $imagePath)) {
        echo "Face image saved successfully!";
    } else {
        echo "Failed to save face image.";
    }
} else {
    // If the request method is not POST, return an error
    echo "Invalid request method.";
}
?>