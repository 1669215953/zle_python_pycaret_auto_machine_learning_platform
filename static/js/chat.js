

// 获取元素
const closeBtn = document.querySelector('.close-btn');
const showChatBtn = document.querySelector('.show-chat-btn');
const chatContainer = document.querySelector('.container');

// 点击退出按钮隐藏聊天窗口
closeBtn.addEventListener('click', () => {
chatContainer.style.display = 'none';
showChatBtn.style.display = 'block'; // 显示聊天按钮
});

// 点击显示按钮显示聊天窗口
showChatBtn.addEventListener('click', () => {
chatContainer.style.display = 'block';
showChatBtn.style.display = 'none'; // 隐藏聊天按钮
});






const chatBody = document.querySelector(".chat-body");
const txtInput = document.querySelector("#txtInput");
const send = document.querySelector(".send");

send.addEventListener("click", () => renderUserMessage());

txtInput.addEventListener("keyup", (event) => {
    if (event.keyCode === 13) {
        renderUserMessage();
    }
});

const renderUserMessage = () => {
    const userInput = txtInput.value;
    renderMessageEle(userInput, "user");
    txtInput.value = "";
    setTimeout(() => {
        renderChatbotResponse(userInput);
        setScrollPosition();
    }, 600);
};

const renderChatbotResponse = (userInput) => {
    const res = getChatbotResponse(userInput);
};

const renderMessageEle = (txt, type) => {
    let className = "user-message";
    if (type !== "user") {
        className = "chatbot-message";
    }
    const messageEle = document.createElement("div");
    const txtNode = document.createTextNode(txt);
    messageEle.classList.add(className);
    messageEle.append(txtNode);
    chatBody.append(messageEle);
};

const getChatbotResponse = (userInput) => {
        
        var xhr_user_message = new XMLHttpRequest();
        xhr_user_message.open("POST", 'http://127.0.0.1:5000/get_user', true);
        xhr_user_message.setRequestHeader('Content-Type', 'application/json');
        xhr_user_message.send(JSON.stringify({
            message: userInput
        }));
        var xhr_ai_response = new XMLHttpRequest();
        xhr_ai_response.open('GET', 'http://127.0.0.1:5000/get_AI?message=' + userInput, true);
        xhr_ai_response.onload = function() {
        if (this.status == 200){
            var response = JSON.parse(this.responseText);
            var message = response.ai_response.content;
            renderMessageEle(message);
            return message;
        }
        };
        xhr_ai_response.send(null);
};

const setScrollPosition = () => {
    if (chatBody.scrollHeight > 0) {
        chatBody.scrollTop = chatBody.scrollHeight;
    }
};







// 获取拖拽的元素
var dragItem = document.querySelector(".show-chat-btn");

// 初始化起始位置
var currentX;
var currentY;
var initialX;
var initialY;
var xOffset = 0;
var yOffset = 0;

// 为SVG图标添加事件监听
dragItem.addEventListener("mousedown", dragStart, false);
window.addEventListener("mouseup", dragEnd, false);
window.addEventListener("mousemove", drag, false);

// 拖拽开始
function dragStart(e) {
// 获取起始位置
initialX = e.clientX - xOffset;
initialY = e.clientY - yOffset;

if (e.target === dragItem) {
window.addEventListener("mousemove", drag, false);
window.addEventListener("mouseup", dragEnd, false);
}
}

// 拖拽结束
function dragEnd(e) {
// 最终的偏移量
initialX = currentX;
initialY = currentY;

window.removeEventListener("mousemove", drag, false);
window.removeEventListener("mouseup", dragEnd, false);
}

// 拖动过程中
function drag(e) {
if (e.target === dragItem) {
e.preventDefault();

// 计算移动距离
currentX = e.clientX - initialX;
currentY = e.clientY - initialY;

xOffset = currentX;
yOffset = currentY;

// 设置元素位置
setTranslate(currentX, currentY, dragItem);
}
}

// 设置元素的新位置
function setTranslate(xPos, yPos, el) {
el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}





