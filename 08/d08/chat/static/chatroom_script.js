const chatMessageInput = $('#chat-message-input');
const chatMessageSubmit = $('#chat-message-submit');

const chatroomId = document.currentScript.dataset.chatroomId;
let socket = new WebSocket(`ws://${window.location.host}/ws/chat/${chatroomId}/`);

socket.onmessage = (e) => {
  let data = JSON.parse(e.data);
  let id = data['id'];
  let chatLog = $('#chat-log');
  let chatUsers = $('#chat-users');

  const eventHandlers = {
    'chat_message': () => {
      let message = data['message'];
      let username = data['username'];
      chatLog.prepend('<p><strong>' + username + ': </strong>' + message + '</p>');
    },
    'user_joined': () => {
      console.log("user_joined")
      let message = data['message'];
      chatLog.prepend(`<p> ${message} </p>`);
    },
    'user_left': () => {
      let message = data['message'];
      chatLog.prepend(`<p> ${message}</p>`);
    },
    'user_list': () => {
      let users = data['users'];
      chatUsers.empty();
      for (let user of users) {
        console.log(user);
        chatUsers.prepend(`<li class="list-group-item">${user}</li>`);
      }
    }
  };

  if (eventHandlers[id]) {
    eventHandlers[id]();
  }
};

socket.onclose = (e) => {
  console.error('Chat socket closed unexpectedly');
};

chatMessageInput.focus();
chatMessageInput.keyup((e) => {
  if (e.keyCode === 13) {  // enter, return
    chatMessageSubmit.click();
  }
});

chatMessageSubmit.click((e) => {
  let message = chatMessageInput.val();
  if (message.trim() === '') {
    return;
  }
  socket.send(JSON.stringify({
    'message': message
  }));
  chatMessageInput.val('');
});