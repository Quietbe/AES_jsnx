
const CryptoJS = require("C:\\Users\\Administrator\\AppData\\Roaming\\npm\\node_modules\\crypto-js");
const variate = {
    "key": {
        "words": [
            863652730,
            2036741733,
            1164342596,
            1782662963
        ],
        "sigBytes": 16
    },
    "aceIV": {
        "words": [
            1719227713,
            1314533489,
            1397643880,
            1749959510
        ],
        "sigBytes": 16
    },
    "xgGjcArray": [],
    "xgGjcIndex": 0,
    "isPageLoad": false
}
function AESDecrypt(str) {
    var nContent = CryptoJS.AES.decrypt(str, variate.key, {
        iv: variate.aceIV,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    })
    if (nContent && nContent != null) {
        try {
            var constr = CryptoJS.enc.Utf8.stringify(nContent)
            if (constr != "") {
                var data = JSON.parse(constr);
                return data;
            } else
                return null;
        } catch (err) {
            return null;
        }

    } else
        return null;
}

// var aa = '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'
// aa = AESDecrypt(aa);
// // 将aa 转换成 str
// // aa = toString(aa)
// console.log(aa)

