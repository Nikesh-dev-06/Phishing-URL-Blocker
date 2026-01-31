chrome.webNavigation.onBeforeNavigate.addListener(
  async function (details) {
    // only main page loads
    if (details.frameId !== 0) return;
    const url = details.url;
    // skip chrome / extension pages
    if (
      url.startsWith("chrome://") ||
      url.startsWith("chrome-extension://")
    ) {
      return;
    }
    try {
      const response = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ url })
      });
      const result = await response.json();
      if (result.status === "block") {
        const reason = encodeURIComponent(result.reason);
        chrome.tabs.update(details.tabId, {
          url: chrome.runtime.getURL(`warning.html?reason=${reason}`)
        });
      }
    } catch (err) {
      console.error("Backend not reachable", err);
    }
  },
  {
    url: [{ schemes: ["http", "https"] }]
  }
);
