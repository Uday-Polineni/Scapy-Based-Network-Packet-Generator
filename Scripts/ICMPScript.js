// Function to validate ICMP form inputs
function validateICMPForm() {
    const destinationIP = document.getElementById("destinationIP").value;

    // Regex for validating IPv4 addresses
    const ipRegex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

    if (!ipRegex.test(destinationIP)) {
        alert("Invalid Destination IP Address");
        return false;
    }

    return true;
}

// Attach the validation function to the form
document.addEventListener("DOMContentLoaded", () => {
    const icmpForm = document.getElementById("icmpForm");
    if (icmpForm) {
        icmpForm.onsubmit = validateICMPForm;
    }
});
