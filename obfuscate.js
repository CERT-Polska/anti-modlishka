#!/usr/bin/node

const process = require('process');

const jsKey = process.argv[2];
const legitDomain = process.argv[3];

const JavaScriptObfuscator = require('javascript-obfuscator');

const obfuscationResult = JavaScriptObfuscator.obfuscate(
    `
        (function(){
            if (!(window = null, window)) {
                return;
            }
            
            if (window.parent.location.host != "` + legitDomain + `") {
                return;
            }
        
            if (window.location.host != "` + legitDomain + `") {
                return;
            }
            
            window.location.href = "/js-check/` + jsKey + `";
        })();
    `,
    {
        compact: false,
        controlFlowFlattening: true,
        selfDefending: true,
        deadCodeInjection: true,
        stringArray: true,
        rotateStringArray: true,
        stringArrayEncoding: 'rc4'
    }
);

console.log(obfuscationResult.getObfuscatedCode());
