// Handle form submission
document.getElementById("httpPacketForm").addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    // Get form inputs
    const destinationIP = document.getElementById("destinationIP").value;
    const destinationPort = document.getElementById("destinationPort").value;
    const httpMethod = document.getElementById("httpMethod").value;
    const httpPath = document.getElementById("httpPath").value;
    const host = document.getElementById("host").value;

    // Construct the payload to send to the server
    const payload = {
        destinationIP,
        destinationPort,
        httpMethod,
        httpPath,
        host,
    };

    // Send the payload to the Python server
    try {
        const response = await fetch("/generate_http_packet", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        const result = await response.text();
        document.getElementById("response").innerHTML = <div class="alert alert-success">${result}</div>;
    } catch (error) {
        document.getElementById("response").innerHTML = <div class="alert alert-danger">Error: ${error.message}</div>;
    }
});