/*
*   页面加载完毕访问cookie数据
*/
window.onload = function () {
 
    // 得到浏览器所有的Cookie的键值对
    var username = getCookie("username");
    var password = getCookie("password");
 
    // 开始自动登录
    if (username != null && password != null) {
        
        // 将用户名和密码放在表单中，提交表单登录
        document.getElementById("username").value = username;
        document.getElementById("password").value = password;
 
        // 提交表单
        document.getElementById("loginForm").submit();
    }
 
    /**
     * 通过Cookie的名字得到值
     */
    function getCookie(name) {
 
        // 得到所有cookie字符串
        var cookie = document.cookie;
        if (cookie != ""){
 
            // 使用分号来拆分成一个数组
            var arr = cookie.split(";");
 
            // 遍历数组，用等号拆分每个元素
            for (var i = 0; i < arr.length; i++){
 
                e = arr[i];
 
                // 得到键值对数组
                var nameAndValue = e.split("=");
                var cname = nameAndValue[0].trim();
                var cvalue = nameAndValue[1].trim();
 
                // 判断名字是否等于第0个元素，如果相等就返回第一个元素
                // 这是第一次登录
                if (name == cname){
 
                    return cvalue;
                }
            }
        }
    }
}