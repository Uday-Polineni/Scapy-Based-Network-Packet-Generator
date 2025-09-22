<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = "Static User";
    $comments = "Static Comment";

    $sql = "INSERT INTO feedback (user, comments) VALUES ('$user', '$comments')";
    if ($conn->query($sql) === TRUE) {
        echo "Static feedback submitted successfully!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
?>
