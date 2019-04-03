$(function () {
    $.getScript("http://www.sso.com:5003/setLoginState", function () {
        console.log('success.');
    });
});