const button = document.createElement("button");
button.id = "speechToTextButton";
button.textContent = "🎙️";
button.style.position = "fixed";
button.style.bottom = "20px";
button.style.right = "20px";
button.style.zIndex = "10000";
button.style.background = "#000";
button.style.color = "#fff";
button.style.border = "none";
button.style.borderRadius = "50%";
button.style.width = "50px";
button.style.height = "50px";
button.style.fontSize = "24px";
button.style.cursor = "pointer";
button.style.display = "none";
document.body.appendChild(button);

let activeElement;
button.addEventListener("mousedown", (event) => {
    activeElement = document.activeElement;});
button.addEventListener("click", (e) => {
    // chrome.runtime.sendMessage({ command: "toggleRecognition" });
    // e.preventDefault();
    if (activeElement) activeElement.focus();
    toggleRecognition();});
function insertTextAtCursor(text) {
    const el = document.activeElement;
    const tagName = el.tagName.toLowerCase();
    if (tagName === "input" || tagName === "textarea") {
        const start = el.selectionStart;
        const end = el.selectionEnd;
        const value = el.value;
        el.value = value.slice(0, start) + text + value.slice(end);
        el.selectionStart = el.selectionEnd = start + text.length;
    } else if (
        tagName === "div" &&
        el.getAttribute("contenteditable") === "true") {
        const selection = window.getSelection();
        const range = selection.getRangeAt(0);

        range.deleteContents();
        const textNode = document.createTextNode(text);
        range.insertNode(textNode);
        range.setStartAfter(textNode);
        range.setEndAfter(textNode);
        selection.removeAllRanges();
        selection.addRange(range);}
    const inputEvent = new Event("input", { bubbles: true, cancelable: true });
    el.dispatchEvent(inputEvent);
    const changeEvent = new Event("change", {
        bubbles: true,
        cancelable: true,
    });
    el.dispatchEvent(changeEvent);}
if (!window.recognition) {
    window.recognition = new webkitSpeechRecognition();}
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;
recognition.continuous = true;

recognition.onresult = (event) => {
    console.log("log start");

    const transcript = event.results[event.results.length - 1][0].transcript;
    if (transcript.toLowerCase().includes("that's all.")) {
        const el = document.activeElement;
        const e = new KeyboardEvent("keydown", {
            keyCode: 13,
            bubbles: true,
            cancelable: true,});
        el.dispatchEvent(e);
        toggleRecognition();
        return;}

    insertTextAtCursor(transcript);};
recognition.onend = () => {
    console.log("log start");
    if (!recognition.manualStop) {
        setTimeout(() => {
            recognition.start();
            console.log("log start");
        }, 100);}};
chrome.runtime.onMessage.addListener((request) => {
    if (request.command === "toggleRecognition") {
        toggleRecognition();}});
function toggleRecognition() {
    console.log("toggle了");
    if (!recognition.manualStop) {
        recognition.manualStop = true;
        recognition.stop();
        button.style.background = "#000";
    } else {
        recognition.manualStop = false;
        recognition.start();
        button.style.background = "#f00";}}
