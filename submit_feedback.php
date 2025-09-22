<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$servername = "127.0.0.1";
$username = "root";
$password = "";
$dbname = "feedback_db";
$port = 3306;

$conn = new mysqli($servername, $username, $password, $dbname, $port);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize user input
    $user = $conn->real_escape_string($_POST['user']);
    $comments = $conn->real_escape_string($_POST['comments']);

    // Insert data into database
    $sql = "INSERT INTO feedback (user, comments) VALUES ('$user', '$comments')";
    if ($conn->query($sql) === TRUE) {
        echo "
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Feedback Success</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f9f9f9;
                    font-family: Arial, sans-serif;
                }
                .success-message {
                    text-align: center;
                    color: green;
                    font-size: 2em;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class='success-message'>Feedback submitted successfully!</div>
        </body>
        </html>";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
