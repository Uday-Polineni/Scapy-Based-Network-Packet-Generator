// Function to validate UDP form inputs
function validateUDPForm() {
    const destinationIP = document.getElementById("destinationIP").value;
    const destinationPort = document.getElementById("destinationPort").value;
    const sourceIP = document.getElementById("sourceIP").value;

    // Regex for validating IPv4 addresses
    const ipRegex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

    if (!ipRegex.test(destinationIP)) {
        alert("Invalid Destination IP Address");
        return false;
    }

    if (sourceIP !== "" && !ipRegex.test(sourceIP)) {
        alert("Invalid Source IP Address");
        return false;
    }

    if (destinationPort < 1 || destinationPort > 65535 || isNaN(destinationPort)) {
        alert("Invalid Destination Port. It must be a number between 1 and 65535.");
        return false;
    }

    return true;
}
