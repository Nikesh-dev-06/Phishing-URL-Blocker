const params = new URLSearchParams(window.location.search);
const reason = params.get("reason");

document.getElementById("reason").innerText =
  reason || "This website is unsafe";

document.getElementById("goBack").addEventListener("click", () => {
  history.back();
});
