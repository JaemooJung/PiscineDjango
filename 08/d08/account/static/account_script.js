$(document).ready(() => {
  checkLoginStatus();

  $("#loginForm").on("submit", (e) => {
    e.preventDefault();
    login();
  });
  
  $("#logoutButton").on("click", logout);
});

const checkLoginStatus = () => {
  $.ajax({
    type: "GET",
    url: "/account/check_login/",
    success: (data) => {
      switchUserState(true, data.username);
    },
    error: (jqXHR) => {
      if (jqXHR.responseJSON.status === 'logged_out') {
        switchUserState(false);
      }
    }
  });
};

const login = () => {
  $.ajax({
    type: "POST",
    url: "/account/login/",
    data: $("#loginForm").serialize(),
    beforeSend: setCSRFToken,
    success: (data) => {
      if (data.status === 'ok') {
        switchUserState(true, data.username);
        CSRF_TOKEN = data.csrf_token;
      } 
    },
    error: (jqXHR) => {
      if (jqXHR.responseJSON.status === 'error') {
        const errors = jqXHR.responseJSON.errors;
        const errorMessage = Object.entries(errors)
          .map(([field, error]) => `${field}: ${error}`)
          .join('\n');
        $("#errorMessages").text(errorMessage).show();
      }
    }
  });
};

const logout = () => {
  $.ajax({
    type: "POST",
    url: "/account/logout/",
    beforeSend: setCSRFToken,
    success: (data) => {
      switchUserState(false);
      CSRF_TOKEN = data.csrf_token;
    }
  });
};

const setCSRFToken = (xhr) => {
  xhr.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
};

const switchUserState = (isLoggedIn, username) => {
  if (isLoggedIn) {
    $("#loginForm").hide();
    $("#usernameText").text(username);
    $("#userMenu").show();
  } else {
    $("#loginForm").show();
    $("#userMenu").hide();
  }
};
