
window = global;
window.c = "4h@$udD2s";
window.r = "3sd&d2";
window.a = "*";

const CryptoJS = require("C:\\Users\\Administrator\\AppData\\Roaming\\npm\\node_modules\\crypto-js");

function decrypt(n) {
    var o = o || "".concat(r).concat(c).concat(a);
    var t = CryptoJS.enc.Utf8.parse(o)
        , e = CryptoJS.AES.decrypt(n, t, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    let dd = CryptoJS.enc.Utf8.stringify(e).toString();
    return dd

}

// var return_data = decrypt(data)
// console.log(decrypt(data))

