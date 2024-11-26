#!/usr/bin/node

const fs = require('fs');

// Retrieve the file path from the command-line arguments
const filePath = process.argv[2];

if (!filePath) {
    console.error("Usage: node script.js <file_path>");
    process.exit(1);
}

// Read the file content with UTF-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // Print the error object if an error occurs
        console.error("An error occurred:", err);
        return;
    }
    // Print the content of the file
    console.log(data);
});
