document.addEventListener("DOMContentLoaded", function () {

    /* ================= FORM VALIDATION ================= */

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (e) {
            const locationInput = form.querySelector("input[name='location']");
            const descInput = form.querySelector("textarea[name='description']");
            const imageInput = form.querySelector("input[name='image']");

            if (locationInput && descInput && imageInput) {

                const location = locationInput.value.trim();
                const desc = descInput.value.trim();
                const image = imageInput.value;

                if (location === "" || desc === "" || image === "") {
                    e.preventDefault();
                    alert("Please fill all fields before submitting.");
                }
            }
        });
    }


    /* ================= CARD HOVER EFFECT ================= */

    const cards = document.querySelectorAll(".card");

    cards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {
            card.style.transform = "translateY(-8px)";
            card.style.boxShadow = "0 10px 25px rgba(0,0,0,0.2)";
            card.style.transition = "0.3s";
        });

        card.addEventListener("mouseleave", function () {
            card.style.transform = "translateY(0px)";
            card.style.boxShadow = "0 4px 8px rgba(0,0,0,0.1)";
        });

    });


    /* ================= CHATBOT ================= */

    const chatbotIcon = document.getElementById("chatbotIcon");

    if (chatbotIcon) {

        const chatbotBox = document.getElementById("chatbotBox");
        const sendBtn = document.getElementById("sendBtn");
        const chatInput = document.getElementById("chatInput");
        const chatMessages = document.getElementById("chatMessages");

        chatbotIcon.addEventListener("click", function () {
            if (chatbotBox.style.display === "flex") {
                chatbotBox.style.display = "none";
            } else {
             chatbotBox.style.display =
             chatbotBox.style.display === "flex" ? "none" : "flex";            }
        });

        function addMessage(message, sender) {
            const msgDiv = document.createElement("div");
            msgDiv.style.marginBottom = "8px";

            if (sender === "user") {
                msgDiv.style.textAlign = "right";
                msgDiv.innerHTML =
                    "<span style='background:#e8f5e9;padding:6px 10px;border-radius:10px;display:inline-block;'>" +
                    message +
                    "</span>";
            } else {
                msgDiv.innerHTML =
                    "<span style='background:#f1f1f1;padding:6px 10px;border-radius:10px;display:inline-block;'>" +
                    message +
                    "</span>";
            }

            chatMessages.appendChild(msgDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function botReply(text) {
            text = text.toLowerCase();

            if (text.includes("complaint")) {
                return "To submit a complaint, go to the Submit Complaint page.";
            }
            else if (text.includes("track")) {
                return "You can track your complaints in My Complaints section.";
            }
            else if (text.includes("dry")) {
                return "Dry waste includes paper, plastic bottles, and metal cans.";
            }
            else if (text.includes("wet")) {
                return "Wet waste includes food waste and vegetable scraps.";
            }
            else {
                return "I can help you with complaints and waste information 😊";
            }
        }

        if (sendBtn) {
            sendBtn.addEventListener("click", function () {
                const userText = chatInput.value.trim();
                if (userText === "") return;

                addMessage(userText, "user");

                setTimeout(function () {
                    addMessage(botReply(userText), "bot");
                }, 500);

                chatInput.value = "";
            });
        }

        if (chatInput) {
            chatInput.addEventListener("keypress", function (e) {
                if (e.key === "Enter") {
                    sendBtn.click();
                }
            });
        }
    }

});