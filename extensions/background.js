console.log("=== DELETE DUPLICATES EXTENSION LOADING ===");

// Test initial connection
if (typeof browser !== 'undefined' && browser.runtime && browser.runtime.sendNativeMessage) {
    console.log("=== NATIVE MESSAGING AVAILABLE ===");
    
    // Test connection
    browser.runtime.sendNativeMessage('com.deleteduplicates.python', { fileName: "test-connection.txt" })
        .then(response => {
            console.log('=== INITIAL CONNECTION TEST SUCCESS ===', response);
        })
        .catch(error => {
            console.log('=== INITIAL CONNECTION TEST FAILED ===');
            console.error('Error:', error);
            console.error('Error message:', error.message);
        });
} else {
    console.error("=== NATIVE MESSAGING NOT AVAILABLE ===");
}

// Listen for download events
browser.downloads.onChanged.addListener((downloadDelta) => {
    console.log("=== DOWNLOAD EVENT ===", downloadDelta);
    
    // Check if download is complete
    if (downloadDelta.state && downloadDelta.state.current === 'complete') {
        console.log("=== DOWNLOAD COMPLETE ===");
        
        // Get download info
        browser.downloads.search({ id: downloadDelta.id }).then(downloads => {
            console.log("=== SEARCH RESULTS ===", downloads);
            
            if (downloads.length > 0) {
                const download = downloads[0];
                const fileName = download.filename.split('/').pop();
                console.log("=== SENDING TO NATIVE HOST ===", fileName);
                
                // Send to native messaging host
                browser.runtime.sendNativeMessage('com.deleteduplicates.python', { fileName: fileName })
                    .then(response => {
                        console.log('=== DUPLICATE CHECK SUCCESS ===', response);
                        if (response.duplicatesRemoved > 0) {
                            console.log(`Removed ${response.duplicatesRemoved} duplicate(s) for ${fileName}`);
                        }
                    })
                    .catch(error => {
                        console.error('=== DUPLICATE CHECK ERROR ===', error);
                    });
            }
        });
    }
});

console.log("=== DELETE DUPLICATES EXTENSION LOADED ===");