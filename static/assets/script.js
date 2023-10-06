function shareTo(platform, url) {
    const websiteLink = 'http://yourwebsite.com'; // Replace with your website's URL
    const encodedURL = encodeURIComponent(url);
    const encodedWebsiteLink = encodeURIComponent(websiteLink);
    const customMessage = `Hey, look at this QR code that I created on John's site (${encodedWebsiteLink})!`;
    let shareURL = '';
    const width = 600, height = 400;

    switch(platform) {
        case 'facebook':
            shareURL = `https://www.facebook.com/sharer/sharer.php?u=${encodedURL}&quote=${customMessage}`;
            break;
        case 'twitter':
            shareURL = `https://twitter.com/intent/tweet?url=${encodedURL}&text=${customMessage}`;
            break;
    }

    window.open(shareURL, 'ShareDialog', `width=${width},height=${height}`);
}
